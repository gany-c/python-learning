from flask import Flask
from flask_graphql import GraphQLView
import graphene

"""
pip3 install flask flask-graphql graphene
python3 main.py
Hit the server at http://127.0.0.1:5000/graphql
"""



class Query(graphene.ObjectType):
    hello = graphene.String(description="Just a placeholder")

    def resolve_hello(self, info):
        return "Hello World"


schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
