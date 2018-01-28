import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

start = False;
end = False;

def takePictureAccessor():
	global start
	start = True

def haltCam():
	global end
	end = True

def takePicture():
	global img_counter
	img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

def camOn():
	global start
	global end

	while True:
    		ret, frame = cam.read()
	    	cv2.imshow("test", frame)
	    	if not ret:
			break

		cv2.waitKey(30)

	    	if end:
			# ESC pressed
			print("Escape hit, closing...")
			cam.release()
			cv2.destroyAllWindows()
			break
	    	elif start:
			takePicture(img_counter)
			break
        

def cameraOn():
	ret, frame = cam.read()
	cv2.imshow("test", frame)
	#if not ret:
	#	break
	
	takePicture()
	cam.release()
	cv2.destroyAllWindows()


