import hashlib
import time

class Block:
    def __init__(self, index, prev_hash, timestamps, transaction, proof):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamps = timestamps
        self.transaction = transaction
        self.proof = proof
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        data = str(self.index) + str(self.prev_hash) + str(self.timestamps) + str(self.transaction) + str(self.proof)
        return hashlib.sha256(data.encode()).hexdigest()
    