import json
import os
import argparse
from exceptions import ParseException
from generator import *
from parser import parseFile

DEFAULT_CONFIG = {
    "recursive": True,
    "input": [ "src/" ],
    "extensions": [ ".S", ".asm" ],
    "output": "html/"
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create HTML-Documentation from assembly source files")
    parser.add_argument("-c", "--config", help="path of the config file", default="asmdoc.cfg")
    parser.add_argument("-g", "--generate", help="generates default config file", action="store_true")

    args = parser.parse_args()

    if args.generate:
        json.dump( DEFAULT_CONFIG, open(args.config, "w") )
        print("Default configuration generated!")
        exit()

    if not os.path.exists(args.config):
        print("Configuration files does not exist. You can generate it with -g option")
        exit()

    cfg = json.load( open(args.config, "r") )

    # all scanned files
    scanned = []
    modules = {}

    cwd = os.getcwd()
    if cfg['recursive']:
        for path in cfg['input']:
            
            # Absolute path
            path = os.path.join(cwd, path) 

            for root, dirs, files in os.walk(path):
                for f in files:
                    filePath = os.path.join( root, f )
                    name, ext = os.path.splitext( filePath )
                    name = name.split("/")[-1]

                    # Wrong file extension
                    if not ext in cfg['extensions']:
                        continue
                    
                    # File already scanned
                    if filePath in scanned:
                        continue

                    scanned.append( filePath )
                    module, functions = parseFile( open(filePath, "r") )
                    if module == None:
                        module = name

                    if not module in modules:
                        modules[module] = []
                    modules[module] += functions
                

    else:
        pass # TODO


    for module, functions in modules.items():
        if len(functions) > 0:
            generateModule(cfg['output'], module, functions)