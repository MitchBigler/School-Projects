class HashMap:
    # Initialize HashMap
    def __init__(self):
        self.init_capacity = 7
        self._capacity = self.init_capacity
        self._size = 0
        self.buckets = [None] * self._capacity

    # Return the value associated with key if it exists, else raise a KeyError.
    def get(self, key):
        bucket = hash(key) % self._capacity
        buckets_probed = 0

        while self.buckets[bucket] is not None and buckets_probed < self._size:
            # Bucket found
            if self.buckets[bucket] != 'E' and self.buckets[bucket][0] == key:
                return self.buckets[bucket][1]
            
            # Increment bucket index
            bucket = (bucket + 1) % self._capacity
            buckets_probed += 1

        # Bucket not found
        raise KeyError

    # Add (key,value) to map, resize if >= 80%
    def set(self, key, value):
        bucket = hash(key) % self._capacity
        buckets_probed = 0

        if self.load_factor() >= 0.8:
            self.rehash()

        while (buckets_probed < self._capacity):
            # Bucket is empty
            if self.buckets[bucket] is None or self.buckets[bucket] == 'E':
                self.buckets[bucket] = (key, value)
                self._size += 1
                return True
            
            # Update if already exists
            if self.buckets[bucket][0] == key:
                self.buckets[bucket] = (key, value)
                return True
            
            # Increment bucket index
            bucket = (bucket + 1) % self._capacity
            buckets_probed += 1

        return False 

    # Remove (key, value) from map
    def remove(self, key):
        bucket = hash(key) % self._capacity
        buckets_probed = 0

        while self.buckets[bucket] is not None and buckets_probed < self._size:
            # Bucket found
            if self.buckets[bucket] != 'E' and self.buckets[bucket][0] == key:
                self.buckets[bucket] = 'E'
                self._size -= 1
                return
            
            # Increment bucket index
            bucket = (bucket + 1) % self._capacity
            buckets_probed += 1

        raise KeyError

    # Empty and reset capacity
    def clear(self):
        self._capacity = self.init_capacity
        self._size = 0
        self.buckets = [None] * self._capacity

    # Return current capacity
    def capacity(self):
        return self._capacity

    # Return num of buckets filled
    def size(self):
        return self._size

    # Return list of all keys
    def keys(self):
        pass

    # Generate index for item
    def hash(self, key, value):
        return (key+value) % self._capacity
    
    # Rebuild hashtable with increase capacity
    def rehash(self):
        old_buckets = self.buckets
        self._capacity = (self._capacity * 2) - 1
        self.buckets = [None] * self._capacity
        self._size = 0

        # Reinsert items
        for bucket in old_buckets:
            if bucket is not None and bucket != 'E':
                key, value = bucket
                self.set(key, value)
    
    # Return current load factor
    def load_factor(self):
        return self._size / self._capacity
    
    # Return list of buckets
    def keys(self):
        key_list = []

        for bucket in self.buckets:
            if bucket is not None and bucket != 'E':
                key_list.append(bucket[0])
        return key_list