"""bmp2supersede.py: Python script to convert 320x200 monochrome bitmaps
into loadable files that can be displayed on the Supersoft HR40, HR40b and HR80 graphics card
and my *SuperSede* clone series for the CBM PET series."""

__author__      = "InsaneDruid"
__copyright__   = "Copyright 2024, Creative Commons Zero v1.0 Universal"

class wrongwidth(Exception):
    pass
class wrongheight(Exception):
    pass

import argparse
parser = argparse.ArgumentParser(description="BMP to PET")
parser.add_argument("sourcefile", help="the name of the bmp file.")
parser.add_argument("destinationfile", help="the name of the file to be created.")
parser.add_argument("-i","--invert",action="store_true", help="write inverted image data")
args = parser.parse_args()

startaddress= 36864  #start of SuperSoft screen memory

print(f"reading file {args.sourcefile}")

with open(args.sourcefile, "rb") as file:
    
    # read pixeldata start offset
    file.seek(10) 
    pixeldata = int.from_bytes(file.read(4), byteorder='little')
    
    # read file width
    file.seek(18)
    width = int.from_bytes(file.read(4), byteorder='little') 
    
    # read file height
    file.seek(22)
    height = int.from_bytes(file.read(4), byteorder='little') 

    try:
        if width != 320:
            raise wrongwidth(width)
        if height != 200:
            raise wrongheight(height)
        
    except wrongwidth:
        print(f"{args.sourcefile} has width of {width}. Must be 320")
        quit()
    
    except wrongheight:
        print(f"{args.sourcefile} has width of {height}. Must be 200")
        quit()

    padding = width % 4
    currentline = height
    
    if args.invert==True:
        print ("image will be inverted")
    print(f"writing file {args.destinationfile}")
    
    with open(args.destinationfile,"wb") as writefile:

        writefile.write(startaddress.to_bytes(2, 'little'))
        
        # seek to first image data position
        file.seek(pixeldata)                            
        while currentline >0:
            content = file.read((width+padding) // 8)   # reading one full line of the image, last to first

            block = (currentline - 1) % 8               # line is in which 1k Block
            offset = ((currentline - 1) // 8)           # line position in block (we are writing back to front)
            seek = (block * 1024) + (offset * 40) + 2
            writefile.seek(seek)

            # invert the image data?
            if args.invert==True:                       
                for i in range(40):
                    writefile.write((255-content[i]).to_bytes(1))        
            else:
                writefile.write(content)
            
            currentline = currentline -1