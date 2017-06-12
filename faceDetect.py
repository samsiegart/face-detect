import threading
import cv2
import time

class faceDetect:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.threadLock = threading.Lock()
        self.faces = []
        self.looping = True

    def checkForFaceThread(self, threadLock, cf, faceCascade):
        while self.looping:
            gray = cv2.cvtColor(cf.getFrame(), cv2.COLOR_BGR2GRAY)
            self.faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.9,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            time.sleep(0.05)

    def checkForFace(self, cf):
        thread = threading.Thread(target=self.checkForFaceThread, args=(self.threadLock, cf, self.faceCascade))
        thread.start()

    def numFaces(self):
        return len(self.faces)

    def allFaces(self):
        return self.faces

    def stopLoop(self):
        self.looping = False
