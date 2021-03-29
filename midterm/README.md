# midterm

This assignment extends the web API from homework 3 with additional routes and the Redis database.

## Running the Container

Get started by cloning this repository and navigating to the `midterm` folder:

```bash
git clone https://github.com/johnmmason/johnmmason-coe332.git
cd johnmmason-coe332/midterm
```

Launch the container using `docker-compose`:

```bash
docker-compose up -d
```
**The first time you launch the container, the database will be empty.  To populate the database, run:**

```bash
curl "localhost:5018/init?num_animals=5"
```

When you're done, stop the container and clean up:

```bash
docker-compose down
```

## The Web API

### /init
Generate a set of random animals to populate the database.  This route takes a query parameter `num_animals` which defaults to `num_animals = 100` if not provided.

```bash
curl "localhost:5018/init" # OR
curl "localhost:5018/init?num_animals=5"
```

### /clear
Remove all animals from the database.

```bash
curl "localhost:5018/clear"
```

### /get_animals_by_dates
Get all animals created between query parameters `start_date` and `end_date`.  Dates in format `2021-03-30` have been tested, although other formats should also be recognized.

```bash
curl "localhost:5018/get_animals_by_dates?start_date='2021-03-28'&end_date='2021-07-04'"
```

### /get_animal_by_uuid
Get the animal with the UUID matching query parameter `uuid`.  Since UUIDs are generated randomly, you will need to replace the example UUID with one from your database.

```bash
curl "localhost:5018/get_animal_by_uuid?uuid=6e60b258-f8fb-43db-a64e-983f157feadb"
```

### /edit_animal_by_uuid
Update the animal with UUID matching query parameter `uuid`.  Since UUIDs are generated randomly, you will need to replace the example UUID with one from your database.
**This route uses a POST request instead of a GET request.**

```bash
curl --header "Content-Type: application/json" \
--request POST \
--data '{"legs": 25}' \
"http://localhost:5018/edit_animal_by_uuid?uuid=e050c7a2-8683-477e-a622-e41eef355b74"
```

### /delete_animals_by_dates
Delete all animals created by query parameters `start_date` and `end_date`.  Dates in format `2021-03-30` have been tested, although other formats should be recognized.

```bash
curl "localhost:5018/delete_animals_by_dates?start_date='2021-03-28'&end_date='2021-07-04'"
```

### /get_average_legs
Get the floating point average number of legs for all animals in the database.

```bash
curl "localhost:5018/get_average_legs"
```

### /count_animals
Get the integer number of animals in the database.

```bash
curl "localhost:5018/count_animals"
```
