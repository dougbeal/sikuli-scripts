from sikuli import *
from org.sikuli.android import ADBScreen
from org.sikuli.android import ADBDevice
from pprint import pprint as pp
import json
import fnmatch

tmpdir = os.path.join(getBundlePath(), "screencap")
base_img = os.path.join(getBundlePath(), "../img/base")
json_file = os.path.join(getBundlePath(), "image-region.json")

try:
    json.load(open(json_file, 'w'))
except (OSError, IOError) as e:
    print "json file doesn't exist yet."

Debug.on(3)    
filenames = os.listdir(base_img)
for filename in filenames:
    basename = os.path.basename(filename)
    Finder f = None
    for section in fnmatch.filter(filenames, basename + "*"):
        if finder is None:
            finder = Finder(os.path.join(base_img, basename))
        image = os.path.join(base_img, section)
        print "matching %s in %s" % section, filename
        # match section in filename
        matches = [m for m in finder.findAll(image) ]
        pp([m.toString() for m in matches])
        # add to dict
    if finder is not None:
        finder.destroy() # release the natives
