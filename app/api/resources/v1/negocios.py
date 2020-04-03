from flask import jsonify
from . import api_v1

tipos_negocios = [
    'Acessórios',
    'Armarinho',
    'Bar ou Lanchonete',
    'Calçados',
    'Farmácia',
    'Informática',
    'Mercado',
    'Mercearia',
    'Padaria',
    'Restaurante',
    'Saúde e Beleza',
    'Vestuário',
    'Veterinário',
    'Outros'
]


@api_v1.route('/tiposNegocios', methods=['GET'])
def get_tipos_negocios():
    return jsonify({'tipos_negocios': tipos_negocios})