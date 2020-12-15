import turtle

import geometria

CURSOR_FORMA = "blank"
CURSOR_VELOCIDADE = 10

class LogoIF:
    def __init__(self, cursor):
        self.cursor = cursor

        self.comprimento_quadrado = 100
        self.cor_borda_quadrado = "green"
        self.cor_fundo_quadrado = "green"

        self.numero_quadrados_primeira_pilha = 3
        self.numero_quadrados_segunda_pilha = 4
        self.numero_quadrados_terceira_pilha = 3 # Na logo padrão, a terceira pilha tem virtualmente 3 quadrados(e não 2), pois o segundo deles não é desenhado, já que é pulado. 

        # A numeração abaixo dos quadrados a serem pulados inicia pelo número 1(não 0).
        # O 1 representa o primeiro quadrado da pilha, o 2 , o segundo, e etc.

        self.lista_quadrados_para_pular_da_primeira_pilha = []
        self.lista_quadrados_para_pular_da_segunda_pilha = []
        self.lista_quadrados_para_pular_da_terceira_pilha = [2]

        self.raio_circulo = self.comprimento_quadrado / 2
        self.cor_borda_circulo = "red"
        self.cor_fundo_circulo = "red"
        self.deve_desenhar_circulo = True
        
        self.distancia_entre_figuras = self.comprimento_quadrado / 10
        self.distancia_de_posicao_x_inicial_entre_pilhas = self.comprimento_quadrado + self.distancia_entre_figuras
        self.ponto_origem_desenho = (0, 0)


    def desenhar_logo(self):
        self.mover_cursor_ate_origem_desenho()
        self.desenhar_circulo()
        self.desenhar_primeira_pilha_quadrados()
        self.desenhar_segunda_pilha_quadrados()
        self.desenhar_terceira_pilha_quadrados()


    def desenhar_circulo(self):
        if self.deve_desenhar_circulo:
            geometria.desenhar_circulo(self.cursor, 
                self.raio_circulo, 
                self.cor_borda_circulo, 
                self.cor_fundo_circulo)


    def desenhar_quadrado(self):
        geometria.desenhar_poligono(self.cursor, 
            self.comprimento_quadrado, 
            4, 
            self.cor_borda_quadrado, 
            self.cor_fundo_quadrado)


    def mover_cursor_ate_origem_desenho(self):
        self.cursor.penup()
        self.cursor.setposition(self.ponto_origem_desenho)
        self.cursor.pendown()


    def desenhar_primeira_pilha_quadrados(self):
        self.levar_cursor_para_ponto_inicial_primeira_pilha_quadrados()
        self.desenhar_pilha_quadrados(self.numero_quadrados_primeira_pilha, self.lista_quadrados_para_pular_da_primeira_pilha)


    def desenhar_segunda_pilha_quadrados(self):
        self.levar_cursor_para_ponto_inicial_segunda_pilha()
        self.desenhar_pilha_quadrados(self.numero_quadrados_segunda_pilha, self.lista_quadrados_para_pular_da_segunda_pilha)


    def desenhar_terceira_pilha_quadrados(self):
        self.levar_cursor_para_ponto_inicial_terceira_pilha()
        self.desenhar_pilha_quadrados(self.numero_quadrados_terceira_pilha, self.lista_quadrados_para_pular_da_terceira_pilha)


    def levar_cursor_para_ponto_inicial_primeira_pilha_quadrados(self):
        self.descer_ate_a_base_do_quadrado_inferior()
        self.mover_meio_comprimento_quadrado_para_esquerda()


    def mover_meio_comprimento_quadrado_para_esquerda(self):
        self.cursor.penup()
        self.cursor.right(180)
        self.cursor.forward(self.comprimento_quadrado / 2)
        self.cursor.left(180)
        self.cursor.pendown()


    def levar_cursor_para_ponto_inicial_segunda_pilha(self):
        self.cursor.penup()
        self.levar_cursor_para_posicao_x_inicial_segunda_pilha()
        self.levar_cursor_para_posicao_y_incial_segunda_pilha()
        self.cursor.pendown()


    def levar_cursor_para_posicao_x_inicial_segunda_pilha(self):
        self.cursor.forward(self.distancia_de_posicao_x_inicial_entre_pilhas)


    def levar_cursor_para_posicao_y_incial_segunda_pilha(self):
        self.cursor.left(90)
        distancia_para_posicao_y_inicial = self.calcular_distancia_para_posicao_y_inicial_da_segunda_pilha()
        self.cursor.forward(distancia_para_posicao_y_inicial)
        self.cursor.right(90)

    def calcular_distancia_para_posicao_y_inicial_da_segunda_pilha(self):
        if self.numero_quadrados_primeira_pilha == 0:
            distancia_para_posicao_y_inicial = self.comprimento_quadrado + self.distancia_entre_figuras
        
        else:
            numero_espacos = self.numero_quadrados_primeira_pilha
            distancia_para_posicao_y_inicial = (self.numero_quadrados_primeira_pilha * self.comprimento_quadrado + numero_espacos * self.distancia_entre_figuras)

        return distancia_para_posicao_y_inicial

    def levar_cursor_para_ponto_inicial_terceira_pilha(self):
        self.cursor.penup()
        self.levar_cursor_para_posicao_x_inicial_terceira_pilha()
        self.levar_cursor_para_posicao_y_incial_terceira_pilha()
        self.cursor.pendown()


    def levar_cursor_para_posicao_x_inicial_terceira_pilha(self):
        self.cursor.forward(self.distancia_de_posicao_x_inicial_entre_pilhas)


    def levar_cursor_para_posicao_y_incial_terceira_pilha(self):
        self.cursor.left(90)
        distancia_para_posicao_y_inicial = self.calcular_distancia_para_posicao_y_inicial_da_terceira_pilha()
        self.cursor.forward(distancia_para_posicao_y_inicial)
        self.cursor.right(90)

    def calcular_distancia_para_posicao_y_inicial_da_terceira_pilha(self):
        if self.numero_quadrados_segunda_pilha == 0:
            distancia_para_posicao_y_inicial = 0

        else:
            numero_espacos = self.numero_quadrados_segunda_pilha
            distancia_para_posicao_y_inicial = ((self.numero_quadrados_segunda_pilha - 1) * self.comprimento_quadrado + (numero_espacos - 1) * self.distancia_entre_figuras)
    
        return distancia_para_posicao_y_inicial

    def descer_ate_a_base_do_quadrado_inferior(self):
        self.cursor.penup()
        self.descer_um_espaco()
        self.descer_um_quadrado()
        self.cursor.pendown()


    def descer_um_espaco(self):
        self.cursor.right(90)
        self.cursor.forward(self.distancia_entre_figuras)
        self.cursor.left(90)


    def descer_um_quadrado(self):
        self.cursor.right(90)
        self.cursor.forward(self.comprimento_quadrado)
        self.cursor.left(90)


    def desenhar_pilha_quadrados(self, numero_quadrados, lista_quadrados_para_pular):
        ultimo_quadrado = numero_quadrados

        for quadrado_atual in range(1 , numero_quadrados + 1):
            if quadrado_atual not in lista_quadrados_para_pular:
                self.desenhar_quadrado()
            
            if quadrado_atual != ultimo_quadrado:
                self.descer_ate_a_base_do_quadrado_inferior()


if __name__ == "__main__":
    cursor = turtle.Turtle()
    cursor.shape(CURSOR_FORMA)
    cursor.speed(CURSOR_VELOCIDADE)

    logo_if = LogoIF(cursor)
    logo_if.desenhar_logo()

    turtle.mainloop()