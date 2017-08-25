import cv2
import numpy

from keras.models import load_model
video_path = 'C:/Users/NickLyubimov/Desktop/akn.222.075.left.avi'
semaphores_cascade_path = ''

def classify_semaphore(semaphore):
    return model.predict_classes(semaphore)[0] == 1

def detect_semaphores(frame, semaphore_cascade):
    semaphores = semaphore_cascade.detectMultiScale(frame)
    for(x, y, w, h) in semaphores:
        semaphore = frame[x:y, w:h]
        if classify_semaphore(semaphore):
            return True
    return False

def start_detection(video_path, semaphores_cascade_path):
    cap = cv2.VideoCapture(video_name)
    semaphores_cascade = cv2.CascadeClassifier(semaphores_cascade_path)
    index = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
            if detect_semaphores(frame, semaphores_cascade):
                cap.release()
                return index
        else:
            cap.release()
            return -1
        index+=1
    cap.release()
    return -1


videos = filter(lambda x: x.endswith(extension), os.listdir(directory))
f = open('results.txt', 'w')
for video in videos:
    f.write(video+'  %05d' % start_detection(directory+'\\'+video, semaphores_cascade_path))
