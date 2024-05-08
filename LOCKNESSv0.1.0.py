#OS_test
#Made by Unlisted_dev
#Unlisted_dev on discord
import sys
import os
import json
import time

curdir = "/"
answer = ""
accounts = []
account = ""

def makepath(nstr):
    print(f"MAKEPATH NSTR {nstr}")
    string = ""
    if nstr[0] != "/": 
        string += "/"
    for item in nstr:
        string += item
    print(f"MAKEPATH STRING {string}")
    return(str(string))

def ls():
    returnables = []
    for item in pathfind(): 
        returnables.append(item)
    return(returnables) 

def pathfind(path=""):
    #print("PATHFIND " + path)
    global curdir
    global memory
    data = read(memory)
    if path != "":
        locations = []
        if path[0] == "/":
            locations = path.split("/")
            locations[0] = ("/")
        else:
            locations = path.split("/")
        for item in locations:
            if item == '':
                locations.remove(item)
        for item in locations:
            data = data[item]
        return(data)
    else: 
        locations = []
        if curdir[0] == "/":
            locations = curdir.split("/")
            locations[0] = ("/")
            #print(locations)
        else:
            locations = curdir.split("/")
        for item in locations:
            if item == '':
                locations.remove(item)
        for item in locations:
            data = data[item]
        return(data)
def ascii(art,width):
    width = int(width)
    art = list(art)
    strlength = len(art)
    #print(strlength)
    lines = int(strlength / width)
    #print(str(lines))
    count = 0
    line = ""
    for letter in art:
        count = count +1
        line = str(line) + str(letter)
        if len(line) == width:
            print(line)
            line = ""
            time.sleep(0.25)

logo2 = ".____    ________  _________  ____  __._______  ___________ _________ _________ |    |   \_____  \ \_   ___ \|    |/ _|\      \ \_   _____//   _____//   _____/ |    |    /   |   \/    \  \/|      <  /   |   \ |    __)_ \_____  \ \_____  \  |    |___/    |    \     \___|    |  \/    |    \|        \/        \/        \ |_______ \_______  /\______  /____|__ \____|__  /_______  /_______  y/_______  / \/       \/        \/        \/       \/        \/        \/        \/"
logo = (r'''.____    ________  _________  ____  __._______  ___________ _________ _________
|    |   \_____  \ \_   ___ \|    |/ _|\      \ \_   _____//   _____//   _____/
|    |    /   |   \/    \  \/|      <  /   |   \ |    __)_ \_____  \ \_____  \ 
|    |___/    |    \     \___|    |  \/    |    \|        \/        \/        \
|_______ \_______  /\______  /____|__ \____|__  /_______  /_______  y/_______  /
        \/       \/        \/        \/       \/        \/        \/        \/''')

#Read and write
def read(memory):
    with open(memory, "r") as file:
        data = json.load(file)
        dict(data)
        return data
def write(memory,data):
    with open(memory, "w") as file:
        json.dump(data,file)

#Console log function
def cnsl(text="",dir = ""):
    if text != "":
        ui = 50#len(text) + 5
        print(" " + "_" * ui)
        print("/" + "=" * ui)
        print("|==> " + text)
    else:
        ui = 50
        print(" " + "_" * ui)
        print("/" + "=" * ui)
        
    escape = input("| "+dir+" ==: ")
    return(escape)

def login():
    global memory
    global accounts
    global account
    for item in (read(memory)["/"]["usrid"]):
        print(item)
        accounts.append(item)
    while True:
        answer = cnsl("Choose account")
        if answer in accounts:
            print(f"Account selected: {answer}")
            passwd = read(memory)["/"]["usrid"][answer]
            result = input("ENTER PASSWORD: ")
            if result == passwd:
                account = answer
                print("ACCESS GRANTED")
                break
            else: 
                print("ACCESS DENIED")
                input("")
        else: print(f"ACCOUNT {answer} NOT FOUND")

def main():
    while True:
        global curdir
        #print(curdir)
        found = False
        answer = cnsl("",curdir)
        cmd = answer.split(" ")
        args = []
        if len(cmd) > 1:
            for item in cmd:
                args.append(item)
            args.pop(0)
        for folder in pathfind("/executables"):
            if cmd[0] in pathfind(f"/executables/{folder}"):
                exec(pathfind(f"/executables/{folder}/{cmd[0]}"))
                found = True
        if found == False:
            print(f"Item {answer} not found")

#Json location
memory = input("JSON PATH: ")
ans = input("RESET ALL SYSTEM? [Y/N]")
if ans == "y" or ans == "Y":
        write(memory,{"/":{"Hello World":"Hello World"}})
else: print("CONTINUING WITH PREVIOUS SAVE")

#OS setup
#print(read(memory)["Hello World"])
if read(memory)["/"]["Hello World"] == "Hello World":
    setup = {"/":{"root":{"documents":""},"usrid":{"guest": "", "root": "Hello World"},"Hello World":"LOGGED IN","executables":{"preset":{"exit":"sys.exit()","ls":"for item in ls(): print(item)","cd":'''global curdir
if len(args) == 1:                                                                                                                                                                                                                                         
    if args[0] in pathfind():
        if curdir == "/":
            curdir = curdir + args[0]
        else:
            curdir = curdir + "/" + args[0]
    else: print("folder " + args[0] + " not found in current directory")
elif len(args) == 0: 
    if curdir == "/": print("Cannot go higher than /")
    else:
        place = "/"
        places = curdir.split("/")
        places.pop(-1)
        for item in places: place += item
        #print(place)
        curdir = place
    ''',"dir":'''print(curdir)''',"pathfind":'''
if len(args) == 1: 
    print(pathfind(args[0]))
else: print(pathfind())''',"credits":'''print("Created by: Unlisted_dev")
print("Contact: Unlisted_dev on discord")'''}}}}
    #setup = {"/":{"usrid":{"guest": "", "root": "Hello World"},"Hello World":"LOGGED IN"}}
    write(memory,setup)
    data = read(memory)
    print(data["/"]["usrid"]["root"])
    ascii(logo2,80)
    answer = cnsl("WELCOME TO LOCKNESS! CREATE ROOT PASSWORD")
    data["/"]["usrid"]["root"] = answer
    write(memory,data)
    print("ROOT USRID: root:" + (answer))
    print("")

    login()
else: 
    print("WELCOME TO")
    time.sleep(1)
    ascii(logo2,80)
    login()

if account != "":
    print(pathfind("/usrid/root"))
    main()
else:
    print("ERROR! NO ACTIVE USER FOUND! ==SYSTEM SHUTDOWN==")
    print("This error occurs when no user is found to be logged in while trying to access a shell object. There should be zero circumstances where this message sgould appear, unless your a sneaky hacker trying to get in without a shell object, or something is very wrong with the code that runs this OS. No idea how to fix this haha, DM me, Unlisted_games27 on discord, or Unlisted_dev")
    sys.exit()