import xml.etree.ElementTree as ET

data='''
<person>
    <name>Mathew</name>
    <phone type="int l">
    +91 7994941468
    </phone>
    <email hide="yes"/>
    </person>'''
tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
