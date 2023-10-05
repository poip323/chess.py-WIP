#problem: 
# vars

# boards
white_board = '''
 ...###...###...###...###
8.a8.#b8#.c8.#d8#.e8.#f8#.g8.#h8#
 ...###...###...###...###
 ###...###...###...###...
7#a7#.b7.#c7#.d7.#e7#.f7.#g7#.h7.
 ###...###...###...###...
 ...###...###...###...###
6.a6.#b6#.c6.#d6#.e6.#f6#.g6.#h6#
 ...###...###...###...###
 ###...###...###...###...
5#a5#.b5.#c5#.d5.#e5#.f5.#g5#.h5.
 ###...###...###...###...
 ...###...###...###...###
4.a4.#b4#.c4.#d4#.e4.#f4#.g4.#h4#
 ...###...###...###...###
 ###...###...###...###...
3#a3#.b3.#c3#.d3.#e3#.f3.#g3#.h3.
 ###...###...###...###...
 ...###...###...###...###
2.a2.#b2#.c2.#d2#.e2.#f2#.g2.#h2#
 ...###...###...###...###
 ###...###...###...###...
1#a1#.b1.#c1#.d1.#e1#.f1.#g1#.h1.
 ###...###...###...###...
  a  b  c  d  e  f  g  h'''
#^
#|
#x
# Y-->

black_board = '''
 ...###...###...###...###
1.h1.#g1#.f1.#e1#.d1.#c1#.b1.#a1#
 ...###...###...###...###
 ###...###...###...###...
2#h2#.g2.#f2#.e2.#d2#.c2.#b2#.a2.
 ###...###...###...###...
 ...###...###...###...###
3.h3.#g3#.f3.#e3#.d3.#c3#.b3.#a3#
 ...###...###...###...###
 ###...###...###...###...
4#h4#.g4.#f4#.e4.#d4#.c4.#b4#.a4.
 ###...###...###...###...
 ...###...###...###...###
5.h5.#g5#.f5.#e5#.d5.#c5#.b5.#a5#
 ...###...###...###...###
 ###...###...###...###...
6#h6#.g6.#f6#.e6.#d6#.c6.#b6#.a6.
 ###...###...###...###...
 ...###...###...###...###
7.h7.#g7#.f7.#e7#.d7.#c7#.b7.#a7#
 ...###...###...###...###
 ###...###...###...###...
8#h8#.g8.#f8#.e8.#d8#.c8.#b8#.a8.
 ###...###...###...###...
 h  g  f  e  d  c  b  a'''

# white vars

king_w = [True, 1, 5, 'white']

queen_w = [True, 1, 4, 'white']

bishop0_w = [True, 1, 3, 'white']
bishop1_w = [True, 1, 6, 'white']

knight0_w = [True, 1, 2, 'white']
knight1_w = [True, 1, 7, 'white']

rook0_w = [True, 1, 1, 'white']
rook1_w = [True, 1, 8, 'white']

pawn0_w = [True, 2, 1, True, '', True, 'white']
pawn2_w = [True, 2, 2, True, '', True, 'white']
pawn3_w = [True, 2, 3, True, '', True, 'white']
pawn4_w = [True, 2, 4, True, '', True, 'white']
pawn5_w = [True, 2, 5, True, '', True, 'white']
pawn6_w = [True, 2, 6, True, '', True, 'white']
pawn7_w = [True, 2, 7, True, '', True, 'white']
pawn8_w = [True, 2, 8, True, '', True, 'white']

# global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn1_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w
# black vars

king_b = [True, 8, 5, 'black']

queen_b = [True, 8, 4, 'black']

bishop0_b = [True, 8, 3, 'black']
bishop1_b = [True, 8, 7, 'black']

knight0_b = [True, 8, 2, 'black']
knight1_b = [True, 8, 7, 'black']

rook0_b = [True, 8, 1, 'black']
rook1_b = [True, 8, 8, 'black']

pawn0_b = [True, 7, 1, True, '', True, 'black']
pawn2_b = [True, 7, 2, True, '', True, 'black']
pawn3_b = [True, 7, 3, True, '', True, 'black']
pawn4_b = [True, 7, 4, True, '', True, 'black']
pawn5_b = [True, 7, 5, True, '', True, 'black']
pawn6_b = [True, 7, 6, True, '', True, 'black']
pawn7_b = [True, 7, 7, True, '', True, 'black']
pawn8_b = [True, 7, 8, True, '', True, 'black']

#    global pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
#    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w
#    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b

# pieces index

