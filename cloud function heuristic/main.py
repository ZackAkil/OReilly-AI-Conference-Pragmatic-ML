import json
from flask import Response

def predict(request):
    
    resp = Response()
    resp.headers.set('Content-Type','application/json')
    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Access-Control-Allow-Headers', 'Content-Type')
    
    if request.method == 'OPTIONS':
        resp.status_code = 204
        return resp

    request_json = request.get_json()
    
    flower_data = request_json['instances'][0]

    output = None

    if flower_data[0] < 5.5:
        output = 0
    elif flower_data[0] < 6.5:
        output = 1
    else:
        output = 2     
    
    resp.response = json.dumps({"predictions":[output]})
    
    return resp

