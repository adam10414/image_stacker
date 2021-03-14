from os import listdir
import subprocess

import numpy
from tqdm import tqdm  #loading bar function
from simplejpeg import decode_jpeg_header
from simplejpeg import decode_jpeg
from simplejpeg import encode_jpeg

#Gathering file names from ./stack and storing them in a list/array.
file_list = listdir('./stack')
#Filtering out .DS_Store from file list.
#.DS_Store is a system generated file that's unavoidable.
file_names = [x for x in file_list if not '.DS_Store' in x]
number_of_files = len(file_names)

#Pulling header information from the first image in the stack
#  to construct a result_image image of the same demensions.
with open('./stack/' + file_names[0], 'rb') as image:
    data = image.read()
    #header_info = (4480, 6720, 'YCbCr', '422')
    #header_info = (hieght, width, color_space, color_subsampling)
    header_info = decode_jpeg_header(data)
    rows = range(header_info[0])
    pixels_per_row = range(header_info[1])

result_image = []  #A blank image that will eventually become our result image.

#Filling image with rows.
print()
print("Generating a blank image with the demensions of your image stack...")
for row in tqdm(rows):
    result_image.append([])

    #Filling pixel values per row.
    for pixel in pixels_per_row:
        #Pixel values are set to 0 so we can add other values to them later.
        result_image[row].append([0, 0, 0])

print()

#Opening each file and adding their values to the result_image list/array.
print("Adding the stack to our base image...")

#Something is taking a long time here, and I don't know what...
#Perhaps memory being re-allocated?
for file in tqdm(file_names):
    stack_path = './stack/'

    #Keeping the computer from falling asleep...
    print("Caffeinating...")
    subprocess.Popen('caffeinate')

    with open(stack_path + file, 'rb') as image:
        data = image.read()
        print(file)
        current_image = decode_jpeg(data)
        """
        #Adding the pixel values to result image...one at a time.
        for row in tqdm(current_image):
            for pixel in row:
                for channel in pixel:
                    result_image[row][pixel] += channel
        """

        #I know this is gross, but I need/want something quick and dirty to see a result.

        #TO DO:
        #MAKE THIS A NUMPY ARRAY, IT'S A GAZILLIION TIMES FASTER!
        #DO IT FOR REAL, JESUS CHRIST YOU'RE DUMB FOR DOING IT THIS WAY.

        row = 0
        while row < len(current_image):
            pixel = 0
            #print(f"Added row {row} to result image...")
            while pixel < len(current_image[row]):
                channel = 0
                while channel < len(current_image[row][pixel]):
                    result_image[row][pixel][channel] = result_image[row][
                        pixel][channel] + current_image[row][pixel][channel]

                    channel += 1
                pixel += 1
            row += 1
print()

#Iterating over every row to divide the pixel values by the number of files.
#Then we will be rounding to the nearest integer.
print("Averaging all the pixels...")
"""
for row in tqdm(result_image):
    for pixel in row:
        for channel in pixel:
            channel = channel / number_of_files
            channel = round(channel)
"""

row = 0
while row < len(result_image):
    pixel = 0
    print(f"Averaging row {row} to result image...")
    while pixel < len(result_image[row]):
        channel = 0
        while channel < len(result_image[row][pixel]):
            #Averaging channel values.
            result_image[row][pixel][
                channel] = result_image[row][pixel][channel] / number_of_files

            #Rouding channel values to nearest int.
            result_image[row][pixel][channel] = round(
                result_image[row][pixel][channel])

            channel += 1
        pixel += 1
    row += 1

result_image = numpy.array(result_image, dtype='uint8')

with open('./output.jpg', 'wb') as image:
    data = encode_jpeg(result_image, 100)
    image.write(data)