piece_index = [king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_w, king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b]
piece_index_str = ['king', 'queen', 'bishop', 'bishop', 'knight', 'knight', 'rook', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'king', 'queen', 'bishop', 'bishop', 'knight', 'knight', 'rook', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

# white

white_piece_index = [king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w]
white_piece_index_str = ['king_w', 'queen_w', 'bishop0_w', 'bishop1_w', 'knight0_w', 'knight1_w', 'rook0_w', 'rook1_w', 'pawn0_w', 'pawn3_w', 'pawn4_w', 'pawn5_w', 'pawn6_w', 'pawn7_w', 'pawn8_w']

# black

black_piece_index = [king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b]
black_piece_index_str = ['king_b', 'queen_b', 'bishop0_b', 'bishop1_b', 'knight0_b', 'knight1_b', 'rook0_b', 'rook1_b', 'pawn0_b', 'pawn3_b', 'pawn4_b', 'pawn5_b', 'pawn6_b', 'pawn7_b']

# pawns

# white

white_pawn_index = [pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_w]
white_pawn_index_str  = ['pawn0_w', 'pawn2_w,' 'pawn3_w', 'pawn4_w', 'pawn5_w', 'pawn6_w', 'pawn7_w', 'pawn8_w']

# black

black_pawn_index = [pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_w]
black_pawn_index_str = ['pawn0_b', 'pawn2_b', 'pawn3_b', 'pawn4_b', 'pawn5_b', 'pawn6_b', 'pawn7_b', 'pawn8_w']

# moves

# general moves

moves_king = [[1, 0], [0, 1], [1, 1], [-1, 1], [-1, 0], [0, -1], [-1, -1], [1, -1]]

moves_queen = [
[8, 0], [-8, 0], [0, 8], [0, -8], [8 ,8], [-8, 8], [8, -8], [-8, -8], 
[7, 0], [-7, 0], [0, 7], [0, -7], [7 ,7], [-7, 7], [7, -7], [-7, -7], 
[6, 0], [-6, 0], [0, 6], [0, -6], [6 ,6], [-6, 6], [6, -6], [-6, -6], 
[5, 0], [-5, 0], [0, 5], [0, -5], [5 ,5], [-5, 5], [5, -5], [-5, -5], 
[4, 0], [-4, 0], [0, 4], [0, -4], [4 ,4], [-4, 4], [4, -4], [-4, -4], 
[3, 0], [-3, 0], [0, 3], [0, -3], [3 ,3], [-3, 3], [3, -3], [-3, -3], 
[2, 0], [-2, 0], [0, 2], [0, -2], [2 ,2], [-2, 2], [2, -2], [-2, -2], 
[1, 0], [-1, 0], [0, 1], [0, -1], [1 ,1], [-1, 1], [1, -1], [-1, -1]]

moves_bishop = [
[8, 0], [0, 8], [8, 8], [-8, 0], [0, -8], [-8, -8], 
[7, 0], [0, 7], [7, 7], [-7, 0], [0, -7], [-7, -7], 
[6, 0], [0, 6], [6, 6], [-6, 0], [0, -6], [-6, -6], 
[5, 0], [0, 5], [8, 5], [-5, 0], [0, -5], [-5, -5], 
[4, 0], [0, 4], [4, 4], [-4, 0], [0, -4], [-4, -4], 
[3, 0], [0, 3], [3, 3], [-3, 0], [0, -3], [-3, -3], 
[2, 0], [0, 2], [2, 2], [-2, 0], [0, -2], [-2, -2], 
[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1]]

moves_knight = [
[3, 1], [1, 3], 
[-3, 1], [-1, 3], 
[3, -1], [1, -3], 
[-3, -1], [-1, -3]]

moves_rook = [
[8, 0], [0, 8], [-8, 0], [0, -8], 
[7, 0], [0, 7], [-7, 0], [0, -7], 
[6, 0], [0, 6], [-6, 0], [0, -6], 
[5, 0], [0, 5], [-5, 0], [0, -5], 
[4, 0], [0, 4], [-4, 0], [0, -4], 
[3, 0], [0, 3], [-3, 0], [0, -3], 
[2, 0], [0, 2], [-2, 0], [0, -2], 
[1, 0], [0, 1], [-1, 0], [0, -1]]

# white moves

w_moves_pawn = [[1, 0]]
w_moves_x_pawn = [[1, 1], [1, -1]]
w_moves_special_pawn = [[2, 0]]

# black moves

b_moves_pawn = [[-1, 0]]
b_moves_x_pawn = [[-1, 1], [-1, -1]]
b_moves_special_pawn = [[-2, 0]]
# general vars

cleanup = True
virgin_index = ['isaac calrk']
white_specal_char = ['\033[48;5;240mK\033[0m', '\033[48;5;240mQ\033[0m', '\033[48;5;240mR\033[0m', '\033[48;5;240mN\033[0m', '\033[48;5;240mB\033[0m', '\033[48;5;240mP\033[0m']
white_specal_char_id = ['wK', 'wQ', 'wR', 'wN', 'wB', 'wP']
pawn_promotions = [moves_queen, moves_rook, moves_bishop, moves_knight]
pawn_promotions_str = ['queen', 'rook', 'bishop', 'knight']
DEBUG = False
DEBUGG = False
out_of_bounds = False
players_2 = False
black_playing = False
white_playing = True
black_score = 0
white_score = 0
board_out = ''
counter = 0
board_spots = [
'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 
'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 
'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 
'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 
'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 
'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',  
'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 
'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

# moves layout:
# [[move1] ,[move2]...]
# data layout:
# [alive, pos_x, pos_y]
# pawns:
# [alive, pos_x, pos_y, promoted, promotion_state, special_move]
#    0      1      2       3            4              5
# [True, 7, 8, True, '', True]
#   0    1  2   3    4    5

# functions

# general functions

def make_it_magical(text, coulor, effect='reset', back_for='foreground'):
    effects = ['reset', 'bold', 'bright', 'underline', 'inverse', 'bright off', 'underline off', 'inverse off']
    effects_num = [0, 1, 1, 4, 7, 21, 21, 24, 27]
    coulors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'grey']
    back_coulors_id = [40, 41, 42, 43, 44, 45, 46, 47, 250]
    for_coulors_id = [30, 31, 32, 33, 34, 35, 36, 37, 250]
    counter = 0
    counter = 0
    for x in effects:
        if effect == x:
            effect = str(effects_num[counter])
        counter += 1
    counter = 0
    if back_for == 'background':
        for x in coulors:
            if x == coulor:
                coulor = str(back_coulors_id[counter])
            counter += 1
        counter = 0
    elif back_for == 'foreground': 
        for x in coulors:
            if x == coulor:
                coulor = str(for_coulors_id[counter])
            counter += 1
        counter = 0
    return '\033['+effect+';'+coulor+'m'+str(text)+'\033[0m'

def xy_to_algebreic(piece_x, piece_y):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
    global out_of_bounds
    out_of_bounds = False
    piece_x = str(piece_x)
    if piece_y == 1:
        piece_yy = 'a'
    if piece_y == 2:
        piece_yy = 'b'
    if piece_y == 3:
        piece_yy = 'c'
    if piece_y == 4:
        piece_yy = 'd'
    if piece_y == 5:
        piece_yy = 'e'
    if piece_y == 6:
        piece_yy = 'f'
    if piece_y == 7:
        piece_yy = 'g'
    if piece_y == 8:
        piece_yy = 'h'
    if int(piece_x) > 8 or piece_y > 8:
        out_of_bounds = True
    return piece_yy+piece_x

def check_spot_player(spot):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
    global counter
    counter = 0
    # for each piece in piece index
    # cycle all of its vars
    # see if the cycled var is black/white
    # and see if ots pos dat is the spot
    # and check if the piece is alive or not
    for x in piece_index:
        if x[0] == True:
            for y in x:
                if y == 'black' and xy_to_algebreic(x[1], x[2]) == spot:
                    if DEBUGG == True:
                        return xy_to_algebreic(x[1], x[2])+' is white'
                    return 'black'
                elif y == 'white' and xy_to_algebreic(x[1], x[2]) == spot:
                    if DEBUGG == True:
                        return xy_to_algebreic(x[1], x[2])+' is black'
                    return 'white'
    if DEBUGG == True:
        return spot+' has no pieces'
    return 'open'

def algebraic_to_xy(alg):
    alg = alg.replace('h', '8 ')
    alg = alg.replace('g', '7 ')
    alg = alg.replace('f', '6 ')
    alg = alg.replace('e', '5 ')
    alg = alg.replace('d', '4 ')
    alg = alg.replace('c', '3 ')
    alg = alg.replace('b', '2 ')
    alg = alg.replace('a', '1 ')
    
    return alg.split(' ')

def pawn_promotion_edit(piece_var, promotion_state, promoted):
    global pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
    if piece_var == 'pawn0_w':
        pawn0_w[3] = promoted
        pawn0_w[4] = promotion_state
    if piece_var == 'pawn2_w':
        pawn2_w[3] = promoted
        pawn2_w[4] = promotion_state
    if piece_var == 'pawn3_w':
        pawn3_w[3] = promoted
        pawn3_w[4] = promotion_state
    if piece_var == 'pawn4_w':
        pawn4_w[3] = promoted
        pawn4_w[4] = promotion_state
    if piece_var == 'pawn5_w':
        pawn5_w[3] = promoted
        pawn5_w[4] = promotion_state
    if piece_var == 'pawn6_w':
        pawn6_w[3] = promoted
        pawn6_w[4] = promotion_state
    if piece_var == 'pawn7_w':
        pawn7_w[3] = promoted
        pawn7_w[4] = promotion_state
    if piece_var == 'pawn8_w':
        pawn8_w[3] = promoted
        pawn8_w[4] = promotion_state
    if piece_var == 'pawn0_b':
        pawn0_b[3] = promoted
        pawn0_b[4] = promotion_state
    if piece_var == 'pawn2_b':
        pawn2_b[3] = promoted
        pawn2_b[4] = promotion_state
    if piece_var == 'pawn3_b':
        pawn3_b[3] = promoted
        pawn3_b[4] = promotion_state
    if piece_var == 'pawn4_b':
        pawn4_b[3] = promoted
        pawn4_b[4] = promotion_state
    if piece_var == 'pawn5_b':
        pawn5_b[3] = promoted
        pawn5_b[4] = promotion_state
    if piece_var == 'pawn6_b':
        pawn6_b[3] = promoted
        pawn6_b[4] = promotion_state
    if piece_var == 'pawn7_b':
        pawn7_b[3] = promoted
        pawn7_b[4] = promotion_state
    if piece_var == 'pawn8_b':
        pawn8_b[3] = promoted
        pawn8_b[4] = promotion_state

def pawn_special_edit(piece_var, special_state):
    global pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
    if piece_var == 'pawn0_w':
        pawn0_w[5] = special_state
    if piece_var == 'pawn2_w':
        pawn2_w[5] = special_state
    if piece_var == 'pawn3_w':
        pawn3_w[5] = special_state
    if piece_var == 'pawn4_w':
        pawn4_w[5] = special_state
    if piece_var == 'pawn5_w':
        pawn5_w[5] = special_state
    if piece_var == 'pawn6_w':
        pawn6_w[5] = special_state
    if piece_var == 'pawn7_w':
        pawn7_w[5] = special_state
    if piece_var == 'pawn8_w':
        pawn8_w[5] = special_state
    if piece_var == 'pawn0_b':
        pawn0_b[5] = special_state
    if piece_var == 'pawn2_b':
        pawn2_b[5] = special_state
    if piece_var == 'pawn3_b':
        pawn3_b[5] = special_state
    if piece_var == 'pawn4_b':
        pawn4_b[5] = special_state
    if piece_var == 'pawn5_b':
        pawn5_b[5] = special_state
    if piece_var == 'pawn6_b':
        pawn6_b[5] = special_state
    if piece_var == 'pawn7_b':
        pawn7_b[5] = special_state
    if piece_var == 'pawn8_b':
        pawn8_b[5] = special_state

def spot_piece(spot, styalised=False):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
    global counter, out
    out = ''
    counter = 0
    # cycle through piece index
    # if the piece that we cycle is in the spot we are looking for we remove extra bits and return it
    for x in piece_index:
        if xy_to_algebreic(x[1], x[2]) == spot:
            out = piece_index_str[counter]
            out = out.replace('0', '')
            out = out.replace('1', '')
            out = out.replace('2', '')
            out = out.replace('3', '')
            out = out.replace('4', '')
            out = out.replace('5', '')
            out = out.replace('6', '')
            out = out.replace('7', '')
            out = out.replace('8', '')
            out = out.replace('_w', '')
            out = out.replace('_b', '')
            if styalised == True:
                out = out.replace('king', 'K')
                out = out.replace('queen', 'Q')
                out = out.replace('pawn', 'P')
                out = out.replace('knight', 'N')
                out = out.replace('rook', 'R')
                out = out.replace('bishop', 'B')
            if DEBUG == True:
                print('out: '+out)
                print('piece spot: '+xy_to_algebreic(x[1], x[2]))
            return out
        else:
            # if DEBUG == True:
            #    print('out: '+out)
            #    print('piece spot: '+xy_to_algebreic(x[1], x[2]))
            counter += 1
    return 'open'

def genorate_board():
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
    if white_playing == True:
        board_out = white_board
        # for each spot on board we replace it with the player and th piece
        # then replace that with its coressponding assci colorised character
        for x in board_spots:
            spot_player = check_spot_player(x)
            spot_the_piece = spot_piece(x, True)
            if spot_player == 'white':
                spot_player = 'w'
            elif spot_player == 'black':
                spot_player = 'tBt'
            else: 
                spot_player = ''
            board_out = board_out.replace(x, spot_player+spot_the_piece)
        if cleanup == True:
            board_out = board_out.replace(white_specal_char_id[0], white_specal_char[0])
            board_out = board_out.replace(white_specal_char_id[1], white_specal_char[1])
            board_out = board_out.replace(white_specal_char_id[2], white_specal_char[2])
            board_out = board_out.replace(white_specal_char_id[3], white_specal_char[3])
            board_out = board_out.replace(white_specal_char_id[4], white_specal_char[4])
            board_out = board_out.replace(white_specal_char_id[5], white_specal_char[5])
            board_out = board_out.replace('open', ' ')
            board_out = board_out.replace('tBt', '')
        return board_out   

print(genorate_board())

def check_spot(spot):
    global out_of_bounds
    out = ''
    if out_of_bounds == True:
        return 'taken'
    for x in piece_index:
        if x[0] == True:
            if xy_to_algebreic(x[1], x[2]) == spot:
                return 'taken'
    return 'open'

def change_state(piece_var, state):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b
    if piece_var == 'king_w':
        king_w[0] = state
    if piece_var == 'queen_w':
        queen_w[0] = state
    if piece_var == 'bishop0_w':
        bishop0_w[0] = state
    if piece_var == 'bishop1_w':
        bishop1_w[0] = state
    if piece_var == 'knight0_w':
        knight0_w[0] = state
    if piece_var == 'knight1_w':
        knight1_w[0] = state
    if piece_var == 'rook0_w':
        rook0_w[0] = state
    if piece_var == 'rook1_w':
        rook1_w[0] = state
    if piece_var == 'pawn0_w':
        pawn0_w[0] = state
    if piece_var == 'pawn2_w':
        pawn2_w[0] = state
    if piece_var == 'pawn3_w':
        pawn3_w[0] = state
    if piece_var == 'pawn4_w':
        pawn4_w[0] = state
    if piece_var == 'pawn5_w':
        pawn5_w[0] = state
    if piece_var == 'pawn6_w':
        pawn6_w[0] = state
    if piece_var == 'pawn7_w':
        pawn7_w[0] = state
    if piece_var == 'pawn8_w':
        pawn8_w[0] = state
    if piece_var == 'king_b':
        king_b[0] = state
    if piece_var == 'queen_b':
        queen_b[0] = state
    if piece_var == 'bishop0_b':
        bishop0_b[0] = state
    if piece_var == 'bishop1_b':
        bishop1_b[0] = state
    if piece_var == 'knight0_b':
        knight0_b[0] = state
    if piece_var == 'knight1_b':
        knight1_b[0] = state
    if piece_var == 'rook0_b':
        rook0_b[0] = state
    if piece_var == 'rook1_b':
        rook1_b[0] = state
    if piece_var == 'pawn0_b':
        pawn0_b[0] = state
    if piece_var == 'pawn2_b':
        pawn2_b[0] = state
    if piece_var == 'pawn3_b':
        pawn3_b[0] = state
    if piece_var == 'pawn4_b':
        pawn4_b[0] = state
    if piece_var == 'pawn5_b':
        pawn5_b[0] = state
    if piece_var == 'pawn6_b':
        pawn6_b[0] = state
    if piece_var == 'pawn7_b':
        pawn7_b[0] = state
    if piece_var == 'pawn8_b':
        pawn8_b[0] = state

def modify_piece_dat(piece_var, target_x, target_y):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_b
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b
    if piece_var == 'king_w':
        king_w[1] = target_x
        king_w[2] = target_y
        return 'done'
    if piece_var == 'queen_w':
        queen_w[1] = target_x
        queen_w[2] = target_y
        return 'done'
    if piece_var == 'bishop0_w':
        bishop0_w[1] = target_x
        bishop0_w[2] = target_y
        return 'done'
    if piece_var == 'bishop1_w':
        bishop1_w[1] = target_x
        bishop1_w[2] = target_y
        return 'done'
    if piece_var == 'knight0_w':
        knight0_w[1] = target_x
        knight0_w[2] = target_y
        return 'done'
    if piece_var == 'knight1_w':
        knight1_w[1] = target_x
        knight1_w[2] = target_y
        return 'done'
    if piece_var == 'rook0_w':
        rook0_w[1] = target_x
        rook0_w[2] = target_y
        return 'done'
    if piece_var == 'rook1_w':
        rook1_w[1] = target_x
        rook1_w[2] = target_y
        return 'done'
    if piece_var == 'pawn0_w':
        pawn0_w[1] = target_x
        pawn0_w[2] = target_y
        return 'done'
    if piece_var == 'pawn2_w':
        pawn2_w[1] = target_x
        pawn2_w[2] = target_y
        return 'done'
    if piece_var == 'pawn3_w':
        pawn3_w[1] = target_x
        pawn3_w[2] = target_y
        return 'done'
    if piece_var == 'pawn4_w':
        pawn4_w[1] = target_x
        pawn4_w[2] = target_y
        return 'done'
    if piece_var == 'pawn5_w':
        pawn5_w[1] = target_x
        pawn5_w[2] = target_y
        return 'done'
    if piece_var == 'pawn6_w':
        pawn6_w[1] = target_x
        pawn6_w[2] = target_y
        return 'done'
    if piece_var == 'pawn7_w':
        pawn7_w[1] = target_x
        pawn7_w[2] = target_y
        return 'done'
    if piece_var == 'pawn8_w':
        pawn8_w[1] = target_x
        pawn8_w[2] = target_y
        return 'done'
    if piece_var == 'king_b':
        king_b[1] = target_x
        king_b[2] = target_y
        return 'done'
    if piece_var == 'queen_b':
        queen_b[1] = target_x
        queen_b[2] = target_y
        return 'done'
    if piece_var == 'bishop0_b':
        bishop0_b[1] = target_x
        bishop0_b[2] = target_y
        return 'done'
    if piece_var == 'bishop1_b':
        bishop1_b[1] = target_x
        bishop1_b[2] = target_y
        return 'done'
    if piece_var == 'knight0_b':
        knight0_b[1] = target_x
        knight0_b[2] = target_y
        return 'done'
    if piece_var == 'knight1_b':
        knight1_b[1] = target_x
        knight1_b[2] = target_y
        return 'done'
    if piece_var == 'rook0_b':
        rook0_b[1] = target_x
        rook0_b[2] = target_y
        return 'done'
    if piece_var == 'rook1_b':
        rook1_b[1] = target_x
        rook1_b[2] = target_y
        return 'done'
    if piece_var == 'pawn0_b':
        pawn0_b[1] = target_x
        pawn0_b[2] = target_y
        return 'done'
    if piece_var == 'pawn2_b':
        pawn2_b[1] = target_x
        pawn2_b[2] = target_y
        return 'done'
        return 'done'
    if piece_var == 'pawn3_b':
        pawn3_b[1] = target_x
        pawn3_b[2] = target_y
        return 'done'
    if piece_var == 'pawn4_b':
        pawn4_b[1] = target_x
        pawn4_b[2] = target_y
        return 'done'
    if piece_var == 'pawn5_b':
        pawn5_b[1] = target_x
        pawn5_b[2] = target_y
        return 'done'
    if piece_var == 'pawn6_b':
        pawn6_b[1] = target_x
        pawn6_b[2] = target_y
        return 'done'
    if piece_var == 'pawn7_b':
        pawn7_b[1] = target_x
        pawn7_b[2] = target_y
        return 'done'
    if piece_var == 'pawn8_b':
        pawn8_b[1] = target_x
        pawn8_b[2] = target_y
        return 'done'
    else: 
        return 'cant move piece: '+piece_var

def observe_spot(spot):
    global out_of_bounds
    counter = 0
    if out_of_bounds == True:
        return 'Ob'
    for x in piece_index:
        if x[0] == True:
            if xy_to_algebreic(x[1], x[2]) == spot:
                return piece_index_str[counter]
        counter += 1
    return 'open'

def take_spot(spot):
    if observe_spot(spot) != 'Ob':
        change_state(observe_spot(spot), False)

def check_xy(xx, yy):
    return check_spot(xy_to_algebreic(xx, yy))

# pawns:
# [alive, pos_x, pos_y, promoted, promotion_state, special_move]
#    0      1      2       3            4              5
# [True, 7, 8, True, '', True]
#   0    1  2   3    4    5

# complete 
def pawn_moves(player, dest_x, dest_y):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_b
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b
    global counter
    counter = 0
    if player == 'black':
        for x in black_pawn_index:
            out = dest_x == x[1]-1 and dest_y == x[2] and x[0] == True and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]-1, x[2])) != 'Ob'
            if dest_x == x[1]-1 and dest_y == x[2] and x[0] == True and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]-1, x[2])) != 'Ob':
                print(modify_piece_dat(str(black_pawn_index_str[counter]), x[1]-1, x[2]))
                pawn_special_edit(str(black_pawn_index_str[counter]), False)
                if DEBUG == True:
                    print()
                    print('wanted x:'+str(dest_x))
                    print('wanted y:'+str(dest_y))
                    print('pawn x:'+str(x[1]))
                    print('pawn y:'+str(x[2]))
                    print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                    print('predicted x:'+str(x[1]-1))
                    print('predicted y:'+str(x[2]))
                    print('destination: '+xy_to_algebreic(dest_x, dest_y))
                    print('algebreic: '+xy_to_algebreic(x[1]-1, x[2]))
                    print('alive: '+str(x[0]))
                    print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                    print('predictded destination check: '+xy_to_algebreic(x[1]-1, x[2]))
                    print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]-1, x[2])))
                    print('move check return: '+str(out))
                return 'moved'
            elif DEBUG == True:
                print()
                print('wanted x:'+str(dest_x))
                print('wanted y:'+str(dest_y))
                print('pawn x:'+str(x[1]))
                print('pawn y:'+str(x[2]))
                print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                print('predicted x:'+str(x[1]-1))
                print('predicted y:'+str(x[2]))
                print('destination: '+xy_to_algebreic(dest_x, dest_y))
                print('algebreic: '+xy_to_algebreic(x[1]-1, x[2]))
                print('alive: '+str(x[0]))
                print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                print('predictded destination check: '+xy_to_algebreic(x[1]-1, x[2]))
                print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]-1, x[2])))
                print('move check return: '+str(out))
            counter += 1
    if player == 'white':
        for x in white_pawn_index:
            out = dest_x == x[1]-1 and dest_y == x[2] and x[0] == True and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]+1, x[2])) != 'Ob'
            if dest_x == x[1]-1 and dest_y == x[2] and x[0] == True and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]+1, x[2])) != 'Ob':
                print(modify_piece_dat(str(white_pawn_index_str[counter]), x[1]+1, x[2]))
                if DEBUG == True:
                    print()
                    print('wanted x:'+str(dest_x))
                    print('wanted y:'+str(dest_y))
                    print('pawn x:'+str(x[1]))
                    print('pawn y:'+str(x[2]))
                    print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                    print('predicted x:'+str(x[1]+1))
                    print('predicted y:'+str(x[2]))
                    print('destination: '+xy_to_algebreic(dest_x, dest_y))
                    print('algebreic: '+xy_to_algebreic(x[1]+1, x[2]))
                    print('alive: '+str(x[0]))
                    print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                    print('predictded destination check: '+xy_to_algebreic(x[1]+1, x[2]))
                    print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]+1, x[2])))
                    print('move check return: '+str(out))
                return 'moved'
            elif DEBUG == True:
                print()
                print('wanted x:'+str(dest_x))
                print('wanted y:'+str(dest_y))
                print('pawn x:'+str(x[1]))
                print('pawn y:'+str(x[2]))
                print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                print('predicted x:'+str(x[1]+1))
                print('predicted y:'+str(x[2]))
                print('destination: '+xy_to_algebreic(dest_x, dest_y))
                print('algebreic: '+xy_to_algebreic(x[1]+1, x[2]))
                print('alive: '+str(x[0]))
                print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                print('predictded destination check: '+xy_to_algebreic(x[1]+1, x[2]))
                print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]+1, x[2])))
                print('move check return: '+str(out))
            counter += 1
    return 'cant move'

