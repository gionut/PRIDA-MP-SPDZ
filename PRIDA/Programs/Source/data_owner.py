#!/usr/bin/python3


# To be copied to MP-SPDZ/ExternalIO/data_owner.py
import sys

sys.path.append('.')

from client import *
from domains import *

client_id = int(sys.argv[1])
n_parties = int(sys.argv[2])
value = float(sys.argv[3])
finish = int(sys.argv[4])

client = Client(['localhost'] * n_parties, 14000, client_id)

for socket in client.sockets:
    os = octetStream()
    os.store(finish)
    os.Send(socket)

def run(x):
    client.send_private_inputs([x])

run(value)
