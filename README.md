You will need to set up a JSON for this to work.
Setup: 
Note: I used VS code for everything, my system is Linux Debian and it's worked on Windows as well.
Create and save a file for the code, something that you can execute with python3. Create a JSON file wherever (I would recommend creating it in the same directory as the code). When running the code, you will first get a prompt to paste the directory of the JSON you created. Select reset system the first time you use this OS.
Requirements: python3, repositories: sys, json, time

Features: Login system, file system, all login details save to JSON, a few built-in commands

Commands:
anything within [] is args for the command, so for example if a command instruction says: print [args/what to print], you would write something like: print HelloWorld
ls - 
usage: ls
prints the name of every folder in a directory. 
WARNING! This command is incomplete, trying to use it when your directory is a file (not a folder) will cause an error/OS crash

cd - 
usage: cd [folder]
providing a folder in the arguments will change the directory to that folder. Note that you can only go to folders listed within the current directory. Providing no args will go back one directory. 
WARNING!: cd gives you the ability to cd to a file not a folder. This is unintended and is being fixed. Having your directory as a file will not crash immediately, but is not supposed to happen, and can cause things like ls to cause a crash.

exit-
Usage: exit
Exits the system. All changes are saved in the JSON

dir-
usage: dir
prints the current directory

print-
usage: print [string]
prints the provided args

credits-
usage: credits
prints the credits for the OS.  If you make changes, please leave my name in the credits as the original creator, but feel free to add your name if you make changes to the OS

ADVANCED:

pathfind-
usage: pathfind [directory]
prints the provided directory in the form of a dictionary, including everything contained within

Contact me:
Im open for questions, comments, suggestions, etc. DM me whenever!
Unlisted_dev on discord
