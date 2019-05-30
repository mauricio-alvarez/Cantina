import json
import sys
import os

sys_arg = sys.argv[1]

def retrieve_values(obj, key):
    array = []
    search_val = key
    def retrieve(obj, key):
        if isinstance(obj, dict):
            for key, val in obj.items():
                if isinstance(val, (dict, list)):
                    retrieve(val, key)
                elif val == search_val:
                    print(json.dumps(obj, indent=4) + '\n')
                    array.append(val)
        elif isinstance(obj, list):
            for item in obj:
                retrieve(item, key)
            #print(obj, '\n')
        return array
    results = retrieve(obj, key)

    if len(array) == 0: 
        print("Dead End! Maybe an invalid selector.")
    return results

def retrieve_file(obj):
    json_file_path = obj 
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data

def search():
    selector = input("Input CSS3 selector: ")
    
    if not selector[0].isalpha():
        updated_sel = selector[:0] + '' + selector[1:]
    else:
        updated_sel = selector

    complete_path = os.path.abspath(sys_arg)
    json_file = retrieve_file(complete_path)
    retrieve_values(json_file, updated_sel)

def main():
    if len(sys.argv) == 2:
        try: 
            input_file = open(sys_arg, 'r')
            file_content = input_file.read()
            print("Fetching file...")
            print(file_content)
            print("Ready!")
            search()
        except Exception as e: 
            print("ERROR:", e)        
main()     