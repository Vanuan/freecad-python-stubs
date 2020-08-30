# Corresponding implementation files:
# * src/App/Application.cpp
# * src/Base/UnitsApiPy.cpp
from typing import overload, Tuple

# * src/Base/QuantityPy.cpp
# * src/Base/QuantityPyImp.cpp
class Quantity:
    Value: float
    UserString: str
    @overload
    def __init__(self, value: str) -> None: ...
    @overload
    def __init__(self, quanity: Quantity) -> None: ...
    @overload
    def __init__(self, amount: float, unit: Unit) -> None: ...
    @overload
    def __init__(self, amount: float, unit: Tuple[int,int,int,int,int,int,int,int]) -> None: ...

    def __gt__(self, other: Quantity) -> bool: ...
    def getUserPreferred(self): ...

class Unit:
    """
    Unit()                        -- empty constructor
    Unit(i1,i2,i3,i4,i5,i6,i7,i8) -- unit signature
    Unit(Quantity)                -- copy unit from Quantity
    Unit(Unit)                    -- copy constructor
    Unit(string)                  -- parse the string for units
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
            self,
            i1: int, i2: int = ..., i3: int = ..., i4: int = ...,
            i5: int = ..., i6: int = ..., i7: int = ..., i8: int = ...
        ) -> None: ...
    @overload
    def __init__(self, quanity: Quantity) -> None: ...
    @overload
    def __init__(self, unit: Unit) -> None: ...
    @overload
    def __init__(self, units: str) -> None: ...

# * src/App/InitScript.h
Length  = Unit(1)
Area    = Unit(2)
Volume  = Unit(3)
Mass    = Unit(0,1)