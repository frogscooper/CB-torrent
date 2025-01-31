import bencodepy

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
print(torrent)

