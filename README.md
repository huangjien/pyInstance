# pyInstance

## Run
Build the Docker image:

```docker-compose build```
Run the docker-compose environment:

```docker-compose up```

## Test
This application comes with the unit tests.

To run the tests do:

```docker-compose run --rm example py.test instance/tests.py --cov=instance```