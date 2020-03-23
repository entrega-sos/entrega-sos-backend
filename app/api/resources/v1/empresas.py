from flask import abort, g, jsonify, make_response, request, url_for
from flask_expects_json import expects_json
from . import api_v1
from app.api.auth.empresas import basic_auth, token_auth
from app.api.common import rest, errors
from app.api.models import db
from app.api.models.empresas import Empresas


class SchemaJSON:
    create_empresa = {
        'type': 'object',
        'properties': {
            'descricao': {'type': 'string'},
            'usuario': {'type': 'string'},
            'email': {'type': 'string'},
            'telefone': {'type': 'string'},
            'whatsapp': {'type': 'string'},
            'senha': {'type': 'string'},
            'cep': {'type': 'string'},
            'endereco': {'type': 'string'},
            'bairro': {'type': 'string'},
            'cidade': {'type': 'string'},
            'uf': {'type': 'string'},
            'tipo_negocio': {'type': 'string'},
            'meio_pagamento': {'type': 'array'},
            'dias_horarios': {'type': 'string'},
            'delivery': {'type': 'boolean'},
            'instagram': {'type': 'string'},
            'facebook': {'type': 'string'},
            'site': {'type': 'string'},
            'obs': {'type': 'string'}
        },
        'required': ['descricao', 'usuario', 'senha']
    }


@api_v1.route('/empresas', methods=['POST'])
@expects_json(SchemaJSON.create_empresa)
def create_empresa():
    data = request.get_json() or {}
    if Empresas.query.filter_by(usuario=data['usuario']).first():
        return errors.error_response(409, 'informe outro usuário')

    empresa = Empresas()
    empresa.from_dict(data, new_user=True)
    
    db.session.add(empresa)
    db.session.commit()

    response = jsonify(empresa.to_json())
    response.status_code = 201
    response.headers['Location'] = url_for('api_v1.get_empresa', 
                                           usuario=empresa.usuario)
    return response


@api_v1.route('/empresas/<string:usuario>', methods=['GET'])
@token_auth.login_required
def get_empresa(usuario):
    empresa = Empresas.query.filter_by(usuario=usuario).first()
    if empresa == None: 
        return errors.error_response(404, 'usuário não encontrado')
    return jsonify(empresa.to_json())


@api_v1.route('/empresas', methods=['GET'])
@token_auth.login_required
def get_all_empresas():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = rest.pagination(Empresas.query,
                           page, per_page,
                           'api_v1.get_all_empresas')
    return jsonify(data)


@api_v1.route('/empresas/<string:usuario>', methods=['PUT'])
@token_auth.login_required
def update_empresa(usuario):
    if g.current_user.usuario != usuario:
        abort(403)

    empresa = Empresas.query.filter_by(usuario=usuario).first()
    if empresa == None: 
        return errors.error_response(404, 'usuário não encontrado')

    data = request.get_json() or {}
    if \
    'usuario' in data and \
    data['usuario'] != empresa.usuario and \
    Empresas.query.filter_by(usuario=usuario).first():
        return errors.error_response(409, 'informe outro usuário')

    empresa.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(empresa.to_json())


@api_v1.route('/empresas/<string:usuario>', methods=['DELETE'])
@token_auth.login_required
def delete_empresa(usuario):
    if g.current_user.usuario != usuario:
        abort(403)

    empresa = Empresas.query.filter_by(usuario=usuario).first()
    if empresa == None: 
        return errors.error_response(404, 'usuário não encontrado')

    db.session.delete(empresa)
    db.session.commit()
    return make_response('', 204)


@api_v1.route('/empresas/auth/token', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({'token': token})


@api_v1.route('/empresas/auth/token', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    g.current_user.revoke_token()
    db.session.commit()
    return make_response('', 204)