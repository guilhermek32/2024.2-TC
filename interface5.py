import tkinter as tk
import math

# Lista de estados e tempos respectivos
estados = ["q0", "q1", "q2", "q3", "q4", "fim_loop"]
tempos = {"q0": 5000, "q1": 3000, "q2": 5000, "q3": 3000, "q4": 5000}
indice_estado = 0  # Índice do estado atual
running = True  # Variável para controlar a execução do loop

# Função que atualiza os semáforos conforme o estado clicado
def mudar_semaforo(estado):
    global running
    global indice_estado
    
    if estado == "q0":
        # Top: verde; Left e Right: vermelho; Pedestre: vermelho
        indice_estado = 0
        canvas_right.itemconfig(semaforo_top_green, fill="gray")
        canvas_right.itemconfig(semaforo_top_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_top_red, fill="red")
        canvas_right.itemconfig(semaforo_left_green, fill="green")
        canvas_right.itemconfig(semaforo_left_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_left_red, fill="gray")
        canvas_right.itemconfig(semaforo_right_green, fill="green")
        canvas_right.itemconfig(semaforo_right_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_right_red, fill="gray")
        canvas_right.itemconfig(semaforo_pedestre_red, fill="gray")
        canvas_right.itemconfig(semaforo_pedestre_green, fill="green")
    elif estado == "q1":
        # Right: verde; Top e Left: vermelho; Pedestre: vermelho
        indice_estado = 1
        canvas_right.itemconfig(semaforo_top_green, fill="gray")
        canvas_right.itemconfig(semaforo_top_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_top_red, fill="red")
        canvas_right.itemconfig(semaforo_left_green, fill="gray")
        canvas_right.itemconfig(semaforo_left_yellow, fill="yellow")
        canvas_right.itemconfig(semaforo_left_red, fill="gray")
        canvas_right.itemconfig(semaforo_right_green, fill="gray")
        canvas_right.itemconfig(semaforo_right_yellow, fill="yellow")
        canvas_right.itemconfig(semaforo_right_red, fill="gray")
        canvas_right.itemconfig(semaforo_pedestre_red, fill="gray")
        canvas_right.itemconfig(semaforo_pedestre_green, fill="green")
    elif estado == "q2":
        # Left: verde; Top e Right: vermelho; Pedestre: vermelho
        indice_estado = 2
        canvas_right.itemconfig(semaforo_top_green, fill="green")
        canvas_right.itemconfig(semaforo_top_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_top_red, fill="gray")
        canvas_right.itemconfig(semaforo_left_green, fill="gray")
        canvas_right.itemconfig(semaforo_left_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_left_red, fill="red")
        canvas_right.itemconfig(semaforo_right_green, fill="gray")
        canvas_right.itemconfig(semaforo_right_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_right_red, fill="red")
        canvas_right.itemconfig(semaforo_pedestre_red, fill="red")
        canvas_right.itemconfig(semaforo_pedestre_green, fill="gray")
    elif estado == 'q3':  # estado "q3"
        indice_estado = 3
        canvas_right.itemconfig(semaforo_top_green, fill="gray")
        canvas_right.itemconfig(semaforo_top_yellow, fill="yellow")
        canvas_right.itemconfig(semaforo_top_red, fill="gray")
        canvas_right.itemconfig(semaforo_left_green, fill="gray")
        canvas_right.itemconfig(semaforo_left_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_left_red, fill="red")
        canvas_right.itemconfig(semaforo_right_green, fill="gray")
        canvas_right.itemconfig(semaforo_right_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_right_red, fill="red")
        canvas_right.itemconfig(semaforo_pedestre_red, fill="red")
        canvas_right.itemconfig(semaforo_pedestre_green, fill="gray")
    elif estado == 'q4':
        indice_estado = 4
        canvas_right.itemconfig(semaforo_top_green, fill="gray")
        canvas_right.itemconfig(semaforo_top_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_top_red, fill="gray")
        canvas_right.itemconfig(semaforo_left_green, fill="gray")
        canvas_right.itemconfig(semaforo_left_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_left_red, fill="gray")
        canvas_right.itemconfig(semaforo_right_green, fill="gray")
        canvas_right.itemconfig(semaforo_right_yellow, fill="gray")
        canvas_right.itemconfig(semaforo_right_red, fill="gray")
        canvas_right.itemconfig(semaforo_pedestre_red, fill="gray")
        canvas_right.itemconfig(semaforo_pedestre_green, fill="gray")
    elif estado == 'fim_loop':
        if (running):
            indice_estado = 4
            running = False
            canvas_right.itemconfig(semaforo_top_green, fill="gray")
            canvas_right.itemconfig(semaforo_top_yellow, fill="gray")
            canvas_right.itemconfig(semaforo_top_red, fill="gray")
            canvas_right.itemconfig(semaforo_left_green, fill="gray")
            canvas_right.itemconfig(semaforo_left_yellow, fill="gray")
            canvas_right.itemconfig(semaforo_left_red, fill="gray")
            canvas_right.itemconfig(semaforo_right_green, fill="gray")
            canvas_right.itemconfig(semaforo_right_yellow, fill="gray")
            canvas_right.itemconfig(semaforo_right_red, fill="gray")
            canvas_right.itemconfig(semaforo_pedestre_red, fill="gray")
            canvas_right.itemconfig(semaforo_pedestre_green, fill="gray")
        else:
            running = True
            proximo_estado()
    
    desenhar_botao()
        

