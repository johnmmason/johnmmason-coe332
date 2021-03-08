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

### /generate

Generate a set of random animals and populate the database. This route takes a query parameter `num_animals` which specifies the number of animals to be generated. If `num_animals` is not given, `num_animals = 1`.

```bash
curl localhost:5018/generate?num_animals=20
```

### /get

Get a specified number of animals from the database.  This route takes a query parameter `num_animals` which specifies the number of animals to be retrieved. If `num_animals` is not given, all animals are printed.

```bash
curl localhost:5018/get # OR
curl localhost:5018/get?num_animals=5
```
### /pop

Get a specified number of animals from the database, and remove them from the database.  This route takes a query parameter `num_animals` which specifies the number of animals to be retrieved. If `num_animals` is not given, `num_animals = 1`.

```bash
curl localhost:5018/pop # OR
curl localhost:5018/pop?num_animals=5
```