# complete
def special_pawns(player, dest_x, dest_y):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_b
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b
    global counter
    counter = 0
    if player == 'black':
        for x in black_pawn_index:
            out = x[1]-2 == dest_x and x[2] == dest_y and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]-2, x[2])) != 'taken'
            if x[1]-2 == dest_x and x[2] == dest_y and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]-2, x[2])) != 'taken':
                print(modify_piece_dat(str(black_pawn_index_str[counter]), x[1]-2, x[2]))
                pawn_special_edit(black_pawn_index_str[counter], False)
                if DEBUG == True:
                    print()
                    print('wanted x:'+str(dest_x))
                    print('wanted y:'+str(dest_y))
                    print('pawn x:'+str(x[1]))
                    print('pawn y:'+str(x[2]))
                    print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                    print('predicted x:'+str(x[1]-2))
                    print('predicted y:'+str(x[2]))
                    print('destination: '+xy_to_algebreic(dest_x, dest_y))
                    print('algebreic: '+xy_to_algebreic(x[1]-1, x[2]))
                    print('alive: '+str(x[0]))
                    print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                    print('predictded destination check: '+xy_to_algebreic(x[1]-2, x[2]))
                    print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]-2, x[2])))
                    print('move check return: '+str(out))
                return 'moved'
            elif DEBUG == True:
                print()
                print('wanted x:'+str(dest_x))
                print('wanted y:'+str(dest_y))
                print('pawn x:'+str(x[1]))
                print('pawn y:'+str(x[2]))
                print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                print('predicted x:'+str(x[1]-2))
                print('predicted y:'+str(x[2]))
                print('destination: '+xy_to_algebreic(dest_x, dest_y))
                print('algebreic: '+xy_to_algebreic(x[1]-2, x[2]))
                print('alive: '+str(x[0]))
                print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                print('predictded destination check: '+xy_to_algebreic(x[1]-2, x[2]))
                print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]-2, x[2])))
                print('move check return: '+str(out))
            counter += 1
    if player == 'white':
        for x in white_pawn_index:
            out = dest_x == x[1]+2 and dest_y == x[2] and x[0] == True and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]+2, x[2])) != 'Ob' and x[4] == True
            if dest_x == x[1]+2 and dest_y == x[2] and x[0] == True and check_spot(xy_to_algebreic(dest_x, dest_y)) != 'Ob' and check_spot(xy_to_algebreic(x[1]+2, x[2])) != 'Ob' and x[4] == True:
                print(modify_piece_dat(str(white_pawn_index_str[counter]), x[1]-2, x[2]))
                pawn_special_edit(white_pawn_index_str[counter], False)
                if DEBUG == True:
                    print()
                    print('wanted x:'+str(dest_x))
                    print('wanted y:'+str(dest_y))
                    print('pawn x:'+str(x[1]))
                    print('pawn y:'+str(x[2]))
                    print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                    print('predicted x:'+str(x[1]+2))
                    print('predicted y:'+str(x[2]))
                    print('destination: '+xy_to_algebreic(dest_x, dest_y))
                    print('algebreic: '+xy_to_algebreic(x[1]+2, x[2]))
                    print('alive: '+str(x[0]))
                    print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                    print('predictded destination check: '+xy_to_algebreic(x[1]+2, x[2]))
                    print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]+2, x[2])))
                    print('move check return: '+str(out))
                return 'moved'
            elif DEBUG == True:
                print()
                print('wanted x:'+str(dest_x))
                print('wanted y:'+str(dest_y))
                print('pawn x:'+str(x[1]))
                print('pawn y:'+str(x[2]))
                print('pawn position:'+xy_to_algebreic(x[1], x[2]))
                print('predicted x:'+str(x[1]+2))
                print('predicted y:'+str(x[2]))
                print('destination: '+xy_to_algebreic(dest_x, dest_y))
                print('algebreic: '+xy_to_algebreic(x[1]+2, x[2]))
                print('alive: '+str(x[0]))
                print('dest out of bouns check: '+check_spot(xy_to_algebreic(dest_x, dest_y)))
                print('predictded destination check: '+xy_to_algebreic(x[1]+2, x[2]))
                print('predictded spot check: '+check_spot(xy_to_algebreic(x[1]+2, x[2])))
                print('move check return: '+str(out))
            counter += 1

