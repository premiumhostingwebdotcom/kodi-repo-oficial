# -*- coding: utf-8 -*-
import xbmc,xbmcgui
try:
    from YDStreamExtractor import getVideoInfo
    from YDStreamExtractor import handleDownload
    
except Exception:
    print 'importing Error. You need youtubedl module which is in official xbmc.org'
    xbmc.executebuiltin("XBMC.Notification(LiveStreamsPro,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000,"")")
    
def single_YD(url,download=False,dl_info=False):
    if dl_info:
        handleDownload(dl_info,bg=True)
        return
    else:
        info = getVideoInfo(url,quality=3,resolve_redirects=True)
    if info is None:
        print 'Fail to extract'
        return None    
    elif info and download : ##handleDownload(info,duration=None,bg=False):
        handleDownload(info,bg=True)
    else:
    
        for s in info.streams():
            try:
                stream_url = s['xbmc_url'].encode('utf-8','ignore')
                print stream_url
                return stream_url
            except Exception:
                return None 
             
