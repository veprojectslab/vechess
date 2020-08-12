import vechess.core as vech
import json
import datetime
import base64
import sys
try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

def app(env, start_response):
    request_method = env["REQUEST_METHOD"]
    path_info = env["PATH_INFO"]
    std_headers = [('Content-Type','application/json')]
    if "HTTP_AUTHORIZATION" in env:
        u_name = base64.b64decode(env["HTTP_AUTHORIZATION"].split(" ")[1]).split(":")[0]
    else:
        u_name = "someone"
    if request_method == "GET" and path_info == "/state/":
        start_response('200 OK', std_headers)
        return [json.dumps(vech.BoardState_data(), sort_keys=True)]
    elif request_method == "GET" and path_info == "/init/":
        vech.initialize()
        vech.BoardState_clear()
        vech.BoardState_populate_from_single_dict({"KW": "E1", "QW": "D1", "R1W": "A1", "N1W": "B1", "B1W": "C1", "R2W": "H1", "N2W": "G1", "B2W": "F1", "P1W": "A2", "P2W": "B2", "P3W": "C2", "P4W": "D2", "P5W": "E2", "P6W": "F2", "P7W": "G2", "P8W": "H2", "KB": "E8", "QB": "D8", "R1B": "H8", "N1B": "G8", "B1B": "F8", "R2B": "A8", "N2B": "B8", "B2B": "C8", "P1B": "H7", "P2B": "G7", "P3B": "F7", "P4B": "E7", "P5B": "D7", "P6B": "C7", "P7B": "B7", "P8B": "A7", "U": u_name, "MoveTime": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
        start_response('200 OK', std_headers)
        return [json.dumps({"response": "OK"})]
    elif request_method == "POST" and path_info == "/newmove/":
        vech.initialize()
        wsgi_data = env["wsgi.input"].read(0)
        data_dict = {"U": u_name, "MoveTime": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
        data_dict.update(json.loads(wsgi_data))
        vech.BoardState_populate_from_single_dict(data_dict)
        start_response('200 OK', std_headers)
        return [json.dumps({"response": "OK"})]
    start_response('501 Not Implemented', std_headers)
    return [json.dumps({"response": "Not implemented"})]
