# FreeCAD python stubs

This meant to contain all the FreeCAD C++ to Python bindings, types for the Document Object property system and Scripted Object Python types.

FreeCAD's Python API is partially implemented in C++ code and contains no native type information, making it impossible for IDEs and static analysis tools to provide intelligent code completion, type checking, or refactoring support. This forces developers to write Python code without the safety nets and productivity tools that modern Python development expects.

Developers should manually create .pyi type stub files in the stubs/ directory to provide type signatures for FreeCAD's C++ Python bindings. These stubs define class structures like DocumentObject, inheritance hierarchies like TopoShape inheriting from ComplexGeoData, and method signatures with proper type hints including overloads. The stub files serve as the authoritative source of type information that bridges the gap between FreeCAD's C++ implementation and Python's type system, enabling IDE support and static analysis for FreeCAD scripting.

## Structure

* `stubs/` - `*.pyi` files for FreeCAD C++ defined Python modules and packages
* `docker/` - scripts to develop sphinx documentation locally

## Generate sphinx documentation

    # rename workaround, see https://github.com/readthedocs/sphinx-autoapi/issues/243
    ./rename.sh
    # generate html
    ./docker/run.sh make clean html


## Pipeline vision

Here's how python stub files are intended to be generated and used:

![](generation.jpg)

We're not there yet though.


## See also

* [DocumentObject model proposal](https://github.com/FreeCAD/FreeCAD-Enhancement-Proposals/wiki/FEP03-DocumentObject-model) ([discussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=49619))
