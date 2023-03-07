import os,allmove
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

from tkinter import Tk
rootTK = Tk()

def moveT(y,x):
    return "".join(["abcdefgh"[x],str(int(abs(8-(y))))])

def even(n): return (n % 2) == 0
def iswhite(p): return False if p.lower() == p else True
def opp(p):
    if iswhite(p):
        return p.lower()
    return p.upper()
def legalmoves(y,x,p):
    b = p.lower()
    moves = []
    if b == "k":
        t = allmove.k(y,x)
        for g in t:
            if ((g[0] < 0) or (g[0] >= 8)) or ((g[1] < 0) or (g[1] >= 8)):
                continue
            if SET[g[0]][g[1]] == None:
                moves.append(g)
                continue
            if (iswhite(p) == iswhite(SET[g[0]][g[1]])):
                continue
            else:
                moves.append(g)
                continue
        # cy = 7 if iswhite(p) else 0
        # if y == cy and x in (3,4):
    if b == "n":
        t = allmove.n(y,x)
        for g in t:
            if ((g[0] < 0) or (g[0] >= 8)) or ((g[1] < 0) or (g[1] >= 8)):
                continue
            if SET[g[0]][g[1]] == None:
                moves.append(g)
                continue
            if (iswhite(p) == iswhite(SET[g[0]][g[1]])):
                continue
            else:
                moves.append(g)
                continue
    if b == "p":
        if iswhite(p):
            t = allmove.wp(y,x)
        else:
            t = allmove.bp(y,x)
        g1 = (t[0][0],t[0][1])
        g2 = (t[1][0],t[1][1])
        fir = False
        if not (((g1[0] < 0) or (g1[0] >= 8)) or ((g1[1] < 0) or (g1[1] >= 8))):
            if SET[g1[0]][g1[1]] == None:
                moves.append(g1)
                fir = True
        if not (((g2[0] < 0) or (g2[0] >= 8)) or ((g2[1] < 0) or (g2[1] >= 8))):
            if y in (1,6):
                if (SET[g2[0]][g2[1]] == None) and fir:
                    moves.append(g2)
        for g in t[2:]:
            if not (((g[0] < 0) or (g[0] >= 8)) or ((g[1] < 0) or (g[1] >= 8))):
                try:
                    if SET[g[0]][g[1]] != None:
                        if (iswhite(p) != iswhite(SET[g[0]][g[1]])):
                            moves.append(g)
                except Exception as e:
                    print(str(e))
                    print(SET)
                    print(g)
                    raise e
                
    elif b == "r":
        t = allmove.straight
        for f in t:
            for b in range(1,8):
                g = f(y,x,b)
                if ((g[0] < 0) or (g[0] >= 8)) or ((g[1] < 0) or (g[1] >= 8)):
                    break
                if SET[g[0]][g[1]] == None:
                    moves.append(g)
                    continue
                if (iswhite(p) == iswhite(SET[g[0]][g[1]])):
                    break
                if (iswhite(p) != iswhite(SET[g[0]][g[1]])):
                    moves.append(g)
                    break
    elif b == "b":
        t = allmove.diagnol
        for f in t:
            for b in range(1,8):
                g = f(y,x,b)
                if ((g[0] < 0) or (g[0] >= 8)) or ((g[1] < 0) or (g[1] >= 8)):
                    break
                if SET[g[0]][g[1]] == None:
                    moves.append(g)
                    continue
                if (iswhite(p) == iswhite(SET[g[0]][g[1]])):
                    break
                if (iswhite(p) != iswhite(SET[g[0]][g[1]])):
                    moves.append(g)
                    break
    elif b == "q":
        for t in (allmove.straight,allmove.diagnol):
            for f in t:
                for b in range(1,8):
                    g = f(y,x,b)
                    if ((g[0] < 0) or (g[0] >= 8)) or ((g[1] < 0) or (g[1] >= 8)):
                        break
                    if SET[g[0]][g[1]] == None:
                        moves.append(g)
                        continue
                    if (iswhite(p) == iswhite(SET[g[0]][g[1]])):
                        break
                    if (iswhite(p) != iswhite(SET[g[0]][g[1]])):
                        moves.append(g)
                        break
    moves.append((y,x))
    return moves
            
        
global WIDTH,HEIGHT,CLOCK,RGB,ASSETS,SIZE,WINSIZE,SET,OFFSET,HOLDING,M,PREV

