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


class Suggestion(ObjectType):
    id = ID()
    created = DateTime()
    modified = DateTime()
    excerpt = String()
    start_index = Int()
    end_index = Int()
    content = String()
    author = Field(User)


class Query(ObjectType):
    users = List(User)
    suggestions = List(Suggestion, idSugestion=Int(
        required=False), idUser=Int(required=False))

    def resolve_users(self, info, **kwargs):
        users = api_call_user()["results"]
        return json2obj(dumps(users))

    def resolve_suggestions(self, info, idSugestion=None, idUser=None):
        if idSugestion:
            users = api_call_sugestion(idSugestion)["results"]
        elif idUser:
            users = api_call_sugestions_user(idUser)["results"]
        else:
            users = api_call_sugestions()["results"]
        return json2obj(dumps(users))


def api_call_user():
    response = requests.get('https://edemocracia.camara.leg.br/wikilegis/api/v1/users/',
                            headers={'Accept': 'application/json'})
    return response.json()


def api_call_sugestions():
    response = requests.get('https://edemocracia.camara.leg.br/wikilegis/api/v1/sugestions/',
                            headers={'Accept': 'application/json'})
    return response.json()


def api_call_sugestion(id: Int):
    url_format = 'https://edemocracia.camara.leg.br/wikilegis/api/v1/sugestions/?id={}'.format(
        id)
    response = requests.get(url_format, headers={'Accept': 'application/json'})
    return response.json()


def api_call_sugestions_user(id: Int):
    url_format = 'https://edemocracia.camara.leg.br/wikilegis/api/v1/sugestions/?author__id={}'.format(
        id)
    response = requests.get(url_format, headers={'Accept': 'application/json'})
    return response.json()
