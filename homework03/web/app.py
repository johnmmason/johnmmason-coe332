#!/bin/python3

import json
import random
import generate_animals
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/generate', methods = ['GET'])
def gen_animals():
    # parse URL arguments, or if none specify 1 animal
    num_animals = request.args.get('num_animals')

    if num_animals is None:
        num_animals = 1

    try:
        num_animals = int(num_animals)
    except ValueError:
        abort(400, "\'num_animals\' must be of type int.")
    except:
        abort(400)

    # generate specified number of animals
    barn = { "animals": [] }
    for i in range(num_animals):
        barn['animals'].append( generate_animals.generate_animal() )

    # write to a file
    with open('animals.json', 'w') as outfile:
        json.dump(barn, outfile, indent=4)

    # return specified num of animals
    return json.dumps(barn, indent=4)

@app.route('/get', methods = ['GET'])
def get_animals():
    # read from file
    try:
        with open('animals.json') as infile:
            barn = json.load(infile)
        assert len(barn['animals']) > 0
    except AssertionError:
        abort(404, "Animals database is empty.")
    except FileNotFoundError:
        abort(404, "Animals database does not exist.")

    # parse URL arguments
    num_animals = request.args.get('num_animals')

    if num_animals is None:
        num_animals = len(barn['animals'])

    try:
        num_animals = int(num_animals)
        assert num_animals <= len(barn['animals'])
        assert num_animals > 0
    except AssertionError:
        abort(400, "\'num_animals\' must be within the range 1 and " + str(len(barn['animals'])) + ", inclusive.")
    except ValueError:
        abort(400, "\'num_animals\' must be of type int.")
    except:
        abort(400)

    # get requested number of animals frim the list
    selected_animals = []
    for n in range(num_animals):
        this_choice = random.choice(barn['animals'])
        selected_animals.append( this_choice )
        barn['animals'].remove(this_choice)

    return json.dumps(selected_animals, indent=4)

@app.route('/pop', methods = ['GET'])
def pop_animals():
    # open file and read animals
    try:
        with open('animals.json') as infile:
            barn = json.load(infile)
        assert len(barn['animals']) > 0
    except AssertionError:
        abort(404, "Animals database is empty.")
    except FileNotFoundError:
        abort(404, "Animals database does not exist.")

    # parse URL arguments, or if none specify 1 animal
    num_animals = request.args.get('num_animals')

    if num_animals is None:
        num_animals = 1

    try:
        num_animals = int(num_animals)
        assert num_animals <= len(barn['animals'])
        assert num_animals > 0
    except AssertionError:
        abort(400, "\'num_animals\' must be within the range 1 and " + str(len(barn['animals'])) + ", inclusive.")
    except ValueError:
        abort(400, "\'num_animals\' must be of type int.")
    except:
        abort(400)

    # pop and print animals from the list
    selected_animals = []
    for n in range(num_animals):
        this_choice = random.choice(barn['animals'])
        selected_animals.append(this_choice)
        barn['animals'].remove(this_choice)

    # save remaining animals to file
    with open('animals.json', 'w') as outfile:
        json.dump(barn, outfile, indent=4)

    # return list of animals removed from db
    return json.dumps(selected_animals, indent=4)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5013)
