#!/usr/bin/env python3

import json
import random
import petname
from datetime import date

head_options = [ 'snake', 'bull', 'lion', 'raven', 'bunny' ]

def generate_animal():
    head = random.choice(head_options)
    body = generate_body()
    arms = random.randint(2,10)
    legs = 3*random.randint(1,4)
    tails = arms + legs
    created_on = str(date.today())
    
    new_animal = {
        'head': head,
        'body': body,
        'arms': arms,
        'legs': legs,
        'tails': tails,
        'created_on': created_on
    }
    return new_animal

def generate_body():
    animal1 = petname.name()
    animal2 = petname.name()

    while ( animal1 == animal2 ):
        animal2 = petname.name()

    return animal1 + '-' + animal2
