from Block import Block
from Blockchain import Blockchain
# from Genesis import Genesis

import string
import random

def gen_string():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(6))

chain = Blockchain()

for i in range(6):
    print(gen_string())
    chain.add_block(gen_string())

print(chain)
print(chain.verify_ledger())