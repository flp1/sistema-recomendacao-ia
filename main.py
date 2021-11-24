from db_itens import *
from db_users import *
from function import *


print('\nRecomendação de bebidas por similaridade:')
print(calculaItensSimilares(avaliacoesBebidas))

print('\n-----------------------------------------')

print('\nLista de recomendação por bebida especifica:')
print(getSimilares(avaliacoesBebidas,'Vinho'))

print('\n-----------------------------------------')

print('\nRecomendação de bebidas por usuário:')
print(getRecomendacoesUsuario(avaliacoesUser, 'Gustavo'))
