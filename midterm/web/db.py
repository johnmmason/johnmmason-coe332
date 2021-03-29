import redis
import json
import uuid
import datetime
from dateutil import parser
import generate_animals

REDIS_HOST='redis'
REDIS_PORT=6379

###################################
### GENERAL FUNCTIONS
###################################

# function add_animals:
# generates the specified number of animals and adds them to the database
def add_animals(num):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    
    for n in range(num):
        unique = str(uuid.uuid4())
        animal = generate_animals.generate_animal()

        rd.set(unique, json.dumps(animal))

# function clear_animals:
# clears all entires from the database
def clear_animals():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    redis_keys = [key.decode('utf-8') for key in rd.keys()]

    for key in redis_keys:
        rd.delete(key)

# function get_animals:
# returns a dict containing all animals in the format { 'uuid': {traits} , ... }
def get_animals():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    redis_keys = [key.decode('utf-8') for key in rd.keys()]

    animals = {}
    for key in redis_keys:
        animals[key] = json.loads(rd.get(key).decode('utf-8'))

    return animals

###################################
### ROUTE OPERATION FUNCTIONS
###################################

# function query_dates:
# returns a dict containing the animals created between the given start and end dates in the format { 'uuid': {traits}, ... }
def query_dates(start, end):
    animals = get_animals()

    start_date = parser.parse(start)
    end_date = parser.parse(end)

    assert start_date <= end_date
    
    selected_animals = {}
    for key in animals.keys():
        this_date = parser.parse( animals[key]['created_on'] )
        if start_date <= this_date <= end_date:
            selected_animals[key] = animals[key]
        else:
            pass

    return selected_animals
    
# function get_animal_by_uuid:
# returns a dict containing the animal with the specified uuid in the format { 'uuid': {traits} }
def get_animal_by_uuid(unique):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    traits = json.loads( rd.get(unique).decode('utf-8') )
    return { unique: traits }

# function edit_animal_by_uuid
# updates or adds a trait to an existing animal specified by its UUID
def edit_animal_by_uuid(unique, new_traits):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    traits = json.loads( rd.get(unique).decode('utf-8') )

    for key in new_traits.keys():
        traits[key] = new_traits[key]
    
    rd.delete(unique)
    rd.set(unique, json.dumps(traits))

# function delete_by_date_range
# removes animals from the database which were created between given dates
def delete_by_date_range(start, end):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    
    animals = get_animals()

    start_date = parser.parse(start)
    end_date = parser.parse(end)

    assert start_date <= end_date

    selected_animals = []
    for key in animals.keys():
        this_date = parser.parse(animals[key]['created_on'])
        if start_date <= this_date <= end_date:
            rd.delete(key)
        else:
            pass

# function get_average_num_legs:
# returns the decimal average of legs for all animals in the database
def get_average_num_legs():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    redis_keys = [key.decode('utf-8') for key in rd.keys()]
    
    animals = get_animals()

    total_legs = 0
    for key in redis_keys:
        total_legs = total_legs + animals[key]['legs']

    average_legs = total_legs/count_animals()
    return average_legs

        
# function count_animals:
# returns the integer number of animals in the database
def count_animals():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    return len( [key.decode('utf-8') for key in rd.keys()] )

