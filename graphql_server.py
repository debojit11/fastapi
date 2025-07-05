from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
import strawberry

@strawberry.type
class Book:
   title: str
   author: str
   price: int

@strawberry.type
class Query:
   @strawberry.field
   def book(self) -> Book:
    return Book(title="Computer Fundamentals", author="Sinha", price=300)
   

schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)
app = FastAPI()

app.include_router(graphql_app, prefix="/book")
app.add_websocket_route("/book", graphql_app)

