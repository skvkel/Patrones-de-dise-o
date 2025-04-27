import copy
from typing import Any


class MyClass:

    def __init__(self,
                 my_float: float,
                 object_list: list[Any]):
        self.my_float = my_float
        self.object_list = object_list

    def __copy__(self):
        """ Create a shallow copy """

        # Copy the nested objects
        object_list = copy.copy(self.object_list)

        new_object = self.__class__(
            self.my_float,
            object_list
        )
        new_object.__dict__.update(self.__dict__)

        return new_object

    def __deepcopy__(self, memo=None):
        """ Create a deep copy """
        if memo is None:
            memo = {}

        # Copy the nested objects
        object_list = copy.deepcopy(self.object_list, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new_object = self.__class__(
            self.my_float, object_list
        )
        new_object.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new_object
