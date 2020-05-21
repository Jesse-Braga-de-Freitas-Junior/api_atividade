from flask import Flask, Request
from flask_restful import Resource, Api
import models

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = models.Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.idade
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada'
            }
        return response

    def put(self, nome):
        pessoa = models.Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = models.Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa excluída com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso', 'mensagem':mensagem}

class ListaPessoas(Resource):
    def get(self):
        pessoas = models.Pessoas.query.all()
        response = [{'id':id.id, 'nome':id.nome, 'idade':id.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = models.Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = models.Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = models.Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = models.Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.nome
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividade/')

if __name__ == '__main__':
    app.run(debug=True)