import cv2
import numpy as np
import playsound
from Run import Alam


Alarm= True
Fire_Reported = 0

def play_audio():
	while True:
		playsound.playsound('alam1.mp3',True)




video = cv2.VideoCapture(0)
 
while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    frame = cv2.resize(frame, (960, 540)) 
 
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)
 
    output = cv2.bitwise_and(frame, hsv, mask=mask)
    
    no_red = cv2.countNonZero(mask)
    
    if int(no_red) > 15000:
        Fire_Reported = Fire_Reported + 1

        cv2.imshow("output", output)

        if Fire_Reported >= 1:
    
    	        if Alarm==False:
                   play_audio()
                   Alarm = True

    
    if grabbed==False:
        break
    cv2.imshow("fire Detected",output)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cv2.destroyAllWindows()
video.release()