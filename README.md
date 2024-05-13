# install required packages

pip install grapene-django reqeusts djangorestframework

# To run the project

1. Apply makemigrations: `python manage.py makemigrations planets`
2. Apply migrations: `python manage.py migrate`
3. Run the utility function to fetch data: 
    `python manage.py shell` and then 
    `from planets.utils import fetch_planets;` 
    `fetch_planets()`
    `exit()`
4. Start the server: `python manage.py runserver`

# You can access the GraphQL endpoint at `http://localhost:8000/graphql` and the RESTful API at `http://localhost:8000/api/planets/` on postman.

To retrieve all planets, send a GET request to `http://localhost:8000/api/planets/`.
To create a new planet, send a POST request to `http://localhost:8000/api/planets/` with the planet data in the request body.
To update a planet, send a PUT request to `http://localhost:8000/api/planets/<id>/` with the updated planet data in the request body.
To delete a planet, send a DELETE request to `http://localhost:8000/api/planets/<id>/`.