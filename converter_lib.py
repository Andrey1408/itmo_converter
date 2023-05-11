import xmlplain
with open("среда.yaml") as inf:
    root = xmlplain.obj_from_yaml(inf)

with open("среда.xml", 'w') as outf:
    xmlplain.xml_from_obj(root, outf, pretty=True)

