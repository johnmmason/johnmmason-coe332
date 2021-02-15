# homework02 - The Containers and Repositories of Dr. Moreau

This folder builds on the Python scripts created in `johnmmason-coe332/homework01`

## Project Overview

#### Folder Contents
* `generate_animals.py`, which generates `animals.json`
* `animals.json`, the output of `generate_animals.py`, which contains 20 bizarre animals
* `read_animals.py`, which reads `animals.json` and prints a specificed number of animals to the screen

#### Key Changes

* `read_animals.py` now takes a positional parameter `{num_animals}` so you can specify how many animals to get, without replacement
* `read_animals.py` employs assertions and error checking on `{num_animals}`, and prints specific error messages when given an invalid input

## Running this Project

Get started by cloning this repository and navigating to the `homework02` folder:

```
git clone https://github.com/johnmmason/johnmmason-coe332.git
cd johnmmason-coe332/homework02
```

Make the `.py` files executable:

```
chmod 700 *.py
```

### Run Locally

First, ensure you have the required Python libraries to run this project:

```
pip3 install --user -r requirements.txt
```

Now, you can run the scripts as follows:

generate_animals.py:
```
./generate_animals.py
./read_animals.py {num_animals}
```

### Run through Docker

First, navigate to the `homework02` directory on your machine and run:

```
docker build -t {username}/json_parser:1.0 .
```

To launch a container, run:

```
docker run --rm -it -v $PWD:/data {username}/json_parser:1.0 /bin/bash
```

Then, navigate to the mounted directory `/host`:

```
cd /host
```

Now, run the scripts:

```
./generate_animals.py
./read_animals.py {num_animals}
```
*Copies of the code will also be available in `/code` in case you would prefer not to mount your host's PWD, or choose to mount a PWD other than `johnmmason-coe332/homework02`.*

## Unit Testing

Tests for the function `get_num_animals` within `read_animals.py` are available in the file `test_read_animals.py`.  You can run these tests using:
```
./test_read_animals.py
```
