
import xml.etree.ElementTree as ET


def xml():
    t = ET.Element('students')

    t0 = ET.SubElement(t, 'student')
    t00 = ET.SubElement(t0, 'name')
    t00.set('id', '00')
    t00.text = 'Abasi'
    t01 = ET.SubElement(t0, 'surname')
    t01.set('id', '01')
    t01.text = 'Ali'
    t02 = ET.SubElement(t0, 'email')
    t02.set('id', '02')
    t02.text = 'albnji@gmail.net'
    t03 = ET.SubElement(t0, 'dni')
    t03.set('id', '03')
    t03.text = '34567845W'
    t1 = ET.SubElement(t, 'student')
    t10 = ET.SubElement(t1, 'name')
    t10.set('id', '10')
    t10.text = 'Joanet'
    t11 = ET.SubElement(t1, 'surname')
    t11.set('id', '11')
    t11.text = 'Ariaka'
    t12 = ET.SubElement(t1, 'email')
    t12.set('id', '12')
    t12.text = 'asdpoui@gmail.com'
    t13 = ET.SubElement(t1, 'dni')
    t13.set('id', '13')
    t13.text = '45328657D'
    t2 = ET.SubElement(t, 'student')
    t20 = ET.SubElement(t2, 'name')
    t20.set('id', '20')
    t20.text = 'Paco'
    t21 = ET.SubElement(t2, 'surname')
    t21.set('id', '21')
    t21.text = 'Jaume'
    t22 = ET.SubElement(t2, 'email')
    t22.set('id', '22')
    t22.text = 'Jordi'
    t23 = ET.SubElement(t2, 'dni')
    t23.set('id', '23')
    t23.text = '98623498S'
    t3 = ET.SubElement(t, 'student')
    t30 = ET.SubElement(t3, 'name')
    t30.set('id', '30')
    t30.text = 'Cintia'
    t31 = ET.SubElement(t3, 'surname')
    t31.set('id', '31')
    t31.text = 'Jovanof'
    t32 = ET.SubElement(t3, 'email')
    t32.set('id', '32')
    t32.text = 'jajajajajaja@gmdi.jer'
    t33 = ET.SubElement(t3, 'dni')
    t33.set('id', '33')
    t33.text = '19283756I'
    t4 = ET.SubElement(t, 'student')
    t40 = ET.SubElement(t4, 'name')
    t40.set('id', '40')
    t40.text = 'Quevedo'
    t41 = ET.SubElement(t4, 'surname')
    t41.set('id', '41')
    t41.text = 'Muscha'
    t42 = ET.SubElement(t4, 'email')
    t42.set('id', '42')
    t42.text = 'megamegafono@fono.mega'
    t43 = ET.SubElement(t4, 'dni')
    t43.set('id', '43')
    t43.text = '24608534X'

    ET.indent(t)
    ET.dump(t)
    tree = ET.ElementTree(t)
    tree.write('xmlA12.xml')


