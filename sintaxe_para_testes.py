from animal import Animal
from cachorro import Cachorro
from gato import Gato
from doador import Doador
from adotante import Adotante
from doacao import Doacao
from adocao import Adocao
from datetime import date
from sistema import Sistema

sistema = Sistema()
patrick = Doador('100.100.100-81', 'Patrick', date(2006,8,11), 'Fullbox 200')
sol = Gato('501', 'Sol', 'Frajola')
tabata = Adotante('100.100.100-82', 'Tabata', date(2011,4,17), 'Fullbox 200', 'Apartamento médio', True)

sistema.registrar_doacao(date(2024, 9, 30), sol, patrick, 'Me acordou de manhã')
print(sistema.doacoes)
print(sistema.listar_animais_disponiveis())

sistema.registrar_adocao(date(2024, 10, 1), sol, tabata, True)
print(sistema.adocoes)
print(sistema.listar_animais_disponiveis())