import json
import os
from time import sleep
import random

def slideshow():
    value = int(input("Enter The Wallpaper To Start:"))
    end = int(input("Enter How many Wallpaper To Change:"))
    wait = int(input("Enter The Wait Time (in seconds):"))

    for i in range(0, end):
        value += 1
        data["profiles"]["list"][1]["backgroundImage"] = "D:\\Wallpapaer\\{}.jpg".format(value)
        print(data["profiles"]["list"][1]["backgroundImage"])
        with open(settings_path, "w") as f:
            json.dump(data, f, indent=4)
        sleep(wait)

def rand_popup_background():
    import subprocess
    random_value = random.randint(1, 25)
    data["profiles"]["list"][1]["backgroundImage"] = "D:\\Wallpapaer\\{}.jpg".format(random_value)
    print(data["profiles"]["list"][1]["backgroundImage"])
    with open(settings_path, "w") as f:
        json.dump(data, f, indent=4)
    subprocess.Popen(["wt.exe"])  #Currently Working..

        

#Main Function
appdata_path = os.getenv("LOCALAPPDATA")

# print(appdata_path)

#Setting.json location Path
settings_path = os.path.join(
    appdata_path,
    "Packages",
    "Microsoft.WindowsTerminal_8wekyb3d8bbwe",
    "LocalState",
    "settings.json"
)


with open(settings_path) as f:
    data = json.load(f)    

choice = int(input("Enter '1' For SlideShow or '2' For Opening Terminal with a Random Wallpaper :"))


if (choice == 1):
    slideshow()
if (choice == 2):
    rand_popup_background()
#TASKS:
# Now Make a Program when you open the terminal the wallpaper changes.
# There settings.json file is not being recogined. (x)
