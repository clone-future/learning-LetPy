import canvas
import random
import sys

cntrs = {1: [58, 58], 2: [174, 58], 3: [290, 58], 4: [58, 174], 5: [174, 174], 6: [290, 174], 7: [58, 290],
         8: [174, 290], 9: [290, 290]}
GAME_STATE = [None, None, None, None, None, None, None, None, None]


def draw_o(position):
    canvas.circle(int(cntrs[position][0]), int(cntrs[position][1]), 30)
    canvas.draw


def draw_x(position):
    canvas.radius_line(int(cntrs[position][0]), int(cntrs[position][1]), 45, 60)
    canvas.radius_line(int(cntrs[position][0]), int(cntrs[position][1]), -45, 60)
    canvas.radius_line(int(cntrs[position][0]), int(cntrs[position][1]), 135, 60)
    canvas.radius_line(int(cntrs[position][0]), int(cntrs[position][1]), -135, 60)
    canvas.draw


def get_bot_move(GAME_STATE):
    try:
        rnd_pos = []
        qwe = 0
        for i in GAME_STATE:
            if i == None:
                rnd_pos.append(qwe)
            qwe = qwe + 1
        return random.choice(rnd_pos)
    except IndexError:
        return None


def draw_state(GAME_STATE):
    canvas.canvas.radius_line(116, 0, 180, 370)
    canvas.canvas.radius_line(232, 0, 180, 370)
    canvas.canvas.radius_line(0, 116, 90, 370)
    canvas.canvas.radius_line(0, 232, 90, 370)
    y_counter = 0
    for i in GAME_STATE:
        y_counter = y_counter + 1
        if i == 'x':
            draw_x(y_counter)
        elif i == 'o':
            draw_o(y_counter)
    canvas.draw()


draw_state(GAME_STATE)


def click(x, y):
    if y <= 116:
        if x <= 116:
            set_pos = 0
        if x <= 232 and x > 116:
            set_pos = 1
        if x <= 348 and x > 232:
            set_pos = 2
    if y <= 232 and y > 116:
        if x <= 116:
            set_pos = 3
        if x <= 232 and x > 116:
            set_pos = 4
        if x <= 348 and x > 232:
            set_pos = 5
    if y <= 348 and y > 232:
        if x <= 116:
            set_pos = 6
        if x <= 232 and x > 116:
            set_pos = 7
        if x <= 348 and x > 232:
            set_pos = 8
    if GAME_STATE[set_pos] == None:
        GAME_STATE[set_pos] = 'x'
        if get_bot_move(GAME_STATE) != None:
            GAME_STATE[get_bot_move(GAME_STATE)] = 'o'
            print(get_winner(GAME_STATE))
        else:
            print('Game over')
        draw_state(GAME_STATE)
        print(get_winner(GAME_STATE))


def get_winner(GAME_STATE):
    for win in [['x', 'x', 'x'], ['o', 'o', 'o']]:
        if GAME_STATE[:3] == win:
            return win[0] + '_win'
        elif GAME_STATE[3:6] == win:
            return win[0] + '_win'
        elif GAME_STATE[6:9] == win:
            return win[0] + '_win'
        elif GAME_STATE[:9:3] == win:
            return win[0] + '_win'
        elif GAME_STATE[1:9:3] == win:
            return win[0] + '_win'
        elif GAME_STATE[2:9:3] == win:
            return win[0] + '_win'
        elif [GAME_STATE[0], GAME_STATE[4], GAME_STATE[8]] == win:
            return win[0] + '_win'
        elif [GAME_STATE[2], GAME_STATE[4], GAME_STATE[6]] == win:
            return win[0] + '_win'
    if None not in GAME_STATE:
        return 'draw'
        return None


# print(get_winner(['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']))
canvas.set_onclick(click)
canvas.listen()