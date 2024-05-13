import requests
from .models import Planet  # Import the Planet model

def fetch_planets():
    query = """
        query Query {
            allPlanets {
                planets {
                    name
                    population
                    terrains
                    climates
                }
            }
        }
    """

    url = 'https://swapi-graphql.netlify.app/.netlify/functions/index'
    response = requests.post(url, json={'query': query})
    data = response.json()['data']['allPlanets']['planets']

    for planet in data:
        Planet.objects.get_or_create(
            name=planet['name'],
            population=planet['population'],
            terrains=','.join(planet['terrains']),
            climates=','.join(planet['climates'])
        )