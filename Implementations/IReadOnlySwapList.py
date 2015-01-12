from IReadOnlyList import *

class IReadOnlySwapList(IReadOnlyList):
    """ Describes a generic read-only list that uses a list of the same element type as backing storage.
        This backing list can be swapped with another list. """
    # Remarks:
    # A read-only swap list's backing list can be changed by the client, but its elements cannot be modified by the client.
    # It may seem like this creates obvious loophole for list modification, as the client could retain a reference to the backing list.
    # The loophole is not reliable, however, as the class that contains the 'IReadOnlySwapList<T>' can also change the swap list's backing storage.
    # Thus, depending on said loophole could leave the client thinking they have a reference to the swap list's backing storage, even though they do in fact not.

    def swap(self, Container):
        """ Swaps the swap list's backing storage with the provided list. """
        # Pre:
        # 'Container' should be an empty list.
        # Post:
        # The swap list's backing list is set to list 'Container'.
        # If 'Container' is not empty, the swap list may clear it.
        # Remarks:
        # This method cannot be used to reliably insert new items in the swap list, as 'Container' may be cleared by the swap list.
        raise NotImplementedError("Method 'IReadOnlySwapList.swap' was not implemented.")