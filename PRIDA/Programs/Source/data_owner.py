#!/usr/bin/python3

# To be copied to MP-SPDZ/ExternalIO/data_owner.py
import sys

sys.path.append('.')

from client import *
from domains import *

client_id = int(sys.argv[1])
n_parties = int(sys.argv[2])
finish = int(sys.argv[3])

client = Client(['localhost'] * n_parties, 14000, client_id)

for socket in client.sockets:
    os = octetStream()
    os.store(finish)
    os.Send(socket)

def run():
    with open('DataOwner/input_' + str(client_id), 'r') as f:
        x = [int(line) for line in f]
    client.send_private_inputs(x)

run()
