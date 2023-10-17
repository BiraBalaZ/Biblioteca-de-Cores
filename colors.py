# Text Style
st_none  = 0
st_bold  = 1
st_undr  = 4
st_ngtv  = 7

# Text Color
c_gray   = 30
c_red    = 31
c_green  = 32
c_yellow = 33
c_blue   = 34
c_purple = 35
c_cian   = 36
c_white  = 37

# Background Color
bg_gray   = 40
bg_red    = 41
bg_green  = 42
bg_yellow = 43
bg_blue   = 44
bg_purple = 45
bg_cian   = 46
bg_white  = 47

def color_ini(color, style = st_none, bg_color = bg_gray):
    '''
     --> Define a cor do texto deste ponto para baixo.
         Até que seja usada a função "color_end()" para
         descolorir os textos seguintes.
    
    :param style:    Estilo do Texto;
    :param color:    Cor principal do texto;
    :param bg_color: Cor do background;
    :return:         Sem retorno.
     ________________________________________
    |  Estilos  |    Cores    |     Fundo    |
    |-----------|-------------|--------------|
    |-> st_none | -> c_gray   | -> bg_gray   |
    |-> st_bold | -> c_red    | -> bg_red    |
    |-> st_undr | -> c_green  | -> bg_green  |
    |-> st_ngtv | -> c_yellow | -> bg_yellow |
    |           | -> c_blue   | -> bg_blue   |
    |           | -> c_purple | -> bg_purple |
    |           | -> c_cian   | -> bg_cian   |
    |           | -> c_white  | -> bg_white  |
    |___________|_____________|______________|
    //Function created by Erick Monteiro.
    '''
    print(f'\033[{style};{color};{bg_color}m')

def color_end():
    '''
     --> Finish color_ini()
    
    :return: Sem retorno.
    
    //Function created by Erick Monteiro.
    '''
    print('\033[m')

def colored_print(color, text, style = st_none, bg_color = bg_gray):
    '''
     --> Cria um Print colorido
    
    :param style:     Estilo do Texto;
    :param color:     Cor principal do texto;
    :param bg_color:  Cor de fundo do texto;
    :param text:      Texto;
    :return:          Sem retorno.
     ________________________________________
    |  Estilos  |    Cores    |     Fundo    |
    |-----------|-------------|--------------|
    |-> st_none | -> c_gray   | -> bg_gray   |
    |-> st_bold | -> c_red    | -> bg_red    |
    |-> st_undr | -> c_green  | -> bg_green  |
    |-> st_ngtv | -> c_yellow | -> bg_yellow |
    |           | -> c_blue   | -> bg_blue   |
    |           | -> c_purple | -> bg_purple |
    |           | -> c_cian   | -> bg_cian   |
    |           | -> c_white  | -> bg_white  |
    |___________|_____________|______________|
    //Function created by Erick Monteiro.
    '''
    print(f'\033[{style};{color};{bg_color}m{text}\033[m')