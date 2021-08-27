from blog import schema as blog_schema
import graphene

class Query(blog_schema.Query,graphene.ObjectType):
	pass


schema = graphene.Schema(query = Query)