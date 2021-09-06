import graphene

from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth.mutations import Register,ObtainJSONWebToken

from medpack.products.query import ProductQuery

class Mutations(graphene.ObjectType):
    register = Register.Field()
    token_auth = ObtainJSONWebToken.Field()

class Query(UserQuery, MeQuery,ProductQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutations)
