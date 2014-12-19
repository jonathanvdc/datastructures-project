from ISortableTable import *

class ListTable(ISortableTable):
    """ An implementation of a table that uses a list as backing storage. """

    def __init__(self, KeyMap, List):
        """ Creates a new list table instance. """
        self.key_map = KeyMap
        self.list = List

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        for item in self.list:
            if self.key_map.map(item) == Key:
                return True
        return False

    def remove(self, Key):
        """ Removes a key from the table. """
        i = 0
        while i < self.list.count:
            if self.key_map.map(self.list[i]) == Key:
                self.list.remove_at(i)
                return True
            i += 1
        return False

    def insert(self, Item):
        """ Inserts an item into the table. """
        if self.contains_key(self.key_map.map(Item)):
            return False
        else:
            self.list.add(Item)
            return True

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.list.__iter__()

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        return self.list

    def sort(self, ItemComparer):
        """ Sorts the list based on the given item comparer. """
        self.quicksort(ItemComparer, 0, self.list.count - 1)

    def quicksort(self, ItemComparer, Start, End):
        """ Sorts (a portion of) the list table's list in-place using the quicksort algorithm. """
        if Start < End:
            p = self.partition(ItemComparer, Start, End)
            self.quicksort(ItemComparer, Start, p - 1)
            self.quicksort(ItemComparer, p + 1, End)

    def partition(self, ItemComparer, Start, End):
        """ 'Partitions' the list. Basically, a pivot item is selected, and all items that have a search key less than the pivot will be moved to the start of the list. The pivot item will be the next item in the list, followed immediately by all items that have a search key greater than or equal to the pivot. The returns value consists of the index of the pivot in the modified list. This method is used by the quicksort sorting method. """
        pivotIndex = (Start + End) // 2
        pivot = self.list[pivotIndex]
        lowIndex = Start
        self.swap(pivotIndex, End)
        i = Start
        while i < End:
            if ItemComparer.compare(self.list[i], pivot) < 0:
                self.swap(lowIndex, i)
                lowIndex += 1
            i += 1
        self.swap(lowIndex, End)
        return lowIndex

    def swap(self, First, Second):
        """ Swaps two item's positions in the list. """
        temp = self.list[First]
        self.list[First] = self.list[Second]
        self.list[Second] = temp

    @property
    def key_map(self):
        """ Gets the value-to-key mapping function of this list table. """
        return self.key_map_value

    @key_map.setter
    def key_map(self, value):
        """ Sets the value-to-key mapping function of this list table. """
        self.key_map_value = value

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        for item in self.list:
            if self.key_map.map(item) == Key:
                return item
        return None

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        return self.list.count