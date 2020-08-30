from . import BaseClass

class Persistence(BaseClass):
    """This is a persistence class"""
    def dumpContent(self):
        """Dumps the content of the object, both the XML representation as well as the additional datafiles  
    required, into a byte representation. It will be returned as byte array.
    dumpContent() -- returns a byte array with full content
    dumpContent(Compression=1-9) -- Sets the data compression from 0 (no) to 9 (max)
                    """
        ...

    def restoreContent(self):
        """Restore the content of the object from a byte representation as stored by \"dumpContent\".
    It could be restored from any python object implementing the buffer protocol.
    restoreContent(buffer) -- restores from the given byte array
                    """
        ...

    @property
    def Content(self):
        """Content of the object in XML representation"""
        ...

    @property
    def MemSize(self):
        """Memory size of the object in byte"""
        ...


