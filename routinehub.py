# routinehub.py - Made by dante_nl (https://rhub.tk?u=dante_nl)
# Just a fun project.

# Why is this variable here named "Details"? It shows you what's going on!
# These details are prefixed with ">".
# If you want to enable it, just replace "False" with "True"!

details = False

# The real stuff starts here

import requests
import sys
import urllib
import re
import os

print(" ")

version = "1.3.2"


def connected(host='https://google.com'):
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

r = requests.get('https://routinehubpy.dantenl.tk/u/latest.json')

if not r.ok:
    print('No connection could be made.')
    print(" ")
    sys.exit(1)

data = r.json()
if data.get('version') != version:
    print("Update! You don't have to do anything; everything will be done automatically")
    print(f"Release notes: \n{data.get('notes')}")
    print(f"{version} -> {data.get('version')}")
    if details:
        print("> Getting file...")
    url = 'https://routinehubpy.dantenl.tk/routinehub.py'
    r = requests.get(url, allow_redirects=True)
    if not r.ok:
        print("Could not connect!")
        sys.exit(1)
    open('routinehub.py', 'wb').write(r.content)
    if details:
        print("> Download complete! Restarting...")
    os.system("python3 routinehub.py")
    sys.exit(1)


print(
    f"Hi! Welcome to RoutineHub.py! | Type 'help' to get some help. ALL COMMANDS ARE LOWERCASE!")

while True:
    txt = input("What do you want to do? ")
    if txt == "help":
        print("""
Here are a few things that work with me:

- 'help'     - Sends this message
- 'shortcut' - Get a Shortcut's stats
- 'author'   - Lookup an author
- 'credits'  - Shows the credits
- 'restore'  - Redownloads the current routinehub.py. Can be useful when you did an oopsie whilst editing it
- 'restart'  - If you did some changes while coding, you can just type this
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
            name = data.get('name')
            subtitle = data.get('subtitle')

            if details:
                print("> Requesting data from official API...")
            r = requests.get(
                f'https://routinehub.co/api/v1/shortcuts/{txt}/versions/latest')
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
Name: {name}
Subtitle: {subtitle}
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
        if details:
            print("> Scraping data from RoutineHub website")
        user_url = f"https://routinehub.co/user/{txt}"
        response = requests.get(user_url)
        if not r.ok:
            print('No connection could be made.')
            sys.exit(1)
        try:
            data = r.json()

            bio = data.get('bio')
            total_downloads = data.get('total_downloads')
            downloads_average = data.get('downloads_average')

            # Hearts

            ex = '(?<=<i class="fas fa-heart"></i></span>\n).*(?=\n</small>)'
            hearts_list = re.findall(ex, response.text)

            hearts = 0

            for num in hearts_list:
                num = int(num)
                hearts += num

            # Shortcuts

            ex = "(?<=<p>Shortcuts: ).*(?=</p>)"
            sc = re.findall(ex, response.text)[0]

            # Username

            ex = "(?<=<strong>).*(?=</strong>)"
            username = re.findall(ex, response.text)[0]

            print(f"""
Username: {username}
Biography: {bio}
Shortcuts: {sc}
Downloads: {total_downloads}
Average downloads: {downloads_average}
Hearts: {hearts}
""")
        except:
            print("No user with that name could be foud!")

    elif txt == "credits":
        print("""
- @alombi - Used his API for this script
- @elio27 - Used parts of his RoutineBot code for the author part
""")

    elif txt == "restore":
        print("File will be downloaded in the current directory. It will restart automatically")
        if details:
            print("> Getting file...")
        url = 'https://routinehubpy.dantenl.tk/routinehub.py'
        r = requests.get(url, allow_redirects=True)
        if not r.ok:
            print("Could not connect!")
            sys.exit(1)
        open('routinehub.py', 'wb').write(r.content)
        print("Download complete")
        os.system("python3 routinehub.py")
        sys.exit(1)

    elif txt == "restart":
        print("Restarting...")
        os.system("python3 routinehub.py")
        sys.exit(1)

    elif txt == "exit":
        print("Goodbye!")
        sys.exit(1)

    else:
        print("That is not a valid command!")
