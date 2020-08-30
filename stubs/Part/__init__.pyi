import __FreeCADBase__ as Base
from FreeCAD import Vector, GeoFeature
from typing import Any, Sequence, overload, List
from .TopoShape import TopoShape

from draftutils.utils import tolerance

# Mod/Part/App/AppPart.cpp

# Part::TopoShapeCompoundPy;
class Compound:
    def __init__(self, polygon): ...    

# Part::TopoShapeEdgePy
class Edge:
    def __init__(self): ...

# Part::TopoShapeFacePy
class Face:
    def __init__(self, polygon): ...

# Part::LinePy
class Line:
    def __init__(self, p1, p2): ...

    def toShape(self): ...

class PointType:
    def __init__(self): ...

# Part::TopoShapeCompSolidPy
class CompSolid:
    def __init__(self): ...

# Part::TopoShapeShellPy
class Shell:
    def __init__(self): ...

# Part::TopoShapeVertexPy
class Vertex:
    Point: PointType
    def __init__(self): ...

Shape = TopoShape
# AppPart.cpp
# Part::TopoShapePy
#class Shape:
#    @property
#    def Solids(self) -> Sequence[Solid]: ...
#
#    def __getstate__(self):
#        "Serialize the content of this shape to a string in BREP format."
#        ...
#    def __setstate__(self, s: str):
#        "Deserialize the content of this shape from a string in BREP format."
#        ...
#    def read(self):
#        "Read in an IGES, STEP or BREP file."
#        ...
#    def writeInventor(self):
#        "Write the mesh in OpenInventor format to a string."
#        ...
#    def exportIges(self):
#        "Export the content of this shape to an IGES file."
#        ...
#    def exportStep(self):
#        "Export the content of this shape to an STEP file."
#        ...
#    def exportBrep(self):
#        "Export the content of this shape to an BREP file. BREP is a CasCade native format."
#        ...
#    def exportBinary(self):
#        "Export the content of this shape in binary format to a file."
#        ...
#    def exportBrepToString(self):
#        "Export the content of this shape to a string in BREP format. BREP is a CasCade native format."
#        ...
#    def dumpToString(self):
#        "Dump information about the shape to a string."
#        ...
#    def exportStl(self):
#        "Export the content of this shape to an STL mesh file."
#        ...
#
#    def importBrep(self):
#        "Load the shape from a file in BREP format."
#        ...
#
#    def importBinary(self):
#        "Import the content to this shape of a string in BREP format."
#        ...
#
#    def importBrepFromString(self):
#        "Load the shape from a string that keeps the content in BREP format.\nimportBrepFromString(str,False) to not display a progress bar."
#        ...
#
#    def extrude(self):
#        "Extrude the shape along a direction."
#        ...
#
#    def revolve(self, v1, v2, degree):
#        """Revolve the shape around an Axis to a given degree.
#
#        # revolves the shape around the Z Axis 360 degree.
#        Part.revolve(Vector(0,0,0),Vector(0,0,1),360)
#        
#Hints: Sometimes you want to create a rotation body out of a closed edge or wire.
#Example:
#
#        from FreeCAD import Base
#        import Part
#        V=Base.Vector
#        
#        e=Part.Ellipse()
#        s=e.toShape()
#        r=s.revolve(V(0,0,0),V(0,1,0), 360)
#        Part.show(r)
#        
#However, you may possibly realize some rendering artifacts or that the mesh
#creation seems to hang. This is because this way the surface is created twice.
#Since the curve is a full ellipse it is sufficient to do a rotation of 180 degree
#only, i.e. r=s.revolve(V(0,0,0),V(0,1,0), 180)
#        
#Now when rendering this object you may still see some artifacts at the poles. Now the
#problem seems to be that the meshing algorithm doesn't like to rotate around a point
#where there is no vertex.
#        
#The idea to fix this issue is that you create only half of the ellipse so that its shape
#representation has vertexes at its start and end point.
#        
#        from FreeCAD import Base
#        import Part
#        V=Base.Vector
#        
#        e=Part.Ellipse()
#        s=e.toShape(e.LastParameter//4,3*e.LastParameter//4)
#        r=s.revolve(V(0,0,0),V(0,1,0), 360)
#        Part.show(r)"""
#        ...
#    def check(self, runBopCheck):
#        """Checks the shape and report errors in the shape structure.
#This is a more detailed check as done in isValid().
#myShape.check(runBopCheck = False)
#if runBopCheck is True, a BOPCheck analysis is also performed."""
#        ...
#    def fuse(self):
#        "Union of this and a given (list of) topo shape.\nfuse(tool) -> Shape\n  or\nfuse((tool1,tool2,...),[tolerance=0.0]) -> Shape\n\nUnion of this and a given list of topo shapes.\n\nSupports (OCCT 6.9.0 and above):\n- Fuzzy Boolean operations (global tolerance for a Boolean operation)\n- Support of multiple arguments for a single Boolean operation\n- Parallelization of Boolean Operations algorithm\n\nBeginning from OCCT 6.8.1 a tolerance value can be specified."
#        ...
#    def multiFuse(self, v: Sequence[Shape], tolerance=0.0) -> Shape:
#        "multiFuse((tool1,tool2,...),[tolerance=0.0]) -> Shape\n\nUnion of this and a given list of topo shapes.\n\nSupports (OCCT 6.9.0 and above):\n- Fuzzy Boolean operations (global tolerance for a Boolean operation)\n- Support of multiple arguments for a single Boolean operation\n- Parallelization of Boolean Operations algorithm\n\nBeginning from OCCT 6.8.1 a tolerance value can be specified.\nDeprecated: use fuse() instead."
#        ...
#    def oldFuse(self):
#        "Union of this and a given topo shape (old algorithm)."
#        ...
#    def common(self):
#        "Intersection of this and a given (list of) topo shape.\ncommon(tool) -> Shape\n  or\ncommon((tool1,tool2,...),[tolerance=0.0]) -> Shape\n\nIntersection of this and a given list of topo shapes.\n\nSupports:\n- Fuzzy Boolean operations (global tolerance for a Boolean operation)\n- Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))\n- Parallelization of Boolean Operations algorithm\n\nOCC 6.9.0 or later is required."
#        ...
#    def section(self):
#        "Section of this with a given (list of) topo shape.\nsection(tool,[approximation=False]) -> Shape\n  or\nsection((tool1,tool2,...),[tolerance=0.0, approximation=False]) -> Shape\n\nIf approximation is True, section edges are approximated to a C1-continuous BSpline curve.\n\nSection of this and a given list of topo shapes.\n\nSupports:\n- Fuzzy Boolean operations (global tolerance for a Boolean operation)\n- Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))\n- Parallelization of Boolean Operations algorithm\n\nOCC 6.9.0 or later is required."
#        ...
#    def slices(self):
#        "Make slices of this shape."
#        ...
#    def slice(self):
#        "Make single slice of this shape."
#        ...
#    def cut(self):
#        "Difference of this and a given (list of) topo shape\ncut(tool) -> Shape\n  or\ncut((tool1,tool2,...),[tolerance=0.0]) -> Shape\n\nSubstraction of this and a given list of topo shapes.\n\nSupports:\n- Fuzzy Boolean operations (global tolerance for a Boolean operation)\n- Support of multiple arguments for a single Boolean operation\n- Parallelization of Boolean Operations algorithm\n\nOCC 6.9.0 or later is required."
#        ...
#    def generalFuse(self):
#        "generalFuse(list_of_other_shapes, fuzzy_value = 0.0): Run general fuse algorithm (GFA) between this and given shapes.\n\nlist_of_other_shapes: shapes to run the algorithm against (the list is\neffectively prepended by 'self').\n\nfuzzy_value: extra tolerance to apply when searching for interferences, in\naddition to tolerances of the input shapes.\n\nReturns a tuple of 2: (result, map).\n\nresult is a compound containing all the pieces generated by the algorithm\n(e.g., for two spheres, the pieces are three touching solids). Pieces that\ntouch share elements.\n\nmap is a list of lists of shapes, providing the info on which children of\nresult came from which argument. The length of list is equal to length of\nlist_of_other_shapes + 1. First element is a list of pieces that came from\nshape of this, and the rest are those that come from corresponding shapes in\nlist_of_other_shapes.\nhint: use isSame method to test shape equality\n\nParallelization of Boolean Operations algorithm\n\nOCC 6.9.0 or later is required.\n"
#        ...
#    def sewShape(self):
#        "Sew the shape if there is a gap."
#        ...
#    def childShapes(self):
#        "\nchildShapes([cumOri=True, cumLoc=True]) -> list\nReturn a list of sub-shapes that are direct children of this shape.\n * If cumOri is true, the function composes all\n   sub-shapes with the orientation of this shape.\n * If cumLoc is true, the function multiplies all\n   sub-shapes by the location of this shape, i.e. it applies to\n   each sub-shape the transformation that is associated with this shape."
#        ...
#    def ancestorsOfType(self):
#        "ancestorsOfType(shape, shape type) -> list\nFor a sub-shape of this shape get its ancestors of a type.\n        "
#        ...
#    def removeInternalWires(self):
#        "Removes internal wires (also holes) from the shape."
#        ...
#    def mirror(self):
#        "Mirror this shape on a given plane.\nThe plane is given with its base point and its normal direction."
#        ...
#    def transformGeometry(self):
#        "Apply geometric transformation on this or a copy the shape.\nThis method returns a new shape.\nThe transformation to be applied is defined as a 4x4 matrix.\nThe underlying geometry of the following shapes may change:\n- a curve which supports an edge of the shape, or\n- a surface which supports a face of the shape;\n\nFor example, a circle may be transformed into an ellipse when\napplying an affinity transformation. It may also happen that\nthe circle then is represented as a B-spline curve.\n\nThe transformation is applied to:\n- all the curves which support edges of the shape, and\n- all the surfaces which support faces of the shape.\n\nNote: If you want to transform a shape without changing the\nunderlying geometry then use the methods translate or rotate.\n\ntransformGeometry(Matrix) -> Shape\n"
#        ...
#    def transformShape(self):
#        "Apply transformation on a shape without changing\nthe underlying geometry.\ntransformShape(Matrix,[boolean copy=False, checkScale=False]) -> None\n\nIf checkScale is True, it will use transformGeometry if non-uniform\nscaling is detected."
#        ...
#    def transformed(self):
#        "\ntransformed(Matrix,copy=False,checkScale=False,op=None) -> shape\n\nCreate a new transformed shape\n"
#    def translate(self):
#        "Apply the translation to the current location of this shape."
#        ...
#    def translated(self):
#        "\ntranslated(vector) -> shape\n\nCreate a new shape with translation\n"
#        ...
#    def rotate(self):
#        "\nApply the rotation (base,dir,degree) to the current location of this shape\nShp.rotate(Vector(0,0,0),Vector(0,0,1),180) - rotate the shape around the Z Axis 180 degrees.\n"
#        ...
#    def rotated(self):
#        "\nrotated(base,dir,degree) -> shape\n\nCreate a new shape with rotation.\n"
#        ...
#    def scale(self):
#        "Apply scaling with point and factor to this shape."
#        ...
#    def scaled(self):
#        "\nscaled(factor,base=Vector(0,0,0)) -> shape\n\nCreate a new shape with scale.\n"
#        ...
#    def makeFillet(self):
#        "Make fillet."
#        ...
#    def makeChamfer(self):
#        "Make chamfer."
#        ...
#    def makeThickness(self):
#        "makeThickness(List of shapes, Offset (Float), Tolerance (Float)) -> Shape\nA hollowed solid is built from an initial solid and a set of faces on this solid,\nwhich are to be removed. The remaining faces of the solid become the walls of\nthe hollowed solid, their thickness defined at the time of construction."
#        ...
#    def makeOffsetShape(self):
#        "makeOffsetShape(offset, tolerance, inter = False, self_inter = False,\noffsetMode = 0, join = 0, fill = False): makes an offset shape (3d offsetting).\nThe function supports keyword arguments.\n\n* offset: distance to expand the shape by. Negative value will shrink the\nshape.\n\n* tolerance: precision of approximation.\n\n* inter: (parameter to OCC routine; not implemented)\n\n* self_inter: (parameter to OCC routine; not implemented)\n\n* offsetMode: 0 = skin; 1 = pipe; 2 = recto-verso\n\n* join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =\nintersection\n\n* fill: if true, offsetting a shell is to yield a solid\n\nReturns: result of offsetting."
#        ...
#    def makeOffset2D(self):
#        "makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection =\nfalse): makes an offset shape (2d offsetting). The function supports keyword\narguments. Input shape (self) can be edge, wire, face, or a compound of those.\n\n* offset: distance to expand the shape by. Negative value will shrink the\nshape.\n\n* join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =\nintersection\n\n* fill: if true, the output is a face filling the space covered by offset. If\nfalse, the output is a wire.\n\n* openResult: affects the way open wires are processed. If False, an open wire\nis made. If True, a closed wire is made from a double-sided offset, with rounds\naround open vertices.\n\n* intersection: affects the way compounds are processed. If False, all children\nare offset independently. If True, and children are edges/wires, the children\nare offset in a collective manner. If compounding is nested, collectiveness\ndoes not spread across compounds (only direct children of a compound are taken\ncollectively).\n\nReturns: result of offsetting (wire or face or compound of those). Compounding\nstructure follows that of source shape."
#        ...
#    def makeWires(self):
#        "\nmakeWires(op=None): make wire(s) using the edges of this shape\n\nThe function will sort any edges inside the current shape, and connect them\ninto wire. If more than one wire is found, then it will make a compound out of\nall found wires.\n\nThis function is element mapping aware. If the input shape has non-zero Tag,\nit will map any edge and vertex element name inside the input shape into the\nitself.\n\nop: an optional string to be appended when auto generates element mapping.\n        "
#        ...
#    def reverse(self):
#        "Reverses the orientation of this shape."
#    def complement(self):
#        "Computes the complement of the orientation of this shape,\ni.e. reverses the interior/exterior status of boundaries of this shape."
#        ...
#    def nullify(self):
#        "Destroys the reference to the underlying shape stored in this shape.\nAs a result, this shape becomes null."
#        ...
#    def isClosed(self):
#        "Checks if the shape is closed\nIf the shape is a shell it returns True if it has no free boundaries (edges).\nIf the shape is a wire it returns True if it has no free ends (vertices).\n(Internal and External sub-shepes are ignored in these checks)\nIf the shape is an edge it returns True if its vertices are the same.\n"
#        ...
#    def isPartner(self):
#        "Checks if both shapes share the same geometry.\n        Placement and orientation may differ.\n        "
#        ...
#    def isSame(self):
#        "Checks if both shapes share the same geometry\n        and placement. Orientation may differ.\n        "
#        ...
#    def isEqual(self):
#        "Checks if both shapes are equal.\n        This means geometry, placement and orientation are equal.\n        "
#        ...
#    def isNull(self):
#        "Checks if the shape is null."
#        ...
#    def isValid(self):
#        "Checks if the shape is valid, i.e. neither null, nor empty nor corrupted."
#        ...
#    def isCoplanar(self):
#        "isCoplanar(shape,tol=None) -- Checks if this shape is coplanar with the given shape."
#        ...
#    def findPlane(self):
#        "findPlane(tol=None) -- return a plane if the shape is planar"
#        ...
#    def fix(self):
#        "Tries to fix a broken shape. True is returned if the operation succeeded, False otherwise.\nfix(working precision, minimum precision, maximum precision)\n        "
#        ...
#    def hashCode(self):
#        "This value is computed from the value of the underlying shape reference and the location.\nOrientation is not taken into account."
#        ...
#    def tessellate(self):
#        "Tessellate the shape and return a list of vertices and face indices"
#        ...
#    def project(self):
#        "Project a list of shapes on this shape"
#        ...
#    def makeParallelProjection(self):
#        "Parallel projection of an edge or wire on this shape\nmakeParallelProjection(shape, dir)\n        "
#        ...
#    def makePerspectiveProjection(self):
#        "Perspective projection of an edge or wire on this shape\nmakePerspectiveProjection(shape, pnt)\n        "
#        ...
#    def reflectLines(self):
#        "Build reflect lines on a shape according to the axes of view.\nReflect lines are represented by edges in 3d.\nreflectLines(ViewDir, ViewPos, UpDir) -> Shape\n        "
#        ...
#    def makeShapeFromMesh(self):
#        "Make a compound shape out of mesh data.\nNote: This should be used for rather small meshes only."
#        ...
#    def toNurbs(self):
#        "Conversion of the complete geometry of a shape into NURBS geometry.\nFor example, all curves supporting edges of the basis shape are converted\ninto B-spline curves, and all surfaces supporting its faces are converted\ninto B-spline surfaces."
#        ...
#    def copy(self) -> Shape:
#        "Create a copy of this shape\ncopy(copyGeom=True, copyMesh=False) -> Shape\nIf copyMesh is True, triangulation contained in original shape will be\ncopied along with geometry.\nIf copyGeom is False, only topological objects will be copied, while\ngeometry and triangulation will be shared with original shape.\n"
#        ...
#    def cleaned(self):
#        "This creates a cleaned copy of the shape with the triangulation removed.\nThis can be useful to reduce file size when exporting as a BREP file.\nWarning: Use the cleaned shape with care because certain algorithms may work incorrectly\nif the shape has no internal triangulation any more.\n"
#        ...
#    def replaceShape(self):
#        "Replace a sub-shape with a new shape and return a new shape.\nThe parameter is in the form list of tuples with the two shapes."
#        ...
#    def removeShape(self):
#        "Remove a sub-shape and return a new shape.\nThe parameter is a list of shapes."
#        ...
#    def defeaturing(self):
#        "Remove a feature defined by supplied faces and return a new shape.\nThe parameter is a list of faces."
#        ...
#    def isInside(self):
#        "Checks whether a point is inside or outside the shape.\nisInside(App.Vector, float, Boolean) => Boolean\nThe App.Vector is the point you want to check if it's inside or not\nfloat gives the tolerance\nBoolean indicates if the point lying directly on a face is considered to be inside or not \n        "
#        ...
#    def removeSplitter(self) -> Shape:
#        "Removes redundant edges from the B-REP model"
#        ...
#    def proximity(self):
#        "proximity(Shape s): Returns two lists of Face indexes for the Faces involved in the intersection."
#        ...
#    def distToShape(self):
#        "Find the minimum distance to another shape.\ndistToShape(Shape s):  Returns a list of minimum distance and solution point pairs.\n\nReturned is a tuple of three: (dist, vectors, infos).\n\ndist is the minimum distance, in mm (float value).\n\nvectors is a list of pairs of App.Vector. Each pair corresponds to solution.\nExample: [(Vector (2.0, -1.0, 2.0), Vector (2.0, 0.0, 2.0)), (Vector (2.0,\n-1.0, 2.0), Vector (2.0, -1.0, 3.0))] First vector is a point on self, second\nvector is a point on s.\n\ninfos contains additional info on the solutions. It is a list of tuples:\n(topo1, index1, params1, topo2, index2, params2)\n\n    topo1, topo2 are strings identifying type of BREP element: 'Vertex',\n    'Edge', or 'Face'.\n\n    index1, index2 are indexes of the elements (zero-based).\n\n    params1, params2 are parameters of internal space of the elements. For\n    vertices, params is None. For edges, params is one float, u. For faces,\n    params is a tuple (u,v). "
#        ...
#    def getElement(self):
#        "Returns a SubElement"
#        ...
#    def countElement(self):
#        "Returns the count of a type of element"
#        ...
#    def getTolerance(self):
#        "\n        getTolerance(mode, ShapeType=Shape) -> float\n\n        Determines a tolerance from the ones stored in a shape\n        mode = 0 : returns the average value between sub-shapes,\n        mode > 0 : returns the maximal found,\n        mode < 0 : returns the minimal found.\n        ShapeType defines what kinds of sub-shapes to consider:\n        Shape (default) : all : Vertex, Edge, Face,\n        Vertex : only vertices,\n        Edge   : only edges,\n        Face   : only faces,\n        Shell  : combined Shell + Face, for each face (and containing\n                 shell), also checks edge and Vertex\n        "
#        ...
#    def overTolerance(self):
#        "\n        overTolerance(value, ShapeType=Shape) -> float\n\n        Determines which shapes have a tolerance over the given value\n        ShapeType is interpreted as in the method getTolerance\n        "
#        ...
#    def inTolerance(self):
#        "\n        inTolerance(value, ShapeType=Shape) -> float\n\n        Determines which shapes have a tolerance within a given interval\n        ShapeType is interpreted as in the method getTolerance\n        "
#        ...
#    def globalTolerance(self):
#        "\n        globalTolerance(mode) -> float\n\n        Returns the computed tolerance according to the mode\n        mode = 0 : average\n        mode > 0 : maximal\n        mode < 0 : minimal\n        "
#        ...
#    def fixTolerance(self):
#        "\n        fixTolerance(value, ShapeType=Shape)\n\n        Sets (enforces) tolerances in a shape to the given value\n        ShapeType = Vertex : only vertices are set\n        ShapeType = Edge   : only edges are set\n        ShapeType = Face   : only faces are set\n        ShapeType = Wire   : to have edges and their vertices set\n        ShapeType = other value : all (vertices,edges,faces) are set\n        "
#        ...
#    def limitTolerance(self):
#        "\n        limitTolerance(tmin, tmax=0, ShapeType=Shape)\n\n        Limits tolerances in a shape as follows :\n        tmin = tmax -> as fixTolerance (forces)\n        tmin = 0   -> maximum tolerance will be tmax\n        tmax = 0 or not given (more generally, tmax < tmin) ->\n        tmax ignored, minimum will be tmin\n        else, maximum will be max and minimum will be min\n        ShapeType = Vertex : only vertices are set\n        ShapeType = Edge   : only edges are set\n        ShapeType = Face   : only faces are set\n        ShapeType = Wire   : to have edges and their vertices set\n        ShapeType = other value : all (vertices,edges,faces) are set\n        Returns True if at least one tolerance of the sub-shape has\n        been modified\n        "
#        ...
#
#    def optimalBoundingBox(self):
#        "\n        optimalBoundingBox(useTriangulation = True, useShapeTolerance = False) -> bound box\n        "
#        ...

