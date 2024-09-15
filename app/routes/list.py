from flask import jsonify, current_app
from app import db
from app.models import Manifestacao

@current_app.route('/manifestacoes', methods=['GET'])
def listar_manifestacoes():
    manifestacoes = Manifestacao.query.all()
    resultado = [{"id": m.id, "tipo": m.tipo, "descricao": m.descricao, "data_criacao": m.data_criacao} for m in manifestacoes]
    return jsonify(resultado)

@current_app.route('/manifestacao/<int:id>', methods=['GET'])
def buscar_manifestacao(id):
    manifestacao = Manifestacao.query.get_or_404(id)
    return jsonify({
        "id": manifestacao.id,
        "tipo": manifestacao.tipo,
        "descricao": manifestacao.descricao,
        "data_criacao": manifestacao.data_criacao
    })