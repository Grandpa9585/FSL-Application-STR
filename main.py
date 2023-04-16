"""
Main

UI elements formatting should only be here but for now it is:
    April 2023: where all the boilerplate code is put in initially
                refactoring the sample code into something expandable
                code will not be written as OOP just yet
                no Kivy just yet
"""

# from skimage.exposure import rescale_intensity
import numpy as numpy_object
import cv2


def main():
    video_input_object = cv2.VideoCapture(0)
    
    # camera input
    while True:
        # frame by frame processing

        ret, frame = video_input_object.read()

        cv2.imwrite("images\main_image.png", frame)

        temporary_frame_1 = cv2.imread("images\main_image.png")
        temporary_frame_2 = cv2.GaussianBlur(temporary_frame_1, (3, 3), 0)
        current_video_frame = cv2.cvtColor(temporary_frame_2, cv2.COLOR_BGR2GRAY)
        output_frame = getConvolutions("canny_edge_detection", current_video_frame)

        cv2.imshow('convolution', output_frame)

        # break condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


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
