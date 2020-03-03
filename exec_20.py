# !/Pasta Pessoal/Documentos/WF rpg

from random import randint


print('selecione em qual situação está :')
print('A : tesde de percepcão Ultilizar D8')
print('B : turnos de colldown  Ultilizar D6')
print('C : teste de dano Ultilizar o 2*D20')

situation = input('Situacao')
if situation == 'a':
    dadoD08 = randint(1, 8)
    print(f'O Resultado D08 é : {dadoD08}')
    if dadoD08 <= 1:
        print(f'{dadoD08} Resultado foi uma merda')
    elif dadoD08 == 8:
        print(f'{dadoD08} Você e um ninja')
    elif dadoD08 <= 6:
        print(f'{dadoD08} Pois é acho que o resultado poderia ter sido melhor')
    else:
        print(f'{dadoD08} Resultado satisfatório')
elif situation == 'b':
    print('Coloque o nivel de sua invocação')
    print('Livel 1: invocação de animais de 500g ate 500 kg')
    print('Livel 2: invocação de bosses e pessoas')
    print('Livel 3: invocação de entidade')
    magic_level = input('Nivel de magia: ')
    if magic_level == '1':
        dadoD06 = randint(1, 6)
        print(f'O Resultado D06 é: {dadoD06}')
        print(f'O total de turnos de espera para invocação LVL 1 é: {dadoD06}')
    elif magic_level == '2':
        dadoD06 = randint(1, 6)
        dadoD06res1 = dadoD06 + 2
        print(f'O Resultado D06 é: {dadoD06res1}')
        print(f'O total de turnos de espera para '
              'invocação LVL 2 é: {dadoD06res1}')
    else:
        dadoD06 = randint(1, 6)
        dadoD06res2 = dadoD06 + 5
        print(f'O Resultado D06 é : {dadoD06res2}')
        print(f'O total de turnos de espera para '
              'invocação LVL 3 é: {dadoD06res2}')
else:
    print('teste de dano')
    print('Para testar o quanto de dano que vai tomar o calculo  é: ')
    print('Dano - Defesa vs Difernças de rolagem')
    print(' Coloque o modificador do dados')
    modificador = int(input('modificador'))
    print(f' O modificador é de: {modificador}')
    rolagem_atacante1 = randint(0, 20)
    rolagem_atacante2 = randint(0, 20)
    print(f'Primera rolagem: {rolagem_atacante2},'
          'Segunda Rolagem: {rolagem_atacante1}')
    soma_rolagem_e_modificador = int(
        (modificador) + rolagem_atacante1 + rolagem_atacante2)
    print(f'Resultado de Rolagem {soma_rolagem_e_modificador}')
    modificador_adiversario = int(input('modificador_adiversario'))
    print(f' O modificador_adversario é de: {modificador_adiversario}')
    rolagem_atacante3 = randint(0, 20)
    rolagem_atacante4 = randint(0, 20)
    print(f'Primera rolagem: {rolagem_atacante3}, '
          'Segunda Rolagem: {rolagem_atacante4}')
    soma_rolagem_e_modificador_adversario = int((
        modificador_adiversario) + rolagem_atacante3 + rolagem_atacante4)
    print(f'Resultado de Rolagem {soma_rolagem_e_modificador_adversario}')
    dano_habilidade = int(input('DANO: '))
    resistencia_defesa = int(input('DEFESA: '))
    hp = int(input('HP: '))
    calculo_total_parcial_atacante = int(
        dano_habilidade * soma_rolagem_e_modificador/40)
    calculo_total_parcial_defensor = int(
        resistencia_defesa * soma_rolagem_e_modificador_adversario/40)
    calculo_final_fantasy = int(
        calculo_total_parcial_atacante - calculo_total_parcial_defensor)
    print(f'DANO TOTAL{calculo_final_fantasy}')
    calculo_de_hp_final_do_adversario = int(hp-calculo_final_fantasy)
    if calculo_de_hp_final_do_adversario >= 0:
        print('NAO DEU DANO NENHUM')
    else:
        print(f'TA AI O HP FINAL{calculo_de_hp_final_do_adversario}')