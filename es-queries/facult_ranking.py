import pandas as pd
from elasticsearch import Elasticsearch

# Read the faculty rankings from the Excel file
df = pd.read_excel('faculty_rankings.xlsx', sheet_name='Sheet1')
faculty_rankings = dict(zip(df['University'].tolist(), df['Ranking'].tolist()))

# Connect to the Elasticsearch cluster
es = Elasticsearch(['localhost:9200'])

# Define the search query
query = {
    "query": {
        "bool": {
            "must": [
                {"term": {"object_name": "University"}},
                {"exists": {"field": "canadianRanking"}}
            ]
        }
    },
    "_source": ["_id", "object_name"],
    "size": 12,
    "sort": [{"_script": {
        "type": "number",
        "script": {
            "source": f"if (params.faculty_rankings.containsKey(doc['object_name.keyword'].value)) {{ params.faculty_rankings[doc['object_name.keyword'].value] }} else {{ 0 }}",
            "params": {"faculty_rankings": faculty_rankings}
        },
        "order": "desc"
    }}]
}

# Execute the search query
results = es.search(index="canadian_universities", body=query)

# Print the top 12 universities based on their faculty rankings
print("Top 12 universities based on faculty rankings:")
for i, hit in enumerate(results['hits']['hits']):
     print(f"{i+1}. {hit['_source']['object_name']} (Ranking: {faculty_rankings.get(hit['_source']['object_name'], '-')})")


#Without having to seek approval from canadianRanking first

import pandas as pd
from elasticsearch import Elasticsearch

# Read the faculty rankings from the Excel file
df = pd.read_excel('faculty_rankings.xlsx', sheet_name='Sheet1')
faculty_rankings = dict(zip(df['University'].tolist(), df['Ranking'].tolist()))

# Connect to the Elasticsearch cluster
es = Elasticsearch(['localhost:9200'])

# Define the search query
query = {
    "query": {
        "bool": {
            "must": [
                {"term": {"object_name": "University"}},
                {"exists": {"field": "canadianRanking"}}
            ]
        }
    },
    "_source": ["_id", "object_name"],
    "size": 12,
    "sort": [{"script": {
        "type": "number",
        "script": {
            "source": f"params.faculty_rankings.containsKey(doc['object_name.keyword'].value) ? params.faculty_rankings[doc['object_name.keyword'].value] : 0",
            "params": {"faculty_rankings": faculty_rankings}
        },
        "order": "desc"
    }}]
}

# Execute the search query
results = es.search(index="canadian_universities", body=query)

# Print the top 12 universities based on their faculty rankings
print("Top 12 universities based on faculty rankings:")
for i, hit in enumerate(results['hits']['hits']):
    print(f"{i+1}. {hit['_source']['object_name']} (Ranking: {faculty_rankings.get(hit['_source']['object_name'], '-')})")