"""
Test

To do, find 2 identical cameras
    has to be identical otherwise the merging thing won't work at all
"""

# importing necessary things
from skimage.exposure import rescale_intensity
import numpy as numpyObj
# import argparse
import cv2


# somehow incorporate the one below with the camera feed
videoObject = cv2.VideoCapture(0)

while True:
    ret, frame = videoObject.read()

    cv2.imshow('frame', frame)

    # shows what the camera sees as is
    cv2.imwrite('images\capture.png', frame)

    # creates an object that represents the picture
    image = cv2.imread("images\capture.png")

    # converts the image to grayscale
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # for the anaglyph effect thing, make one only have red and the other have no red
    # blue 0, green 1, red 2

    """
    red = image.copy()  # shows red
    red[:, :, 1] = 0
    red[:, :, 0] = 0

    green = image.copy()
    green[:, :, 2] = 0  # filters out red
    """

    red = cv2.imread("images\left.png")
    red[:, :, 1] = 0
    red[:, :, 0] = 0

    green = cv2.imread("images\ight.png")
    green[:, :, 2] = 0

    # uses one of the convolutions above
    # opencvOutput = cv2.filter2D(gray, -1, sobelX)

    # display converted image/s
    cv2.imshow('red', red)  # to be used for phys proj
    cv2.imshow('green', green)  # to be used for phys proj

    # cv2.imshow("{} - opencv".format("thing"), opencvOutput)
    # cv2.imshow('images\image.png', gray)

    cv2.imshow('combined', cv2.addWeighted(green, 1, red, 1, 1))

    # set q as the quitting button
    # breaks the loop when the user desires
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # was  used to test if the code was working, no longer needed
    """
    if cv2.waitKey(1) & 0xFF == ord('e'):
        image = cv2.imread("images\capture.png")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite('images\image.png', gray)
    """

videoObject.release()

cv2.destroyAllWindows()
# ________________________________________end_of_code_______________________
