import base64
import os
import uuid
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from . import db


class Empresas(db.Model):
    __tablename__ = 'empresas'
    id = db.Column(db.String(32), primary_key=True, default=uuid.uuid4().hex)
    data_criacao = db.Column(db.DateTime, default=datetime.now())
    descricao = db.Column(db.String(32))
    usuario = db.Column(db.String(32), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    telefone = db.Column(db.String(16))
    whatsapp = db.Column(db.String(16))
    senha = db.Column(db.String(128))
    cep = db.Column(db.String(8))
    endereco = db.Column(db.String(64))
    bairro = db.Column(db.String(32))
    cidade = db.Column(db.String(32))
    uf = db.Column(db.String(2))
    tipo_negocio = db.Column(db.String(16))
    meio_pagamento = db.Column(db.String(32))
    dias_horarios = db.Column(db.String(128))
    delivery = db.Column(db.Boolean())
    instagram = db.Column(db.String(64))
    facebook = db.Column(db.String(64))
    site = db.Column(db.String(64))
    obs = db.Column(db.String(200))
    token = db.Column(db.String(32), unique=True)
    token_expiration = db.Column(db.DateTime)


    def set_password(self, senha):
        self.senha = generate_password_hash(senha)


    def check_password(self, senha):
        return check_password_hash(self.senha, senha)


    def from_dict(self, data, new_user=False):
        if 'meio_pagamento' in data:
            data['meio_pagamento'] = ','.join(map(str, data['meio_pagamento']))
        
        table = ['descricao', 'usuario', 'email', 
                 'telefone', 'whatsapp', 'cep',
                 'endereco', 'bairro', 'cidade',
                 'uf', 'tipo_negocio', 'meio_pagamento',
                 'dias_horarios', 'delivery', 'instagram',
                 'facebook', 'site', 'obs',]
        for field in table:
            if field in data:
                setattr(self, field, data[field])

        if new_user and 'senha' in data:
            self.set_password(data['senha'])


    def to_json(self):
        data = {
            'id': self.id,
            'descricao': self.descricao,
            'usuario': self.usuario,
            'email': self.email,
            'telefone': self.telefone,
            'whatsapp': self.whatsapp,
            'cep': self.cep,
            'endereco': self.endereco,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'uf': self.uf,
            'tipo_negocio': self.tipo_negocio,
            'meio_pagamento': self.meio_pagamento.split(','),
            'dias_horarios': self.dias_horarios,
            'delivery': self.delivery,
            'instagram': self.instagram,
            'facebook': self.facebook,
            'site': self.site,
            'obs': self.obs
        }
        return data


    def get_token(self):
        now = datetime.now()

        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token

        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=3600)

        db.session.add(self)
        return self.token


    def revoke_token(self):
        self.token = None
        self.token_expiration = None


    @staticmethod
    def check_token(token):
        empresa = Empresas.query.filter_by(token=token).first()
        if empresa is None or empresa.token_expiration < datetime.now():
            return None
        return empresa


    def __repr__(self):
        return f'<Empresa {self.id_empresa}>'