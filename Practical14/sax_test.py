import xml.sax
import datetime

start = datetime.datetime.now()

class GOHandler(xml.sax.ContentHandler):

    def __init__(self):

        super().__init__()

        self.current = ""

        self.name = ""
        self.namespace = ""
        self.is_a_count = 0

        self.results = {
            "molecular_function": ("", 0),
            "biological_process": ("", 0),
            "cellular_component": ("", 0)
        }

    def startElement(self, tag, attributes):

        self.current = tag

        if tag == "term":

            self.name = ""
            self.namespace = ""
            self.is_a_count = 0

        elif tag == "is_a":

            self.is_a_count += 1

    def characters(self, content):

        if self.current == "name":

            self.name += content

        elif self.current == "namespace":

            self.namespace += content

    def endElement(self, tag):

        if tag == "term":

            if self.namespace in self.results:

                if self.is_a_count > self.results[self.namespace][1]:

                    self.results[self.namespace] = (
                        self.name,
                        self.is_a_count
                    )

        self.current = ""


parser = xml.sax.make_parser()

handler = GOHandler()

parser.setContentHandler(handler)

parser.parse("go_obo.xml")

end = datetime.datetime.now()

for namespace in handler.results:

    print(namespace)

    print("Term:", handler.results[namespace][0])

    print("Number of is_a:", handler.results[namespace][1])

    print()

print("SAX running time:", end - start)