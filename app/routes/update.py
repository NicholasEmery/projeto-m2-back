from flask import request, jsonify, current_app
from app import db
from app.models import Manifestacao, Usuario

@current_app.route('/manifestacao/<int:id>', methods=['PUT'])
def atualizar_manifestacao(id):
    manifestacao = Manifestacao.query.get_or_404(id)
    dados = request.get_json()

    manifestacao.tipo = dados.get('tipo', manifestacao.tipo)
    manifestacao.descricao = dados.get('descricao', manifestacao.descricao)

    db.session.commit()
    return jsonify({"mensagem": "Manifestação atualizada com sucesso"})


@current_app.route('/usuario/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    dados = request.get_json()

    usuario.user = dados.get('nome', usuario.user)
    usuario.password = dados.get('senha', usuario.password)

    db.session.commit()
    return jsonify({"server": "Usuario atualizado com sucesso"})


@current_app.route('/manifestacao/<int:id>', methods=['DELETE'])
def excluir_manifestacao(id):
    manifestacao = Manifestacao.query.get_or_404(id)
    db.session.delete(manifestacao)
    db.session.commit()

    return jsonify({"mensagem": "Manifestação excluída com sucesso"})

@current_app.route('/usuario/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"server": "Usuario excluído com sucesso"})