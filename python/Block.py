import hashlib as hasher
import datetime as date

class Block: 
    def __init__ (self, index, time_stamp, data, prev_hash):
        self.index = index
        self.time_stamp = time_stamp 
        self.prev_hash = prev_hash
        self.data = data 
        self.hash = self.hash_block()

    def hash_block(self):
        key = hasher.sha256()
        key_str = (str(self.index) +
                   str(self.time_stamp) + 
                   str(self.data) + 
                   str(self.prev_hash)).encode('utf-8')
        key.update(key_str) 
        return key.hexdigest()
    
    def next_block(last_block, data):
        next_index = last_block.index + 1
        next_time_stamp = date.datetime.now()
        next_data = data
        next_hash = last_block.hash

        return Block(next_index, next_time_stamp, next_data, next_hash)

    def __repr__(self):
        return (str(self.index) + " - " +
                str(self.time_stamp) + " - " + 
                str(self.data) + " - " + 
                str(self.hash) + " - " + 
                str(self.prev_hash))