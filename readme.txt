This is a for fun project intended to get some better astrophotography photos. 
This program will evaluate a series of images, average out the pixel values, and produce a new image with the averaged values.
The idea is that while noise is random, and the content (signal) is not, then we can increase the Signal to Noise Ratio (SNR) by averaging the pixel values across a lot of images.

Installation: 
1. Clone this repo to your local directory.
2. In terminal, navigate to your local dir, and run pip3 install -r requirements.txt

Usage: 
1. Some sample images have been provided in the stack dir. 
2. In terminal: python3 image_stacker.py 
3. The porgram should output a new image to the root dir.


Notes: 
- At this time, this porgram only accepts .jpg images. Stretch goal is to decode and encode raw image files so they can be worked in photoshop.
- If you want RAW photo editing, I would recommend to edit the RAW images first, export to jpeg, and use those images for this program to stack. I would recommend keeping editing light as most editing introduces more noise which reduces the effectiveness of this program.
- It's important that the camera is on a tripod so all of the pixels are exactly aligned. Any movement will blur the image.
- If you do not have a star tracker to track objects across the sky, you'll want to use the 500 rule. 
   * 500 rule = 500 / focal length. The result is about as much time you have before the stars start moving within the frame.

- You can replace the sample images with your own in ./stack, ensure that they are from 1 set of images. Do not add any other directories here or any other kind of files.
- All images in stack dir should be the same demensions.