#!/bin/user/env/Python3

import os
from PIL import Image
from importlib_metadata import files
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
#My Logo
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

cwd = os.getcwd()
os.chdir(os.path.join(cwd, "images"))

files = os.listdir()

if len(files) == 0:
    print(gr+"You don't have any files in the ./images folder...")
    exit()
for file in files:
    try:
        img = Image.open(file)
        img_data = list(img.getdata())
        img_no_exif = Image.new(img.mode, img.size)
        img_no_exif.putdata(img_data)
        img_no_exif.save(file)
    except IOError:
        print(gr+"File format is not supported!!!")        
    