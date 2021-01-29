import json
import random

if __name__ == '__main__':
    with open('animals.json', 'r') as infile:
        barn = json.load(infile)

    random_animal = random.choice( barn['animals'] )
    
    print( json.dumps(random_animal, indent=4) )
