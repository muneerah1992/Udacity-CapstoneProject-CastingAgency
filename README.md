# Udacity Capstone Project - Casting Agency
Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

App live at : https://myfsnd-casting-agency.herokuapp.com 

## Motivation
To apply all the knowledge obtained from Udacity Full Stack Web Developer Nanodegree. 

## Getting Started

### Virtual Enviornment
Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Dependencies
After virtual environment is up and running, all the dependencies can be found in `requirements.txt` file. 
They can be installed by running 
```bash
pip3 install -r requirements.txt
```

## Running the server
From within the project directory first ensure you are working using your created virtual environment.
Each time you open a new terminal session, run:
```bash
export FLASK_APP=app.py;
```
To run the server, execute:
```bash
flask run --reload
```

## Authentication
This API has three registered users:

1. Casting Assistant
```
email: casting_assistant@agency.com
password: casting_assistant@agency.com123
```
2. Casting Director
```
email: casting_director@agency.com
password: casting_director@agency.com123
```
3. Executive Producer
```
email: executive_producer@casting.com
password: executive_producer@casting.com123
```
The Auth0 domain and api audience can be found in `setup.sh`.

## Test
all tests can be found in Udacity_Casting_Agency_Tests.postman_collection.json within the project directory.
Import the postman collection then run.

## Endpoints

### GET '/movies'
- Fetches an array of movies.
- Returns: the id of the movie, title, release date and sucess value.
- Response: 
``` 
{
    "movies": [
        {
            "id": 1,
            "release date": "1/1/2021",
            "title": "new movie"
        },
        {
            "id": 2,
            "release date": "1/5/2021",
            "title": "new movie 2"
        },
        {
            "id": 3,
            "release date": "1/5/2021",
            "title": "new movie 3"
        }
    ],
    "success": true
}
```

### GET '/actors'
- Fetches an array of actors.
- Returns: the id of the actor, name,  gender, age and sucess value.
- Response: 
``` 
{
    "actors": [
        {
            "age": 18,
            "gender": "Female",
            "id": 3,
            "name": "Muna"
        },
        {
            "age": 40,
            "gender": "Male",
            "id": 2,
            "name": "Reda"
        },
        {
            "age": 45,
            "gender": "Female",
            "id": 1,
            "name": "Sara"
        }
    ],
    "success": true
}
```

### POST '/movies'
- Creates a new movie using the submitted title, and release date.
- Returns: the id of the created movie, title and success value.
- Response: 
``` 
{
    "created": 4,
    "movie": "new movie 4",
    "success": true
}
```

### POST '/actors'
- Creates a new actor using the submitted name, age  and  gender.
- Returns: the id of the created movie, title and success value.
- Response: 
``` 
{
    "actor": "Saad",
    "created": 4,
    "success": true
}
```

### DELETE '/movies/<id>'
- Deletes a movie of the given ID if it exists.
- Returns: the id of the deleted movie and success value
- Response:    
``` 
{
    "delete": "1",
    "success": true
}
``` 

### DELETE '/actors/<id>'
- Deletes an actor of the given ID if it exists.
- Returns: the id of the deleted actor and success value
- Response:    
``` 
{
    "delete": "1",
    "success": true
}
``` 

### PATCH '/movies/<id>'
- Update a movie of the given ID if it exists.
- Returns: the title of the movie, release date and success value
- Response:    
``` 
{
    "movie": "new movie 1",
    "release_date": "1/1/2021",
    "success": true
}
``` 

### PATCH '/actors/<id>'
- Update an actor of the given ID if it exists.
- Returns: the name of the actor, age, gender and success value
- Response:    
``` 
{
    "actor": "Hamad",
    "age": 40,
    "gender": "Male",
    "success": true
}
``` 
