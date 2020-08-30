# App/Application.cpp

# Base::BaseExceptionFreeCADError
class FreeCADError(Exception):
    ...


class FreeCADAbort(Exception):
    ...


# Base::VectorPy
class Vector: ...
# Base::MatrixPy
class Matrix: ...
# Base::BoundBoxPy
class BoundBox: ...
# Base::PlacementPy
class Placement: ...
# Base::RotationPy
class Rotation: ...
# Base::AxisPy
class Axis: ...
# Base::CoordinateSystemPy
class CoordinateSystem: ...
# Base::TypePy
class TypeId: ...