#!/usr/bin/env python3
import json
import random
import sys

def error_exit(error_text):
    print("[ERROR] read_animals.py: " + error_text)
    sys.exit(1)

def get_num_animals(arg, max_animals):
    num_animals = int(arg)
    
    assert num_animals >= 1
    assert num_animals <= max_animals

    return num_animals

if __name__ == '__main__':

    with open('animals.json', 'r') as infile:
        barn = json.load(infile)

    try:
        num_animals = get_num_animals(sys.argv[1], len(barn['animals']))
    except IndexError:
        error_exit("read_animals.py requires a positional paramater \'num_animals\'.")
    except AssertionError:
        error_exit("\'num_animals\' must be within the range 1 and " + str(len(barn['animals'])) + ", inclusive.")
    except ValueError:
        error_exit("\'num_animals\' must be an integer")

    selected_animals = []
    for n in range(num_animals):
        selected_animals.append( random.choice(barn['animals']) )

    print( json.dumps(selected_animals, indent=4) )
