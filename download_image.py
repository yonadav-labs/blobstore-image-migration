import pdb

import os

import requests

from google.cloud import datastore
from google.appengine.ext import blobstore
from google.appengine.api import apiproxy_stub_map, datastore_file_stub

APP_ID = 'billionacts'

# datastore_file = '/dev/null'
# apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap() 
# stub = datastore_file_stub.DatastoreFileStub(APP_ID, datastore_file, '/')
# apiproxy_stub_map.apiproxy.RegisterStub('datastore_v3', stub)

client = datastore.Client()

kind = 'NetworkMember'
os.environ['APPLICATION_ID'] = APP_ID

query = client.query(kind=kind)
# query.add_filter('property', '=', 'val')
query_iter = query.fetch(limit=5)

for entity in query_iter:
    pdb.set_trace()

    filename = entity['Name'] + '.png'
    image_key = entity['LogoKey']


    image = blobstore.BlobReader(image_key)

    with open(filename, 'w') as f:
        f.write(image.read())

    print (image)
