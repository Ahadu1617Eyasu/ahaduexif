#!user/bin/env Python3
# Tool Created By Ahadu Eyasu(Alpha)
# Tool Name BetaXif
# Note:
# BetaXif is used to extract image location.
# This program is for .JPG & .TIFF format files and it might support .HEIC, .PNG & Other Formats.

from lib2to3.pytree import convert
import os
import sys
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def create_google_maps_url(gps_coords):
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]), float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

def convert_decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees

# Logo Print
print(re+"                            -+/`                                      .:hs/`                        ")
print(re+"                         -odmNNmho.                                 -ydmmNNmy/`          ")           
print(re+"                      `/hmNNNo::-`                                    ```oNNNNdo.                ")   
print(re+"                    `+dNNNNNN:                                           oNNNNNNms.               ")  
print(re+"                  `+dNNNNNNNNo                `:s+`                      dNNNNNNNNmo.         ")      
print(re+"                 :hNNNNNNNNNNd`             `-/:oNh-                    :NNNNNNNNNNNd/          ")    
print(re+"               `omNNNNNNNNNNNNo             ./mNmNNmh+-`               `dNNNNNNNNNNNNNs`            ")
print(re+"              `yNNNNNNNNNNNNNNN:           .+mNNNNNNNNdh-             `yNNNNNNNNNNNNNNNy`        ")   
print(re+"             `yNNNNNNNNNNNNNNNNm-           oNNNNmNNNNdmd.           `sNNNNNNNNNNNNNNNNNy`          ")
print(re+"             sNNNNNNNNNNNNNNNNNNm:          dNNNmymNmNNNNd/         `yNNNNNNNNNNNNNNNNNNNs        ")  
print(re+"            +NNNNNNNNNNNNNNNNNNNNmo`        mNNNN++y-hmmdNmy-     `/dNNNNNNNNNNNNNNNNNNNNN/         ")
print(re+"           `mNNNNNNNNNNNNNNNNNNNNNNd/`      yNNNNh.`  /mmhhm:    :hNNNNNNNNNNNNNNNNNNNNNNNd`        ")
print(re+"           +NNNNNNNNNNNNNNNNNNNNNNNNNh/`    :NNNNNo    -mN:/  `:yNNNNNNNNNNNNNNNNNNNNNNNNNN:        ")
print(re+"           sNNNNNNNNNNNNNNNNNNNNNNNNNNNh+.   yNNNNN/    ./-`.+hNNNNNNNNNNNNNNNNNNNNNNNNNNNN+       ") 
print(re+"           hNNNNNNNNNNNNNNNNNNNNNNNNNNNNNms-`.dNNNNN+`  `-ohNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNo        ")
print(re+"           yNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNdymNNNNNNhyydNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN/        ")
print(re+"           +NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN.        ")
print(re+"           -NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNNNNNNNNNhhmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd           ")
print(re+"            dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNs--mNNNNNNNNs  -mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNo                  ")
print(re+"            /NNNNNNNNNNNNNNNNNNNNNNNNNNNNNo   dNNNNNNNNd.  :NNNNNNNNNNNNNNNNNNNNNNNNNNNNNm`                      ")
print(re+"             dNNNNNNNNNNNNNNNNNNNhhdNNNNNN`  :NNNNNNNNNNd.  yNNNNmyo+sdNNNNNNNNNNNNNNNNNNo                              ")
print(re+"             :NNNNNNNNNNNNNNNNNd.   `/hNNm   yNNNNNNNNNNNd. .NNm/`    `dNNNNNNNNNNNNNNNNd`                                       ")
print(re+"              sNNNNNNNNNNNNNNNN/       :mm   hNNNNNNNNNNNNh  hm-       sNNmddNNNNNNNNNNm-                                                  ")
print(re+"              `hNNNNNNNd+:..:yN+        .d-  sNNNNNNNNNNNNN/ os        yh:`  `:hNNNNNNN/                                                       ")
print(re+"               `hNNNNNy`      -o`        `+  .mNNNNNNNNNNNNd -/       .:       `mNNNNN/                                         ")
print(re+"                `sNNNN/         `         .-  :NNNNNNNNNNNNN `-                 hNNNd-                                                  ")
print(re+"                  +mNNo                    .`  sNNNNNNNNNNNm  -                `mNNy.                                                      ")
print(re+"                   -dNm.                       +NNNNNNNNNNNy                   +Nm+`                                                       ")
print(re+"                    `+dh`                    `/mNNNNNNNNNNm-                  /mo.                                                     ")
print(re+"                      `+s.               `-/sdNNNNNNNNNNNm:                 `:o.                                                            ")
print(re+"                        `--.         `-+ydmNNNNNNNNNNNNds.                 --`                                                      ")
print(re+"                          ``       .+hmNNNNNNNNNNNmdhs/.                   `                                                     ")
print(re+"                                  /dNNNNNNNNmdyo/-..`                                                                                  ")
print(re+"                                `sNNNNNNNds:.`                                                                                        ")
print(re+"                               -sNNNNNNd/`          ``     ``....``                                                               ")
print(re+"                             .smNNNNNNh.          `/d+:/++osssyyhdhy+-`                                                ")
print(re+"                            .dNNNNNNNd`       ``./ody/:-.``    `.:sNNNh:                                           ")
print(re+"                            +omNNNNNNh       ....` `               yNNNm                                                ")
print(re+"                            : dNNNNNNN+`                         `-dNNNh                                            ")
print(re+"                              dyhNNNNNNms/.`                 `.:ohNNNNd.                                           ")
print(re+"                              + `+dNNNNNNNNdys+:-..```..-:/oyhmNNNNmh/`                                 ")
print(re+"                                  `+NNNNNNNNNNNNNNNNNNNNNNNNNNNmmy+-                          ")      
print(re+"                                    :dNs+oshdmmmNNNNNNNNNNmmds+-`                                            ")
print(re+"                                      ::.     `--::////::-.                                                                                 ")
print("____       _       __  ___  __")
print("| __ )  ___| |_ __ _\ \/ (_)/ _|")
print("|  _ \ / _ \ __/ _` |\  /| | |_")      
print("| |_) |  __/ || (_| |/  \| |  _|")
print("|____/ \___|\__\__,_/_/\_\_|_|")
print(gr+"Tool Created By Ahadu Eyasu(Alpha)")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             


