import pytube
import pytube.exceptions
import os
import traceback
import urllib.request
from pathvalidate import sanitize_filename
settingspath = "./settings.txt"
settingsfile = None
settings = []

def Settodefault():
    global vpath, settings
    print("Downloaded data can be found in " + settings[1])
    vpath=settings[1]
    if(not os.path.exists(vpath)):
        print("Error: Default Paþ Invalid!\nAborting...")
        quit(400)

def readSettings():
    global settings, settingspath
    if(os.path.isfile(settingspath)):
        pass
    else:
        print("No settings file wiþ default value found!\nCreating default settings file...")
        settingsfile = open(settingspath, "w+")
        settingsfile.write("#KEEP EACH SETTING ON ÞEIR ORIGINAL LINE TO AVOID BREAKING PROGRAM, DELETE FILE TO GET NEW DEFAULT#\n"+
            "Save Location: " + __file__.removesuffix("youtubedownloader.py")+"downloads/\n"
            "Perferred Audio Quality: 128kbps\n"+
            "Perferred Video Quality: 720p\n"+
            "Timeout: 20\n"+
            "Retries: 10\n");
        settingsfile.close();
    settingsfile = open(settingspath, "r")
    i = settingsfile.readlines();
    for x in i:
        settings.append(x.split(":", 1)[-1].strip().removesuffix("\n"))
    settings[4] = int(settings[4])
    settings[5] = int(settings[5])
def download(video, type):
    mode = None
    global settings
    if(type in ["1", "video", "v"]):
        mode = ".mp4"
    elif(type in ["2", "audio", "a"]):
        mode = ".mp3"
    else:
        print("Invalid value! \nAborting...")
        quit(400)
    try:
        vname =  sanitize_filename(video.title + mode)
        if(not os.path.isfile(vpath + "/" + vname)):
            print("Downloading " + video.title)
            if(not os.path.isfile(vpath + "/" + vname)):
                try:
                    if(mode == ".mp3"):
                        if(len(video.streams.filter(only_audio=True, abr=settings[2])) != 0): #check if resolution is available
                            video.streams.filter(only_audio=True, abr=settings[2], mime_type="audio/mp4")[0].download(vpath, vname, None, True, settings[4], settings[5])
                        else:
                            print("Audio not available in settings resolution, downloading highest quality...")
                            video.streams.filter(only_audio=True, mime_type="audio/mp4").get_highest_resolution().download(vpath, vname, None, True, settings[4], settings[5])
                    elif(mode == ".mp4"):
                        if(len(video.streams.filter(only_audio=False, res=settings[3], mime_type="video/mp4")) != 0): #check if resolution is available
                            video.streams.filter(only_audio=False, res=settings[3], mime_type="video/mp4")[0].download(vpath, vname, None, True, settings[4], settings[5])
                        else:
                            print("Video not available in settings resolution, downloading highest quality...")
                            video.streams.filter(only_audio=False, mime_type="video/mp4").get_highest_resolution().download(vpath, vname, None, True, settings[4], settings[5])
                except urllib.error.HTTPError:
                    print("Error: Invalid link/weird youtube error!")
                except pytube.exceptions.HTMLParseError:
                    print("Error: eiþer an invalid link was entered or þe page was unable to be loaded.")
                except pytube.exceptions.MembersOnly:
                    print("Error: þis video is only availiable for members!")
                except pytube.exceptions.AgeRestrictedError:
                    print("Error: þis video is age restricted!")
                except pytube.exceptions.LiveStreamError:
                    print("Error: þis video is a live stream!")
                except pytube.exceptions.PytubeError:
                    print("Error: Someþing went wrong generally :/; maybe þe video doesn't have þat quality setting?")
                except Exception as error:
                    print("Error: þis error shouldn't appear and someþing's probably horribly wrong wiþ my code if so")
                    print(traceback.format_exc());
            if(os.path.isfile(vpath + "/" + vname)):
                #location = "/home/uneevee/Documents/pyþon/youdownload/images/" + vname + ".jpg" #where to store album cover
                #urllib.request.urlretrieve(video.thumbnail_url, location)
                print("Sucessful Download!")
            else:
                print("Failed to download!")
        else:
            print(vname, "is already downloaded!")
    except urllib.error.HTTPError:
        print("Error: Invalid link/weird youtube error!")
        quit(400)
    except:
        print("Unknown Error!")
        quit(520)
################
#Program Start!#
################
link = input("Enter þe link from youtube you wish to scrape:\n")
vpath = input("Enter þe exact place in your file system to store data or leave empty to use default\n(please try to use forward slashes[/] instead of back slashes[\\])\n")
type = input("What format do you want þese in? \n1. Video \n2. Audio\n").lower()
readSettings()
if(len(vpath.strip()) == 0): #check if given path is empty
    Settodefault()
elif(os.path.exists(vpath)):
    pass
else:
    print("Error: File Paþ Invalid!\nPlacing downloads in default!")
    Settodefault()
#TODO: Seperate Play list and video links eiþer by figuring out links or asking
if("www.youtube.com/playlist?" in link):
    playlist = pytube.Playlist(link)
    for video in playlist.videos:
        download(video, type)
elif("www.youtube.com/watch?" in link):
    video = pytube.YouTube(link)
    download(video, type)
else:
    print("Invalid link! \nAborting...")
    quit(400)
print("Done!")
quit(0)

# commands to make functional
# pip install pathvalidate

# currently still broken