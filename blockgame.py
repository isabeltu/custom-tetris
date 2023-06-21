
import pygame
import random

pygame.init()


pixsize = 30
smallfont = pygame.font.Font("orange kid.otf", int(1.5*pixsize))
bigfont = pygame.font.Font("VIDEOPHREAK.ttf", int(1.6*pixsize))
mediumfont = pygame.font.Font("orange kid.otf", int(2*pixsize))
titlefont = pygame.font.Font("VIDEOPHREAK.ttf", int(3*pixsize))
arrowfont = pygame.font.Font("orange kid.otf", int(3*pixsize))

colors = {}
colors["white"] = (255, 255, 255)
colors["red"] = (255, 0, 0)
colors["orange"] = (255, 127, 0)
colors["yellow"] = (255, 255, 0)
colors["green"] = (50, 255, 0)
colors["cyan"] = (0,255, 255)
colors["blue"] = (0, 50, 255)
colors["purple"] = (255, 0, 255)

darkcolors = {}
darkcolors["red"] = (200, 0, 0)
darkcolors["orange"] = (200, 100, 0)
darkcolors["yellow"] = (200, 200, 0)
darkcolors["green"] = (40, 200, 0)
darkcolors["cyan"] = (0,200, 200)
darkcolors["blue"] = (0, 40, 200)
darkcolors["purple"] = (200, 0, 200)


screen = pygame.display.set_mode([16*pixsize, 24*pixsize])
pygame.display.set_caption("Custom Tetris")

clock=pygame.time.Clock()

highscore = 0
quit = False


