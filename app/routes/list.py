from flask import jsonify, current_app
from app import db
from app.models import Manifestacao, Usuario

@current_app.route('/manifestacoes', methods=['GET'])
def listar_manifestacoes():
    manifestacoes = Manifestacao.query.all()
    resultado = [{"id": m.id, "tipo": m.tipo, "descricao": m.descricao, "data_criacao": m.data_criacao} for m in manifestacoes]
    return jsonify(resultado)

@current_app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    resultado = [{"id": m.id, "nome": m.user, "senha": m.password, "data_criacao": m.data_criacao} for m in usuarios]
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

@current_app.route('/usuario/<int:id>', methods=['GET'])
def buscar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify({
        "id": usuario.id,
        "tipo": usuario.user,
        "descricao": usuario.password,
        "data_criacao": usuario.data_criacao
    })