# Part::TopoShapeSolidPy
class Solid(Shape):
    def __init__(self): ...

# PartFeature.cpp
# Part::PartFeaturePy (Part.Feature)             
class Feature(GeoFeature):
    @property
    def Shape(self) -> Shape: ...

# (Part.FeaturePython)
class FeaturePython(Feature):
    ...


# Part::TopoShapeWirePy
class Wire:
    def __init__(self, obj: Shape) -> None: ...

# PartExceptionOCCError
class OCCError(Base.FreeCADError):
    ...

# PartExceptionOCCDomainError
class OCCDomainError(OCCError):
    ...

# PartExceptionOCCRangeError
class OCCRangeError(OCCDomainError): ...

# PartExceptionOCCConstructionError
class OCCConstructionError(OCCDomainError): ...

# PartExceptionOCCDimensionError
class OCCDimensionError(OCCDomainError): ...

# Part::LineSegmentPy                
class LineSegment:
    @overload
    def __init__(self, line: Line, fist, last): ...
    @overload
    def __init__(self, line_segment: LineSegment, fist, last): ...
    @overload
    def __init__(self, line_segment: LineSegment): ...
    @overload
    def __init__(self, v1, v2): ...

    def toShape(self): ...

# Part::PointPy                      
class Point: ...

# Part::ConicPy                      
class Conic: ...

