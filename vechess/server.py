import vechess.core as vech
import json

def app(env, start_response):
    request_method = env["REQUEST_METHOD"]
    query_string = env["QUERY_STRING"]
    if request_method == "GET":
        if query_string == "/state/":
            start_response('200 OK', [('Content-Type','application/json')])
            return [json.dumps(vech.BoardState_data(), sort_keys=True)]
        elif query_string == "/init/":
            vech.initialize()
            start_response('200 OK', [('Content-Type','application/json')])
            return [json.dumps({"response": "OK"})]
    start_response('501 Not Implemented', [('Content-Type','application/json')])
    return [json.dumps({"response": "Not implemented"})]
