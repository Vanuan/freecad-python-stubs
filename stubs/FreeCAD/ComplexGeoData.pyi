from .Base.Persistence import Persistence

class ComplexGeoData(Persistence):
    """Father of all complex geometric data types"""
    def getFacesFromSubelement(self):
        """Return vertexes and faces from a sub-element"""
        ...

    @property
    def BoundBox(self):
        """Get the BoundBox of the object"""
        ...

    @property
    def Placement(self):
        """Get the current transformation of the object as placement"""
        ...

    @property
    def Matrix(self):
        """Get the current transformation of the object as matrix"""
        ...

    @property
    def Tag(self):
        """Geometry Tag"""
        ...


