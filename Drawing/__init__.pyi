import Part, FreeCAD as App
from draftutils.utils import tolerance

# This module is the Drawing module
# AppDrawingPy.cpp

# Project a shape and return the visible/invisible parts of it.
# [visiblyG0,visiblyG1,hiddenG0,hiddenG1] = project(TopoShape[,App.Vector Direction, string type])
def project(shape: Part.Shape, Direction: App.Vector = ..., type: str = ...) -> list[Part.Shape]: ...

# Project a shape and return the all parts of it.
# [V,V1,VN,VO,VI,H,H1,HN,HO,HI] = projectEx(TopoShape[,App.Vector Direction, string type])
def projectEx(shape: Part.Shape, Direction: App.Vector = ..., type: str = ...) -> list[Part.Shape]: ...

# string = projectToSVG(TopoShape[, App.Vector direction, string type, float tolerance, dict vStyle,
#                       dict v0Style, dict v1Style, dict hStyle, dict h0Style, dict h1Style])
# Project a shape and return the SVG representation as string
def projectToSVG(s: Part.Shape, direction: App.Vector = ..., type: str = ...,
                tolerance: float = ..., vStyle: dict = ...,
                v0Style: dict = ..., v1Style: dict = ..., hStyle: dict = ..., h0Style: dict = ..., h1Style: dict = ...) -> str: ...

# Project a shape and return the DXF representation as string
def projectToDXF(s: Part.Shape, Direction: App.Vector = ..., type: str = ...) -> str: ...

# Removes the opening and closing svg tags
# and other metatags from a svg code, making it embeddable
def removeSvgTags(s: str) -> str: ...