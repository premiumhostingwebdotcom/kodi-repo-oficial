import xbmc
import xbmcaddon
import download
import extract
import os


ADDON    = xbmcaddon.Addon(id = 'script.tvguideaarronlee')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras   = os.path.join(datapath, 'extras')
logos    = os.path.join(extras, 'logos')
nologos  = os.path.join(logos, 'None')
dest     = os.path.join(extras, 'logos.zip')
url      = 'http://host.premiumhostingweb.com/logos.zip'


try:
    os.makedirs(logos)
    os.makedirs(nologos)
except:
    pass
 
download.download(url, dest)
extract.all(dest, extras)

try:
    os.remove(dest)
except:
    pass