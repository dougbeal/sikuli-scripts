from sikuli import *

class ScreenCrop(object):
    def __init__(self, name, values):
        self.name = name
        self.filename = values['filename']
        self.source_filename = values['source_filename']
        self.x = values['x']
        self.y = values['y']
        self.w = values['w']
        self.h = values['h']

    def getRegion(self, fuzz=Settings.DefaultPadding):
        return Region(self.x,self.y,self.w,self.h).grow(fuzz)


from pprint import pprint as pp
import json
from glob import glob
from os.path import join, splitext, basename, relpath

base_img = join(getBundlePath(), "..", "img", "base")
json_filename = join(getBundlePath(), "..", "create-img-dict.sikuli", "image-region.json")
image_dict = {}
json_file = None
try:
    json_file = open(json_filename, 'r')
    image_dict = json.load(json_file)
except (OSError, IOError) as e:
    print "json file doesn't exist yet."

if json_file is None:
    print "ERROR: failed to open json_file {}".format(json_filename)
    exit(-1)

crops = {}
for key,value in image_dict.iteritems():
    crops[key] = ScreenCrop(key, value)
