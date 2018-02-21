import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
start_time_in_seconds = time.time()
time_limit = 10
while time.time() - start_time_in_seconds < time_limit:
#while True:
	ret, fram = cap.read()
	gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
	out.write(fram)
	cv2.imshow('frame',fram)
	cv2.imshow('gray',gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
out.release()
cv2.destroyAllWindows()
