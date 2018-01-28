from flask import Flask
from flask_ask import Ask, statement, question
import serial
import cv2

def save_image():
	camera_port=0
	ramp_frames = 30
	camera = cv2.VideoCapture(camera_port)

	for i in xrange(ramp_frames):
		temp = get_image(camera)
	print("Taking image...")
	camera_capture = get_image(camera)
	file = "/home/linaro/Desktop/test_image.png"
	cv2.imwrite(file, camera_capture)

	del(camera)

def get_image(cam):
	retval, im = cam.read()
	return im
########################################################
app = Flask(__name__)

ask = Ask(app, '/')

@ask.launch
def default():
	return question("Welcome to aloud!")

@ask.intent("readAloud")
def readAloud():
	save_image()
	pageString = "aloud"
	return question(pageString)

@ask.intent("defineText")
def defineText():
	definition = "definition"
	return question(definition)

@ask.intent('AMAZON.StopIntent')
def stop():
	return statement("good bye!")

@ask.session_ended
def session_ended():
	return "{}", 200

if __name__ == "__main__":
	app.run(debug=True)
