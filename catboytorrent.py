import bencodepy
import requests
import random

version_ID = ("0000")

## Makes sure that the file ends in .torrent

while True:
    torrent_path = input("Please input the path of your torrent file > ")
    if torrent_path.endswith('.torrent') == False:
        print("Please select a file that ends in .torrent")
    else:
        print("Getting started! :)")
        break
    

##Reads and decodes the torrent file

with open(torrent_path, 'rb') as file:
    meta_info = file.read()
    torrent = bencodepy.decode(meta_info)

##Generate the peer ID, which is normally formatted as <2 digits to represent client ID> + <4 digits to represent Client version> + <12 random digits>
random.seed()
random_peer_part = random.randint(0, 999999999999)
peer_ID = (f"CB{version_ID}{random_peer_part}")
print(peer_ID)
