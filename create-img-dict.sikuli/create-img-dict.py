from sikuli import Finder
from org.sikuli.android import ADBScreen
from org.sikuli.android import ADBDevice
from pprint import pprint as pp
import json
import fnmatch
import glob

tmpdir = os.path.join(getBundlePath(), "screencap")
base_img = os.path.join(getBundlePath(), "../img/base")
json_filename = os.path.join(getBundlePath(), "image-region.json")
image_dict = {}
try:
    json_file = open(json_filename, 'w')
    image_dict = json.load(json_file)
except (OSError, IOError) as e:
    print "json file doesn't exist yet."

Debug.on(3)    
filenames = glob.glob(os.path.join(base_img, "*.png"))
print  "{} files found".format(len(filenames))
for filename in filenames:
    basename = os.path.splitext(os.path.basename(filename))[0]
    finder = None
    sections = list(name for name in filenames if filename is not name and os.path.splitext(os.path.basename(name))[0].startswith(basename))
    print sections
    for section in sections:
        print "section " + section
        if finder is None:
            finder = Finder(filename)
        print "matching {} in {}".format(section, filename)
        # match section in filename
        finder.findAll(section)
        matches = sorted((m for m in finder), key=lambda m:m.getScore())
        
        #pp(matches)
        pp([m.toString() for m in matches])
        # add to dict
    if finder is not None:
        finder.destroy() # release the natives
    break

json.dump(image_dict, json_file)