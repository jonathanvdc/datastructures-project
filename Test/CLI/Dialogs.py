from CommandLineDialog import *
from MenuDialog import *
from OptionDialog import *
from CollectionDialog import *
from LazyCollectionDialog import *
from NewUserDialog import *
from NewMovieDialog import *
from NewShowtimeDialog import *
from NewTimeslotDialog import *
from NewAuditoriumDialog import *
from ReserveTicketDialog import *
from RedeemTicketDialog import *
from DeleteTimeslotDialog import *
from SwapBackingListDialog import *
from SwapBackingTableDialog import *
from SwapBackingSortedListDialog import *
from SwapSortableBackingTableDialog import *
from SortTableDialog import *
from QuitDialog import *
from TopLevelDialog import *

from SetTimeDialog import *

# These types can only exist in dynamic programming languages such as Python
# They have been added to the CLI folder, rather than the core 'Implementations' folder,
# to keep the core implementations as portable as possible: they can just as easily be implemented in C++,
# Java, C#, Visual Basic... 
# These types do not belong in said category, as they make borderline use of dynamic typing and runtime reflection.
# Since the command-line interface is Python-specific, it seemed acceptable to include them here.
from FieldComparer import *
from FieldMap import *
from TypeBucketFactory import *

import ShowtimeManager