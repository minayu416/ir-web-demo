import requests
import xml.etree.cElementTree as ET
import StringIO

pusername = "87037"
ppasswd = "0695"
url = "http://120.96.204.3/octopus/modauth/LdapADOSet_V2.pl?type=Auth&pusrname=" + pusername + "&ppasswd=" + ppasswd

response = requests.get(url)
#print response.content
#print response.content.find('rawmessage="Success"')
#root = ET.fromstring(response.content)
#print root.text

#print response.content.decode('big5')
#utf8_parser = ET.XMLParser(encoding='utf-8')
#tree = ET.parse(StringIO(response.content.decode('big5','ignore'), parser = utf8_parser))
#root=tree.getroot()

#r = response.content.decode('big5').encode('ascii','ignore')
r = response.content.decode('big5').encode('utf-8')
#print r
r = r.replace('big5', 'utf-8')
root = ET.fromstring(r)
for child in root.getiterator('{#RowsetSchema}row'):
    x = child.attrib
print type(x['rcode'])
