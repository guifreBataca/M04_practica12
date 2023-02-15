import json
#leer el json
def func1():
    with open("books.json", 'r') as file:
        resultado = json.load(file)
        print(json.dumps(resultado,indent=2))


            
