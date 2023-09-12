import base64

def encodeMp3(filePath):
    with open(filePath, 'rb') as file:
        return base64.b64encode(file.read())
