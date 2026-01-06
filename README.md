# KBS-TASK-3
SHAMITHA K S
25IM10062

# Blockchain Implementation with Proof-of-Work

This project is a simple Python-based blockchain implementation that consists of:
- Block structure
- Tamper detection using validation logic
- Proof-of-Work (PoW) consensus mechanism

The implementation focuses on core blockchain concepts.

---

## 1. Block Structure

Each block in the blockchain is created using the `Block` class. A block contains the following fields:

- **index**  
  Represents the position of the block in the blockchain. With Genesis block at index - 0.

- **timestamp**  
  Stores the time at which the block is created using `time.time()`.

- **data**  
  Contains the information stored in the block as list of dictionaries. The data is converted into a tuple to make it immutable.

- **nonce**  
  A number that is increased during the mining process to generate a valid hash.

- **prev_hash**  
  Stores the hash of the previous block, creating a cryptographic link between blocks.

- **difficulty**  
  Defines the mining difficulty (number of leading zeros required in the hash). It's value is adjusted based on time taken to mine a block using `def adjust_difficulty(self):`

- **hash**  
  The SHA-256 hash of the block, calculated using the block’s contents. `def calculate_hash(self): `

### Hash Calculation
The block hash is generated using:
- index
- timestamp
- data
- nonce
- previous hash

These values are converted into JSON format (after sorting keys in dictionary) and hashed using the SHA-256 algorithm. Any change in these values results in a completely different hash.
Hash is calculated for various nonce values. The hash that is generated for a particular nonce which starts with target value is stored as the hash of that block.

---

## 2. Validation Logic and Tamper Detection

The blockchain uses the `is_valid()` method to verify the integrity of the chain and detect tampering.

### Validation Checks

For every block (except the Genesis Block), the following validity checks are performed:

1. **Index Check**  
   Ensures that block indices are sequential.

2. **Hash Integrity Check**  
   Recalculates the hash of block and compares it with the stored hash. If they do not match, it means the block has been tampered with.

3. **Previous Hash Check**  
   Ensures that the `prev_hash` of the current block matches the `hash` of the previous block.

4. **Proof-of-Work Verification**  
   Checks that the hash of the block satisfies the required difficulty (leading zeros) that is dynamically set.

5. **Timestamp Validation**  
   Ensures that block timestamps are in chronological order.
   `
### Tamper Detection

If any block data is modified:
- The block hash changes
- The link with the next block breaks(as the next block contains the old hash of this tampered block)

As a result, the blockchain becomes invalid and `is_valid()` returns `False`.  
This makes the blockchain **tamper-evident**.

---

## 3. Proof-of-Work (PoW) Approach

This blockchain uses a Proof-of-Work mechanism to securely add new blocks.

### Mining Process

`def mine_block(self): `
- A target value is created with the help of difficulty (`"0000"`).
- The nonce starts from 0 and is increased continuously.
- For each nonce value, the block hash is recalculated using `def calculate_hash(self): `
- Mining continues until the hash satisfies the difficulty condition. (hash should start with target value)

### Dynamic Difficulty Adjustment

The difficulty is automatically adjusted using the `adjust_difficulty()` method:
- If blocks are mined faster than the target time (10 seconds), difficulty increases.
- If blocks are mined slower than the target time , difficulty decreases.

### Importance of Proof-of-Work

- Makes block creation computationally expensive
- Prevents easy modification of blocks
- Requires re-mining all subsequent blocks if tampering occurs in a particular block

---


