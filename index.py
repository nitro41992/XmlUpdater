import lxml.etree as ET

def xmlParse(path):
    tree = ET.parse(path)
    return tree

def xmlgetRoot(tree):
    root = tree.getroot()
    return root


def codeUpdate(text):
    if (len(text) < 6 and len(text) > 3 and "-" not in text and "." not in text) or (text[0].isalpha() and len(text) > 3 and "-" not in text and "." not in text):
        front = text[:3]
        back = text[3:]
        new_value = (front + '.' + back)
        updated = new_value
        return updated
    else:
        return text
        

def xmlLoop(root):
    xsi = '{http://www.inrule.com/XmlSchema/Schema}'
    xmli = '{http://www.w3.org/2001/XMLSchema-instance}'

    for DataElements in root.iter(xsi + 'DataElementDef'):
        if DataElements.attrib[xmli + 'type'] == 'DataFolderDef' and DataElements.attrib['Name'] == 'DiagnosesCodeSets':
            for DataElementDef in DataElements.findall(xsi + 'DataElements/' + xsi + 'DataElementDef/' + xsi + 'Items/' + xsi + 'ValueListItemDef/' + xsi + 'Value'):
                DataElementDef.text = codeUpdate(DataElementDef.text)
    
    return root

def main(path):
    tree = xmlParse(path)
    root = xmlgetRoot(tree)
    Updated = xmlLoop(root)
    with open('xmltree.xml','wb') as f:
        f.write(ET.tostring(Updated,pretty_print=True, encoding = "utf-8", method="xml", xml_declaration=True))


main('KPIMeasuresProcessingIn.xml')
