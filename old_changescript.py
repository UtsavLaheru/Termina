import json
import os
from time import sleep
import random
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
label = tk.Label(root, text="Testing The Terminal Customization GUI")
label.pack()


root.mainloop()   

with open("store.json") as f:
    data2 = json.load(f)

#Check If There is a Null or Not Setted-Up Values
if (data2["value"] == "" or data2["end"] == "" or data2["wait"] == "" or data2["folder"] == ""):

    if (data2["folder"] == ""):
        print("folder is empty")
        folder = filedialog.askdirectory()
        folder = folder.replace("/", "\\")
        print("selected folder:",folder)
        data2["folder"] = folder

    print("Slideshow values initialization")
    #Slideshow Values are Missing.
    if (data2["value"] == ""):
        print("value is not set or missing")
        value = int(input("Enter The Wallpaper To Start:"))
        data2["value"] = value

    if (data2["end"] == ""):
        print("end is not set or missing")
        end = int(input("Enter How many Wallpaper To Change:"))
        data2["end"] = end

    if (data2["wait"] == ""):
        print("wait is not set or missing")
        wait = int(input("Enter The Wait Time (in seconds):"))
        data2["wait"] = wait

    with open("store.json", "w") as f:
        json.dump(data2, f, indent=4)

print("Values Loaded Successfully")


# "If You Enter Nothing You'll Get Nothing"
#                          -somebody(probably)

# def CheckingStoredData():
#     with open("store")

def slideshow():
    value = data2["value"]
    end = data2["end"]
    wait = data2["wait"]
    for i in range(0, end):
        data["profiles"]["list"][1]["backgroundImage"] = data2["folder"]+"\\{}.jpg".format(value)
        print(data["profiles"]["list"][1]["backgroundImage"])
        value += 1
        with open(settings_path, "w") as f:
            json.dump(data, f, indent=4)
        sleep(wait)

def rand_popup_background():
    import subprocess
    random_value = random.randint(1, 25)
    data["profiles"]["list"][1]["backgroundImage"] = data2["folder"]+"\\{}.jpg".format(random_value)
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


match(choice):
    case 1:
        slideshow()
    case 2:
        rand_popup_background()
    case _:
        print("You Have Enterned A Wrong Choice >v<")
    
#TASKS:
#Understand More About tkinter and make a Folder/File Selector.
# Now Make a Program when you open the terminal the wallpaper changes.
# There settings.json file is not being recogined. (x)