#pieces
pieces = {}
pieces["red"] = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces["orange"] = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces["yellow"] = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces["green"] = [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces["cyan"] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces["blue"] = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
pieces["purple"] = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

ogpieces = {}
ogpieces["red"] = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
ogpieces["orange"] = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
ogpieces["yellow"] = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
ogpieces["green"] = [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
ogpieces["cyan"] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
ogpieces["blue"] = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
ogpieces["purple"] = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]



class Piece:
    def __init__(self, color = "none"):
        if color == "none":
            self.color = random.choice(("red", "orange", "yellow", "green", "cyan", "blue", "purple"))
        else:
            self.color = color
        self.shape = pieces[self.color]
        self.x = 3
        self.y = -2
        self.landcount = 0

    def create(self):
        while self.collide() and self.y > -4:
            self.y -= 1
        for i in range(5):
            for j in range(self.y * -1, 5):
                if self.shape[j][i]:
                    board[j+self.y][i+self.x] = self.color



    def collide(self):
        for i in range(5):
            for j in range(5):
                if self.shape[j][i]:
                    if self.x+i < 0 or self.x+i > 9 or self.y+j > 19:
                        return True
                    if self.y+j >= 0 and board[self.y+j][self.x+i] != "":
                        return True
        return False
            
    def clear(self):
        for i in range(5):
            for j in range(5):
                if self.shape[j][i] and self.y+j >= 0:
                    board[self.y+j][self.x+i] = ""

    def redraw(self):
        for i in range(5):
            for j in range(5):
                if self.shape[j][i] and self.y+j>=0:
                    board[self.y+j][self.x+i] = self.color


    def move(self, direction):
        self.clear()
        if direction == "l":
            self.x-=1
            if self.collide():
                self.x+=1
        elif direction == "r":
            self.x+=1
            if self.collide():
                self.x-=1
        elif direction == "d":
            self.y+=1
            if self.collide():
                self.y-=1
                self.landcount += 1
        self.redraw()

    def landed(self):
        if self.landcount >= 2:
            return True
            landcount = 0
        return False

    def rotate(self):
        self.clear()
        ogshape = self.shape
        found = False
        self.shape = list(zip(*self.shape[::-1]))
        for i in range(5):
            self.x += i
            if not self.collide():
                found = True
                break
            self.x -= 2*i
            if not self.collide():
                found = True
                break
            self.x += i
            self.y -= i
            if not self.collide():
                found = True
                break
            self.y += i
        if not found:
            self.shape = ogshape

        self.redraw()


    def bottom(self):
        self.clear()
        for y in range(self.y+1, 20):
            for i in range(5):
                for j in range(5):
                    if self.shape[j][i]:
                        if y+j > 19 or y+j >= 0 and board[y+j][self.x+i] != "":
                            self.redraw()
                            return y-1
        self.redraw()
        return 19;


def game_background():
    screen.fill((50, 50, 50))

    text = bigfont.render("CUSTOM TETRIS", True, colors["white"])
    screen.blit(text, (pixsize, pixsize//2))

    text = smallfont.render("next", True, colors["white"])
    screen.blit(text, (12.5*pixsize, 4.5*pixsize))

    text = smallfont.render("hold", True, colors["white"])
    screen.blit(text, (12.5*pixsize, 9.2*pixsize))

    text = smallfont.render("level", True, colors["white"])
    screen.blit(text, (12.3*pixsize, 14*pixsize))
    text = smallfont.render("1", True, colors["white"])
    screen.blit(text, (13*pixsize, 15.2*pixsize))

    text = smallfont.render("score", True, colors["white"])
    screen.blit(text, (12*pixsize, 17*pixsize))
    text = smallfont.render("0", True, colors["white"])
    screen.blit(text, (12*pixsize, 18.2*pixsize))

    text = smallfont.render("high", True, colors["white"])
    screen.blit(text, (12.5*pixsize, 20*pixsize))
    text = smallfont.render(str(highscore), True, colors["white"])
    screen.blit(text, (12*pixsize, 21.2*pixsize))

    display_next_piece()
    display_held_piece()

def print_board():
    for j in range(20):
        for i in range(10):
            if board[j][i] == '': print(" ", end = "|")
            else: print(board[j][i][0], end = "|")
        print()
        print("--------------------")
    print()


def update_score():
    pygame.draw.rect(screen, (50, 50, 50), (12*pixsize, 17.3*pixsize, 4*pixsize, 2.5*pixsize))
    text = smallfont.render("score", True, colors["white"])
    screen.blit(text, (12*pixsize, 17*pixsize))    
    text = smallfont.render(str(score), True, colors["white"])
    screen.blit(text, (12*pixsize, 18.2*pixsize))

def update_level():
    pygame.draw.rect(screen, (50, 50, 50), (12*pixsize, 14.3*pixsize, 4*pixsize, 2.5*pixsize))
    text = smallfont.render("level", True, colors["white"])
    screen.blit(text, (12.3*pixsize, 14*pixsize))
    text = smallfont.render(str(level), True, colors["white"])
    screen.blit(text, (13*pixsize, 15.2*pixsize))

def display_board():
    pygame.draw.rect(screen, (60, 60, 60), (pixsize, 3*pixsize, 10*pixsize, 20*pixsize))
    for i in range(21):
        pygame.draw.line(screen, (100, 100, 100), (pixsize, (3+i)*pixsize), (11*pixsize, (3+i)*pixsize))
        if(i < 11):
            pygame.draw.line(screen, (100, 100, 100), ((1+i)*pixsize, 3*pixsize), ((1+i)*pixsize, 23*pixsize))
    
    y = cur_piece.bottom()
    x = cur_piece.x
    for i in range(5):
        for j in range(5):
            if cur_piece.shape[j][i] and y+j >= 0:
                pygame.draw.rect(screen, (100, 100, 100), ((x+i+1)*pixsize, (y+j+3)*pixsize, pixsize-1, pixsize-1), border_radius = pixsize//4)
    
    for i in range(10):
        for j in range(20):
            if board[j][i] != "":
                pygame.draw.rect(screen, colors[board[j][i]], ((i+1)*pixsize, (j+3)*pixsize, pixsize-1, pixsize-1), border_radius = pixsize//4)

def check_game_over():
    for i in range(10):
        if board[0][i] != "":
            return True
    return False

def display_next_piece():
    pygame.draw.rect(screen, (60, 60 ,60), (12*pixsize, 6.2*pixsize, 3*pixsize, 3*pixsize))
    pygame.draw.rect(screen, (100, 100 ,100), (12*pixsize, 6.2*pixsize, 3*pixsize, 3*pixsize), 1)

    for i in range(5):
        for j in range(5):
            if next_piece.shape[j][i]:
                pygame.draw.rect(screen, colors[next_piece.color], ((12.25+0.5*i)*pixsize, (6.45+0.5*j)*pixsize, 0.5*pixsize-0.5, 0.5*pixsize-0.5), border_radius = pixsize//8)

def display_held_piece():
    pygame.draw.rect(screen, (60, 60, 60), (12*pixsize, 10.9*pixsize, 3*pixsize, 3*pixsize))
    pygame.draw.rect(screen, (100, 100, 100), (12*pixsize, 10.9*pixsize, 3*pixsize, 3*pixsize), 1)

    if held_piece:
        for i in range(5):
            for j in range(5):
                if held_piece.shape[j][i]:
                    pygame.draw.rect(screen, colors[held_piece.color], ((12.25+0.5*i)*pixsize, (11.15+0.5*j)*pixsize, 0.5*pixsize-0.5, 0.5*pixsize-0.5), border_radius = pixsize//8)

def lines():
    lines = []

    for y in range(20):
        global score
        line = True
        for x in range(10):
            if board[y][x] == "":
                line = False
        if line:
            lines.append(y)

    if len(lines) > 0:
        for i in range(2):
            display_board()
            pygame.display.flip()
            pygame.time.wait(100)
            for y in lines:
                for x in range(10):
                    pygame.draw.rect(screen, (255, 255, 255), ((x+1)*pixsize, (y+3)*pixsize, pixsize, pixsize), border_radius = pixsize // 4)
            pygame.display.flip()
            pygame.time.wait(100)

        lines_under = 0

        for y in range(19, -1, -1):
            if y in lines:
                lines_under += 1
            elif y+lines_under < 20:
                board[y+lines_under] = board[y]

        for y in range(lines_under):
            board[y] = [""]*10

        if len(lines) == 1:
            score += 100
        elif len(lines) == 2:
            score += 300
        elif len(lines) == 3:
            score += 500
        elif len(lines) == 4:
            score += 800
        else:
            score += 800 + 300*(len(lines)-4)

def pause_game():
    global running
    global quit

    pygame.draw.rect(screen, (100, 100 ,100), (4*pixsize, 6*pixsize, 8*pixsize, 10*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (4*pixsize, 6*pixsize, 8*pixsize, 10*pixsize), 5)
    text = mediumfont.render("paused", True, colors["white"])
    screen.blit(text, (5.6*pixsize, 6.5*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize), 3)
    text = smallfont.render("continue", True, colors["white"])
    screen.blit(text, (6*pixsize, 9.8*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
    text = smallfont.render("quit", True, colors["white"])
    screen.blit(text, (7*pixsize, 12.8*pixsize))

    pygame.display.flip()
    paused = True
    
    while paused:
        global quit
        global running
        global highscore
        global score

        in_continue = False
        in_quit = False

        mouse = pygame.mouse.get_pos()
        if 5*pixsize <= mouse[0] <= 11*pixsize and 10*pixsize <= mouse[1] <= 12*pixsize:
            pygame.draw.rect(screen, (120, 120, 120), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("continue", True, colors["white"])
            screen.blit(text, (6*pixsize, 9.8*pixsize))
            pygame.display.flip()

            in_continue = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif 5*pixsize <= mouse[0] <= 11*pixsize and 13*pixsize <= mouse[1] <= 15*pixsize:
            pygame.draw.rect(screen, (120, 120, 120), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("quit", True, colors["white"])
            screen.blit(text, (7*pixsize, 12.8*pixsize))
            pygame.display.flip()

            in_quit = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif 12.5*pixsize <= mouse[0] <= 14.5*pixsize and 2.7*pixsize <= mouse[1] <= 4.7*pixsize:
            pygame.draw.line(screen, (120, 120, 120), (13*pixsize, 3*pixsize), (13*pixsize, 4.4*pixsize), width = pixsize//3)
            pygame.draw.line(screen, (120, 120, 120), (13.9*pixsize, 3*pixsize), (13.9*pixsize, 4.4*pixsize), width = pixsize//3)

            pygame.draw.line(screen, colors["white"], (12.9*pixsize, 2.9*pixsize), (12.9*pixsize, 4.3*pixsize), width = pixsize//3)
            pygame.draw.line(screen, colors["white"], (13.8*pixsize, 2.9*pixsize), (13.8*pixsize, 4.3*pixsize), width = pixsize//3)
            pygame.display.flip()

            in_continue = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:
            pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("continue", True, colors["white"])
            screen.blit(text, (6*pixsize, 9.8*pixsize))

            pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("quit", True, colors["white"])
            screen.blit(text, (7*pixsize, 12.8*pixsize))

            pygame.draw.rect(screen, (50, 50 ,50), (12.5*pixsize, 2.7*pixsize, 2*pixsize, 2*pixsize))
            pygame.draw.line(screen, colors["white"], (13*pixsize, 3*pixsize), (13*pixsize, 4.4*pixsize), width = pixsize//3)
            pygame.draw.line(screen, colors["white"], (13.9*pixsize, 3*pixsize), (13.9*pixsize, 4.4*pixsize), width = pixsize//3)

            pygame.display.flip()

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False
                quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == pygame.MOUSEBUTTONDOWN and in_continue:
                paused = False
            elif event.type == pygame.MOUSEBUTTONDOWN and in_quit:
                paused = False
                running = False
                if score > highscore:
                    highscore = score
                return 1

    game_background()
    return 0

def pause_button():

    in_pause = False

    mouse = pygame.mouse.get_pos()
    if 12.5*pixsize <= mouse[0] <= 14.5*pixsize and 2.7*pixsize <= mouse[1] <= 4.7*pixsize:
        pygame.draw.line(screen, (120, 120, 120), (13*pixsize, 3*pixsize), (13*pixsize, 4.4*pixsize), width = pixsize//3)
        pygame.draw.line(screen, (120, 120, 120), (13.9*pixsize, 3*pixsize), (13.9*pixsize, 4.4*pixsize), width = pixsize//3)

        pygame.draw.line(screen, colors["white"], (12.9*pixsize, 2.9*pixsize), (12.9*pixsize, 4.3*pixsize), width = pixsize//3)
        pygame.draw.line(screen, colors["white"], (13.8*pixsize, 2.9*pixsize), (13.8*pixsize, 4.3*pixsize), width = pixsize//3)

        in_pause = True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.draw.rect(screen, (50, 50 ,50), (12.5*pixsize, 2.7*pixsize, 2*pixsize, 2*pixsize))
        pygame.draw.line(screen, colors["white"], (13*pixsize, 3*pixsize), (13*pixsize, 4.4*pixsize), width = pixsize//3)
        pygame.draw.line(screen, colors["white"], (13.9*pixsize, 3*pixsize), (13.9*pixsize, 4.4*pixsize), width = pixsize//3)

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    if mousepressed and in_pause:
        return pause_game()

def game_over():
    global highscore
    global quit

    pygame.draw.rect(screen, (100, 100 ,100), (4*pixsize, 6*pixsize, 8*pixsize, 10*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (4*pixsize, 6*pixsize, 8*pixsize, 10*pixsize), 5)
    if score > highscore:
        text = mediumfont.render("high score", True, colors["white"])
        screen.blit(text, (4.8*pixsize, 6.5*pixsize))
        highscore = score
    else:
        text = mediumfont.render("good game", True, colors["white"])
        screen.blit(text, (4.6*pixsize, 6.5*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize), 3)
    text = smallfont.render("play again", True, colors["white"])
    screen.blit(text, (5.5*pixsize, 9.8*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
    text = smallfont.render("quit", True, colors["white"])
    screen.blit(text, (7*pixsize, 12.8*pixsize))

    pygame.display.flip()
    pygame.time.wait(300)
    paused = True
    in_again = False
    in_quit = False
    while paused:
        in_again = False
        in_quit = False

        mouse = pygame.mouse.get_pos()
        if 5*pixsize <= mouse[0] <= 11*pixsize and 10*pixsize <= mouse[1] <= 12*pixsize:
            pygame.draw.rect(screen, (120, 120, 120), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("play again", True, colors["white"])
            screen.blit(text, (5.5*pixsize, 9.8*pixsize))
            pygame.display.flip()

            in_again = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif 5*pixsize <= mouse[0] <= 11*pixsize and 13*pixsize <= mouse[1] <= 15*pixsize:
            pygame.draw.rect(screen, (120, 120, 120), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("quit", True, colors["white"])
            screen.blit(text, (7*pixsize, 12.8*pixsize))
            pygame.display.flip()

            in_quit = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 10*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("play again", True, colors["white"])
            screen.blit(text, (5.5*pixsize, 9.8*pixsize))

            pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("quit", True, colors["white"])
            screen.blit(text, (7*pixsize, 12.8*pixsize))

            pygame.display.flip()

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                return 2
            elif event.type == pygame.MOUSEBUTTONDOWN and in_again:
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN and in_quit:
                return 0

board = [[""]*10 for i in range(20)]
cur_piece = 0
next_piece = 0
held_piece = 0
score = 0
mousepressed = False
running = True
level = 1

def play_game():
    global board
    global cur_piece
    global next_piece
    global score
    global mousepressed
    global running
    global quit
    global level
    global held_piece

    board = [[""]*10 for i in range(20)]
    cur_piece = Piece()
    cur_piece.create()
    next_piece = Piece()
    held_piece = 0
    display_next_piece()
    display_held_piece()
    time_count = 0
    left_pressed = 0
    right_pressed = 0
    down_pressed_landed = 0
    score = 0
    level = 1
    dropspeed = 15
    held = False
    landtime = 0
    landtimes = [0, 0, 1, 1, 1, 1, 1, 1, 2, 4]
    game_background()

    running = True
    while running:

        time_count += 1

        keypressed = False
        mousepressed = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit = True
            elif event.type == pygame.KEYDOWN:
                keypressed = event.key
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pressed = 0
                elif event.key == pygame.K_RIGHT:
                    right_pressed = 0
                elif event.key == pygame.K_DOWN:
                    down_pressed_landed = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and time_count%2 == 0:
            if left_pressed > 3:
                cur_piece.move("l")
            else:
                left_pressed += 1
        if keys[pygame.K_RIGHT] and time_count%2 == 0:
            if right_pressed > 3:
                cur_piece.move("r")
            else:
                right_pressed += 1
        if keys[pygame.K_DOWN]:
            cur_piece.move("d")
            if cur_piece.landed():
                if down_pressed_landed < 10:
                    down_pressed_landed += 1
                    cur_piece.landcount -= 1 
            time_count = 0
        elif time_count >= dropspeed:
            cur_piece.move("d")
            if cur_piece.landed():
                if landtime < landtimes[landtime]:
                    landtime += 1
                    cur_piece.landcount -= 1
                else:
                    landtime = 0
            time_count = 0

        pause_return = 0

        if keypressed == pygame.K_LEFT:
            cur_piece.move("l")
        elif keypressed == pygame.K_RIGHT:
            cur_piece.move("r")
        elif keypressed == pygame.K_DOWN:
            cur_piece.move("d")
        elif keypressed == pygame.K_UP:
            cur_piece.rotate()
        elif keypressed == pygame.K_ESCAPE:
            pause_return = pause_game()
        elif keypressed == pygame.K_SPACE:
            while not cur_piece.landed():
                cur_piece.move("d")
        elif keypressed == pygame.K_c and not held:
            if held_piece:
                tmp = held_piece.color
                held_piece = Piece(cur_piece.color)
                cur_piece.clear()
                cur_piece = Piece(tmp)
                cur_piece.create()
                display_held_piece()
                held = True
            else:
                held_piece = Piece(cur_piece.color)
                cur_piece.clear()
                cur_piece = next_piece
                next_piece = Piece()
                cur_piece.create()
                display_held_piece()
                display_next_piece()
                held = True
            
      

        if cur_piece.landed():
            #print_board()
            score += 10
            lines()
            update_score()
            if score >= 1000*level and level < 5:
                level += 1
                dropspeed = 17-2*level
                update_level()
            elif level >= 5 and score >= 4000+2000*(level-4) and level < 10:
                level += 1
                dropspeed = 12 - level
                update_level()  
            #update_level()
            if check_game_over():
                #print("GAME OVER")
                display_board()
                running = False
            else:
                cur_piece = next_piece
                next_piece = Piece()
                cur_piece.create()
                display_next_piece()
                held = False

        if running:
            display_board()
            pause_return = pause_button()


        if quit:
            return 2

        if pause_return:
            return 0

        clock.tick(30)

        pygame.display.flip()

    return game_over()

def menu():
    screen.fill((50, 50, 50))

    custom = "CUSTOM"
    tetris = "TETRIS"
    colorlist = ["red", "cyan", "yellow", "purple", "orange", "green", "blue"]
    for i in range(len(custom)):
        text = titlefont.render(custom[i], True, (0, 0, 0))
        screen.blit(text, ((1.5+2.1*i)*pixsize, 2.3*pixsize))
        text = titlefont.render(custom[i], True, colors[colorlist[i]])
        screen.blit(text, ((1.2+2.1*i)*pixsize, 2*pixsize))
    for i in range(len(tetris)):
        text = titlefont.render(tetris[i], True, (0, 0, 0))
        screen.blit(text, ((1.8+2.1*i)*pixsize, 5.8*pixsize))
        text = titlefont.render(tetris[i], True, colors[colorlist[(4*i+3)%7]])
        screen.blit(text, ((1.5+2.1*i)*pixsize, 5.5*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (4*pixsize, 10*pixsize, 8*pixsize, 2.5*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (4*pixsize, 10*pixsize, 8*pixsize, 2.5*pixsize), 3)
    text = mediumfont.render("play", True, colors["white"])
    screen.blit(text, (6.5*pixsize, 9.75*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (4.8*pixsize, 13*pixsize, 6.4*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 13*pixsize, 6.4*pixsize, 2*pixsize), 3)
    text = smallfont.render("customize", True, colors["white"])
    screen.blit(text, (5.5*pixsize, 13*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (4.8*pixsize, 15.5*pixsize, 6.4*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 15.5*pixsize, 6.4*pixsize, 2*pixsize), 3)
    text = smallfont.render("how-to play", True, colors["white"])
    screen.blit(text, (5.1*pixsize, 15.5*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (4.8*pixsize, 18*pixsize, 6.4*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 18*pixsize, 6.4*pixsize, 2*pixsize), 3)
    text = smallfont.render("exit", True, colors["white"])
    screen.blit(text, (7*pixsize, 18*pixsize))

    pygame.display.flip()

    menuscreen = True
    in_play = False
    in_customize = False
    in_how = False
    in_exit = False
    while menuscreen:
        in_play = False
        in_customize = False
        in_how = False
        in_exit = False
        mouse = pygame.mouse.get_pos()
        if 4*pixsize <= mouse[0] <= 12*pixsize and 10*pixsize <= mouse[1] <= 12.5*pixsize:
            pygame.draw.rect(screen, (120, 120 ,120), (4*pixsize, 10*pixsize, 8*pixsize, 2.5*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4*pixsize, 10*pixsize, 8*pixsize, 2.5*pixsize), 3)
            text = mediumfont.render("play", True, colors["white"])
            screen.blit(text, (6.5*pixsize, 9.75*pixsize))

            in_play = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        elif 4.8*pixsize <= mouse[0] <= 11.2*pixsize and 13*pixsize <= mouse[1] <= 15*pixsize:
            pygame.draw.rect(screen, (120, 120 ,120), (4.8*pixsize, 13*pixsize, 6.4*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 13*pixsize, 6.4*pixsize, 2*pixsize), 3)
            text = smallfont.render("customize", True, colors["white"])
            screen.blit(text, (5.5*pixsize, 13*pixsize))

            in_customize = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif 4.8*pixsize <= mouse[0] <= 11.2*pixsize and 15.5*pixsize <= mouse[1] <= 17.5*pixsize:
            pygame.draw.rect(screen, (120, 120 ,120), (4.8*pixsize, 15.5*pixsize, 6.4*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 15.5*pixsize, 6.4*pixsize, 2*pixsize), 3)
            text = smallfont.render("how-to play", True, colors["white"])
            screen.blit(text, (5.1*pixsize, 15.5*pixsize))

            in_how = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif 4.8*pixsize <= mouse[0] <= 11.2*pixsize and 18*pixsize <= mouse[1] <= 20*pixsize:
            pygame.draw.rect(screen, (120, 120 ,120), (4.8*pixsize, 18*pixsize, 6.4*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 18*pixsize, 6.4*pixsize, 2*pixsize), 3)
            text = smallfont.render("exit", True, colors["white"])
            screen.blit(text, (7*pixsize, 18*pixsize))

            in_exit = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        else:
            pygame.draw.rect(screen, (70, 70 ,70), (4*pixsize, 10*pixsize, 8*pixsize, 2.5*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4*pixsize, 10*pixsize, 8*pixsize, 2.5*pixsize), 3)
            text = mediumfont.render("play", True, colors["white"])
            screen.blit(text, (6.5*pixsize, 9.75*pixsize))

            pygame.draw.rect(screen, (70, 70 ,70), (4.8*pixsize, 13*pixsize, 6.4*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 13*pixsize, 6.4*pixsize, 2*pixsize), 3)
            text = smallfont.render("customize", True, colors["white"])
            screen.blit(text, (5.5*pixsize, 13*pixsize))

            pygame.draw.rect(screen, (70, 70 ,70), (4.8*pixsize, 15.5*pixsize, 6.4*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 15.5*pixsize, 6.4*pixsize, 2*pixsize), 3)
            text = smallfont.render("how-to play", True, colors["white"])
            screen.blit(text, (5.1*pixsize, 15.5*pixsize))

            pygame.draw.rect(screen, (70, 70 ,70), (4.8*pixsize, 18*pixsize, 6.4*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (4.8*pixsize, 18*pixsize, 6.4*pixsize, 2*pixsize), 3)
            text = smallfont.render("exit", True, colors["white"])
            screen.blit(text, (7*pixsize, 18*pixsize))

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN and in_play:
                return "play"
            elif event.type == pygame.MOUSEBUTTONDOWN and in_customize:
                return "customize"
            elif event.type == pygame.MOUSEBUTTONDOWN and in_how:
                return "how"
            elif event.type == pygame.MOUSEBUTTONDOWN and in_exit:
                return "quit"

def customize_menu():
    global ogpieces
    global pieces

    screen.fill((50, 50, 50))

    text = arrowfont.render("<", True, (255, 255, 255))
    screen.blit(text, (pixsize, 0))

    text = bigfont.render("customize", True, (255, 255, 255))
    screen.blit(text, (4*pixsize, pixsize))

    colorlist = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

    for i in range(8):
        pygame.draw.rect(screen, (70, 70 ,70), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize))
        pygame.draw.rect(screen, (255, 255, 255), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize), 3)
        if i < 7:
            for x in range(5):
                for y in range(5):
                    if pieces[colorlist[i]][y][x]:
                        pygame.draw.rect(screen, colors[colorlist[i]], ((1.5+i%2*7.5+0.6*x)*pixsize, (4.5+i//2*5+0.6*y)*pixsize, 0.6*pixsize-0.6, 0.6*pixsize-0.6), border_radius = pixsize//8)

            text = arrowfont.render(">", True, colors["white"])
            screen.blit(text, ((6+i%2*7.5)*pixsize, (4+i//2*5)*pixsize))
        else:
            text = mediumfont.render("reset all", True, colors["white"])
            screen.blit(text, ((9)*pixsize, (19.5)*pixsize))

    pygame.display.flip()

    menuscreen = True
    inside = {}
    while menuscreen:

        inside["red"] = False
        inside["orange"] = False
        inside["yellow"] = False
        inside["green"] = False
        inside["cyan"] = False
        inside["green"] = False
        inside["blue"] = False
        inside["purple"] = False
        inside["reset"] = False
        inside["back"] = False

        is_inside = False

        mouse = pygame.mouse.get_pos()       

        for i in range(8):
            if (1+i%2*7.5)*pixsize <= mouse[0] <= (7.5+i%2*7.5)*pixsize and (4+i//2*5)*pixsize <= mouse[1] <= (8+i//2*5)*pixsize:
                pygame.draw.rect(screen, (120, 120 ,120), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize))
                pygame.draw.rect(screen, (255, 255, 255), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize), 3)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                is_inside = True

                if i < 7:
                    inside[colorlist[i]] = True

                    for x in range(5):
                        for y in range(5):
                            if pieces[colorlist[i]][y][x]:
                                pygame.draw.rect(screen, colors[colorlist[i]], ((1.5+i%2*7.5+0.6*x)*pixsize, (4.5+i//2*5+0.6*y)*pixsize, 0.6*pixsize-0.6, 0.6*pixsize-0.6), border_radius = pixsize//8)

                    text = arrowfont.render(">", True, colors[colorlist[i]])
                    screen.blit(text, ((6+i%2*7.5)*pixsize, (4+i//2*5)*pixsize))
                else:
                    inside["reset"] = True
                    text = mediumfont.render("reset all", True, colors["white"])
                    screen.blit(text, ((9)*pixsize, (19.5)*pixsize))

        if 0.7*pixsize <= mouse[0] <= 2.5*pixsize and 1.2*pixsize <= mouse[1] <= 3*pixsize:
            inside["back"] = True
            is_inside = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            text = arrowfont.render("<", True, (120, 120, 120))
            screen.blit(text, (1*pixsize, 0))         
            text = arrowfont.render("<", True, (255, 255, 255))
            screen.blit(text, (0.9*pixsize, -0.1*pixsize))

        if inside["reset"]:
            for i in range(7):
                pygame.draw.rect(screen, (70, 70 ,70), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize))
                pygame.draw.rect(screen, (255, 255, 255), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize), 3)
                for x in range(5):
                    for y in range(5):
                        if pieces[colorlist[i]][y][x]:
                            pygame.draw.rect(screen, colors[colorlist[i]], ((1.5+i%2*7.5+0.6*x)*pixsize, (4.5+i//2*5+0.6*y)*pixsize, 0.6*pixsize-0.6, 0.6*pixsize-0.6), border_radius = pixsize//8)

                text = arrowfont.render(">", True, colors["white"])
                screen.blit(text, ((6+i%2*7.5)*pixsize, (4+i//2*5)*pixsize))


        if not is_inside:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            pygame.draw.rect(screen, (50, 50, 50), (0.7*pixsize, 1.2*pixsize, 1.8*pixsize, 1.8*pixsize))
            text = arrowfont.render("<", True, (255, 255, 255))
            screen.blit(text, (pixsize, 0))

            for i in range(8):
                pygame.draw.rect(screen, (70, 70 ,70), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize))
                pygame.draw.rect(screen, (255, 255, 255), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize), 3)
                if i < 7:
                    for x in range(5):
                        for y in range(5):
                            if pieces[colorlist[i]][y][x]:
                                pygame.draw.rect(screen, colors[colorlist[i]], ((1.5+i%2*7.5+0.6*x)*pixsize, (4.5+i//2*5+0.6*y)*pixsize, 0.6*pixsize-0.6, 0.6*pixsize-0.6), border_radius = pixsize//8)

                    text = arrowfont.render(">", True, colors["white"])
                    screen.blit(text, ((6+i%2*7.5)*pixsize, (4+i//2*5)*pixsize))
                else:
                    text = mediumfont.render("reset all", True, colors["white"])
                    screen.blit(text, ((9)*pixsize, (19.5)*pixsize))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN and inside["back"]:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN and inside["reset"]:
                for color in colorlist:
                    for x in range(5):
                        for y in range(5):
                            pieces[color][y][x] = ogpieces[color][y][x]
            elif event.type == pygame.MOUSEBUTTONDOWN and is_inside:
                for color in colorlist:
                    if inside[color]:
                        if edit_piece(color):
                            return 1
                screen.fill((50, 50, 50))

                text = arrowfont.render("<", True, (255, 255, 255))
                screen.blit(text, (pixsize, 0))

                text = bigfont.render("customize", True, (255, 255, 255))
                screen.blit(text, (4*pixsize, pixsize))

                colorlist = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

                for i in range(8):
                    pygame.draw.rect(screen, (70, 70 ,70), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize))
                    pygame.draw.rect(screen, (255, 255, 255), ((1+i%2*7.5)*pixsize, (4+i//2*5)*pixsize, 6.5*pixsize, 4*pixsize), 3)
                    if i < 7:
                        for x in range(5):
                            for y in range(5):
                                if pieces[colorlist[i]][y][x]:
                                    pygame.draw.rect(screen, colors[colorlist[i]], ((1.5+i%2*7.5+0.6*x)*pixsize, (4.5+i//2*5+0.6*y)*pixsize, 0.6*pixsize-0.6, 0.6*pixsize-0.6), border_radius = pixsize//8)

                        text = arrowfont.render(">", True, colors["white"])
                        screen.blit(text, ((6+i%2*7.5)*pixsize, (4+i//2*5)*pixsize))
                    else:
                        text = mediumfont.render("reset all", True, colors["white"])
                        screen.blit(text, ((9)*pixsize, (19.5)*pixsize))

                pygame.display.flip()

def edit_piece(color):
    global pieces

    piece = pieces[color]
    last_piece = [[0]*5 for i in range(5)]

    for x in range(5):
        for y in range(5):
            last_piece[y][x] = piece[y][x]

    screen.fill((50, 50, 50))

    text = arrowfont.render("<", True, (255, 255, 255))
    screen.blit(text, (pixsize, 0))

    text = bigfont.render("customize", True, (255, 255, 255))
    screen.blit(text, (4*pixsize, pixsize))

    for x in range(5):
        for y in range(5):
            if piece[y][x] == 0:
                pygame.draw.rect(screen, (70, 70, 70), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                pygame.draw.rect(screen, (120, 120, 120), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)
            else:
                pygame.draw.rect(screen, colors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                pygame.draw.rect(screen, darkcolors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)

    pygame.draw.rect(screen, (70, 70, 70), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (50, 50, 50), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
    text = mediumfont.render("undo", True, (50, 50, 50))
    screen.blit(text, (3.7*pixsize, 15.2*pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
    text = mediumfont.render("reset", True, colors["white"])
    screen.blit(text, (9*pixsize, 15.2*pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize), 2)
    text = mediumfont.render("save", True, colors["white"])
    screen.blit(text, (6.3*pixsize, 17.6*pixsize))

    pygame.display.flip()

    editing = True
    inside = {}

    changes = []
    num_changes = 0

    while editing:
        inside["grid"] = [[0]*5 for i in range(5)]

        inside["back"] = False
        inside["save"] = False
        inside["reset"] = False
        inside["undo"] = False

        is_inside = False

        mouse = pygame.mouse.get_pos()
        
        if 0.7*pixsize <= mouse[0] <= 2.5*pixsize and 1.2*pixsize <= mouse[1] <= 3*pixsize:
            inside["back"] = True
            is_inside = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            text = arrowfont.render("<", True, (120, 120, 120))
            screen.blit(text, (1*pixsize, 0))         
            text = arrowfont.render("<", True, (255, 255, 255))
            screen.blit(text, (0.9*pixsize, -0.1*pixsize))

        elif 3*pixsize <= mouse[0] <= 7.5*pixsize and 15.5*pixsize <= mouse[1] <= 17.5*pixsize and num_changes > 0:
            inside["undo"] = True
            is_inside = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            pygame.draw.rect(screen, (120, 120, 120), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
            text = mediumfont.render("undo", True, colors["white"])
            screen.blit(text, (3.7*pixsize, 15.2*pixsize))

        elif 8.5*pixsize <= mouse[0] <= 13*pixsize and 15.5*pixsize <= mouse[1] <= 17.5*pixsize:
            inside["reset"] = True
            is_inside = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            pygame.draw.rect(screen, (120, 120, 120), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
            text = mediumfont.render("reset", True, colors["white"])
            screen.blit(text, (9*pixsize, 15.2*pixsize))

        elif 3*pixsize <= mouse[0] <= 13*pixsize and 18*pixsize <= mouse[1] <= 20*pixsize:
            inside["save"] = True
            is_inside = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            pygame.draw.rect(screen, (120, 120, 120), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize), 2)
            text = mediumfont.render("save", True, colors["white"])
            screen.blit(text, (6.3*pixsize, 17.6*pixsize))

        for x in range(5):
            for y in range(5):
                if (3+2*x)*pixsize <= mouse[0] <= (5+2*x)*pixsize and (5+2*y)*pixsize <= mouse[1] <= (7+2*y)*pixsize:
                    inside["grid"][y][x] = True
                    is_inside = True
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    if piece[y][x] == 0:
                        pygame.draw.rect(screen, (120, 120, 120), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                    else:
                        pygame.draw.rect(screen, darkcolors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                else:
                    if piece[y][x] == 0:
                        pygame.draw.rect(screen, (70, 70, 70), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                        pygame.draw.rect(screen, (120, 120, 120), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)
                    else:
                        pygame.draw.rect(screen, colors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                        pygame.draw.rect(screen, darkcolors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)

        if not inside["undo"]:
            pygame.draw.rect(screen, (70, 70, 70), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
            if num_changes == 0:
                pygame.draw.rect(screen, (50, 50, 50), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
                text = mediumfont.render("undo", True, (50, 50, 50))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
                text = mediumfont.render("undo", True, colors["white"])
            screen.blit(text, (3.7*pixsize, 15.2*pixsize))

        if not is_inside:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            pygame.draw.rect(screen, (50, 50, 50), (0.7*pixsize, 1.2*pixsize, 1.8*pixsize, 1.8*pixsize))
            text = arrowfont.render("<", True, (255, 255, 255))
            screen.blit(text, (pixsize, 0))

            for x in range(5):
                for y in range(5):
                    if piece[y][x] == 0:
                        pygame.draw.rect(screen, (70, 70, 70), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                        pygame.draw.rect(screen, (120, 120, 120), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)
                    else:
                        pygame.draw.rect(screen, colors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                        pygame.draw.rect(screen, darkcolors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)

            pygame.draw.rect(screen, (70, 70, 70), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
            text = mediumfont.render("reset", True, colors["white"])
            screen.blit(text, (9*pixsize, 15.2*pixsize))

            pygame.draw.rect(screen, (70, 70, 70), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize), 2)
            text = mediumfont.render("save", True, colors["white"])
            screen.blit(text, (6.3*pixsize, 17.6*pixsize))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN and inside["back"]:
                for x in range(5):
                    for y in range(5):
                        piece[y][x] = last_piece[y][x]
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN and inside["reset"]:
                for x in range(5):
                    for y in range(5):
                        piece[y][x] = ogpieces[color][y][x]
                num_changes = 0
                changes = []
            elif event.type == pygame.MOUSEBUTTONDOWN and inside["undo"]:
                piece[changes[num_changes-1][1]][changes[num_changes-1][0]] = 1-changes[num_changes-1][2]
                num_changes -= 1
                changes = changes[:num_changes]
            elif event.type == pygame.MOUSEBUTTONDOWN and inside["save"]:
                for x in range(5):
                    for y in range(5):
                        if piece[y][x]:
                            return 0
                if empty_piece():
                    return 1
                screen.fill((50, 50, 50))

                text = arrowfont.render("<", True, (255, 255, 255))
                screen.blit(text, (pixsize, 0))

                text = bigfont.render("customize", True, (255, 255, 255))
                screen.blit(text, (4*pixsize, pixsize))

                for x in range(5):
                    for y in range(5):
                        if piece[y][x] == 0:
                            pygame.draw.rect(screen, (70, 70, 70), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                            pygame.draw.rect(screen, (120, 120, 120), ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)
                        else:
                            pygame.draw.rect(screen, colors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), border_radius = pixsize//4)
                            pygame.draw.rect(screen, darkcolors[color], ((3+2*x)*pixsize, (5+2*y)*pixsize, 1.9*pixsize, 1.9*pixsize), pixsize//8, border_radius = pixsize//4)

                pygame.draw.rect(screen, (70, 70, 70), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
                pygame.draw.rect(screen, (50, 50, 50), (3*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
                text = mediumfont.render("undo", True, (50, 50, 50))
                screen.blit(text, (3.7*pixsize, 15.2*pixsize))

                pygame.draw.rect(screen, (70, 70, 70), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize))
                pygame.draw.rect(screen, (255, 255, 255), (8.5*pixsize, 15.5*pixsize, 4.5*pixsize, 2*pixsize), 2)
                text = mediumfont.render("reset", True, colors["white"])
                screen.blit(text, (9*pixsize, 15.2*pixsize))

                pygame.draw.rect(screen, (70, 70, 70), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize))
                pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize), 2)
                text = mediumfont.render("save", True, colors["white"])
                screen.blit(text, (6.3*pixsize, 17.6*pixsize))

            elif event.type == pygame.MOUSEBUTTONDOWN and is_inside:
                for x in range(5):
                    for y in range(5):
                        if inside["grid"][y][x]:
                            if piece[y][x]:
                                piece[y][x] = 0
                                num_changes += 1
                                changes.append([x, y, 0])
                            else:
                                piece[y][x] = 1
                                num_changes += 1
                                changes.append([x, y, 1])

def empty_piece():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.draw.rect(screen, (70, 70, 70), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 18*pixsize, 10*pixsize, 2*pixsize), 2)
    text = mediumfont.render("save", True, colors["white"])
    screen.blit(text, (6.3*pixsize, 17.6*pixsize))

    pygame.draw.rect(screen, (100, 100 ,100), (3*pixsize, 8*pixsize, 10*pixsize, 8*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (3*pixsize, 8*pixsize, 10*pixsize, 8*pixsize), 5)
    text = mediumfont.render("piece cannot", True, colors["white"])
    screen.blit(text, (3.8*pixsize, 8*pixsize))
    text = mediumfont.render("be empty", True, colors["white"])
    screen.blit(text, (5*pixsize, 10*pixsize))

    pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
    pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
    text = smallfont.render("okay", True, colors["white"])
    screen.blit(text, (6.8*pixsize, 13*pixsize))

    pygame.display.flip()

    closed = False
    while not closed:
        mouse = pygame.mouse.get_pos()
        in_okay = False

        if 5*pixsize <= mouse[0] <= 11*pixsize and 13*pixsize <= mouse[1] <= 15*pixsize:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            in_okay = True

            pygame.draw.rect(screen, (120, 120 ,120), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("okay", True, colors["white"])
            screen.blit(text, (6.8*pixsize, 13*pixsize))

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            pygame.draw.rect(screen, (70, 70 ,70), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize))
            pygame.draw.rect(screen, (255, 255, 255), (5*pixsize, 13*pixsize, 6*pixsize, 2*pixsize), 3)
            text = smallfont.render("okay", True, colors["white"])
            screen.blit(text, (6.8*pixsize, 13*pixsize))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN and in_okay:
                closed = True
    return 0

def how_to():
    screen.fill((50, 50, 50))

    text = arrowfont.render("<", True, (255, 255, 255))
    screen.blit(text, (pixsize, 0))

    text = bigfont.render("how-to play", True, (255, 255, 255))
    screen.blit(text, (3*pixsize, pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (2*pixsize, 4*pixsize, 2*pixsize, 2*pixsize), border_radius = pixsize//4)
    pygame.draw.rect(screen, colors["white"], (2*pixsize, 4*pixsize, 2*pixsize, 2*pixsize), 2, border_radius = pixsize//4)
    text = arrowfont.render("<", True, colors["white"])
    screen.blit(text, (2.5*pixsize, 2.8*pixsize))
    text = mediumfont.render("move left", True, colors["white"])
    screen.blit(text, (6*pixsize, 3.5*pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (2*pixsize, 6.8*pixsize, 2*pixsize, 2*pixsize), border_radius = pixsize//4)
    pygame.draw.rect(screen, colors["white"], (2*pixsize, 6.8*pixsize, 2*pixsize, 2*pixsize), 2, border_radius = pixsize//4)
    text = arrowfont.render(">", True, colors["white"])
    screen.blit(text, (2.6*pixsize, 5.7*pixsize))
    text = mediumfont.render("move right", True, colors["white"])
    screen.blit(text, (6*pixsize, 6.3*pixsize))   

    pygame.draw.rect(screen, (70, 70, 70), (2*pixsize, 9.6*pixsize, 2*pixsize, 2*pixsize), border_radius = pixsize//4)
    pygame.draw.rect(screen, colors["white"], (2*pixsize, 9.6*pixsize, 2*pixsize, 2*pixsize), 2, border_radius = pixsize//4)
    text = arrowfont.render(">", True, colors["white"])
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (0.8*pixsize, 10.1*pixsize))
    text = mediumfont.render("rotate right", True, colors["white"])
    screen.blit(text, (6*pixsize, 9.1*pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (2*pixsize, 12.4*pixsize, 2*pixsize, 2*pixsize), border_radius = pixsize//4)
    pygame.draw.rect(screen, colors["white"], (2*pixsize, 12.4*pixsize, 2*pixsize, 2*pixsize), 2, border_radius = pixsize//4)
    text = arrowfont.render("<", True, colors["white"])
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (0.8*pixsize, 13*pixsize))
    text = mediumfont.render("soft drop", True, colors["white"])
    screen.blit(text, (6*pixsize, 11.9*pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (pixsize, 15.2*pixsize, 4*pixsize, 2*pixsize), border_radius = pixsize//4)
    pygame.draw.rect(screen, colors["white"], (pixsize, 15.2*pixsize, 4*pixsize, 2*pixsize), 2, border_radius = pixsize//4)
    text = smallfont.render("space", True, colors["white"])
    screen.blit(text, (1.5*pixsize, 15.1*pixsize))
    text = mediumfont.render("hard drop", True, colors["white"])
    screen.blit(text, (6*pixsize, 14.7*pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (2*pixsize, 18*pixsize, 2*pixsize, 2*pixsize), border_radius = pixsize//4)
    pygame.draw.rect(screen, colors["white"], (2*pixsize, 18*pixsize, 2*pixsize, 2*pixsize), 2, border_radius = pixsize//4)
    text = mediumfont.render("c", True, colors["white"])
    screen.blit(text, (2.6*pixsize, 17.5*pixsize))
    text = mediumfont.render("hold piece", True, colors["white"])
    screen.blit(text, (6*pixsize, 17.5*pixsize))

    pygame.draw.rect(screen, (70, 70, 70), (1.5*pixsize, 20.8*pixsize, 3*pixsize, 2*pixsize), border_radius = pixsize//4)
    pygame.draw.rect(screen, colors["white"], (1.5*pixsize, 20.8*pixsize, 3*pixsize, 2*pixsize), 2, border_radius = pixsize//4)
    text = smallfont.render("esc", True, colors["white"])
    screen.blit(text, (2.1*pixsize, 20.7*pixsize))
    text = mediumfont.render("pause game", True, colors["white"])
    screen.blit(text, (6*pixsize, 20.3*pixsize))

    pygame.display.flip()

    in_how = True

    while in_how:
        in_back = False

        mouse = pygame.mouse.get_pos()

        if 0.7*pixsize <= mouse[0] <= 2.5*pixsize and 1.2*pixsize <= mouse[1] <= 3*pixsize:
            in_back = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            text = arrowfont.render("<", True, (120, 120, 120))
            screen.blit(text, (1*pixsize, 0))         
            text = arrowfont.render("<", True, (255, 255, 255))
            screen.blit(text, (0.9*pixsize, -0.1*pixsize))

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            pygame.draw.rect(screen, (50, 50, 50), (0.7*pixsize, 1.2*pixsize, 1.8*pixsize, 1.8*pixsize))
            text = arrowfont.render("<", True, (255, 255, 255))
            screen.blit(text, (pixsize, 0))   

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN and in_back:
                in_how = False
    return 0         


if __name__ == "__main__":

    game_open = True

    while game_open:

        choice = menu()

        #print(choice)

        if choice == "quit":
            game_open = False

        elif choice == "play":
            playing = True
            while playing:
                x = play_game()
                if x == 2:
                    playing = False
                    game_open = False
                elif x == 0:
                    playing = False

        elif choice == "customize":
            if customize_menu():
                game_open = False

        elif choice == "how":
            if how_to():
                game_open = False

    pygame.quit()

