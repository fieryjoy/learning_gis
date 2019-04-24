#!/bin/bash

USER_HOME="/home/up42"
IMAGE_NAME="up42/test"

IMAGE_ID=$(docker images -f "reference=$IMAGE_NAME" -q)

if [ -d .local ]; then rm -Rf .local; fi

if [ -z "$IMAGE_ID" ]
then
    echo "Be patient while image is built..."
    IMAGE_ID=$(docker build --no-cache -t ${IMAGE_NAME} -q `pwd`)
fi

echo "Starting a container based on the image ID: $IMAGE_ID"
CONTAINER_ID=$(docker run --rm -t -d -v `pwd`:$USER_HOME $IMAGE_ID)
echo "Running container ID is: $CONTAINER_ID"
echo "Preparing environment"
docker exec -it $CONTAINER_ID make build
echo "Running the python scripts and verify the results"
docker exec -it $CONTAINER_ID make show
echo "Cleaning and closing"
docker exec -it $CONTAINER_ID make clean
docker stop $CONTAINER_ID