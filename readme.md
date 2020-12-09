# logo-if

Desenha a logo do Instituto Federal(IF) através do módulo *turtle* da linguagem *Python*. Eu comecei esse projeto como uma simples brincadeira, mas que logo acabou se tornando um ótimo desafio e eu diria que até uma homenagem pessoal para a instituição onde estudei. Meu maior desafio foi programar o desenho para ser flexível diante alguns tipos de modificações, tais como cores, dimensões, quantidade de quadrados, e etc.

## Como usar

1. Clone o repositório : `git clone https://github.com/gabr-01/logo-if.git`
2. Execute o arquivo *logo_if.py* e a logo padrão será automaticamente desenhada.
3. Para instruções de como customizar a logo, veja a seção de screenshots.

## Screenshots

A logo padrão desenhada.

![screenshot com a logo regular](imagens/screenshots/screenshot-logo-if-regular.png)

É possível alterar as cores facilmente, bastando modificar as variáveis *cor_borda_circulo*, *cor_fundo_circulo*, *cor_borda_quadrado* e *cor_fundo_quadrado* presentes no construtor da classe *LogoIF*. Você pode encontrar uma paleta com as strings das cores nesse link : https://trinket.io/docs/colors.

![screenshot com a logo de cor alterada](imagens/screenshots/screenshot-logo-if-cor-alterada.png)

Ainda no método construtor, é possível alterar a quantidade de quadrados em cada pilha, sendo necessário modificar as variáveis *numero_quadrados_primeira_pilha*, *numero_quadrados_segunda_pilha* e *numero_quadrados_terceira_pilha*. Além disso, é possível definir se eles devem ser intercalados ou não mudando o booleano nas variáveis *intercalar_quadrados_primeira_pilha* *intercalar_quadrados_segunda_pilha* e *intercalar_quadrados_terceira_pilha*

![screenshot com a logo de cor alterada](imagens/screenshots/screenshot-logo-if-forma-alterada.png)