"""
    chairs in the court
    tent surrounds the court (8:00 to 8:30 am)

    consider cropping the feed and doing adjustments in code
    Too close won't work
    focal length
    missing third layer????



    to do
    1. border
    2. adjust focal length
    3. set viewing point for best experience
"""

# from skimage.exposure import rescale_intensity
import numpy as numpy_object
import cv2
import cv


def main():
    video_input_object = cv2.VideoCapture(1)
    video_input_object_2 = cv2.VideoCapture(2)
    
    # camera input
    while True:
        # frame by frame processing

        ret0, frame = video_input_object.read()
        ret1, otherFrame = video_input_object_2.read()

        if ret0:
            cv2.imwrite("images\main_image.png", frame)#cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE))

        if ret1:
            cv2.imwrite("images\mainer_image.png", cv2.rotate(otherFrame, cv2.ROTATE_180))
            # temp = cv2.rotate(cv2.imread("images\mainer_image.png"), cv2.ROTATE_180)
            # cv2.imwrite("images\mainer_image.png", temp)

        """temporary_frame_1 = cv2.imread("images\main_image.png")
        temporary_frame_2 = cv2.GaussianBlur(temporary_frame_1, (3, 3), 0)
        current_video_frame = cv2.cvtColor(temporary_frame_2, cv2.COLOR_BGR2GRAY)
        output_frame = getConvolutions("canny_edge_detection", current_video_frame)"""

        red = cv2.imread("images\main_image.png")
        red[:, :, 2] = 0    # red
        #red[:, :, 1] = 0    # filter green
        #red[:, :, 0] = 0    # filer blue

        # red[:, :, 2] = 0

        green = cv2.imread("images\mainer_image.png")
        #green[:, :, 2] = 0
        green[:, :, 1] = 0
        qgreen[:, :, 0] = 0

        # green[:, :, 1] = 0
        # green[:, :, 0] = 0

        # cv2.imshow('red', cv2.resize(red, (0, 0), fx=0.5, fy=0.55))  # to be used for phys proj
        # cv2.imshow('green', cv2.resize(green, (0, 0), fx=0.5, fy=0.55))  # to be used for phys proj

        factor = 2.2  # resize
        cv2.imshow('combined', cv2.addWeighted(
            cv2.resize(green, (0, 0), fx=factor, fy=factor), 1,
            cv2.resize(red, (0, 0), fx=factor, fy=factor), 1, 1))

        factor_operator = 1
        cv2.imshow('operator', cv2.addWeighted(
            cv2.resize(green, (0, 0), fx=factor_operator, fy=factor_operator), 1,
            cv2.resize(red, (0, 0), fx=factor_operator, fy=factor_operator), 1, 1))

        # break condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('e'):
            cv2.imwrite("images\capture.png", cv2.addWeighted(
            cv2.resize(green, (0, 0), fx=factor, fy=factor), 1,
            cv2.resize(red, (0, 0), fx=factor, fy=factor), 1, 1))


# convolution
def getConvolutions(convolution_label, video_frame_object=None):
    # construct average blurring kernels used to smooth an image
    smallBlur = numpy_object.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
    largeBlur = numpy_object.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
    cannyEdgeDetection = cv2.Canny(image=video_frame_object, threshold1=50, threshold2=100)
    # construct a sharpening filter
    sharpen = numpy_object.array((
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]), dtype="int")

    # construct the Laplacian kernel used to detect edge-like
    # regions of an image
    #
    # also useful in detecting blur in an image
    laplacian = numpy_object.array((
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]), dtype="int")

    # construct the Sobel x-axis kernel
    sobelX = numpy_object.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int")

    # construct the Sobel y-axis kernel
    sobelY = numpy_object.array((
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]), dtype="int")

    # construct the kernel bank, a list of kernels
    kernelBank = {
        "small_blur": smallBlur,
        "large_blur": largeBlur,
        "sharpen": sharpen,
        "laplacian": laplacian,
        "sobel_x": sobelX,
        "sobel_y": sobelY,
        "canny_edge_detection": cannyEdgeDetection
    }

    return kernelBank[convolution_label]


if __name__ == "__main__":
    main()
