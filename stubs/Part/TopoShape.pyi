from FreeCAD.ComplexGeoData import ComplexGeoData

class TopoShape(ComplexGeoData):
    """TopoShape is the OpenCasCade topological shape wrapper.
Sub-elements such as vertices, edges or faces are accessible as:
* Vertex#, where # is in range(1, number of vertices)
* Edge#, where # is in range(1, number of edges)
* Face#, where # is in range(1, number of faces)"""
    def __getstate__(self):
        """Serialize the content of this shape to a string in BREP format."""
        ...

    def __setstate__(self):
        """Deserialize the content of this shape from a string in BREP format."""
        ...

    def read(self):
        """Read in an IGES, STEP or BREP file."""
        ...

    def writeInventor(self):
        """Write the mesh in OpenInventor format to a string."""
        ...

    def exportIges(self):
        """Export the content of this shape to an IGES file."""
        ...

    def exportStep(self):
        """Export the content of this shape to an STEP file."""
        ...

    def exportBrep(self):
        """Export the content of this shape to an BREP file. BREP is a CasCade native format."""
        ...

    def exportBinary(self):
        """Export the content of this shape in binary format to a file."""
        ...

    def exportBrepToString(self):
        """Export the content of this shape to a string in BREP format. BREP is a CasCade native format."""
        ...

    def dumpToString(self):
        """Dump information about the shape to a string."""
        ...

    def exportStl(self):
        """Export the content of this shape to an STL mesh file."""
        ...

    def importBrep(self):
        """Load the shape from a file in BREP format."""
        ...

    def importBinary(self):
        """Import the content to this shape of a string in BREP format."""
        ...

    def importBrepFromString(self):
        """Load the shape from a string that keeps the content in BREP format.
    importBrepFromString(str,False) to not display a progress bar.
            """
        ...

    def extrude(self):
        """Extrude the shape along a direction."""
        ...

    def revolve(self):
        """Revolve the shape around an Axis to a given degree.
    Part.revolve(Vector(0,0,0),Vector(0,0,1),360) - revolves the shape around the Z Axis 360 degree.
    
    Hints: Sometimes you want to create a rotation body out of a closed edge or wire.
    Example:
    from FreeCAD import Base
    import Part
    V=Base.Vector
    
    e=Part.Ellipse()
    s=e.toShape()
    r=s.revolve(V(0,0,0),V(0,1,0), 360)
    Part.show(r)
    
    However, you may possibly realize some rendering artifacts or that the mesh
    creation seems to hang. This is because this way the surface is created twice.
    Since the curve is a full ellipse it is sufficient to do a rotation of 180 degree
    only, i.e. r=s.revolve(V(0,0,0),V(0,1,0), 180)
    
    Now when rendering this object you may still see some artifacts at the poles. Now the
    problem seems to be that the meshing algorithm doesn't like to rotate around a point
    where there is no vertex.
    
    The idea to fix this issue is that you create only half of the ellipse so that its shape
    representation has vertexes at its start and end point.
    
    from FreeCAD import Base
    import Part
    V=Base.Vector
    
    e=Part.Ellipse()
    s=e.toShape(e.LastParameter/4,3*e.LastParameter/4)
    r=s.revolve(V(0,0,0),V(0,1,0), 360)
    Part.show(r)
            """
        ...

    def check(self):
        """Checks the shape and report errors in the shape structure.
    This is a more detailed check as done in isValid().
    myShape.check(runBopCheck = False)
    if runBopCheck is True, a BOPCheck analysis is also performed."""
        ...

    def fuse(self):
        """Union of this and a given (list of) topo shape.
    fuse(tool) -> Shape
      or
    fuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
    
    Union of this and a given list of topo shapes.
    
    Supports (OCCT 6.9.0 and above):
    - Fuzzy Boolean operations (global tolerance for a Boolean operation)
    - Support of multiple arguments for a single Boolean operation
    - Parallelization of Boolean Operations algorithm
    
    Beginning from OCCT 6.8.1 a tolerance value can be specified."""
        ...

    def multiFuse(self):
        """multiFuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
    
    Union of this and a given list of topo shapes.
    
    Supports (OCCT 6.9.0 and above):
    - Fuzzy Boolean operations (global tolerance for a Boolean operation)
    - Support of multiple arguments for a single Boolean operation
    - Parallelization of Boolean Operations algorithm
    
    Beginning from OCCT 6.8.1 a tolerance value can be specified.
    Deprecated: use fuse() instead."""
        ...

    def oldFuse(self):
        """Union of this and a given topo shape (old algorithm)."""
        ...

    def common(self):
        """Intersection of this and a given (list of) topo shape.
    common(tool) -> Shape
      or
    common((tool1,tool2,...),[tolerance=0.0]) -> Shape
    
    Intersection of this and a given list of topo shapes.
    
    Supports:
    - Fuzzy Boolean operations (global tolerance for a Boolean operation)
    - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
    - Parallelization of Boolean Operations algorithm
    
    OCC 6.9.0 or later is required."""
        ...

    def section(self):
        """Section of this with a given (list of) topo shape.
    section(tool,[approximation=False]) -> Shape
      or
    section((tool1,tool2,...),[tolerance=0.0, approximation=False]) -> Shape
    
    If approximation is True, section edges are approximated to a C1-continuous BSpline curve.
    
    Section of this and a given list of topo shapes.
    
    Supports:
    - Fuzzy Boolean operations (global tolerance for a Boolean operation)
    - Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
    - Parallelization of Boolean Operations algorithm
    
    OCC 6.9.0 or later is required."""
        ...

    def slices(self):
        """Make slices of this shape."""
        ...

    def slice(self):
        """Make single slice of this shape."""
        ...

    def cut(self):
        """Difference of this and a given (list of) topo shape
    cut(tool) -> Shape
      or
    cut((tool1,tool2,...),[tolerance=0.0]) -> Shape
    
    Substraction of this and a given list of topo shapes.
    
    Supports:
    - Fuzzy Boolean operations (global tolerance for a Boolean operation)
    - Support of multiple arguments for a single Boolean operation
    - Parallelization of Boolean Operations algorithm
    
    OCC 6.9.0 or later is required."""
        ...

    def generalFuse(self):
        """generalFuse(list_of_other_shapes, fuzzy_value = 0.0): Run general fuse algorithm (GFA) between this and given shapes.
    
    list_of_other_shapes: shapes to run the algorithm against (the list is
    effectively prepended by 'self').
    
    fuzzy_value: extra tolerance to apply when searching for interferences, in
    addition to tolerances of the input shapes.
    
    Returns a tuple of 2: (result, map).
    
    result is a compound containing all the pieces generated by the algorithm
    (e.g., for two spheres, the pieces are three touching solids). Pieces that
    touch share elements.
    
    map is a list of lists of shapes, providing the info on which children of
    result came from which argument. The length of list is equal to length of
    list_of_other_shapes + 1. First element is a list of pieces that came from
    shape of this, and the rest are those that come from corresponding shapes in
    list_of_other_shapes.
    hint: use isSame method to test shape equality
    
    Parallelization of Boolean Operations algorithm
    
    OCC 6.9.0 or later is required.
    """
        ...

    def sewShape(self):
        """Sew the shape if there is a gap."""
        ...

    def childShapes(self):
        """
    childShapes([cumOri=True, cumLoc=True]) -> list
    Return a list of sub-shapes that are direct children of this shape.
     * If cumOri is true, the function composes all
       sub-shapes with the orientation of this shape.
     * If cumLoc is true, the function multiplies all
       sub-shapes by the location of this shape, i.e. it applies to
       each sub-shape the transformation that is associated with this shape.
            """
        ...

    def ancestorsOfType(self):
        """ancestorsOfType(shape, shape type) -> list
    For a sub-shape of this shape get its ancestors of a type.
            """
        ...

    def removeInternalWires(self):
        """Removes internal wires (also holes) from the shape."""
        ...

    def mirror(self):
        """Mirror this shape on a given plane.
    The plane is given with its base point and its normal direction."""
        ...

    def transformGeometry(self):
        """Apply geometric transformation on this or a copy the shape.
    This method returns a new shape.
    The transformation to be applied is defined as a 4x4 matrix.
    The underlying geometry of the following shapes may change:
    - a curve which supports an edge of the shape, or
    - a surface which supports a face of the shape;
    
    For example, a circle may be transformed into an ellipse when
    applying an affinity transformation. It may also happen that
    the circle then is represented as a B-spline curve.
    
    The transformation is applied to:
    - all the curves which support edges of the shape, and
    - all the surfaces which support faces of the shape.
    
    Note: If you want to transform a shape without changing the
    underlying geometry then use the methods translate or rotate.
    
    transformGeometry(Matrix) -> Shape
    """
        ...

    def transformShape(self):
        """Apply transformation on a shape without changing
    the underlying geometry.
    transformShape(Matrix,[boolean copy=False, checkScale=False]) -> None
    
    If checkScale is True, it will use transformGeometry if non-uniform
    scaling is detected."""
        ...

    def transformed(self):
        """
    transformed(Matrix,copy=False,checkScale=False,op=None) -> shape
    
    Create a new transformed shape
            """
        ...

    def translate(self):
        """Apply the translation to the current location of this shape."""
        ...

    def translated(self):
        """
    translated(vector) -> shape
    
    Create a new shape with translation
             """
        ...

    def rotate(self):
        """
    Apply the rotation (base,dir,degree) to the current location of this shape
    Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) - rotate the shape around the Z Axis 180 degrees.
            """
        ...

    def rotated(self):
        """
    rotated(base,dir,degree) -> shape
    
    Create a new shape with rotation.
            """
        ...

    def scale(self):
        """Apply scaling with point and factor to this shape."""
        ...

    def scaled(self):
        """
    scaled(factor,base=Vector(0,0,0)) -> shape
    
    Create a new shape with scale.
              """
        ...

    def makeFillet(self):
        """Make fillet."""
        ...

    def makeChamfer(self):
        """Make chamfer."""
        ...

    def makeThickness(self):
        """makeThickness(List of shapes, Offset (Float), Tolerance (Float)) -> Shape
    A hollowed solid is built from an initial solid and a set of faces on this solid,
    which are to be removed. The remaining faces of the solid become the walls of
    the hollowed solid, their thickness defined at the time of construction."""
        ...

    def makeOffsetShape(self):
        """makeOffsetShape(offset, tolerance, inter = False, self_inter = False,
    offsetMode = 0, join = 0, fill = False): makes an offset shape (3d offsetting).
    The function supports keyword arguments.
    
    * offset: distance to expand the shape by. Negative value will shrink the
    shape.
    
    * tolerance: precision of approximation.
    
    * inter: (parameter to OCC routine; not implemented)
    
    * self_inter: (parameter to OCC routine; not implemented)
    
    * offsetMode: 0 = skin; 1 = pipe; 2 = recto-verso
    
    * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
    intersection
    
    * fill: if true, offsetting a shell is to yield a solid
    
    Returns: result of offsetting."""
        ...

    def makeOffset2D(self):
        """makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection =
    false): makes an offset shape (2d offsetting). The function supports keyword
    arguments. Input shape (self) can be edge, wire, face, or a compound of those.
    
    * offset: distance to expand the shape by. Negative value will shrink the
    shape.
    
    * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
    intersection
    
    * fill: if true, the output is a face filling the space covered by offset. If
    false, the output is a wire.
    
    * openResult: affects the way open wires are processed. If False, an open wire
    is made. If True, a closed wire is made from a double-sided offset, with rounds
    around open vertices.
    
    * intersection: affects the way compounds are processed. If False, all children
    are offset independently. If True, and children are edges/wires, the children
    are offset in a collective manner. If compounding is nested, collectiveness
    does not spread across compounds (only direct children of a compound are taken
    collectively).
    
    Returns: result of offsetting (wire or face or compound of those). Compounding
    structure follows that of source shape."""
        ...

    def makeWires(self):
        """
    makeWires(op=None): make wire(s) using the edges of this shape
    
    The function will sort any edges inside the current shape, and connect them
    into wire. If more than one wire is found, then it will make a compound out of
    all found wires.
    
    This function is element mapping aware. If the input shape has non-zero Tag,
    it will map any edge and vertex element name inside the input shape into the
    itself.
    
    op: an optional string to be appended when auto generates element mapping.
            """
        ...

    def reverse(self):
        """Reverses the orientation of this shape."""
        ...

    def complement(self):
        """Computes the complement of the orientation of this shape,
    i.e. reverses the interior/exterior status of boundaries of this shape."""
        ...

    def nullify(self):
        """Destroys the reference to the underlying shape stored in this shape.
    As a result, this shape becomes null."""
        ...

    def isClosed(self):
        """Checks if the shape is closed
    If the shape is a shell it returns True if it has no free boundaries (edges).
    If the shape is a wire it returns True if it has no free ends (vertices).
    (Internal and External sub-shepes are ignored in these checks)
    If the shape is an edge it returns True if its vertices are the same.
    """
        ...

    def isPartner(self):
        """Checks if both shapes share the same geometry.
            Placement and orientation may differ.
            """
        ...

    def isSame(self):
        """Checks if both shapes share the same geometry
            and placement. Orientation may differ.
            """
        ...

    def isEqual(self):
        """Checks if both shapes are equal.
            This means geometry, placement and orientation are equal.
            """
        ...

    def isNull(self):
        """Checks if the shape is null."""
        ...

    def isValid(self):
        """Checks if the shape is valid, i.e. neither null, nor empty nor corrupted."""
        ...

    def isCoplanar(self):
        """isCoplanar(shape,tol=None) -- Checks if this shape is coplanar with the given shape."""
        ...

    def findPlane(self):
        """findPlane(tol=None) -- return a plane if the shape is planar"""
        ...

    def fix(self):
        """Tries to fix a broken shape. True is returned if the operation succeeded, False otherwise.
    fix(working precision, minimum precision, maximum precision)
            """
        ...

    def hashCode(self):
        """This value is computed from the value of the underlying shape reference and the location.
    Orientation is not taken into account."""
        ...

    def tessellate(self):
        """Tessellate the shape and return a list of vertices and face indices"""
        ...

    def project(self):
        """Project a list of shapes on this shape"""
        ...

    def makeParallelProjection(self):
        """Parallel projection of an edge or wire on this shape
    makeParallelProjection(shape, dir)
            """
        ...

    def makePerspectiveProjection(self):
        """Perspective projection of an edge or wire on this shape
    makePerspectiveProjection(shape, pnt)
            """
        ...

    def reflectLines(self):
        """Build reflect lines on a shape according to the axes of view.
    Reflect lines are represented by edges in 3d.
    reflectLines(ViewDir, ViewPos, UpDir) -> Shape
            """
        ...

    def makeShapeFromMesh(self):
        """Make a compound shape out of mesh data.
    Note: This should be used for rather small meshes only."""
        ...

    def toNurbs(self):
        """Conversion of the complete geometry of a shape into NURBS geometry.
    For example, all curves supporting edges of the basis shape are converted
    into B-spline curves, and all surfaces supporting its faces are converted
    into B-spline surfaces."""
        ...

    def copy(self):
        """Create a copy of this shape
    copy(copyGeom=True, copyMesh=False) -> Shape
    If copyMesh is True, triangulation contained in original shape will be
    copied along with geometry.
    If copyGeom is False, only topological objects will be copied, while
    geometry and triangulation will be shared with original shape.
    """
        ...

    def cleaned(self):
        """This creates a cleaned copy of the shape with the triangulation removed.
    This can be useful to reduce file size when exporting as a BREP file.
    Warning: Use the cleaned shape with care because certain algorithms may work incorrectly
    if the shape has no internal triangulation any more.
    """
        ...

    def replaceShape(self):
        """Replace a sub-shape with a new shape and return a new shape.
    The parameter is in the form list of tuples with the two shapes."""
        ...

    def removeShape(self):
        """Remove a sub-shape and return a new shape.
    The parameter is a list of shapes."""
        ...

    def defeaturing(self):
        """Remove a feature defined by supplied faces and return a new shape.
    The parameter is a list of faces."""
        ...

    def isInside(self):
        """Checks whether a point is inside or outside the shape.
    isInside(App.Vector, float, Boolean) => Boolean
    The App.Vector is the point you want to check if it's inside or not
    float gives the tolerance
    Boolean indicates if the point lying directly on a face is considered to be inside or not 
            """
        ...

    def removeSplitter(self):
        """Removes redundant edges from the B-REP model"""
        ...

    def proximity(self):
        """proximity(Shape s): Returns two lists of Face indexes for the Faces involved in the intersection."""
        ...

    def distToShape(self):
        """Find the minimum distance to another shape.
    distToShape(Shape s):  Returns a list of minimum distance and solution point pairs.
    
    Returned is a tuple of three: (dist, vectors, infos).
    
    dist is the minimum distance, in mm (float value).
    
    vectors is a list of pairs of App.Vector. Each pair corresponds to solution.
    Example: [(Vector (2.0, -1.0, 2.0), Vector (2.0, 0.0, 2.0)), (Vector (2.0,
    -1.0, 2.0), Vector (2.0, -1.0, 3.0))] First vector is a point on self, second
    vector is a point on s.
    
    infos contains additional info on the solutions. It is a list of tuples:
    (topo1, index1, params1, topo2, index2, params2)
    
        topo1, topo2 are strings identifying type of BREP element: 'Vertex',
        'Edge', or 'Face'.
    
        index1, index2 are indexes of the elements (zero-based).
    
        params1, params2 are parameters of internal space of the elements. For
        vertices, params is None. For edges, params is one float, u. For faces,
        params is a tuple (u,v). """
        ...

    def getElement(self):
        """Returns a SubElement"""
        ...

    def countElement(self):
        """Returns the count of a type of element"""
        ...

    def getTolerance(self):
        """
            getTolerance(mode, ShapeType=Shape) -> float
    
            Determines a tolerance from the ones stored in a shape
            mode = 0 : returns the average value between sub-shapes,
            mode > 0 : returns the maximal found,
            mode < 0 : returns the minimal found.
            ShapeType defines what kinds of sub-shapes to consider:
            Shape (default) : all : Vertex, Edge, Face,
            Vertex : only vertices,
            Edge   : only edges,
            Face   : only faces,
            Shell  : combined Shell + Face, for each face (and containing
                     shell), also checks edge and Vertex
            """
        ...

    def overTolerance(self):
        """
            overTolerance(value, ShapeType=Shape) -> float
    
            Determines which shapes have a tolerance over the given value
            ShapeType is interpreted as in the method getTolerance
            """
        ...

    def inTolerance(self):
        """
            inTolerance(value, ShapeType=Shape) -> float
    
            Determines which shapes have a tolerance within a given interval
            ShapeType is interpreted as in the method getTolerance
            """
        ...

    def globalTolerance(self):
        """
            globalTolerance(mode) -> float
    
            Returns the computed tolerance according to the mode
            mode = 0 : average
            mode > 0 : maximal
            mode < 0 : minimal
            """
        ...

    def fixTolerance(self):
        """
            fixTolerance(value, ShapeType=Shape)
    
            Sets (enforces) tolerances in a shape to the given value
            ShapeType = Vertex : only vertices are set
            ShapeType = Edge   : only edges are set
            ShapeType = Face   : only faces are set
            ShapeType = Wire   : to have edges and their vertices set
            ShapeType = other value : all (vertices,edges,faces) are set
            """
        ...

    def limitTolerance(self):
        """
            limitTolerance(tmin, tmax=0, ShapeType=Shape)
    
            Limits tolerances in a shape as follows :
            tmin = tmax -> as fixTolerance (forces)
            tmin = 0   -> maximum tolerance will be tmax
            tmax = 0 or not given (more generally, tmax < tmin) ->
            tmax ignored, minimum will be tmin
            else, maximum will be max and minimum will be min
            ShapeType = Vertex : only vertices are set
            ShapeType = Edge   : only edges are set
            ShapeType = Face   : only faces are set
            ShapeType = Wire   : to have edges and their vertices set
            ShapeType = other value : all (vertices,edges,faces) are set
            Returns True if at least one tolerance of the sub-shape has
            been modified
            """
        ...

    def optimalBoundingBox(self):
        """
            optimalBoundingBox(useTriangulation = True, useShapeTolerance = False) -> bound box
            """
        ...

    @property
    def ShapeType(self):
        """Returns the type of the shape."""
        ...

    @property
    def Orientation(self):
        """Returns the orientation of the shape."""
        ...

    @property
    def Faces(self):
        """List of faces in this shape."""
        ...

    @property
    def Vertexes(self):
        """List of vertexes in this shape."""
        ...

    @property
    def Shells(self):
        """List of subsequent shapes in this shape."""
        ...

    @property
    def Solids(self):
        """List of subsequent shapes in this shape."""
        ...

    @property
    def CompSolids(self):
        """List of subsequent shapes in this shape."""
        ...

    @property
    def Edges(self):
        """List of Edges in this shape."""
        ...

    @property
    def Wires(self):
        """List of wires in this shape."""
        ...

    @property
    def Compounds(self):
        """List of compounds in this shape."""
        ...

    @property
    def SubShapes(self):
        """List of sub-shapes in this shape."""
        ...

    @property
    def Length(self):
        """Total length of the edges of the shape."""
        ...

    @property
    def Area(self):
        """Total area of the faces of the shape."""
        ...

    @property
    def Volume(self):
        """Total volume of the solids of the shape."""
        ...


