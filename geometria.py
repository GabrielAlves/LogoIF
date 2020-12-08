import math

def desenhar_polilinha(turtle, comprimento_lado, numero_lados, angulo, cor_borda, cor_fundo):
    turtle.pencolor(cor_borda)
    turtle.fillcolor(cor_fundo)
    turtle.begin_fill()

    for i in range(numero_lados):
        turtle.forward(comprimento_lado)
        turtle.left(angulo)

    turtle.end_fill()

def desenhar_poligono(turtle, comprimento_lado, numero_lados, cor_borda, cor_fundo):
    angulo = 360 / numero_lados
    desenhar_polilinha(turtle, comprimento_lado, numero_lados, angulo, cor_borda, cor_fundo)

def desenhar_arco(turtle, raio, angulo, cor_borda, cor_fundo):
    comprimento_arco = (math.pi * raio * angulo) / 180 
    numero_lados = int(comprimento_arco / 5) + 1 
    comprimento_lado = comprimento_arco / numero_lados 
    angulo_lado = angulo / numero_lados 
    desenhar_polilinha(turtle, comprimento_lado, numero_lados, angulo_lado, cor_borda, cor_fundo)

def desenhar_circulo(turtle, raio, cor_borda, cor_fundo):
    desenhar_arco(turtle, raio, 360, cor_borda, cor_fundo)