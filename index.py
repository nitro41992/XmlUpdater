import lxml.etree as ET

tree = ET.parse('KPIMeasuresProcessingIn.xml')
root = tree.getroot()

# ET.register_namespace('', "http://www.inrule.com/XmlSchema/Schema")
# ET.register_namespace('xsd', "http://www.w3.org/2001/XMLSchema")
# ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")


xsi = '{http://www.inrule.com/XmlSchema/Schema}'
xmli = '{http://www.w3.org/2001/XMLSchema-instance}'
codeArray = []
updatedCodes=[]

for Element in root.iter(xsi + 'DataElements'):
    for DataFolder in Element.iter(xsi + 'DataElementDef'):
        if DataFolder.attrib[xmli + 'type'] == 'DataFolderDef' and DataFolder.attrib['Name'] == 'DiagnosesCodeSets':
            for each in DataFolder:
                for DataElements in each:
                     if DataElements.attrib[xmli + 'type'] == 'InlineValueListDef':
                        for DataElement in DataElements.iter(xsi + 'Items'):
                            for item in DataElement: 
                                for value in item:
                                    if value.tag == xsi + 'Value':  
                                         if (len(value.text) < 6 and len(value.text) > 3 and "-" not in value.text and "." not in value.text) or (value.text[0].isalpha() and "." not in value.text):
                                            
                                            front = value.text[:3]
                                            back = value.text[3:]
                                            new_value = (front + '.' + back)
                                            value.text = new_value



tree.write('output.xml', encoding="utf-8", xml_declaration=True, method="xml")
#tree.write_c14n('output.xml')

       