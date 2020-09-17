# Generates *.pyi from FreeCAD DocumentObject XML metadata format

import sys
import xml.etree.ElementTree as ET

def indent(block):
    indented_lines = []
    for line in block.splitlines():
        indented_lines.append(' ' * 4 + line)
    return '\n'.join(indented_lines)

def gen_name(name, module=None):
    _name = name.rstrip('Py')
    _name = _name.lstrip('Topo')
    if module:
        _name = module + '.' + _name
    return _name

def gen_parent_name(child):
    name = child.attrib['Father']
    return gen_name(name, child.attrib['FatherNamespace'])

def gen_class_name(child):
    name = child.attrib['Name']
    return gen_name(name)

def gen_doc(doc_str):
    return '"""' + doc_str + '"""\n'

def gen_class(child):
    class_str = 'class '
    name = gen_class_name(child)
    class_str += name
    parent = gen_parent_name(child)
    if parent:
        class_str += '(' + parent + ')'
    class_str += ':\n    '
    doc_str = child.find('./Documentation/UserDocu').text
    class_str += gen_doc(doc_str)
    methods = child.findall('Methode')
    for method_node in methods:
        method_str = gen_method(method_node)
        class_str += indent(method_str) + '\n\n'
    attributes = child.findall('Attribute')
    for attribute_node in attributes:
        attr_str = gen_attr(attribute_node)
        class_str += indent(attr_str) + '\n\n'
    return class_str

def gen_attr(node):
    doc_str = node.find('./Documentation/UserDocu').text
    return '@property\ndef ' + node.attrib['Name'] + '(self):\n    ' + gen_doc(doc_str) + '    ...'

def gen_method(node):
    doc_str = node.find('./Documentation/UserDocu').text
    return 'def ' + node.attrib['Name'] + '(self):\n    ' + gen_doc(doc_str) + '    ...'

if __name__ == '__main__':
    filename = sys.argv[1]
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        if child.tag == 'PythonExport':
          class_definition = gen_class(child)
          print(class_definition)
