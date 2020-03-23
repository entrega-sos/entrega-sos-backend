from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.api.models.empresas import Empresas

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(usuario, senha):
    empresa = Empresas.query.filter_by(usuario=usuario).first()
    if empresa is None:
        return False

    g.current_user = empresa
    return empresa.check_password(senha)


@token_auth.verify_token
def verify_token(token):
    g.current_user = Empresas.check_token(token) if token else None
    return g.current_user is not None