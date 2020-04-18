from flask import jsonify
from . import api_v1

cidades = [
    'Brumado',
    'Feira de Santana',
    'Guanambi',
    'Jequié',
    'Salvador',
    'Santo Antônio de Jesus',
    'Simões Filho'
]


@api_v1.route('/cidades', methods=['GET'])
def get_all_cidades():
    return jsonify({'cidades': cidades})