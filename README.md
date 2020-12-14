# EventHub-Containerised-PythonSender
Submits Faked names to an Event Hub in Python from a Container

# About this code
Uses the [Faker library](https://github.com/joke2k/faker/) to send fake data to an Event Hub. It is intended to run in a container and be extended by the user.

## Build
Assuming you want to build a container using this given name.
````
    docker build -t event-sender:1 . 
````

To build for your own Azure Container Registry change that to look more like this.
````
    docker build -t yourcontainerreg.azurecr.io/event-sender:1 .
````

## Run
Assuming you called your docker image is called event-sender and tagged version 1 run the following to run the image.

Note you need to get the send connection string for your event hub and use that in the command line that invokes the container.

````
docker run -e EVENT_HUB_CONN_STR=YOUR_EVENT_HUB_CONNECTION_STRING -e EVENT_HUB_NAME=EVENT_HUB_NAME event_hub_loader:tag
````

# Authors
A superb fun team build this on December 14th 2020 as a remote mini CSA Hack 
