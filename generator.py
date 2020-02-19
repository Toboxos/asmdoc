from container import Function
import os

tplParam = open( os.path.join(os.path.dirname(__file__), "templates/fn-param.html"), "r").read()
tplFunc = open( os.path.join(os.path.dirname(__file__), "templates/function.html"), "r").read()
tplModule = open( os.path.join(os.path.dirname(__file__), "templates/module.html"), "r").read()

def generateFunction(function):

    numParams = len(function.params)

    params = ""
    definition = function.name + "("
    for i, (pName, pDesc) in enumerate(function.params):
        access = "sp+" + str((numParams - i - 1) * 4)   # Params put on stack in the order they are set
        if i < 4:                                       # First 4 params put in register
            access = "r" + str(i)

        params += tplParam.replace("{name}", pName).replace("{description}", pDesc).replace("{access}", access)
        definition += pName + ", "

    if len(params) > 0:
        definition = definition[:-2] + ")"
    else:
        definition += ")"
    return tplFunc.replace("{name}", function.name).replace("{description}", function.description).replace("{returns}", function.returns).replace("{params}", params).replace("{definition}", definition)

def generateFunctions(functions):
    html = ""
    for function in functions:
        html += generateFunction(function)
    return html

def generateModule(path, name, functions):
    html = generateFunctions( functions )

    f = open(os.path.join(path, name + ".html"), "w")
    f.write( tplModule.replace("{name}", name).replace("{html}", html) )
    f.close()