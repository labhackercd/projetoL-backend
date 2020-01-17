import graphene

import api_proxy.wikilegis


class Query(api_proxy.wikilegis.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
