from OpenHashtableItem import *
from ArrayList import *
from ITable import *

class OpenHashtable(ITable):
    """ Represents a hash table that uses open addressing. """

    def __init__(self, KeyMap, ProbeSequenceMap):
        """ Creates a new hash table, with the provided key map and probe sequence map. """
        self.prime_list = [31, 97, 389, 1543, 6151, 24593, 98317, 393241, 1572869, 6291469, 25165843, 100663319, 402653189, 1610612741, 4294967291]
        self.values = [None] * self.prime_list[0]
        self.key_map_value = None
        self.probe_sequence_map_value = None
        self.count_value = 0
        self.key_map = KeyMap
        self.probe_sequence_map = ProbeSequenceMap

    def get_next_prime(self):
        """ Gets the next prime in the prime list. If this prime is not available, -1 is returned. """
        i = 0
        while i < len(self.prime_list) - 1:
            if self.prime_list[i] > self.capacity:
                return self.prime_list[i]
            i += 1
        return -1

    def resize_table(self):
        """ Tries to resize the table to the next prime and re-hashes every element. """
        nextPrime = self.get_next_prime()
        if nextPrime > -1:
            oldValues = self.values
            self.values = [None] * nextPrime
            self.count = 0
            for i in range(len(oldValues)):
                if oldValues[i] is not None and (not oldValues[i].is_empty):
                    self.insert(oldValues[i].value)

    def insert(self, Item):
        """ Inserts an item into the table. """
        key = self.key_map.map(Item)
        openItem = self.find_open_item(key)
        if openItem is None:
            return False
        else:
            self.count += 1
            openItem.value = Item
            openItem.is_empty = False
            if self.load_factor > 0.75:
                self.resize_table()
            return True

    def find_open_item(self, Key):
        hashCode = hash(Key)
        seq = self.probe_sequence_map.map(hashCode)
        for index in seq:
            i = index % self.capacity
            if self.is_open(i):
                if self.values[i] is None:
                    self.values[i] = OpenHashtableItem(None, True)
                return self.values[i]
            elif self.key_map.map(self.values[i].value) == Key:
                return None

    def is_open(self, Index):
        """ Finds out if the position at the given index is open. """
        return self.values[Index] is None or self.values[Index].is_empty

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        return self[Key] is not None

    def remove(self, Key):
        """ Removes a key from the table. """
        hashCode = hash(Key)
        seq = self.probe_sequence_map.map(hashCode)
        for index in seq:
            i = index % self.capacity
            if self.values[i] is None:
                return False
            elif (not self.values[i].is_empty) and self.key_map.map(self.values[i].value) == Key:
                self.values[i].is_empty = True
                self.count -= 1
                return True

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        for i in range(len(self.values)):
            if self.values[i] is not None and (not self.values[i].is_empty):
                yield self.values[i].value

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        results = ArrayList()
        for i in range(len(self.values)):
            if self.values[i] is not None and (not self.values[i].is_empty):
                results.add(self.values[i].value)
        return results

    @property
    def capacity(self):
        """ Gets the table's capacity. """
        return len(self.values)

    @property
    def count(self):
        """ Gets the number of items in the table. """
        return self.count_value

    @count.setter
    def count(self, value):
        """ Sets the number of items in the table. """
        self.count_value = value

    @property
    def key_map(self):
        """ Gets the record-to-key mapping function used by this hash table. """
        return self.key_map_value

    @key_map.setter
    def key_map(self, value):
        """ Sets the record-to-key mapping function used by this hash table. """
        self.key_map_value = value

    @property
    def probe_sequence_map(self):
        """ Gets the open addressed hash table's hash key to probe sequence mapping function. """
        return self.probe_sequence_map_value

    @probe_sequence_map.setter
    def probe_sequence_map(self, value):
        """ Sets the open addressed hash table's hash key to probe sequence mapping function. """
        self.probe_sequence_map_value = value

    @property
    def load_factor(self):
        """ Gets the table's load factor. """
        return self.count / self.capacity

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        hashCode = hash(Key)
        seq = self.probe_sequence_map.map(hashCode)
        for index in seq:
            i = index % self.capacity
            if self.values[i] is None:
                return None
            elif (not self.values[i].is_empty) and self.key_map.map(self.values[i].value) == Key:
                return self.values[i].value

    @property
    def is_empty(self):
        """ Gets a boolean value that indicates whether the table is empty or not. """
        return self.count == 0