import base64
import os
import uuid
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

class Empresas(db.Model):
    __tablename__ = 'empresas'
    
    id = db.Column(db.String(32), primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now())
    descricao = db.Column(db.String())
    usuario = db.Column(db.String(), unique=True, index=True)
    email = db.Column(db.String(), unique=True, index=True)
    telefone = db.Column(db.String())
    whatsapp = db.Column(db.String())
    senha = db.Column(db.String())
    cep = db.Column(db.String())
    endereco = db.Column(db.String())
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())
    uf = db.Column(db.String())
    tipo_negocio = db.Column(db.String())
    outro_negocio = db.Column(db.String())
    meio_pagamento = db.Column(db.String())
    dias_horarios = db.Column(db.String())
    delivery = db.Column(db.Boolean())
    instagram = db.Column(db.String())
    facebook = db.Column(db.String())
    site = db.Column(db.String())
    obs = db.Column(db.String())
    admin = db.Column(db.Boolean())
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
                 'uf', 'tipo_negocio', 'outro_negocio',
                 'meio_pagamento', 'dias_horarios', 'delivery',
                 'instagram', 'facebook', 'site', 'obs', 'admin']
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
            'outro_negocio': self.outro_negocio,
            'meio_pagamento': self.meio_pagamento.split(','),
            'dias_horarios': self.dias_horarios,
            'delivery': self.delivery,
            'instagram': self.instagram,
            'facebook': self.facebook,
            'site': self.site,
            'obs': self.obs
            # 'admin': self.admin
        }
        return data


    def get_token(self):
        now = datetime.now()

        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token

        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(days=365)

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