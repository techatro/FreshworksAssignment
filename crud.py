import os
import sys
import json

filename = "data.json"
directory = os.path.dirname(os.path.realpath(__file__))

class CRUD():

    global filename
    global directory

    def __init__(self):

        if os.path.isfile(filename): 
            pass # file exists

        else : 
            if sys.platform == 'win32':
                operator = '\\'
            else:
                operator = '/'

            filelocation = directory + operator + filename

            with open(filelocation, 'w') as fp: # create a new file as data.json
                temp = "{}"
                fp.write(temp)
                fp.close()
                pass

    def create(self, dictkey,dictvalue):
        with open(filename, 'r+') as f:
            try:
                data = json.loads(f.read())
                if dictkey in data.keys(): # Checking if a key already exists
                    f.close()
                    return "Key already exists\n"

                else: # Writing values into the json
                    temp = {dictkey:dictvalue}
                    data.update(temp)
                    f.close()
                    with open(filename, 'w') as w:
                        w.write(json.dumps(data, indent=4))
                        w.close()
                    return "Key created\n"
            except: # Empty file
                temp = {dictkey:dictvalue}
                f.write(json.dumps(temp, indent=4))
                f.close()
                return "Key created\n"

            

    def read(self, dictkey=None):
        if os.path.isfile(filename):

            with open(filename, 'r') as f:
                data = json.loads(f.read())
                f.close()
                if dictkey is not None:
                    return json.dumps(data[dictkey], indent=4)
                else:
                    return json.dumps(data, indent=4)

        else:
            return "File doesnt exist in the current directory. Try creating first\n"

    def update(self, dictkey, dictvalue):

        if os.path.isfile(filename):

            with open(filename, 'r+') as f:
                data = json.loads(f.read())
                data[dictkey] = dictvalue
                f.close()
                with open(filename, 'w') as w:
                        w.write(json.dumps(data, indent=4))
                        w.close()
                return ("\n\nJSON Updated\n\n"+self.read())

        else:
            return "File doesnt exist in the current directory. Try creating first\n"

    def delete(self, dictkey):
        
        if os.path.isfile(filename):

            with open(filename, 'r+') as f:
                data = json.loads(f.read())

                if dictkey in data.keys(): # Checking if a key exists in JSON
                    data.pop(dictkey, None) # Delete the key
                    f.close()
                    with open(filename, 'w') as w:
                        w.write(json.dumps(data, indent=4)) # Writing the update json
                        w.close()
                    return "Key deleted\n"

                else:
                    f.close()
                    return "Key doesnt exist\n"

        else:
            return "File doesnt exist in the current directory. Try creating first\n"
