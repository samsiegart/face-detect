import cv2
from faceDetect import faceDetect

cv2.namedWindow("preview",flags=cv2.WINDOW_NORMAL)
vc = cv2.VideoCapture(0)
faceDetector = faceDetect()

class CurFrame:
    def __init__(self):
        self.frame = None

    def getFrame(self):
        return self.frame

    def updateFrame(self, newFrame):
        self.frame = newFrame

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

cf = CurFrame()
cf.updateFrame(frame)

faceDetector.checkForFace(cf)
facesSeen = 0

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    cf.updateFrame(frame)
    allFaces = faceDetector.allFaces()
    for face in allFaces:
        cv2.rectangle(frame, (face[0],face[1]), (face[0]+face[2],face[1]+face[3]),(0, 255, 0))
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        faceDetector.stopLoop()
        break
cv2.destroyWindow("preview")
