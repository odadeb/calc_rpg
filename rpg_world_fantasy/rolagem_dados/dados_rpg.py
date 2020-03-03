class Dados_rpg():

    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self, titulo, randomizer):
        from random import randint
        # Atributos de cada objeto criado a partir desta classe. 
        # O self indica que estes são atributos dos objetos
        self.titulo= titulo
        self.randomazer = randint(1,6)
        print('DESCRICÃO:O D6 E UTILIZADO PARA CONJUGACAO'
              'DE FENTICOS DE INVOCACAO E MAGIAS ESPECIFICAS')