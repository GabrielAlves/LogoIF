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

        self.posicao_inicial_primeira_pilha_quadrados = (-50, -110)
        self.posicao_inicial_segunda_pilha_quadrados = (60, 0)
        self.posicao_inicial_terceira_pilha_quadrados = (170, 0)

    def desenhar_logo(self):
        self.desenhar_circulo_da_primeira_pilha()
        self.desenhar_primeira_pilha_quadrados()
        self.desenhar_segunda_pilha_quadrados()
        self.desenhar_terceira_pilha_quadrados()

    def desenhar_circulo_da_primeira_pilha(self):
        geometria.desenhar_circulo(self.cursor, self.raio_circulo, self.cor_borda_circulo, self.cor_fundo_circulo)

    def desenhar_primeira_pilha_quadrados(self):
        self.levar_cursor_para_posicao(self.posicao_inicial_primeira_pilha_quadrados)
        self.desenhar_pilha_quadrados(self.numero_quadrados_primeira_pilha, self.intercalar_quadrados_primeira_pilha)

    def desenhar_segunda_pilha_quadrados(self):
        self.levar_cursor_para_posicao(self.posicao_inicial_segunda_pilha_quadrados)
        self.desenhar_pilha_quadrados(self.numero_quadrados_segunda_pilha, self.intercalar_quadrados_segunda_pilha)

    def desenhar_terceira_pilha_quadrados(self):
        self.levar_cursor_para_posicao(self.posicao_inicial_terceira_pilha_quadrados)
        self.desenhar_pilha_quadrados(self.numero_quadrados_terceira_pilha, self.intercalar_quadrados_terceira_pilha)

    def levar_cursor_para_posicao(self, posicao):
        self.cursor.penup()
        self.cursor.setposition(posicao)
        self.cursor.pendown()

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
            geometria.desenhar_poligono(self.cursor, self.comprimento_quadrado, 4, self.cor_borda_quadrado, self.cor_fundo_quadrado)
            
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