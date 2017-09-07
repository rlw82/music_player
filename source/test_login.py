from gmusicapi import Mobileclient
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

api = Mobileclient()
data = {}
with open('../../credential.json') as data_file:
    data = json.load(data_file)

logged_in = api.login(data['username'],data['password'],Mobileclient.FROM_MAC_ADDRESS)

@app.route("/search")
def searchQuery():
    query = request.args['query']
    num_results = 50
    if "results" in request.args:
        num_results = request.args['results']
    if (logged_in):
        query_results = api.search(query,num_results)
        return jsonify(query_results)
