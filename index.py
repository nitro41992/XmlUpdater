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


for DataElements in root.iter(xsi + 'DataElementDef'):
    if DataElements.attrib[xmli + 'type'] == 'DataFolderDef' and DataElements.attrib['Name'] == 'DiagnosesCodeSets':
        for DataElementDef in DataElements.findall(xsi + 'DataElements/'+ xsi + 'DataElementDef/'+ xsi + 'Items/' + xsi + 'ValueListItemDef/' + xsi + 'Value'):
            if (len(DataElementDef.text) < 6 and len(DataElementDef.text) > 3 and "-" not in DataElementDef.text and "." not in DataElementDef.text) or (DataElementDef.text[0].isalpha() and len(DataElementDef.text) > 3 and "-" not in DataElementDef.text and "." not in DataElementDef.text):
                front = DataElementDef.text[:3]
                back = DataElementDef.text[3:]
                new_value = (front + '.' + back)
                DataElementDef.text = new_value


tree.write('output.xml', encoding="utf-8", xml_declaration=True, method="xml")
