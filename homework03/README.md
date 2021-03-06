# homework03 - The Containerized API of Dr. Moreau

This assignment creates a web API for the scripts in `johnmmason-coe332/homework02` which can be run through Docker.

## Running the Container

Get started by cloning this repository and navigating to the `homework03` folder:

```bash
git clone https://github.com/johnmmason/johnmmason-coe332.git
cd johnmmason-coe332/homework03
```

Launch the container using `docker-compose`:

```bash
docker-compose up -d
```

When you're done, stop the container and clean up:

```bash
docker-compose down
```

## The Web API

This project consists of 3 routes which perform unique operations on the animals database.

### /generate_animals

Generate a set of random animals and populate the database. This route takes a query parameter `num_animals` which specifies the number of animals to be generated. If `num_animals` is not given, `num_animals = 1`.

```bash
curl localhost:5018/generate_animals?num_animals=20
```

### /animals

Get a specified number of animals from the database.  This route takes a query parameter `num_animals` which specifies the number of animals to be retrieved. If `num_animals` is not given, all animals are printed.  You can also specify an additional query parameter `head_type` which limits the output to animals with a specified head type.  If `head_type` is not given, all animals are printed.  Note: If you specify `head_type`, `num_animals` must not be greater than the number of animals with the given head type.

```bash
curl localhost:5018/animals # OR
curl localhost:5018/animals?num_animals=5 # OR
curl "localhost:5018/animals?num_animals=2&head_type=snake"
```
### /pop_animals

Get a specified number of animals from the database, and remove them from the database.  This route takes a query parameter `num_animals` which specifies the number of animals to be retrieved. If `num_animals` is not given, `num_animals = 1`.

```bash
curl localhost:5018/pop_animals # OR
curl localhost:5018/pop_animals?num_animals=5
```