# Part::ArcOfConicPy                 
class ArcOfConic: ...

# Part::CirclePy                     
class Circle: ...

# Part::EllipsePy                    
class Ellipse: ...

# Part::HyperbolaPy                  
class Hyperbola: ...

# Part::ParabolaPy                   
class Parabola: ...

# Part::ArcPy                        
class Arc: ...

# Part::ArcOfCirclePy                
class ArcOfCircle: ...

# Part::ArcOfEllipsePy               
class ArcOfEllipse: ...

# Part::ArcOfParabolaPy              
class ArcOfParabola: ...

# Part::ArcOfHyperbolaPy             
class ArcOfHyperbola: ...

# Part::BezierCurvePy                
class BezierCurve: ...

# Part::BSplineCurvePy               
class BSplineCurve: ...

# Part::OffsetCurvePy                
class OffsetCurve: ...

# Part::PlanePy                      
class Plane: ...

# Part::CylinderPy                   
class Cylinder: ...

# Part::ConePy                       
class Cone: ...

# Part::SpherePy                     
class Sphere: ...

# Part::ToroidPy                     
class Toroid: ...

# Part::BezierSurfacePy              
class BezierSurface: ...

# Part::BSplineSurfacePy             
class BSplineSurface: ...

# Part::OffsetSurfacePy              
class OffsetSurface: ...

# Part::PlateSurfacePy               
class PlateSurface: ...

# Part::SurfaceOfExtrusionPy         
class SurfaceOfExtrusion: ...

# Part::SurfaceOfRevolutionPy        
class SurfaceOfRevolution: ...

# Part::RectangularTrimmedSurfacePy  
class RectangularTrimmedSurface: ...

# Attacher::AttachEnginePy           
class AttachEngine: ...

# Part::GeometryIntExtensionPy       
class GeometryIntExtension: ...

# Part::GeometryStringExtensionPy    
class GeometryStringExtension: ...

# Part::GeometryBoolExtensionPy      
class GeometryBoolExtension: ...

# Part::GeometryDoubleExtensionPy    
class GeometryDoubleExtension: ...

def makePolygon(pntslist: List[Vector]) -> Wire: ...
def makeCompound(shapes: List[Shape]): ...
def makeFace(wires, type: str): ...

def makePlane(length: float, width: float, pnt: Vector = ..., dirZ: Vector = ..., dirX: Vector = ...):
    "makePlane(length,width,[pnt,dirZ,dirX]) -- Make a plane\n"
    "By default pnt=Vector(0,0,0) and dirZ=Vector(0,0,1), dirX is ignored in this case"
    ...