def proximo_estado():
    global indice_estado
    global running
    
    if not running:
        return;
    if estados[indice_estado] != "fim_loop":
        mudar_semaforo(estados[indice_estado])
        root.after(tempos[estados[indice_estado]], proximo_estado)
    else:
        root.after(0, proximo_estado)
    indice_estado = (indice_estado + 1) % len(estados)

# Função para lidar com o clique nos "botões" (círculos)
def clique_botao(event):
    x, y = event.x, event.y
    itens = canvas_left.find_overlapping(x, y, x, y)
    for item in itens:
        tags = canvas_left.gettags(item)
        for tag in tags:
            if tag in estados:
                mudar_semaforo(tag)
                return

# Função auxiliar para desenhar um semáforo com 3 luzes dentro de um retângulo
def criar_semaforo(x, y):
    raio = 20   # raio das "bolas"
    espacamento = 5
    margem = 5  # margem para o retângulo
    
    # Calcula as posições dos centros das luzes (dispostas verticalmente)
    centro_red = y
    centro_yellow = y + 2 * raio + espacamento
    centro_green = y + 4 * raio + 2 * espacamento

    # Coordenadas do retângulo (corpo do semáforo)
    x1_rect = x - raio - margem
    y1_rect = centro_red - raio - margem
    x2_rect = x + raio + margem
    y2_rect = centro_green + raio + margem
    canvas_right.create_rectangle(x1_rect, y1_rect, x2_rect, y2_rect, fill="dim gray", outline="black", width=2)
    
    # Desenha as luzes (círculos)
    red = canvas_right.create_oval(x - raio, centro_red - raio, x + raio, centro_red + raio, fill="red", outline="black", width=2)
    yellow = canvas_right.create_oval(x - raio, centro_yellow - raio, x + raio, centro_yellow + raio, fill="gray", outline="black", width=2)
    green = canvas_right.create_oval(x - raio, centro_green - raio, x + raio, centro_green + raio, fill="green", outline="black", width=2)
    return red, yellow, green


# Função auxiliar para desenhar um semáforo de pedestres com 2 luzes dentro de um retângulo
def criar_semaforo_pedestre(x, y):
    raio = 20   # raio das "bolas"
    espacamento = 5
    margem = 5  # margem para o retângulo
    
    # Calcula as posições dos centros das luzes (dispostas verticalmente)
    centro_red = y
    centro_green = y + 2 * raio + espacamento

    # Coordenadas do retângulo (corpo do semáforo)
    x1_rect = x - raio - margem
    y1_rect = centro_red - raio - margem
    x2_rect = x + raio + margem
    y2_rect = centro_green + raio + margem
    canvas_right.create_rectangle(x1_rect, y1_rect, x2_rect, y2_rect, fill="dim gray", outline="black", width=2)
    
    # Desenha as luzes (círculos)
    red = canvas_right.create_oval(x - raio, centro_red - raio, x + raio, centro_red + raio, fill="red", outline="black", width=2)
    green = canvas_right.create_oval(x - raio, centro_green - raio, x + raio, centro_green + raio, fill="gray", outline="black", width=2)
    return red, green

# Função para calcular os pontos de início e fim da linha, para que ela não ultrapasse os botões
def calcular_pontos_linha(x1, y1, x2, y2, raio):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.hypot(dx, dy)
    if dist == 0:
        return x1, y1, x2, y2
    # Calcula os pontos ajustados
    novo_x1 = x1 + (raio * dx / dist)
    novo_y1 = y1 + (raio * dy / dist)
    novo_x2 = x2 - (raio * dx / dist)
    novo_y2 = y2 - (raio * dy / dist)
    return novo_x1, novo_y1, novo_x2, novo_y2

# Criação da janela principal
root = tk.Tk()
root.title("Cruzamento com Semáforos e Sinais de Direção")

# Frames para layout
frame_left = tk.Frame(root)
frame_right = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=20, pady=20)
frame_right.pack(side=tk.RIGHT, padx=20, pady=20)

# Canvas da esquerda para os botões redondos e linhas conectando-os
canvas_left = tk.Canvas(frame_left, width=300, height=600, bg="white")
canvas_left.pack()

# Estados e suas posições para os botões
# Atualize as posições para incluir o Q4 e Q5
posicoes = {
    "q0": (75, 150),  # Coluna direita, topo
    "q1": (225, 150),  # Coluna esquerda, abaixo de q0
    "q2": (225, 350),   # Coluna direita, abaixo de q1
    "q3": (75, 350),  # Q4 no centro, onde estava o Q0
    "q4": (150, 250),   # Q5 no meio dos 4 botões
    "fim_loop": (100, 500)  # Q6 no meio dos 4 botões
}

# Ajustar o tamanho do botão
raio_botao = 30

# Redesenhar os botões com o novo layout
canvas_left.delete("all")  # Limpar o canvas anterior

