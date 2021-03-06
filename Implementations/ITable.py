from IReadOnlyCollection import *

class ITable(IReadOnlyCollection):
    """ Describes a slightly modified version of the table ADT. """
    # Remarks:
    # TKey is the type of keys stored in the table, TItem is the type of items.

    def insert(self, Item):
        """ Inserts an item into the table. """
        # Post:
        # Returns true if item is successfully inserted, false if the table already contains an item with the same search key.
        raise NotImplementedError("Method 'ITable.insert' was not implemented.")

    def remove(self, Key):
        """ Removes a key from the table. """
        # Post:
        # This method returns true if the key is in the table, false if not.
        raise NotImplementedError("Method 'ITable.remove' was not implemented.")

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        # Remarks:
        # The original table ADT does not specify this method.
        # It is added, however, to compensate for the lack of the 'success' out parameter when using the retrieve operation.
        raise NotImplementedError("Method 'ITable.contains_key' was not implemented.")

    def to_list(self):
        """ Gets the table's items as a read-only list.
            The elements in this list are in the same order as those in the table's iterator, obtained through '__iter__' (the get iterator method).
            Any statement that applies to this method therefore also applies to the '__iter__' (get iterator) method, and vice-versa. """
        # Post:
        # This method returns a read-only list that describes the items in this table.
        # Modifications to this list are not allowed - it is read-only.
        # Furthermore, this list may be an alias to an internal list containing the table's items, or a copy.
        # This list need not be sorted, but must contain every item in the table.
        raise NotImplementedError("Method 'ITable.to_list' was not implemented.")

    @property
    def key_map(self):
        """ Gets the table's record-to-key map. """
        raise NotImplementedError("Getter of property 'ITable.key_map' was not implemented.")

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        # Pre:
        # For this method to return an item in the table, rather than null, the key must be in the table, i.e.
        # ContainsKey(Key) must return true.
        # Post:
        # The return value of this method will be the item that corresponds with the key, or None, if it is not found.
        # It is recommended to check if the table contains the key by using ContainsKey.
        raise NotImplementedError("Method 'ITable.__getitem__' was not implemented.")