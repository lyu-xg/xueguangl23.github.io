import os
import json
from items import items
dataPath = 'js/dummydata.js'

def readFile(path):
    with open(path, 'r') as inFile:
        content = inFile.read()
    return content

def buildCSS():
    os.system("sass src/style.scss css/style.css")

def getTemplate():
    return readFile('item.html').replace('\n','').replace('  ','').replace('"','\"')

def applyTemplate(T, entry):
    return T.format(*entry).replace('"','\"')

def combineItems(T,items):
    return ''.join(map(lambda x:applyTemplate(T,x),items))

def generateJSON():
    for category in items:
        items[category] = combineItems(T,items[category])
    return json.dumps(items)

def generateJS(jspath):
    with open(jspath,'w') as outfile:
        outfile.write('var dummyData = '+generateJSON())
    return 1

if __name__ == '__main__':
    T = getTemplate()
    buildCSS()
    generateJS(dataPath)
