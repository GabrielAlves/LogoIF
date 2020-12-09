import turtle

import geometria

class LogoIF:
    def __init__(self, cursor):
        self.cursor = cursor

        self.comprimento_quadrado = 100
        self.cor_borda_quadrado = "green"
        self.cor_fundo_quadrado = "green"

        self.numero_quadrados_primeira_pilha = 3
        self.numero_quadrados_segunda_pilha = 4
        self.numero_quadrados_terceira_pilha = 2

        self.intercalar_quadrados_primeira_pilha = False
        self.intercalar_quadrados_segunda_pilha = False
        self.intercalar_quadrados_terceira_pilha = True

        self.raio_circulo = self.comprimento_quadrado / 2
        self.cor_borda_circulo = "red"
        self.cor_fundo_circulo = "red"
        
        self.distancia_entre_figuras = self.comprimento_quadrado / 10
        self.distancia_entre_inicio_pilhas = self.comprimento_quadrado + self.distancia_entre_figuras

        self.ponto_origem_desenho = (0, 0)

    def desenhar_logo(self):
        self.desenhar_circulo()
        self.desenhar_primeira_pilha_quadrados()
        self.desenhar_segunda_pilha_quadrados()
        self.desenhar_terceira_pilha_quadrados()

    def desenhar_circulo(self):
        geometria.desenhar_circulo(self.cursor, self.raio_circulo, self.cor_borda_circulo, self.cor_fundo_circulo)

    def desenhar_quadrado(self):
        geometria.desenhar_poligono(self.cursor, self.comprimento_quadrado, 4, self.cor_borda_quadrado, self.cor_fundo_quadrado)

    def desenhar_primeira_pilha_quadrados(self):
        self.levar_cursor_para_posicao_inicial_primeira_pilha_quadrados()
        self.desenhar_pilha_quadrados(self.numero_quadrados_primeira_pilha, self.intercalar_quadrados_primeira_pilha)

    def desenhar_segunda_pilha_quadrados(self):
        self.levar_cursor_para_posicao_inicial_segunda_pilha()
        self.desenhar_pilha_quadrados(self.numero_quadrados_segunda_pilha, self.intercalar_quadrados_segunda_pilha)

    def desenhar_terceira_pilha_quadrados(self):
        self.levar_cursor_para_posicao_inicial_terceira_pilha()
        self.desenhar_pilha_quadrados(self.numero_quadrados_terceira_pilha, self.intercalar_quadrados_terceira_pilha)

    def levar_cursor_para_posicao_inicial_primeira_pilha_quadrados(self):
        self.descer_ate_a_base_do_quadrado_inferior()
        self.mover_meio_comprimento_quadrado_para_esquerda()

    def mover_meio_comprimento_quadrado_para_esquerda(self):
        self.cursor.penup()
        self.cursor.right(180)
        self.cursor.forward(self.comprimento_quadrado / 2)
        self.cursor.left(180)
        self.cursor.pendown()

    def levar_cursor_para_posicao_inicial_segunda_pilha(self):
        self.cursor.penup()
        self.levar_cursor_para_posicao_x_inicial_segunda_pilha()
        self.levar_cursor_para_posicao_y_incial_segunda_pilha()
        self.cursor.pendown()

    def levar_cursor_para_posicao_x_inicial_segunda_pilha(self):
        self.cursor.forward(self.comprimento_quadrado + self.distancia_entre_figuras)

    def levar_cursor_para_posicao_y_incial_segunda_pilha(self):
        self.cursor.left(90)

        if self.numero_quadrados_primeira_pilha == 0:
            distancia_para_posicao_y_inicial = self.comprimento_quadrado + self.distancia_entre_figuras
        
        else:
            numero_espacos = self.numero_quadrados_primeira_pilha
            distancia_para_posicao_y_inicial = (self.numero_quadrados_primeira_pilha * self.comprimento_quadrado + numero_espacos * self.distancia_entre_figuras)

        self.cursor.forward(distancia_para_posicao_y_inicial)
        self.cursor.right(90)

    def levar_cursor_para_posicao_inicial_terceira_pilha(self):
        self.cursor.penup()
        self.levar_cursor_para_posicao_x_inicial_terceira_pilha()
        self.levar_cursor_para_posicao_y_incial_terceira_pilha()
        self.cursor.pendown()

    def levar_cursor_para_posicao_x_inicial_terceira_pilha(self):
        self.cursor.forward(self.comprimento_quadrado + self.distancia_entre_figuras)

    def levar_cursor_para_posicao_y_incial_terceira_pilha(self):
        self.cursor.left(90)

        if self.numero_quadrados_segunda_pilha == 0:
            distancia_para_posicao_y_inicial = 0

        else:
            numero_espacos = self.numero_quadrados_segunda_pilha
            distancia_para_posicao_y_inicial = ((self.numero_quadrados_segunda_pilha - 1) * self.comprimento_quadrado + (numero_espacos - 1) * self.distancia_entre_figuras)

        self.cursor.forward(distancia_para_posicao_y_inicial)
        self.cursor.right(90)
    
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

    def desenhar_pilha_quadrados(self, numero_quadrados, intercalar_quadrados = False):
        ultimo_quadrado = numero_quadrados - 1

        for quadrado_atual in range(numero_quadrados):
            self.desenhar_quadrado()
            
            if quadrado_atual != ultimo_quadrado:
                self.descer_ate_a_base_do_quadrado_inferior()

                if intercalar_quadrados:
                    self.descer_ate_a_base_do_quadrado_inferior()

if __name__ == "__main__":
    cursor = turtle.Turtle()
    cursor.shape("blank")
    cursor.speed(10)
    
    logo_if = LogoIF(cursor)
    logo_if.desenhar_logo()

    turtle.mainloop()