# routinehub.py - Made by dante_nl (https://rhub.tk?u=dante_nl)
# Just a fun project. 

# Why is this variable here named "Details"? It shows you what's going on!
# These details are prefixed with ">".
# If you want to enable it, just replace "False" with "True"!

details = False

# The real stuff starts here
print(" ")
import requests
import sys
import urllib
import webbrowser

version = "1.0"

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
if connected() == False:
    print("No internet! This is a script to interact with a website, so it's not very useful without internet!")
    print(" ")
    sys.exit(1)

if details == True:
    print("> Checking for updates...")

r = requests.get('https://routinehubpy.tk/u/latest.json')

if not r.ok:
    print('No connection could be made.')
    print(" ")
    sys.exit(1)

data = r.json()
if data.get('version') != version:
    print(f"A new version is ready to be downloaded! Here are the release notes: \n{data.get('notes')}")
    print(f"{version} -> {data.get('version')}")
    txt = input("Do you want to visit the website to download the latest version (y/n): ")
    if details == True:
        print(f"> Input received as {txt}")
    if txt == "y":
        url = "https://routinehubpy.tk?update=True"
        webbrowser.open(url, new=1, autoraise=True)
        print(" ")
        sys.exit(1)
    elif txt == "n":
        print("Update not downloaded. Please come back with the latest version!")
        print(" ")
        sys.exit(1)
    elif txt != "y" or "n":
        print("That's not valid. Please enter 'y' or 'n'! It must be lowercase")
        print(" ")
        sys.exit(1)

print(
    f"Hi! Welcome to RoutineHub.py! | Type 'help' to get some help. ALL COMMANDS ARE LOWERCASE! | You are currently on the latest version ({version})")
def new_func():
    return

while True:
    txt = input("What do you want to do? ")
    if txt == "help":
        print("""
Here are a few things that work with me:

- 'help'     - Sends this message
- 'shortcut' - Get a Shortcut's stats
- 'author'   - Lookup an author
- 'credits'  - Shows the credits
- 'exit'     - Stop this code
""")
    elif txt == "shortcut":
        txt = input("What is the ID of the Shortcut you want to look up? ")
        if details == True:
            print(f"> Input received as {txt}")
            print("> Checking if input is number")
        try:
            int(txt)
            if details:
                print(f"> {txt} appears to be a number")
                print("> Requesting data from alombi's API...")
            r = requests.get(f'https://rh-api.alombi.xyz/shortcut?id={txt}')
            if not r.ok:
                print('No connection could be made.')

            data = r.json()

            hearts = data.get('hearts')
            downloads = data.get('downloads')

            if details:
                print("> Requesting data from official API...")
            r = requests.get(f'https://routinehub.co/api/v1/shortcuts/{txt}/versions/latest')
            if not r.ok:
                print('No connection could be made.')

            data = r.json()
            if data.get('result') != "success":
                print("Could not get data from RoutineHub's API")
                version = "Error"
                notes = "Error"
                release = "Error"
            else:
                version = data.get('Version')
                notes = data.get('Notes')
                release = data.get('Release')

            print(f"""
Hearts: {hearts}
Downloads: {downloads}
Latest version: {version}
Release notes:\n{notes}\n
Released on {release}           
""")



        except:
            print(f"{txt} does not appear to be a valid ID!")
            print(" ")

    elif txt == "author":
        txt = input("What is the author you want to look up? ")
        if details:
            print("> Requesting data from alombi's API...")
        r = requests.get(f'https://rh-api.alombi.xyz/author?username={txt}')
        if not r.ok:
            print('No connection could be made.')
            sys.exit(1)
        try:
            data = r.json()
            bio = data.get('bio')
            total_shortcuts = data.get('total_shortcuts')
            total_downloads = data.get('total_downloads')
            total_hearts = data.get('total_hearts')
            downloads_average = data.get('downloads_average')
            heart_average = data.get('hearts_average')
            username = data.get('username')
            print(f"""
Username: @{username}
Biography: {bio}
Shortcuts: {total_shortcuts} | Due to a bug in the API, the total is only from the first page, so 18 maximum.
Downloads: {total_downloads}
Average downloads: {downloads_average}
Hearts: {total_hearts}
Average hearts: {heart_average}
""")
        except:
            print("No user with that name could be foud!")

    elif txt == "credits":
        print("""
- @alombi - Used his API for this script
""")

    elif txt == "exit":
        print("Goodbye!")
        sys.exit(1)
