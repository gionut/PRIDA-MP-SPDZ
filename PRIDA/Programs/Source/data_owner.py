#!/usr/bin/python3

import sys

sys.path.append('.')

from client import *
from domains import *

client_id = int(sys.argv[1])
n_parties = int(sys.argv[2])

client = Client(['localhost'] * n_parties, 14000, client_id)

def run():
    with open('/workspaces/PRIDA-MP-SPDZ/PRIDA/Programs/DataOwner/input_' + str(client_id), 'r') as f:
        x = [int(line) for line in f]
    client.send_private_inputs(x)

run()
