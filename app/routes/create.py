from flask import request, jsonify, current_app
from app import db
from app.models import Manifestacao, Usuario

@current_app.route('/manifestacao', methods=['POST'])
def criar_manifestacao():
    dados = request.get_json()
    tipo = dados.get('tipo')
    descricao = dados.get('descricao')

    if not tipo or not descricao:
        return jsonify({"erro": "Tipo e descrição são obrigatórios"}), 400

    manifestacao = Manifestacao(tipo=tipo, descricao=descricao)
    db.session.add(manifestacao)
    db.session.commit()

    return jsonify({"mensagem": "Manifestação criada com sucesso", "id": manifestacao.id}), 201

@current_app.route('/usuario', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    user = dados.get('nome')
    password = dados.get('senha')

    if not user or not password:
        return jsonify({"erro": "Nome e senha são obrigatórios"}), 400
    
    if len(password) > 8:
        return jsonify({"erro": "Senha só pode ter até 8 caracteres"}), 400

    usuario = Usuario(user=user, password=password)
    db.session.add(usuario)
    db.session.commit()

    return jsonify({"server": "Usuario criado com sucesso", "id": usuario.id}), 201