# work in  progress
def promo_pawns(player, dest_x, dest_y):
    global counter
    counter = 0
    if player == 'black':
        for x in black_pawn_index:
            for y in pawn_promotions:
                for z in y:
                    # check future spot
                    future_x = x[1]+z[0]
                    future_y = x[2]+z[1]
                    future_spot = xy_to_algebreic(future_x, future_y)
                    if future_x == dest_x and future_y == dest_y and x[0] == True and x[3] == True and x[4] == pawn_promotions_str[promo_count]:
                        if check_spot(future_spot) == 'open':
                            modify_piece_dat(black_pawn_index[counter], future_x, future_y)
                            return 'moved'
                        elif check_spot(future_spot) == 'taken':
                            take_spot(future_spot)
                            modify_piece_dat(black_pawn_index[counter], future_x, future_y)
                            return 'moved'
                promo_count += 1
            counter += 1

def pawn_takes(player, dest_x, dest_y):
    return 'function under construction'

def move_pawns(player, desti_x, desti_y):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_b
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b
    promo = promo_pawns(player, desti_x, desti_y)
    special = special_pawns(player, desti_x, desti_y)
    pawn = pawn_moves(player, desti_x, desti_y)
    if DEBUG == True:
        print('promo: '+str(promo))
        print('special: '+str(special))
        print('pawn: '+ str(pawn))
    if promo == 'moved':
        return promo
    elif special == 'moved':
        return special
    elif pawn == 'moved':
        return pawn
    else:
        return 'cant move'

