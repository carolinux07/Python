from xml.etree import ElementTree as et

file = 'C:\\Projetos\\template.xml'

xml_file = et.parse(file)

for elemento in xml_file.findall(".//media"):
    if elemento.attrib['title'] == "TITULO":
        elemento.attrib['title'] = "Velocidade Máxima"
        print(elemento.attrib)

    if elemento.attrib['mediaName'] == "NOMEARQUIVO":
        elemento.attrib['mediaName'] = "VelMax"
        print(elemento.attrib)

    if elemento.attrib['houseId'] == "NOMEARQUIVO":
        elemento.attrib['houseId'] = "VelMax"
        print(elemento.attrib)

for elemento in xml_pebble.findall(".//media/properties/markups/markup/markupItem"):
    if elemento.attrib['name'] == "TxSegment":
        if elemento.attrib['duration'] == "TEMPOVIDEO":
            elemento.attrib['duration'] = "01:30:56:09"
            print(elemento.attrib)

    if elemento.attrib['comment'] == "COMENTARIO":
        elemento.attrib['comment'] = "Filme de aventura"
        print(elemento.attrib)

for elemento in xml_pebble.findall(".//media/mediaInstances/mediaInstance"):
    if elemento.attrib['duration'] == "DURACAOTOTAL":
        elemento.attrib['duration'] = "01:45:34:11"
        print(elemento.attrib)

    if elemento.attrib['directory'] == "DIRETORIO":
        elemento.attrib['directory'] = "dir"
        print(elemento.attrib)

    if elemento.attrib['filename'] == "NOMEARQUIVOCOMEXT":
        elemento.attrib['filename'] = "video.mp4"
        print(elemento.attrib)

xml_pebble.write(file)