while True:
    output_choice = input("How do you want to resive the output:\n\n1 - File\n2 - Terminal\nEnter choice here: ")
    try:
        conv_val = int(output_choice)
        if conv_val == 1:
            sys.stdout = open("exif_data.txt", "w")
            break
        elif conv_val == 2:
            break
        else:
            print("You entered an incorrect option, please try again...")
    except:
        print("You entered an invalid option, please try again...")
        
cwd = os.getcwd()
os.chdir(os.path.join(cwd, "images"))
files = os.listdir()

if len(files) == 0:
    print("You don't have files in the ./images folder.")
    exit()
    
for file in files:
    try:
        image = Image.open(file)
        print(f"_______________________________________________________________{file}_______________________________________________________________")
        gps_coords = {}
        if image._getexif() == None:
            print(f"{file} contains no exif data.")
        else:
            for tag, value in image._getexif().items():
                tag_name = TAGS.get(tag)
                if tag_name == "GPSInfo":
                    for key, val in value.items():
                        print(f"{GPSTAGS.get(key)} - {val}")
                        if GPSTAGS.get(key) == "GPSLatitude":
                            gps_coords["lat"] = val
                        elif GPSTAGS.get(key) == "GPSLongtude":
                            gps_coords["lon"] = val 
                        elif GPSTAGS.get(key) == "GPSLatitudeRef":
                            gps_coords["lat_ref"] = val
                        elif GPSTAGS.get(key) == "GPSLongitudeRef":
                            gps_coords["lon_ref"] = val
            else:
                print(f"{tag_name} - {value}")
            if gps_coords:
                print(create_google_maps_url(gps_coords))
    except IOError:
        print("File format is not supported!!!")
if output_choice == "1":
    sys.stdout.close()
os.chdir(cwd)    
                                                   
                
                                            