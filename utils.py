from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Braga',idade=32)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Braga').first()
    #print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.quesry.filter_by(nome='Jesse').first()
    pessoa.idade = 30
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Braga').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta()

