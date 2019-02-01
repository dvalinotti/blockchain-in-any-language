from Block import Block
# import Genesis
import datetime as date

class Blockchain:
    def __init__(self, first=None):     
        self.ledger = [get_genesis()]
        self.length = len(self.ledger)
        if first is not None:
            self.add_block(first)

    def add_block(self, data):
        last_block = self.ledger[len(self.ledger) - 1]
        next_block = Block.next_block(last_block, data)
        self.ledger.append(next_block)

    def verify_ledger(self):
        compare = False
        for i in range(1, len(self.ledger)):
            compare = ( self.ledger[i].prev_hash == self.ledger[i-1].hash )
            if (not compare):
                raise ValueError('Blockchain verification FAILED at index ' + str(i))
                break
        return compare

    def __repr__(self):
        ret_str = ""
        for b in self.ledger:
            ret_str += str(b) + "\n"
        return ret_str
def get_genesis():
        return Block(0, date.datetime.now(), "First", "0")