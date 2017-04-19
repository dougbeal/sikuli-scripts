from sikuli import *
from org.sikuli.android import ADBScreen
from org.sikuli.android import ADBDevice
from pprint import pprint as pp
tmpdir = os.path.join(getBundlePath(), "screencap")
if not os.path.exists(tmpdir):
  os.mkdir(tmpdir) 
Debug.on(3)

from .. import ffbe

screen = ADBScreen.start() # get the one attached device
if not screen:
  exit(1)

dev = screen.getDevice()
use(screen) # set as the default region  

start = ffbe.crops['ffbe-startscreen-tap']
if exists(start.filename, start.getRegion()):
  tap(start.getRegion().center())
