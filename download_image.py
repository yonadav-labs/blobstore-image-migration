# Imports the Google Cloud client library
from google.cloud import datastore
# from google.appengine.ext import db

# class NetworkMember(db.Model):
#     LogoKey = db.StringProperty()
#     Name = db.StringProperty()
#     LockTagging = db.BooleanProperty()

# Instantiates a client
datastore_client = datastore.Client()

# The kind for the new entity
kind = 'NetworkMember'
# The name/ID for the new entity
name = 'sampletask1'
# The Cloud Datastore key for the new entity
task_key = datastore_client.key(kind, name)

query = datastore_client.query(kind=kind)
# query.add_filter('property', '=', 'val')
query_iter = query.fetch()
for entity in query_iter:
    print (entity)

# # Prepares the new entity
# task = datastore.Entity(key=task_key)
# task['description'] = 'Buy milk'

# # Saves the entity
# # datastore_client.put(task)

# print('Saved {}: {}'.format(task.key.name, task['description']))

# q = NetworkMember.all()

# for p in q.run(limit=5):
#     print (p.Name)