RGB = {
    "white":(255,255,255),
    "black":(0,0,0),
    "red":(255,0,0),
    "green":(0,255,0),
    "blue":(0,0,255),
    "yellow":(255,255,0),
    "cyan":(0,255,255),
    "magenta":(255,0,255)
}
SIZE = int(min(rootTK.winfo_screenheight(), rootTK.winfo_screenwidth())*(9/10))//8
WINSIZE = SIZE*8
WIDTH,HEIGHT = WINSIZE,WINSIZE
CLOCK = pygame.time.Clock()
FPS = 60
OFFSET = SIZE//4
M = 0
HOLDING = (False,None,None,None,None)
# SET = [[None for j in range(HEIGHT//SIZE)] for i in range(WIDTH//SIZE)]
SET = [
    list("rnbqkbnr"),
    list("pppppppp"),
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    list("PPPPPPPP"),
    list("RNBQKBNR")
]

DIR_ = "./assets/pieces/"

ASSETS = {
    "icon": pygame.image.load(os.path.join(DIR_,"w_king.png")),
    "font": pygame.font.SysFont("Courier New",32,bold=True),
    "pieces":{
        "k" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"b_king.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "q" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"b_queen.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "n" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"b_knight.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "b" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"b_bishop.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "p" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"b_pawn.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "r" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"b_rook.png")),(SIZE-OFFSET,SIZE-OFFSET)),

        "K" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"w_king.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "Q" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"w_queen.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "N" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"w_knight.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "B" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"w_bishop.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "P" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"w_pawn.png")),(SIZE-OFFSET,SIZE-OFFSET)),
        "R" :pygame.transform.scale(pygame.image.load(os.path.join(DIR_,"w_rook.png")),(SIZE-OFFSET,SIZE-OFFSET)),
    },
    # "sound":{
    #  "spark": pygame.mixer.Sound("./assets/spark.wav"),
    #  "win": pygame.mixer.Sound("./assets/win.wav"),
    #  "switch": pygame.mixer.Sound("./assets/switch.wav"),
    #  "deswitch": pygame.mixer.Sound("./assets/deswitch.wav"),
    # }
}


def board(win):
    for i,elist in enumerate(SET):
        for j,ele in enumerate(elist):
            win.rect(pygame.Rect(j*SIZE,i*SIZE,SIZE,SIZE),RGB["white"] if even(j+i) else RGB["black"])
            if ele != None:
                win.blit(ASSETS["pieces"][str(ele)],((j*SIZE)+(OFFSET//2),(i*SIZE)+(OFFSET//2)))

def main(win,events):
    global HOLDING,M
    pos = pygame.mouse.get_pos()
    for event in events:
        if (event.type == pygame.MOUSEBUTTONUP):# and event.button == 3:
            if event.button == 1 or event.button == 3:
                # if ((pos[0] < 0) or (pos[0] > WIDTH)) or ((pos[1] < 0) or (pos[1] > HEIGHT)):
                y,x = pos[1]//SIZE,pos[0]//SIZE
                if HOLDING[0]:
                    if (y,x) in HOLDING[4]:
                        SET[y][x] = HOLDING[1]
                        if not (y == HOLDING[2] and x == HOLDING[3]):
                            M += 1
                            print(moveT(HOLDING[2],HOLDING[3])+moveT(y,x))
                        HOLDING = (False,None,None,None,None)
                elif SET[y][x] == None:
                    continue
                elif (not HOLDING[0]) and (even(M)==iswhite(SET[y][x])):
                    t = SET[y][x]
                    if t == None:
                        continue
                    HOLDING = (True,t,y,x,legalmoves(y,x,t))
                    SET[y][x] = None
            if event.button == 2:
                print(SET)
                        
    if HOLDING[0]:
        win.blit(ASSETS["pieces"][str(HOLDING[1])],((pos[0])-((SIZE-OFFSET)//2),(pos[1])-((SIZE-OFFSET)//2)))
        for p in HOLDING[4]:
            pl = [(d*SIZE)+SIZE//2 for d in p]
            pl.reverse()
            if p == (HOLDING[2],HOLDING[3]):
                win.circle(pl, SIZE//4, RGB["red"])
            elif SET[p[0]][p[1]] == None:
                if even(p[0]+p[1]):
                    win.circle(pl, SIZE//4, RGB["blue"])
                else:
                    win.circle(pl, SIZE//4, RGB["cyan"])
            elif iswhite(SET[p[0]][p[1]]) != iswhite(str(HOLDING[1])):
                win.circle(pl, SIZE//4, RGB["green"])
                      

class Window():
    def __init__(self,title,width,height):
        self.width,self.height,self.title = width,height,title
        self.obj = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(title)
        pygame.display.set_icon(ASSETS["icon"])
        self.fill,self.blit,self.rect = self.obj.fill,self.obj.blit,lambda value,color:pygame.draw.rect(self.obj, color, value)
        self.circle = lambda pos,rad,color: pygame.draw.circle(self.obj, color, pos, rad)
    def update(self):
        return pygame.display.update()

run = True
win = Window("Chess",width=WIDTH,height=HEIGHT)
while run:
    CLOCK.tick(FPS)
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    board(win)
    main(win,events)
    win.update()
pygame.quit()