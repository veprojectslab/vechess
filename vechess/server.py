import vechess.core as vech
import json

def app(env, start_response):
    request_method = env["REQUEST_METHOD"]
    path_info = env["PATH_INFO"]
    if request_method == "GET":
        if path_info == "/state/":
            start_response('200 OK', [('Content-Type','application/json')])
            return [json.dumps(vech.BoardState_data(), sort_keys=True)]
        elif path_info == "/init/":
            vech.initialize()
            vech.BoardState_clear()
            vech.BoardState_populate_from_single_dict({"cmd": "", "id": None, "KW": "E1", "QW": "D1", "R1W": "A1", "N1W": "B1", "B1W": "C1", "R2W": "H1", "N2W": "G1", "B2W": "F1", "P1W": "A2", "P2W": "B2", "P3W": "C2", "P4W": "D2", "P5W": "E2", "P6W": "F2", "P7W": "G2", "P8W": "H2", "KB": "E8", "QB": "D8", "R1B": "H8", "N1B": "G8", "B1B": "F8", "R2B": "A8", "N2B": "B8", "B2B": "C8", "P1B": "H7", "P2B": "G7", "P3B": "F7", "P4B": "E7", "P5B": "D7", "P6B": "C7", "P7B": "B7", "P8B": "A7", })
            start_response('200 OK', [('Content-Type','application/json')])
            return [json.dumps({"response": "OK"})]
    start_response('501 Not Implemented', [('Content-Type','application/json')])
    return [json.dumps({"response": "Not implemented"})]
