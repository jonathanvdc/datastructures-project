from ArrayList import *
from ITable import *

class Hashtable(ITable):
    """ Represents a hash table that uses separate chaining. """

    def __init__(self, KeyMap, BucketFactory):
        """ Creates a new hash table, from the provided key map and the bucket table factory. """
        self.bucket_count = 0
        self.prime_list = [31, 97, 389, 1543, 6151, 24593, 98317, 393241, 1572869, 6291469, 25165843, 100663319, 402653189, 1610612741, 4294967291]
        self.buckets = None
        self.key_map_value = None
        self.bucket_factory_value = None
        self.key_map = KeyMap
        self.bucket_factory = BucketFactory
        self.buckets = [None] * self.prime_list[0]

    def get_next_prime(self):
        """ Gets the next prime in the prime list. If this prime is not available, -1 is returned. """
        i = 0
        while i < len(self.prime_list) - 1:
            if self.prime_list[i] > self.bucket_capacity:
                return self.prime_list[i]
            i += 1
        return -1

    def resize_table(self):
        """ Tries to resize the table to the next prime and re-hashes every element. """
        nextPrime = self.get_next_prime()
        if nextPrime > -1:
            oldBuckets = self.buckets
            self.buckets = [None] * nextPrime
            self.bucket_count = 0
            for i in range(len(oldBuckets)):
                if oldBuckets[i] is not None:
                    for item in oldBuckets[i]:
                        self.insert(item)

    def insert(self, Item):
        """ Inserts an item in the hash table. """
        key = self.key_map.map(Item)
        hashCode = hash(key)
        bucket = self.get_new_bucket(hashCode)
        if self.bucket_contains_key(bucket, key):
            return False
        bucket.insert(Item)
        if self.bucket_load_factor > 0.66:
            self.resize_table()
        return True

    def get_new_bucket(self, HashCode):
        """ Gets the bucket for items with the given hash code or creates a new one, if necessary. """
        index = HashCode % self.bucket_capacity
        bucket = self.buckets[index]
        if bucket is None:
            self.bucket_count += 1
            bucket = self.bucket_factory.create(self.key_map)
            self.buckets[index] = bucket
        return bucket

    def bucket_contains_key(self, Bucket, Key):
        """ Finds out if a bucket contains the given key. """
        return self.find_in_bucket(Bucket, Key) is not None

    def find_in_bucket(self, Bucket, Key):
        """ Finds an item in the given bucket with the given key. """
        if Bucket is None:
            return None
        return Bucket[Key]

    def get_bucket(self, HashCode):
        """ Gets the bucket for items with the given hash code. """
        index = HashCode % self.bucket_capacity
        bucket = self.buckets[index]
        return bucket

    def delete_bucket(self, HashCode):
        """ Deletes the bucket with the provided hash code. """
        index = HashCode % self.bucket_capacity
        self.buckets[index] = None
        self.bucket_count -= 1

    def contains_key(self, Key):
        """ Gets a boolean value that indicates if the hash table contains the given key. """
        return self.bucket_contains_key(self.get_bucket(hash(Key)), Key)

    def remove(self, Key):
        """ Removes a key from the table. """
        hashCode = hash(Key)
        bucket = self.get_bucket(hashCode)
        if bucket is None:
            return False
        result = bucket.remove(Key)
        if bucket.count == 0:
            self.delete_bucket(hashCode)
        return result

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        for i in range(len(self.buckets)):
            if self.buckets[i] is not None:
                for item in self.buckets[i]:
                    yield item

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        results = ArrayList()
        for i in range(len(self.buckets)):
            if self.buckets[i] is not None:
                for item in self.buckets[i]:
                    results.add(item)
        return results

    @property
    def bucket_capacity(self):
        """ Gets the number of buckets in the table. """
        return len(self.buckets)

    @property
    def key_map(self):
        """ Gets the record-to-key mapping function used by this hash table. """
        return self.key_map_value

    @key_map.setter
    def key_map(self, value):
        """ Sets the record-to-key mapping function used by this hash table. """
        self.key_map_value = value

    @property
    def bucket_factory(self):
        """ Gets the factory that is used to create new buckets for this hash table. """
        return self.bucket_factory_value

    @bucket_factory.setter
    def bucket_factory(self, value):
        """ Sets the factory that is used to create new buckets for this hash table. """
        self.bucket_factory_value = value

    @property
    def bucket_load_factor(self):
        """ Gets the bucket load factor. """
        return self.bucket_count / self.bucket_capacity

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        result = 0
        for i in range(len(self.buckets)):
            if self.buckets[i] is not None:
                result += self.buckets[i].count
        return result

    @property
    def is_empty(self):
        for i in range(len(self.buckets)):
            if self.buckets[i] is not None and self.buckets[i].count > 0:
                return False
        return True

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        bucket = self.get_bucket(hash(Key))
        return self.find_in_bucket(bucket, Key)