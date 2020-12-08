import turtle

import geometria

class LogoIF:
    def __init__(self):
        self.cursor = turtle.Turtle()
        self.configurar_cursor()
        
        self.comprimento_quadrado = 100
        self.cor_borda_quadrado = "green"
        self.cor_fundo_quadrado = "green"

        self.raio_circulo = self.comprimento_quadrado / 2
        self.cor_borda_circulo = "red"
        self.cor_fundo_circulo = "red"
        
        self.distancia_entre_figuras = self.comprimento_quadrado / 10

    def configurar_cursor(self):
        self.cursor.shape("blank")
        self.cursor.speed(10)

    def desenhar_logo(self):
        self.desenhar_circulo_da_primeira_pilha()
        self.desenhar_primeira_pilha_quadrados()
        self.desenhar_segunda_pilha_quadrados()
        self.desenhar_terceira_pilha_quadrados()

    def desenhar_circulo_da_primeira_pilha(self):
        geometria.desenhar_circulo(self.cursor, self.raio_circulo, self.cor_borda_circulo, self.cor_fundo_circulo)

    def desenhar_primeira_pilha_quadrados(self):
        self.posicionar_seta_na_base_da_primeira_pilha()
        self.desenhar_pilha_quadrados(3)

    def desenhar_segunda_pilha_quadrados(self):
        self.posicionar_seta_na_base_da_pilha_seguinte()
        self.desenhar_pilha_quadrados(4)

    def desenhar_terceira_pilha_quadrados(self):
        self.posicionar_seta_na_base_da_pilha_seguinte()
        self.desenhar_pilha_quadrados(2, True)

    def posicionar_seta_na_base_da_primeira_pilha(self):
        self.descer_ate_a_base_do_quadrado_inferior()
        self.ir_do_ponto_medio_da_base_ate_o_canto_inferior_esquerdo_quadrado()

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

    def ir_do_ponto_medio_da_base_ate_o_canto_inferior_esquerdo_quadrado(self):
        self.cursor.penup()
        self.cursor.right(180)
        self.cursor.forward(self.comprimento_quadrado / 2)
        self.cursor.left(180)
        self.cursor.pendown()

    def posicionar_seta_na_base_da_pilha_seguinte(self):
        self.cursor.penup()
        self.cursor.forward(self.comprimento_quadrado + self.distancia_entre_figuras)
        self.cursor.left(90)
        self.cursor.forward(3 * self.comprimento_quadrado + 3 * self.distancia_entre_figuras)
        self.cursor.right(90)
        self.cursor.pendown()

    def desenhar_pilha_quadrados(self, numero_quadrados, intercalar_quadrados = False):
        for i in range(numero_quadrados):
            geometria.desenhar_poligono(self.cursor, self.comprimento_quadrado, 4, self.cor_borda_quadrado, self.cor_fundo_quadrado)
            
            if i != numero_quadrados - 1:
                self.descer_ate_a_base_do_quadrado_inferior()

                if intercalar_quadrados:
                    self.descer_ate_a_base_do_quadrado_inferior()

if __name__ == "__main__":
    logo_if = LogoIF()
    logo_if.desenhar_logo()

    turtle.mainloop()