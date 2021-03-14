"""
This module will contian the needed functions to register images.
This module also relies heavily on numpy arrays. Please see the documentation to better understand
this module. 

Numpy Documentation: https://numpy.org/doc/stable/contents.html
"""

import numpy as np
from numpy.lib.function_base import average
import simplejpeg
from tqdm import tqdm  #loading bar function


def generate_test_array():
    """
    A function to generate a test image for me to work with
     while I make functions.
    """

    with open("./stack/sample1.jpg", 'rb') as pic:
        numpy_array = simplejpeg.decode_jpeg(pic.read())

    np.save('test_pixel_array.npy', numpy_array, allow_pickle=False)


sample_pixel_array = np.load('./test_pixel_array.npy', allow_pickle=False)


def detect_stars(pixel_array, demo):
    """
    This function will accept a decoded image as a numpy array. 
    It will then find the stars in the image by measuring their relative brightness
     compared to the average brightness of the image as a whole.

    This method is obviously not the best, but it will do for now. 
    In the future I'd like to find the average brightness of the darkest
     pixels and find more stars by tightening the tolerances on what is and isn't a star.
    """

    print("Looking for stars >= 225 in brightness...")

    #star_pixel_mask is a numpy array that will be a pure black and
    #pure white image. Any pixels detected at or above
    #225 in the pixel_array will get a cooresponding
    #pixel in the star_pixel_mask array of pure white.
    #All other pixels will be black.

    #star_pixel_mask is also initialized to the same shape as the
    #provided numpy array.

    height, width, channels = pixel_array.shape

    #Setting mask to brightness >= 200 across all channels.
    mask = np.where(
        np.average(pixel_array[0, 0, ...]) >= 200, [255, 255, 255], [0, 0, 0])

    print(mask)

    star_pixel_mask = np.zeros(pixel_array.shape, dtype='uint8')
    star_pixel_mask[mask] = 255

    #dtype must = unisnged integer 8 because simple jpg
    #can oly work with this type.

    if demo == True:
        with open('./star_detection.jpg', 'wb') as file:
            data = simplejpeg.encode_jpeg(star_pixel_mask, 100)
            file.write(data)


detect_stars(sample_pixel_array, True)
