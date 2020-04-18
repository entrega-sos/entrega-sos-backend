from flask import jsonify
from . import api_v1

tipos_negocios = [
    'Álcool em Gel',
    'Máscaras',
    'Açaí',
    'Acessórios',
    'Armarinho',
    'Automóveis',
    'Bar',
    'Barbearia',
    'Bazar',
    'Bebidas',
    'Calçados',
    'Celulares',
    'Cosméticos',
    'Construção',
    'Diarista',
    'Educação',
    'Eletricista',
    'Eletrônicos',
    'Estética',
    'Farmácia',
    'Festas',
    'Fitness',
    'Frutos do mar',
    'Informática',
    'Lanchonete',
    'Manicure/Pedicure',
    'Marmita/Quentinha',
    'Mercado',
    'Mercearia',
    'Móveis',
    'Padaria',
    'Papelaria',
    'Páscoa/Chocolates',
    'Pizzaria',
    'Restaurante',
    'São João',
    'Saúde',
    'Serviços',
    'Vestuário',
    'Veterinário',
    'Geral'
]


@api_v1.route('/tiposNegocios', methods=['GET'])
def get_tipos_negocios():
    return jsonify({'tipos_negocios': tipos_negocios})