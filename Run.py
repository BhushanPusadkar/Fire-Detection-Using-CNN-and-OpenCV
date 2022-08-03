from tkinter import Frame, Tk
import cv2
from cv2 import VideoCapture
from cv2 import blur
from matplotlib.pyplot import hsv
import numpy as np
import playsound

root=Tk()

Fire_Repoted=0
Alam =False

def play_audio():
    playsound.playsound("alam1.mp3",True)

video =VideoCapture(0)
#video1.mp4 is insert on the videocapture then show the video

while True:
    ret, Frame=video.read()
    Frame =cv2.resize(Frame,(600,600))
    blur =cv2.GaussianBlur(Frame ,(15,15),0)
    hsv =cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lower=[18,50,50]
    upper=[35,255,255]

    lower=np.array(lower,dtype='uint8')
    upper=np.array(upper,dtype='uint8')

    mask = cv2.inRange(hsv,lower,upper)

    optput =cv2.bitwise_and(Frame,hsv,mask=mask)

    #########################

    size =cv2.countNonZero(mask)

    if int(size) > 15000:
        #pass
        print("Fire Detected")
        Fire_Repoted=Fire_Repoted+1

        if Fire_Repoted >=1:

            if Alam==False:
                play_audio()
                Alam=True

    if ret==False:
        break
    cv2.imshow("fire Detected",optput)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cv2.destroyWindow()
video.release()
root.mainloop()
