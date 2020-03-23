from flask import jsonify, make_response
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {'error': str(status_code)+ ' ' + 
                        HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message

    response = jsonify(payload)
    response.status_code = status_code
    return response


def handle_error(e):
    code = 500
    error, message = str(e).split(':', 1)

    if isinstance(e, HTTPException):
        code = e.code

    # errors = dict(
    #     error=error,
    #     message=message.strip(),
    #     code=code,
    #     path=request.path,
    # )

    return make_response(jsonify(error=error), code)