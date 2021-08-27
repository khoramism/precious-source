from django.test import TestCase

# Create your tests here.


# GRAPHQL tests
import json
import pytest
from graphene_django.utils.testing import graphql_query

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func

# Test you query using the client_query fixture
def test_some_query(client_query):
    response = client_query(
        '''
        query {
            post {
                id
                title
            }
        }
        ''',
        op_name='Post'
    )
    content = json.loads(response.content)
    assert 'errors' not in content