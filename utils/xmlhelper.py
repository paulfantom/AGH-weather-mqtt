#!/usr/bin/env python3

from lxml import etree
# arrow is an awesome lib for dealing with dates in python

# converts an etree to dict, useful to convert xml to dict
def etree2dict(tree):
    root, contents = recursive_dict(tree)
    return {root: contents}


def recursive_dict(element):
    if element.attrib and 'type' in element.attrib and element.attrib['type'] == "array":
        return element.tag, [(dict(map(recursive_dict, child)) or getElementValue(child)) for child in element]
    else:
        return element.tag, dict(map(recursive_dict, element)) or getElementValue(element)


def getElementValue(element):
    if element.text:
        if element.attrib and 'type' in element.attrib:
            attr_type = element.attrib.get('type')
            if attr_type == 'integer':
                return int(element.text.strip())
            if attr_type == 'float':
                return float(element.text.strip())
            if attr_type == 'boolean':
                return element.text.lower().strip() == 'true'
            if attr_type == 'datetime':
                return arrow.get(element.text.strip()).timestamp
        else:
            return element.text
    elif element.attrib:
        if 'nil' in element.attrib:
            return None
        else:
            return element.attrib
    else:
        return None
