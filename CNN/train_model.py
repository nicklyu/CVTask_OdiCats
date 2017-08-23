import numpy
from PIL import Image
import os
import keras
import sys

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_images(directory, extension, class_num):
    images = filter(lambda x: x.endswith(extension), os.listdir(directory+'/'))
    train_x = numpy.array([numpy.array(Image.open(directory+'/'+image).convert("RGB")) for image in images])
    train_y = numpy.array([class_num]*len(images))
    return train_x, train_y

def norm_enc(x_train, x_test, y_train, y_test):
    x_train = numpy.array(x_train).astype('float32')
    x_test = numpy.array(x_test).astype('float32')
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    y_train = keras.utils.to_categorical(y_train, 2)
    y_test = keras.utils.to_categorical(y_test, 2)
    return x_train, x_test, y_train, y_test


def load_classes(first, second, extension):
    x_1, y_1 = load_images(directory=first, extension=extension, class_num=0)
    x_2, y_2 = load_images(directory=second, extension=extension, class_num=1)

    x = numpy.concatenate((x_1, x_2), axis=0)
    y = numpy.concatenate((y_1, y_2), axis=0)
    return x, y


def create_model(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    x_train, x_test, y_train, y_test = norm_enc(x_train, x_test, y_train, y_test)

    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same',
                     input_shape=x_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation('softmax'))

    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])
    return x_train, x_test, y_train, y_test, model

print sys.argv
if len(sys.argv) != 5:
    print('Illegal args number')
    sys.exit()


x, y = load_classes(sys.argv[1], sys.argv[2], sys.argv[3])

x_train, x_test, y_train, y_test, model = create_model(x, y)

model.fit(x_train, y_train,
          batch_size=5,
          epochs=int(sys.argv[4]),
          validation_data=(x_test, y_test),
          shuffle=True)

model.save('cnn_classifier.h5')

print('Accuracy: '+str(accuracy_score(y_test[:,1], model.predict_classes(x_test))))