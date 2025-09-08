import asyncio
import random
import logging
import socket
import bencoding
from struct import unpack
from urllib.parse import urlencode

random.seed()

class cb_tracker_response:
    """
    The response from the tracker after a successful connection to the
    tracker's announce URL

    Even if the connection was successful from a network point of view,
    the tracker might have returned an error (stated in the failure
    property)
    """
    
    def __init__(self, response:dict):
        self.response = response



class cb_tracker:
    
    #Represents the connection to a tracker for an active torrent

    def __init__(self, torrent):
        self.torrent = torrent
        self.peer_id = (f"CB0000-{random.randint(0, 999999999999)}")
        self.http_client = aiohttp.ClientSession()
