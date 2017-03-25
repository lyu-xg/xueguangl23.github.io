import os

def buildCSS():
    os.system("sass src/style.scss css/style.css")

if __name__ == '__main__':
    buildCSS()