def move_bishop(player,destination):
    return 'function under construction'


def move_rook(player, destination):
    return 'function under construction'


def move_knight(player, destination):
    return 'function under construction'


def move_queen(player, destination):
    return 'function under construction'


def move_king(player, destination):
    return 'function under construction'


def move_piece(player='white', piece='', destination_x=0, destination_y=0):
    global king_w, queen_w, bishop0_w, bishop1_w, knight0_w, knight1_w, rook0_w, rook1_w, pawn0_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_b
    global king_b, queen_b, bishop0_b, bishop1_b, knight0_b, knight1_b, rook0_b, rook1_b, pawn0_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b
    destination_x = int(destination_x)
    destination_y = int(destination_y)
    destinationnn = xy_to_algebreic(destination_x, destination_y)
    if piece == 'pawn':
        return move_pawns(player, destination_x, destination_y)
    elif piece == 'bishop':
        return move_bishop(player,destinationnn)
    elif piece == 'rook':
        return move_rook(player, destinationnn)
    elif piece == 'knight':
        return move_knight(player, destinationnn)
    elif piece == 'queen':
        return move_queen(player, destinationnn)
    elif piece == 'king':
        return move_king(player, destinationnn)
    else:
        return 'nope'

while True:
    print(move_piece('black', 'pawn', input('x: '), input('y: ')))
    print(genorate_board())

