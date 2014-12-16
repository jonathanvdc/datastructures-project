from IReadOnlyList import *

class IReadOnlySwapList(IReadOnlyList):
    """ Describes a generic read-only list that uses a list of the same element type as backing storage. This backing list can be swapped with another list. """

    def swap(self, Container):
        """ Swaps the swap list's backing storage with the provided list. """
        raise NotImplementedError("Method 'IReadOnlySwapList.swap' was not implemented.")