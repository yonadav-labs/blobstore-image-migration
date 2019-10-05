from google.cloud import datastore


client = datastore.Client()

kind = 'NetworkMember'

query = client.query(kind=kind)
# query.add_filter('property', '=', 'val')
query_iter = query.fetch()

for entity in query_iter:
    print (entity['LogoKey'])
