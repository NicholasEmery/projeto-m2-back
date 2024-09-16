from app import db

class Manifestacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(64), index=True, nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    data_criacao = db.Column(db.DateTime, index=True, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Manifestacao {self.id} - {self.tipo}>'
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), index=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    data_criacao = db.Column(db.DateTime, index=True, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Usuario {self.id} - {self.user}>'