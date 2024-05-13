import graphene
from graphene_django import DjangoObjectType
from .models import Planet

class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = '__all__'

class Query(graphene.ObjectType):
    planets = graphene.List(PlanetType)

    def resolve_planets(self, info):
        return Planet.objects.all()

schema = graphene.Schema(query=Query)