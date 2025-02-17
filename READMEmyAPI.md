the python file myAPI.py is based on this

https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/


Added to requirements.txt: flask-restful


# Running the docker
docker run -d -p 5000:5000 --restart unless-stopped myAPI-app
