import collections
import bencodepy
import requests
import random
import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename 

## Asks user to select .torrent file

while True:
    tk.Tk().withdraw()
    torrent_file_path = askopenfilename(
            initialdir="~/",
            title="Select .torrent file",
            filetypes=(("Torrent files", "*.torrent"), ("All files", "*.*"))
        )
    print("Getting started! :)")
    break
    

##Reads and decodes the torrent file

with open(torrent_file_path, 'rb') as file:
    content = file.read()
    decoded_file = bencodepy.decode(content) 

print(decoded_file)
##Generate the peer ID, which is normally formatted as <2 digits to represent client ID> + <4 digits to represent Client version> + <-> + <12 random digits>
random.seed()
peer_ID = (f"CB0000-{random.randint(0, 999999999999)}")
print(peer_ID)

#tracker = requests.get
