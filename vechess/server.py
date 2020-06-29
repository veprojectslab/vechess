import vechess.core as vech

def app(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    return [json.dumps(vech.BoardState_data(), sort_keys=True)]