# Função para desenhar linha com seta entre dois botões
def desenhar_linha_entre_botoes(estado1, estado2):
    x1, y1 = posicoes[estado1]
    x2, y2 = posicoes[estado2]
    novo_x1, novo_y1, novo_x2, novo_y2 = calcular_pontos_linha(x1, y1, x2, y2, raio_botao)
    canvas_left.create_line(novo_x1, novo_y1, novo_x2, novo_y2, fill="black", width=2,
                            dash=(4, 2), arrow=tk.LAST)

# Desenhar os botões com texto, incluindo ">" ao lado de q1 fora do botão
def desenhar_botao():
    canvas_left.delete("all") # Limpar o canvas anterior
    global indice_estado
    
    desenhar_linha_entre_botoes("q0", "q1")
    desenhar_linha_entre_botoes("q1", "q2")
    desenhar_linha_entre_botoes("q2", "q3")
    desenhar_linha_entre_botoes("q3", "q0")
    desenhar_linha_entre_botoes("q0", "q4")
    desenhar_linha_entre_botoes("q1", "q4")
    desenhar_linha_entre_botoes("q2", "q4")
    desenhar_linha_entre_botoes("q3", "q4")
    
    for estado in estados:
        x, y = posicoes[estado]
        color = "lightblue"
        if estado == estados[indice_estado]:
            color = "yellow"
        
        if estado == "fim_loop":
            canvas_left.create_rectangle(x, y, x + 100, y + 30, fill="lightgray", outline="black")
            canvas_left.create_text(x + 100 / 2, y + 30 / 2, text="MANUAL", font=("Arial", 12, "bold"), tags=estado)
        else:
            canvas_left.create_oval(x - raio_botao, y - raio_botao, x + raio_botao, y + raio_botao,
                                fill=color, outline="black", width=2, tags=estado)
            canvas_left.create_text(x, y, text=estado, font=("Arial", 12, "bold"), tags=estado)
        # Se o estado for "q1", adiciona o ">" fora do botão
        if estado == "q0":
            canvas_left.create_text(x - raio_botao - 8, y, text=">", font=("Arial", 20, "bold"), tags="seta_q1")
        # Se o estado for "q4", adicionar um círculo maior ao redor
        if estado == "q4":
            raio_maior = 25  # Raio maior para o círculo indicando o estado final
            canvas_left.create_oval(x - raio_maior, y - raio_maior, x + raio_maior, y + raio_maior,
                                fill="", outline="black", width=3, tags="circulo_q4")


desenhar_botao()

# Desenhar as linhas com setas entre os botões:
# Conexões originais:


canvas_left.bind("<Button-1>", clique_botao)

# Atualizar o cruzamento, semáforo e setas conforme necessário.
# (Não é necessário alterar essa parte, pois ela depende dos estados e não da nova posição dos botões)


# Canvas da direita para desenhar o cruzamento, semáforos e setas de direção
canvas_right = tk.Canvas(frame_right, width=600, height=600, bg="white")
canvas_right.pack()

# Desenha o cruzamento (formato de "+")
# Via vertical
canvas_right.create_rectangle(250, 0, 350, 600, fill="gray", outline="")
# Via horizontal
canvas_right.create_rectangle(0, 250, 600, 350, fill="gray", outline="")

# Adiciona setas indicando a direção das vias:
# Para a via horizontal (mão dupla): duas setas curtas, uma acima da outra,
# uma apontando para a direita e outra apontando para a esquerda.
canvas_right.create_line(80, 310, 110, 310, arrow=tk.LAST, width=3, fill="white")  # Seta apontando para a direita (embaixo)
canvas_right.create_line(80, 290, 110, 290, arrow=tk.FIRST, width=3, fill="white")  # Seta apontando para a esquerda (em cima)
canvas_right.create_line(490, 310, 520, 310, arrow=tk.LAST, width=3, fill="white")  # Seta apontando para a direita (embaixo)
canvas_right.create_line(490, 290, 520, 290, arrow=tk.FIRST, width=3, fill="white")  # Seta apontando para a esquerda (em cima)

# Para a via vertical (mão única, indo para cima): uma seta curta apontando para cima.
canvas_right.create_line(300, 500, 300, 470, arrow=tk.LAST, width=3, fill="white")
canvas_right.create_line(300, 100, 300, 70, arrow=tk.LAST, width=3, fill="white")

# Desenha os semáforos posicionados no cruzamento:
# - Top: acima do cruzamento (centro no topo)
# - Left: à esquerda do cruzamento (centro na esquerda)
# - Right: à direita do cruzamento (centro na direita)
semaforo_top_red, semaforo_top_yellow, semaforo_top_green = criar_semaforo(285, 150)
semaforo_left_red, semaforo_left_yellow, semaforo_left_green = criar_semaforo(150, 250)
semaforo_right_red, semaforo_right_yellow, semaforo_right_green = criar_semaforo(450, 250)
semaforo_pedestre_red, semaforo_pedestre_green = criar_semaforo_pedestre(210, 410)
proximo_estado()

# Inicia o loop da interface gráfica
root.mainloop()
