from sikuli import *
from org.sikuli.android import ADBScreen
from org.sikuli.android import ADBDevice
from pprint import pprint as pp

imgdir = os.path.join(getBundlePath(), "..", "img", "craft")
tmpdir = os.path.join(getBundlePath(), "tmp")
if not os.path.exists(tmpdir):
  os.mkdir(tmpdir) 
#print imgdir
#pp( os.listdir(imgdir) )
addImagePath(imgdir)

complete = "craft-complete.png"
yes = "craft-craft-yes.png"
craft = "craft-craft.png"
empty = "craft-empty-slot.png"
equ_acc_sel = "craft-equipment-accessory-sel.png"
equ_acc_unsel = "craft-equipment-accessory-unsel.png"
equ_sel = "craft-equipment-sel.png"
equ_unsel = "craft-equipment-unsel.png"

choco_egg = "craft-equipment-accessory-choc-egg.png"
great_egg = "craft-equipment-accessory-great-egg.png"

Debug.on(3)

screen = ADBScreen.start() # get the one attached device
if not screen:
  exit(1)

dev = screen.getDevice()
use(screen) # set as the default region  
#img = screen.capture()
#img.save(tmpdir)
#wait(1)
#screen.capture()
#wait(1)
#screen.capture()

#img = screen.capture()
#print img
#img.save("screen.png", )
if exists(equ_sel, 0):
  print "equipment select screen"
else:
  print "not found"
  screen.capture().save(tmpdir, equ_sel + "-not_found.png")

# gsearch = "1492317040556.png" # to detect home screen
# img = "1492317073966.png" # an icon to tap

# top = newRegion(Location(0, 0), 300, 300) # top left corner
# iconRow = newRegion(Location(0, 600), 1200, 300) # an icon band
# dev.printDump("input")
# for i in range(3): # just do it 3 times 
#   screen.aKey(ADBDevice.KEY_HOME) # tap the home button
#   screen.wait(gsearch, 10) # wait for home screen
#   screen.click(img) # click icon
#   wait(5) # to give time to the triggered action to process
