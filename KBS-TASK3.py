import hashlib
import json
import time

class Block:
    def __init__(self, index, data, prev_hash, difficulty, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.data = tuple(data)
        self.nonce = nonce
        self.prev_hash = prev_hash
        self.difficulty = difficulty
        self.hash = self.mine_block()
    

    def calculate_hash(self):
        block_content = {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "nonce": self.nonce,
            "prev_hash": self.prev_hash
        }
        block_string = json.dumps(block_content, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    

    def mine_block(self):
        self.nonce = 0
        target = "0" * self.difficulty
        hash_value = self.calculate_hash()

        while hash_value[:self.difficulty] != target:
            self.nonce += 1
            hash_value = self.calculate_hash() 

        return hash_value
            


    def __repr__(self):
        return(f"{self.index}, {self.timestamp}, {self.data}, {self.nonce}, {self.prev_hash}, {self.hash}")
    

    def __str__(self):
        return (f"Index: {self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Nonce: {self.nonce}\n" 
                f"Previous_hash: {self.prev_hash}\n" 
                f"Block_hash: {self.hash}\n")
    

class Blockchain:
    TARGET_BLOCK_TIME = 10

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.difficulty = 4
        self.nodes = set()
        self.add_genesis_block()


    def adjust_difficulty(self):
        if len(self.chain) < 2:
            return
        
        last_block = self.chain[-1]
        prev_block = self.chain[-2]

        time_taken = last_block.timestamp - prev_block.timestamp

        if time_taken < self.TARGET_BLOCK_TIME:
            self.difficulty += 1
        elif time_taken > self.TARGET_BLOCK_TIME and self.difficulty > 1:
            self.difficulty -= 1


    def add_genesis_block(self):
        self.current_data = [{"Block": "Genesis Block" }]
        self.add_block()
        

    def add_block(self):
        self.adjust_difficulty()

        new_block = Block(index = len(self.chain) , data = self.current_data, prev_hash = self.chain[-1].hash if self.chain else "0", difficulty = self.difficulty)
                 
        self.current_data = []
        self.chain.append(new_block)

        return(new_block)
    

    def add_data(self, data): 
        self.current_data.append(data)


    def is_valid(self):
        for i in range(1, len(self.chain)):
            previous_block = self.chain[i-1]
            current_block = self.chain[i]

            if current_block.index != previous_block.index + 1:
                return False

            elif current_block.hash != current_block.calculate_hash():
                return False
            
            elif current_block.prev_hash != previous_block.hash:
                return False
            
            elif current_block.hash[:self.difficulty] != "0" * current_block.difficulty:
                return False
            
            elif current_block.timestamp < previous_block.timestamp:
                return False
            
        return True
    

    def register_node(self, address):
        address = address.replace("http://", "").replace("https://", "")
        self.nodes.add(address)

    @property
    def latest_block(self):
        return self.chain[-1]
        
        
    
    




    
    


