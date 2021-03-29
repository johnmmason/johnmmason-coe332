from flask import Flask, request, abort
import json
import db

app = Flask(__name__)

@app.route('/init', methods = ['GET'])
def init():
    num_animals = request.args.get('num_animals')

    if num_animals is None:
        num_animals = 100

    try:
        num_animals = int(num_animals)
    except:
        abort(400, "\'num_animals\' must be of type int.")
    
    db.add_animals(num_animals)

    return "Success!"

@app.route('/clear', methods = ['GET'])
def clear():
    try:
        db.clear_animals()
    except:
        abort(500)

    return "Success!"

@app.route('/get_animals_by_dates')
def query_dates():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    try:
        assert start_date is not None
        assert end_date is not None
    except AssertionError:
        abort(400, "\'start_date\' and \'end_date\' must be provided!")

    try:                
        return json.dumps( db.query_dates(start_date, end_date), indent=4 )
    except AssertionError:
        abort(400, "\'start_date\' must be before \'end_date\'!")
    except:
        abort(500)

@app.route('/get_animal_by_uuid')
def get_animal_by_uuid():
    unique = request.args.get('uuid')

    try:
        assert unique is not None
    except AssertionError:
        abort(400, "\'uuid\' must be provided!")
        
    try:
        return db.get_animal_by_uuid(unique)
    except:
        abort(404)

@app.route('/edit_animal_by_uuid', methods=['POST'])
def edit_animal_by_uuid():
    unique = request.args.get('uuid')
    
    try:
        assert unique is not None
        new_traits = request.get_json()
    except AssertionError:
        abort(400, "\'unique\' must be provided!")
    except:
        abort(400)

    db.edit_animal_by_uuid(unique, new_traits)

    return "Success!\n"


@app.route('/delete_animals_by_dates', methods=['GET'])
def delete_by_dates():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    try:
        assert start_date is not None
        assert end_date is not None
    except AssertionError:
        abort(400, "\'start_date\' and \'end_date\' must be provided!")

    try:
        db.delete_by_date_range(start_date, end_date)
        return "Success!\n"
    except AssertionError:
        abort(400, "\'start_date\' must be before \'end_date\'!")
    except:
        abort(500)

@app.route('/get_average_legs', methods=['GET'])
def get_average_legs():
    try:
        return str( db.get_average_num_legs() )
    except:
        abort(500)

@app.route('/count_animals', methods=['GET'])
def count_animals():
    try:
        return str( db.count_animals() )
    except:
        abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
