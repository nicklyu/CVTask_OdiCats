import os
import sys
import cv2


def augmentate_set(directory, out, prefix):
    """
    augmentate all frames in directory
    :param directory: directory which contains set
    :param out: output directory
    :param prefix: prefix for every augmented frame
    :return: Void. Also, produces augmented frames to output directory
    """
    imgs = os.listdir(directory)

    if not os.path.exists(out):
        os.makedirs(out)

    for img in imgs:
        frame = cv2.imread(directory + '/' + img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        augmentate_frame(frame, out, prefix)
    print(str(len(os.listdir(out)))+' images created')


def augmentate_frame(frame, output, prefix):
    """
    augmentates frame
    :param frame: frame to augmentate  
    :param output: output directory
    :param prefix: prefix to save
    :return: 
    """
    from keras.preprocessing.image import ImageDataGenerator
    f = frame.reshape((1,) + frame.shape)
    datagen = ImageDataGenerator(rotation_range=10, horizontal_flip=True
                                 )
    i = 0
    for batch in datagen.flow(f, batch_size=1, save_to_dir=output,
                              save_format='jpeg',
                              save_prefix=prefix, ):
        i += 1
        if i > 2:
            break


if len(sys.argv) != 4:
    print('Illegal args number')
    sys.exit()

augmentate_set(directory=sys.argv[1], out=sys.argv[2], prefix=sys.argv[3])