# BMP-2-SuperSede
Python script to convert 320x200 monochrome bitmaps into loadable files that can be displayed on the Supersoft HR40, HR40b and HR80 graphics card and my *SuperSede* clone series for the CBM PET series.

# The Background
The graphics cards of the HRx0 series can display monochrome (white on black or green on black, depending on the PET model) images with a resolution of 320x200 pixels. The lines of the image are stored interleaved into 8 1K blocks of screen memory, starting with the top line on address 36864 ($9000). BMP files store the lines linearly in a bottom-first order. This script reads the BMP header, checks that the image has the correct dimensions, and rearranges the image lines to create a file for the CBM PET with load address $9000. This file can be loaded directly into the screen memory of the HR40, HR40b or HR80 using the standard *load "file",8* basic command.

# The Usage
* Create a suitable 320x200x1Bit BMP file (e.g.: Windows Paint: Select *save as: bmp* and set the file type to *monochrome bmp*.
* Run the script: bmp2supersede.py sourcefile destinationfile
* Transfer the destinationfile to your PET equipped with a HR40, HR40b or HR80 card and simply load the file like any program.

# The License
This work is licensed under a Creative Commons Zero v1.0 Universal License.

See https://creativecommons.org/publicdomain/zero/1.0/.
