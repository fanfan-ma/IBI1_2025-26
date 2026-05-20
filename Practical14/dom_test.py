import datetime
start = datetime.datetime.now()
from xml.dom import minidom
doc = minidom.parse("go_obo.xml")
terms = doc.getElementsByTagName("term")
results = {
    "molecular_function": ("", 0),
    "biological_process": ("", 0),
    "cellular_component": ("", 0)
}
for term in terms:
    name = term.getElementsByTagName("name")[0].firstChild.data
    namespace = term.getElementsByTagName("namespace")[0].firstChild.data
    is_a_list = term.getElementsByTagName("is_a")
    is_a_count = len(is_a_list)
    if is_a_count > results[namespace][1]:
        results[namespace] = (name, is_a_count)
end = datetime.datetime.now()
for namespace in results:
    print(namespace)
    print("Term:", results[namespace][0])
    print("Number of is_a:", results[namespace][1])
    print()
print("DOM running time:", end - start)