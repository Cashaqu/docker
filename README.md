# docker
In this work we will package our application on fastapi using docker.

The application will use the previous project as a basis: https://github.com/Cashaqu/rnn_ceasar

## What the application does:
The application performs "dummy" functions. The main goal of the work is to gain skills in working with fastapi and docker.

Application algorithm:
1. Form a POST request
2. Transmit the text encrypted using the Caesar algorithm to the trained model
3. Get the prediction

## Check application work:
Fastapi app - https://github.com/Cashaqu/docker/blob/master/prediction_endpoint.py

Start the ```req.py```:

![1](https://github.com/Cashaqu/docker/blob/master/examples/1.png)

Status code 200:

![2](https://github.com/Cashaqu/docker/blob/master/examples/2.png)

After I built docker-image using ```Dockerfile```:

```python
FROM python:3.10

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "prediction_endpoint:app", "--host", "0.0.0.0", "--port", "80"]
```
For run container:
```sh
$ docker run -d --name <container_name> -p 80:80 <image_name>
```
And now I can use ```http://localhost``` or ```http://127.0.0.1``` to interact with the container:

![3](https://github.com/Cashaqu/docker/blob/master/examples/3.png)

Deleting container and image:

![4](https://github.com/Cashaqu/docker/blob/master/examples/4.png)
