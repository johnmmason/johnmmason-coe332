#!/usr/bin/env python3
import json
import random
import sys

def get_num_animals(arg, max_animals):
    num_animals = int(arg)
    
    assert num_animals >= 1
    assert num_animals <= max_animals

    return num_animals

if __name__ == '__main__':

    with open('animals.json', 'r') as infile:
        barn = json.load(infile)

    num_animals = get_num_animals(sys.argv[1], len(barn['animals']))

    selected_animals = []
    for n in range(num_animals):
        selected_animals.append( random.choice(barn['animals']) )

    print( json.dumps(selected_animals, indent=4) )
