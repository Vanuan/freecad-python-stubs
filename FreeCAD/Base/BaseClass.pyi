from .PyObjectBase import PyObjectBase

class BaseClass(PyObjectBase):
    """This is the base class"""
    def isDerivedFrom(self):
        """Returns true if given type is a father"""
        ...

    def getAllDerivedFrom(self):
        """Returns all descendants"""
        ...

    @property
    def TypeId(self):
        """Is the type of the FreeCAD object with module domain"""
        ...

    @property
    def Module(self):
        """Module in which this class is defined"""
        ...


