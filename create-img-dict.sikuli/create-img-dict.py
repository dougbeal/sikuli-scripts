from sikuli import Finder
from org.sikuli.android import ADBScreen
from org.sikuli.android import ADBDevice
from pprint import pprint as pp
import json
from glob import glob
from os.path import join, splitext, basename

tmpdir = join(getBundlePath(), "screencap")
base_img = join(getBundlePath(), "../img/base")
json_filename = join(getBundlePath(), "image-region.json")
image_dict = {}
json_file = None
try:
    json_file = open(json_filename, 'w')
    image_dict = json.load(json_file)
except (OSError, IOError) as e:
    print "json file doesn't exist yet."

if json_file is None:
    print "ERROR: failed to open json_file {}".format(json_filename)
    exit(-1)

Debug.on(3)    
filenames = glob(join(base_img, "*.png"))
print  "{} files found".format(len(filenames))
for filename in filenames:
    basename = splitext(basename(filename))[0]
    finder = None
    cropped_images = []
    for crop_filename in filenames:
        crop_basename = splitext(basename(crop_filename))[0]
        if filename is not crop_filename and crop_basename.startswith(basename):
            cropped_images.append(crop_basename)
        
    print cropped_images
    for cropped_image in cropped_images:
        print "cropped_image " + cropped_image
        if finder is None:
            finder = Finder(filename)
        print "matching {} in {}".format(cropped_image, filename)
        # match cropped_image in filename
        finder.findAll(cropped_image)
        matches = sorted((m for m in finder), key=lambda m:m.getScore())
        
        #pp(matches)
        pp([m.toString() for m in matches])
        # add to dict
    if finder is not None:
        finder.destroy() # release the natives
    break


json.dump(image_dict, json_file)
