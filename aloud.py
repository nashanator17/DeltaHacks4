from flask import Flask
from flask_ask import Ask, statement, question
from googletrans import Translator
import serial
import cv2
import requests

#translator
translator = Translator()

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese',
    'zh-tw': 'chinese traditional',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

LANGCODES = dict(map(reversed, LANGUAGES.items()))

#camera functions
def save_image():
	camera_port=0
	ramp_frames = 30
	camera = cv2.VideoCapture(camera_port)

	for i in xrange(ramp_frames):
		temp = get_image(camera)
	camera_capture = get_image(camera)
	file = "/home/linaro/Desktop/deltaHack4-stdlib/JackLinJQL/image-translator/test_image.jpg"
	cv2.imwrite(file, camera_capture)

	del(camera)

def get_image(cam):
	retval, im = cam.read()
	return im

def imageTranslate():
	response = requests.get("http://localhost:8170/JackLinJQL/image-translator/")	
    	return(response.content)

#start of flask app
app = Flask(__name__)

ask = Ask(app, '/')

@ask.launch
def default():
	return question("Welcome to aloud!")

@ask.intent("readAloud")
def readAloud():
	save_image()
	pageString = imageTranslate()
	print(pageString)
	return question(pageString)

@ask.intent("defineText", mapping={'word': 'word'})
def defineText(word):
	print(word)
	response = requests.get("http://localhost:8171/JackLinJQL/define-word/", headers={"word": word})
	definition = response.content
	return question(definition)

@ask.intent("translateText", mapping={'word': 'word', 'targetLang': 'language'})
def translateText(word, targetLang):
	destination = LANGCODES.get(targetLang.lower())
	translation = translator.translate(word, destination, src = 'en')
	return question(translation.text)

@ask.intent('AMAZON.StopIntent')
def stop():
	return statement("good bye!")

@ask.session_ended
def session_ended():
	return "{}", 200

if __name__ == "__main__":
	app.run(debug=True)
