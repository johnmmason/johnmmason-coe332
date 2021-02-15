# homework02

#### Run through Docker

This project and its dependencies are eligible to be run through a Docker container.

First, navigate to the `homework02` directory on your machine and run

```
docker build -t {username}/json_parser:1.0 .
```

To launch a container, run

```
docker run --rm -it -v $PWD:/data {username}/json-parser:1.0 /bin/bash
```

All modules are available in `/code` and can be run with

```
python3 {path/to/program}
```

Also, your project root directory has been mounted in the container's `/data` directory.  You can use this mount point to move the generated `animals.json` to your local machine.

```
cp /code/animals.json /data/
```