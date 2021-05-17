from pathlib import Path
from PIL import Image
from optparse import OptionParser
import sys
import os

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="Image file name. Ext: picture.png", metavar="FILE")
parser.add_option("-d", "--directory", dest="directory",
                  default='./', help='specify directory')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

(options, args) = parser.parse_args()

if options.filename is None:
    print('Filename is required')
else:
    FOLDER = options.directory
    FILE = options.filename
    FULL_PATH_FILE = os.path.abspath(''.join([FOLDER, FILE]))

    screen_shot = Path(FULL_PATH_FILE)

    if screen_shot.is_file():
        # Opens a image in RGB mode
        im = Image.open(screen_shot)

        # Setting the points for cropped image
        x = 750
        y = 226
        width = 410
        height = 676

        # Cropped image of above dimension
        # (It will not change orginal image)
        im1 = im.crop((x, y, x + width, y + height))

        # save a image using extension
        im1.save(''.join(['crop_', FILE]))
    else:
        print('Image file does not exist')
