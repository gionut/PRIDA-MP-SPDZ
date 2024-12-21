#!/usr/bin/python3

import sys

sys.path.append('.')

from client import *
from domains import *

client_id = int(sys.argv[1])
n_parties = int(sys.argv[2])

client = Client(['localhost'] * n_parties, 14000, client_id)

def run():
    M = 1
    cv = [1] * M
    d = [10] * M
    x = cv + d
    client.send_private_inputs(x)

run()
