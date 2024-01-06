# Framework for API testing

### Build docker image:
`docker build -t pytest_framework .`

### Run docker image:
`docker run --rm --mount type=bind,src=$PATH_TO_CURREN§T_DIRECTORY,target=/tests_project/ pytest_framework`

### Run with docker-compose:
`docker-compose up --build`