class ScreenCrop(object):
    def __init__(self, name, values):
        self.name = name
        self.filename = values['filename']
        self.source_filename = values['source_filename']
        self.x = values['x']
        self.y = values['y']
        self.w = values['w']
        self.h = values['h']

    def getRegion(fuzz=Settings.DefaultPadding):
        return Region(x,y,w,h).grow(fuzz)


from pprint import pprint as pp
import json
from glob import glob
from os.path import join, splitext, basename, relpath

tmpdir = join(getBundlePath(), "screencap")
base_img = join(getBundlePath(), "..", "img", "base")
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

crops = {}
for key,value in image_dict:
    crops[key] = ScreenCrop(key, value)
