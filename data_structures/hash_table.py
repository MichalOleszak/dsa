"""
Key-value pair data structure that uses a hash function to map keys to values.
- Key is passed to a hashing function that maps the key to an index in the hash table
- Hash function must be deterministic and irreversible

Dealing with collisions:
- Separate chaining:
  - Approach 1: Store multiple key-value pairs at the same index in a list
  - Approach 2: Each index in the hash table points to a linked list
- Open addressing:
  - Linear probing: if the index is occupied, search for the next available index

Number of addresses in the hash table should be a prime number to reduce the number
of collisions (it tends to distribute hash values more uniformly, reducing
the likelihood of a collision).

Big O:
- Hash method: O(1) - given a key of given length, always same num of operations needed
- Worst case: always collision, all keys map to same index - O(n)
- But we assume uniform distribution of keys over the hash table, collisions very rare
- O(1) for insertion, deletion, lookup
"""


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        hash = 0
        for char in key:
            # ord() returns the unicode code pint of a character
            # prime number 23 is used to reduce collisions (any prime number would do)
            # modulo ensures that the hash is within the size of the hash table
            hash = (hash + ord(char) * 23) % len(self.data_map)
        return hash

    def print(self):
        for k, v in enumerate(self.data_map):
            print(k, " : ", v)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is None:
            return None
        for pair in self.data_map[index]:
            if pair[0] == key:
                return pair[1]

    def keys(self):
        keys = []
        for index in range(len(self.data_map)):
            if self.data_map[index] is not None:
                for pair in self.data_map[index]:
                    keys.append(pair[0])
        return keys
