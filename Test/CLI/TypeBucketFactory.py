import Project

class TypeBucketFactory(Project.IFactory):
    """ A bucket factory that creates buckets based on a function or type that takes one argument, the key map. """

    def __init__(self, Type):
        """ Creates a new bucket factory based on the given function or type. """
        self.type = Type

    def create(self, Argument):
        """ Creates a new bucket based on the given key map. """
        return self.type(Argument)