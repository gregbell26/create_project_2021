import os.path
import json


def loadJson(_jsonPath):
    if not os.path.isfile(_jsonPath):
        print(f"ERROR: File path {_jsonPath} does not exist")
        return json.dumps("{'status': 'ERROR'}")

    return json.loads(open(_jsonPath, 'r').read())
