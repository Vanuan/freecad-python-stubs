# FreeCAD python stubs

This meant to contain all the FreeCAD C++ to Python bindings, types for the Document Object property system and Scripted Object Python types.

## Generate sphinx documentation

    # rename workaround, see https://github.com/readthedocs/sphinx-autoapi/issues/243
    ./rename.sh
    # generate html
    ./docker/run.sh make clean html

## See also

* [DocumentObject model proposal](https://github.com/FreeCAD/FreeCAD-Enhancement-Proposals/wiki/FEP03-DocumentObject-model) ([discussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=49619))
