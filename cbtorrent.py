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
    decoded_torrent_file = bencodepy.decode(content)

#decoded_file = list(decoded_torrent_file.values())
#print(decoded_file)
##Generate the peer ID, which is normally formatted as <2 digits to represent client ID> + <4 digits to represent Client version> + <-> + <12 random digits>
random.seed()
peer_ID = (f"CB0000-{random.randint(0, 999999999999)}")
print(peer_ID)

#tracker = requests.get
torrent_list_length = (len(decoded_torrent_file))
indexed_torrent_file = list(decoded_torrent_file.items())[0:int(torrent_list_length)]
print(indexed_torrent_file)
#print(f"{indexed_torrent_file.items('announce')}?{indexed_torrent_file.items('info-hash')&peer id =-{peer_ID}")

