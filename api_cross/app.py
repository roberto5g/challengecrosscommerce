import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

path = os.getcwd()
os.chdir("..")
path = os.getcwd()+'/data_transformation'

@app.route("/api/numbers")
def index():
    
    with open(path+'/dataOrdained.json', 'r') as file:
        data = json.load(file)
        
        return jsonify(get_paginated_list(
            data,
            '/api/numbers',
            page=request.args.get('page', 1)
        ))


def get_paginated_list(items,url, page):
    
    obj = {}
    count = len(items)
    page = int(page)
    limit = 100
    resto = count % limit
    
    if count <= limit:
        total_pages = 1
        limit = count
    else:
        total_pages = count // limit
        if resto > 0:
            total_pages = total_pages + 1

    start = (page - 1) * limit
    end = start + limit

    if end > count:
        end = count
    
    if page > total_pages or page <= 0:
        obj['numbers'] = []    
        return obj

    obj['numbers'] = items[start:end]
    return obj


if __name__ == "__main__":
    app.run()
