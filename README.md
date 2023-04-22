# Flight delay predictor API - Option ML engineer test

This repository has the code to start an API that consumes an XGBoost classification model that is capable of determining if a flight will be delayed or not. The model returns 1 if the flight will be delayed and 0 if the model will not be delayed.

The data format that has to be sent to the API in order to obtain a response, in JSON format, is the following:
```
{
    "opera":"LATAM",
    "mes":12,
    "tipo_vuelo":"I",
    "sigla_des":"Antofagasta",
    "dia_nom":"Sabado"
}
```
Where:
- **opera:** is a string holding the airline operator name.

- **mes**: is an integer representing the month that the flight will be operated (between 1 and 12, with 1 being January and 12 being December).

- **tipo_vuelo:** is a string having the information to know if it is a national flight or an international flight (N for national - I for International).

- **sigla_des:** is a string holding the destination city name.

- **dia_nom:** is a string holding the day of the week the flight will be operated in spanish (Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo).

## Installation requirements

In order to install the needed python libraries to execute the API, the repository has a `requirements.txt` file that can be used with a package manager to configure the environment. It is recommended to generate a python virtual environment with [python 3.9 distribution](https://www.python.org/downloads/release/python-390/) and tools like [venv](https://docs.python.org/3/library/venv.html) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

A video describing how to install **virtualenvwrapper in Windows** can be found in this [link](https://www.youtube.com/watch?v=e6xHdRegBNs). For other OS the documentation previously provided states the installation instructions.

Once the virtual environment is set up, the required libraries can be installed with pip using the following command while being inside the repository folder:


<div align="center">
  
  `pip install -r requirements.txt`

</div>

## Start the API in Local environment

After having all the requirements installed, in order to start the API in a local environment the following command must be executed while being inside the `src` folder where the `api.py` file is:

<div align="center">

`uvicorn api:app --host 0.0.0.0 --port 3031`

</div>

It is not mandatory for the port number to be 3031, it can be any other. Also, within the `src` folder the file `important_commands.txt` holds some useful commands.

Once the API is up and running in the local environment, it should look like this:

![image](https://user-images.githubusercontent.com/4323981/233800568-d4e57f72-13fd-421a-9b46-65a6378c86b9.png)

When the API is working it is possible to send HTTP POST requests with any testing tool such as [Postmant](https://www.postman.com) or any other similar tool. The format should be the one presented at the beginning of this readme file and the endpoint URL is:

<div align="center">

`http://localhost:3031/predict`

</div>

## Stress test results with [wrk](https://github.com/wg/wrk)

The command to execute the stress test as required is the following:
<div align="center">

`wrk -t10 -c50000 -d45s -s post_request.lua http://localhost:3031/predict`

</div>

Before running that command it may necessary to increase the number of open files in the OS with the following command:
<div align="center">

`ulimit 65536`

</div>

### Results with 1000 connections for 45 seconds
![image](https://user-images.githubusercontent.com/4323981/233805975-c3a69e0b-f349-41d4-9768-57887e2e2111.png)

### Results with 10000 connections for 45 seconds
![image](https://user-images.githubusercontent.com/4323981/233806007-e2348bc5-2aa9-4a61-9317-5288b22934e1.png)

### Results with 15000 connections for 45 seconds
![image](https://user-images.githubusercontent.com/4323981/233806242-3350f032-d3ee-4ae7-95b7-8c2bad8876be.png)

### Results with 50000 connections for 45 seconds
![image](https://user-images.githubusercontent.com/4323981/233807836-55fd1b76-69dd-4fec-852c-99c608ee273f.png)

## Possible improvements for the API

- **Use a production-ready web server:** FastAPI uses the **Uvicorn server** by default, which is suitable for development purposes, but may not be the best choice for production use with high loads. Using a production-ready web server such as [Gunicorn](https://gunicorn.org) or [Hypercorn](https://pgjones.gitlab.io/hypercorn/) could enable the API to handle a large number of concurrent requests efficiently.
- **Load balancing:** In case the API is anticipating a high number of concurrent requests, using load balancing techniques such as distributing the incoming requests across multiple instances of the FastAPI application running on different servers could help distribute the load and prevent any single instance from becoming a bottleneck.
- **Implementing a new endpoint to retrain the model:** Since the performance of the model could deteriorate over time, it is important to have an option that retrains the model with updated data and stores it in the joblib for it to be reused when needed.


