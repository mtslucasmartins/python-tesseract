from wand.image import Image as WImage
from PIL import Image as PImage

import pytesseract

import cv2

import io
import os 


img = "static/out.jpg"

def load_image_grayscale(img, preprocess="thresh"):
    print("image conversion")
    # load the example image and convert it to grayscale
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # check to see if we should apply thresholding to preprocess the
    # image
    if preprocess == "thresh":
        print("threshold")
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif preprocess == "blur":
        print("blur")
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    print("writing...")
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    print("writing done!")

    return filename

# 
if __name__ == "__main__":
    filename = load_image_grayscale(img, "thresh")
    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(PImage.open(filename), config='--psm 6 --oem 3 -c preserve_interword_spaces=1')
    os.remove(filename)

    print(text)
    # show the output images
    # cv2.imshow("Image", img)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)
