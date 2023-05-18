import cohere
from . import auth

co = cohere.Client(auth.COHERE_API)


def generate_query(query_input):
    query_input = f'Write an SQL query for this task: {query_input}'
    return co.generate(model='command', prompt=f'{query_input}\n', max_tokens=2000, temperature=0, k=0, stop_sequences=[], return_likelihoods='NONE')


def explain_query(query):
    query_input = f'Explain this query in detail, be as accurate as possible: {query}'
    return co.generate(model='command', prompt=f'{query_input}\n', max_tokens=2000, temperature=0, k=0, stop_sequences=[], return_likelihoods='NONE')

def fix_query(query):
    query_input = f'Fix this query. Suggest results for Postgres, MySQL: {query}'
    return co.generate(model='command', prompt=f'{query_input}\n', max_tokens=2000, temperature=0, k=0, stop_sequences=[], return_likelihoods='NONE')
