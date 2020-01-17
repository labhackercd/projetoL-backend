from collections import namedtuple
from json import loads, dumps
import requests

from graphene import ObjectType, String, ID, Int, Field, DateTime, Date, List


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    return loads(data, object_hook=_json_object_hook)


class Profile(ObjectType):
    id = ID
    gender = String()
    uf = String()
    country = String()
    birthdate = Date()
    avatar = String()
    profile_type = String()


class User(ObjectType):
    id = ID()
    username = String()
    first_name = String()
    last_name = String()
    last_login = DateTime()
    date_joined = DateTime()
    profile = Field(Profile)


class Query(ObjectType):
    users = List(User)

    def resolve_users(self, info, **kwargs):
        users = api_call()["results"]
        return json2obj(dumps(users))


def api_call():
    response = requests.get('https://edemocracia.camara.leg.br/wikilegis/api/v1/users/',
                            headers={'Accept': 'application/json'})
    return response.json()
