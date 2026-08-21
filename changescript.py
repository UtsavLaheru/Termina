import json
import os
from time import sleep
import random
import tkinter as tk
from tkinter import filedialog

# root = tk.Tk()
# label = tk.Label(root, text="Testing The Terminal Customization GUI")
# label.pack()

# root.mainloop()

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
        value = int(input("Enter The Starting Wallpaper:"))
        data2["value"] = value-1

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

# def extensionChecker():

#File Checker
fileName = [
    f for f in os.listdir(data2["folder"])
    if os.path.isfile(os.path.join(data2["folder"], f))
]
# print(type(fileName))
fileName.sort(key=lambda f: (len(f), f))   #Need Some More Test or Understanding.
# for i in fileName:
    # print("filename:", i)

def reset_json():
    data2["folder"] = ""
    data2["value"] = ""
    data2["end"] = ""
    data2["wait"] = ""
    with open("store.json", "w") as f:
        json.dump(data2, f, indent=4)
    print("store.json is reseted successfully")

def slideshow():
    value = data2["value"]
    end = data2["end"]
    wait = data2["wait"]
    for i in range(0, end):
        data["profiles"]["list"][1]["backgroundImage"] = data2["folder"]+"\\{}".format(fileName[value])
        print(data["profiles"]["list"][1]["backgroundImage"])
        value += 1
        with open(settings_path, "w") as f:
            json.dump(data, f, indent=4)
        sleep(wait)

# def RepeatedSlideShow():  #Currently Working...

def rand_popup_background():
    import subprocess
    random_value = random.randint(data2["value"], data2["end"]-1)
    data["profiles"]["list"][1]["backgroundImage"] = data2["folder"]+"\\{}".format(fileName[random_value])
    print(data["profiles"]["list"][1]["backgroundImage"])
    with open(settings_path, "w") as f:
        json.dump(data, f, indent=4)
    subprocess.Popen(["wt.exe"])

def rand_when_opend_background():
    import psutil
    old_count = 0
    new_count = 0
    passes = 1
    try:
        print("Monitoring For New Terminal Opened To Stop Press Ctrl+c")
        while True:
            new_count = 0
            for p in psutil.process_iter(["name"]):
                if(p.info["name"] == "OpenConsole.exe"):
                    if(passes == 1):
                        old_count += 1
                    else:
                        new_count += 1 
            if(new_count > old_count):
                print("New Console Opened")
                random_value = random.randint(data2["value"], data2["end"]-1)
                data["profiles"]["list"][1]["backgroundImage"] = data2["folder"]+"\\{}".format(fileName[random_value])
                print(data["profiles"]["list"][1]["backgroundImage"])
                with open(settings_path, "w") as f:
                    json.dump(data, f, indent=4)
                #It is For safety (So we don't get stuck in infinit Loop).
                # return False
            if(passes != 1):
                old_count = new_count
            passes = 2
    except KeyboardInterrupt:
        print("Monitoring Ended")
    
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

print("To Reset stored values Enter 0,")
choice = int(input("Enter '1' For SlideShow or '2' For Random Wallpaper :"))

match(choice):
    case 0:
        reset_json()
    case 1:
        slideshow()
    case 2:
        choiceForRand = int(input("Enter '1' For Opening Terminal with a Random Wallpaper or '2' For Random Background every Time You Open Terminal:"))
        match(choiceForRand):
            case 1:
                rand_popup_background()
            case 2:
                rand_when_opend_background()
    case _:
        print("You Have Enterned A Wrong Choice >v<")
    
#TASKS:
# Understand about Textual for TUI.
# Understand More About tkinter and make a Folder/File Selector.
# Now Make a Program when you open the terminal the wallpaper changes. (x)
# There settings.json file is not being recogined. (x)
# Add Reset json Key or action For store.json. (x)

#OPTIONAL:
# We Can Add File Explorer like Sorting
