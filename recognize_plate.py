import pytesseract
import os
from gtts import gTTS
import cv2


def Recognize_plate(plate):

	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Enter your path where tesseract-ocr is installed

	curr_dir = os.getcwd()
	
	#converting the image of cropped plate to grayscale
	plate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
	
	#showing the grayscale image of plate, press 0 to continue when the image pops up...
	cv2.imshow('gray_plate', plate)
	cv2.waitKey(0)

	#Use tesseract to convert number in theimage into string by using its OCR Engine
	text = pytesseract.image_to_string(plate, lang='eng')
	print("Number is : ", text)

	if check(text):
		print("vehicle is allowed")
		#creating and opening a text file to write the license plate number
		plate_number = open(curr_dir + "/plate_number.txt","w")

		#writing the license plate number into the text file.
		plate_number.write(text)

		#finally we need to close the text file.
		plate_number.close()

		str12 = "Vehicle is allowed"
		language = 'en'
		myobj = gTTS(text=str12, lang=language, slow=False)
		myobj.save("/Users/srinu/Desktop/wel.mp3")
		os.system("/Users/srinu/Desktop/wel.mp3")
	else:
		print("vehicle is not allowed")
		str12 = "Vehicle is restricted from entering"
		language = 'en'
		myobj = gTTS(text=str12, lang=language, slow=False)
		myobj.save("/Users/srinu/Desktop/wel.mp3")
		os.system("/Users/srinu/Desktop/wel.mp3")


def check(text):
	str1=text[0:2]
	if str1 != "TN":
		return False
	else:
		return True