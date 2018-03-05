import cv2 as cv
import numpy as np
def face_detect_demo():
	gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
	face_detector = cv.CascadeClassifier("F:/git/opencv/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
	eye_haar = cv.CascadeClassifier("F:/git/opencv/data/haarcascades/haarcascade_eye.xml")
	faces = face_detector.detectMultiScale(gray, 1.1,3)
	for x, y, w,h in faces:
		cv.rectangle(src, (x, y), (x + w, y + h),(0,0,255), 2)
		roi_gray_img = gray[y:y+h, x:x+w]
		roi_img = src[y:y+h,x:x+w]
		eyes = eye_haar.detectMultiScale(roi_gray_img, 1.02,2)
		for eye_x, eye_y, eye_w, eye_h in eyes:
			cv.rectangle(roi_img, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (255, 0, 0), 2)
	cv.imshow("result", src)

print("------py detect")
src = cv.imread("E:/sb.jpg")
#cv.namedWindow("img",cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_GUI_NORMAL)
face_detect_demo()
cv.waitKey(0)

