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
import webbrowser

version = "blub"

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
if connected() == False:
    print("No internet! This is a script to interact with a website, so it's not very useful without internet!")
    sys.exit(1)

if details == True:
    print("> Checking for updates...")

r = requests.get('https://routinehubpy.tk/u/latest.json')

if not r.ok:
    print('No connection could be made.')
    sys.exit(1)

data = r.json()
if data.get('version') != version:
    print(f"A new version is ready to be downloaded! Here are the release notes: \n{data.get('notes')}")
    txt = input("Do you want to visit the website to download the latest version (y/n): ")
    if details == True:
        print(f"> Input received as {txt}")
    if txt == "y":
        url = "https://google.com"
        webbrowser.open(url, new=1, autoraise=True)
        sys.exit(1)
    elif txt == "n":
        print("Update not downloaded. Please come back with the latest version!")
        sys.exit(1)
    elif txt != "y" or "n":
        print("That's not valid. Please enter 'y' or 'n'! It must be lowercase")
        sys.exit(1)
