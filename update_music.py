import time
import os
import datetime
from time import gmtime, strftime

# Directory doesn't have to currently exist in your filesystem, but the rive must exist
directory_to_save_files_to = "D:\Media\Music\YouTube"

# Get the drive letter
drive = directory_to_save_files_to.split(":")
drive = drive[0]+":"

# Change to the drive specified and change directory to the directory specified
os.chdir(drive)
if not os.path.exists(directory_to_save_files_to):
    os.makedirs(directory_to_save_files_to)
os.chdir(directory_to_save_files_to)

music_dict = {
             "Adhesive Wombat"          :"https://www.youtube.com/user/AdhesiveWombat",
             "Alan Walker"              :"https://www.youtube.com/user/DjWalkzz",
             "Approaching Nirvana"      :"https://www.youtube.com/channel/UC9EzN5XNxhxqHZevM9kSuaw",
             "Argofox"                  :"https://www.youtube.com/channel/UC56Qctnsu8wAyvzf4Yx6LIw",
             "Audiopad"                 :"https://www.youtube.com/channel/UCw-i0xtpZQN7Rtx8qcj9rpw",
             "Monstercat Instinct"      :"https://www.youtube.com/channel/UCp8OOssjSjGZRVYK6zWbNLg",
             "Monstercat Uncaged"       :"https://www.youtube.com/user/MonstercatMedia",
             "Mr Suicide Sheep"         :"https://www.youtube.com/user/MrSuicideSheep",
             "Niconico Sou"             :["https://www.youtube.com/playlist?list=PLie6pN6jKiHzD1xzsnQNHPEPvaYsdhnCm",
                                          "https://www.youtube.com/playlist?list=PLie6pN6jKiHx6PfsVGwb2kfJBgfpt8rYk"],
             "NoCopyrightSounds"        :"https://www.youtube.com/user/NoCopyrightSounds",
             "Spinnin Records"          :"https://www.youtube.com/user/SpinninRec",
             "Teminite"                 :"https://www.youtube.com/channel/UCc_bv_5nmxy2xnPNg9kP3Rg",
             "Underwaterbeats"          :"https://www.youtube.com/channel/UC0b6HyntPOxiAwvHNWE9oQw",
             "xKitoMusic"               :"https://www.youtube.com/channel/UCMOgdURr7d8pOVlc-alkfRg",
             "v The Musical"            :"https://www.youtube.com/playlist?list=PL9sDv6wlbrSsPbirEhr9OvNS7evf4rYso",
             "SDVX"                     :"https://www.youtube.com/playlist?list=PLzb9PNZ9VsbDXTNkrWS0e5wvmjIRv_XyV",
             "Older Music"              :"https://www.youtube.com/playlist?list=PL9sDv6wlbrSsKv6o2oAWukRxs47nG_NBZ",
             "YourFavoriteMartian"      :"https://www.youtube.com/user/Yourfavoritemartian",
             "Rhett and Link"           :"https://www.youtube.com/playlist?list=PL5D3BFF118D8928BC",
             "Beat Saber"               :"https://www.youtube.com/playlist?list=PL1h7TB-szIt4z0hUjBsKcvJFc3pH5TK1h",
             "Rocket League OST"        :"https://www.youtube.com/playlist?list=PLfG0HYK6dC4xySMZ6JdLfXri52cpsS5xr",
             }

def download_function(channel):
    """
    1. Create the desired folder if it is not already created
    2. Navigate to the desired folder
    3. Download the desired playlist or video
    4. Clear the Screen
    5. Return to the previous folder
    """
    if not os.path.exists("{}".format(channel)):
        os.makedirs("{}".format(channel))
    os.chdir("{}".format(channel))
    os.system('youtube-dl --extract-audio -i --audio-format mp3 --audio-quality 0 --no-part --no-mtime --embed-thumbnail -o "%(title)s.%(ext)s" --xattrs --add-metadata {}'.format(music_dict[channel]))
    os.system('cls')
    os.chdir('..')

while True:
    """
    On Monday Morning at 7:30:00AM it will update the channels. Uses 24 hour time
    Monday      = 0
    Tuesday     = 1
    Wednesday   = 2
    Thursday    = 3
    Friday      = 4
    Saturday    = 5
    Sunday      = 6
    """
    if strftime("%H:%M:%S%p") == '07:30:00AM' and datetime.datetime.today().weekday() == 0:
        for channel in music_dict:
            if isinstance(music_dict[channel],str):
                # This is for all the dictionary keys whose values are a single YouTube link
                download_function(channel)
            elif not isinstance(music_dict[channel],str):
                # This is for all the dictionary keys whose values are a list of YouTube links
                for playlist in music_dict[channel]:
                    download_function(channel)