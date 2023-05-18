import cohere
from . import auth
co = cohere.Client(auth.COHERE_API)


class Prompts:
    generate = 'Write an SQL query for this task'
    explain = 'Explain this query in detail, be as accurate as possible'
    fix = 'Fix this query. Suggest results for Postgres, MySQL'
    suggest = 'Whichever database systems this query is compatible with, give me suggestions for optimizing this query'

def generate(query_input)
    return co.generate(model='command', prompt=f'{query_input}\n', max_tokens=2000, temperature=0, k=0, stop_sequences=[], return_likelihoods='NONE')


def generate_query(query_input):
    query_input = f'{Prompts.generate}: {query_input}'
    return generate(query_input)


def explain_query(query):
    query_input = f'{Prompts.explain}: {query}'
    return generate(query_input)


def fix_query(query):
    query_input = f'{Prompts.fix}: {query}'
    return generate(query_input)


def suggest_optimizations(query):
    query_input = f'{Prompts.suggest}: {query}. Write the updated query if it\'s different or any sql commands needed for optimization.'
    return generate(query_input)
