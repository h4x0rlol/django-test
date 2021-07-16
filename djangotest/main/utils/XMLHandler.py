import xml.etree.ElementTree as ET


class XMLHandler:

    def build(self, data):
        root = ET.Element('rpcMessage')
        for k, v in data.items():
            field = ET.Element(str(k))
            field.text = str(v)
            root.append(field)
        xml = ET.tostring(root, encoding="utf-8", method="xml")
        return xml

    def parse(self, data):
        parsed = {}
        root = ET.fromstring(data)
        for child in root:
            parsed[child.tag] = child.text
        return parsed
