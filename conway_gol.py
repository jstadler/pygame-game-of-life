# Jordans attempt at Conways Game of Life
# 

import pygame, sys, random, copy

width = 640         # window width
height = 480        # window height
bin_size = 8        # window bins
stall = 200         # milliseconds between refresh
dorand = True       # fill random bins
rand_amount = 10000  # how many random bins to fill

pygame.init()
screen = pygame.display.set_mode( (width,height) )

bins = []
empty_bins = []
temp_bins = []

def setup_bins():
    for i in range(width/bin_size):
        bins.append([])
        empty_bins.append([])
        for j in range(height/bin_size):
            bins[i].append([])
            bins[i][j]=0
            empty_bins[i].append([])
            empty_bins[i][j]=0
    #empty_bins = list(bins)
    #print "here"
    #print empty_bins

def draw_grid():
    # vertical cell lines
    for i in range(width/bin_size):
        pygame.draw.line( screen, (100,100,100), (i*8,0), (i*8,height), 1)
    # horizontal cell lines
    for j in range(height/bin_size):
        pygame.draw.line( screen, (100,100,100), (0,j*8), (width,j*8), 1)

def draw_bins():
    for i in range(width/bin_size):
        for j in range(height/bin_size):
            if( bins[i][j] > 0 ):
                pygame.draw.rect( screen, (200,200,200), pygame.Rect(i*8,j*8,8,8),0)

def check_adjacent_bins(x,y):
    #print "checking bin ", x, " ", y
    count = 0
    xx = []; yy = [];
    # logic
    if x == 0:
        xx = [0,1]
    elif x == (width/bin_size) - 1:
        xx = [-1,0]
    else:
        xx = [-1,0,1]

    if y == 0:
        yy = [0,1]
    elif y == (height/bin_size) - 1:
        yy = [-1, 0]
    else:
        yy = [-1,0,1]

    for i in xx:
        for j in yy:
            if i == 0 and j == 0:
                continue
            if bins[x+i][y+j] > 0:
                count += 1
    return count

def flip_negatives():
    for i in range(width/bin_size):
        for j in range(height/bin_size):
            if bins[i][j] == -1:
                bins[i][j] = 1

def update_bins():
    temp_bins = copy.deepcopy(empty_bins)
    #print temp_bins
    for i in range(width/bin_size):
        for j in range(height/bin_size):
            adj = check_adjacent_bins(i,j)
            # life logic
            if adj < 2:     # under-population
                temp_bins[i][j] = 0
            elif adj > 3:  # overcrowding
                temp_bins[i][j] = 0
            elif adj == 3:  # reproduction
                temp_bins[i][j] = 1
            else:
                temp_bins[i][j] = bins[i][j]
    #print temp_bins
    #pygame.time.wait(50000)
    global bins
    bins = copy.deepcopy(temp_bins)

def refresh():
    pygame.draw.rect( screen, (0,0,0), pygame.Rect(0,0,width,height), 0)
    update_bins()
    #print bins
    #pygame.time.wait(5000)
    #adj = check_adjacent_bins(98,0)
    #print adj
    draw_grid()
    draw_bins()
    #print check_adjacent_bins(11,9)

# tests random display of cells
def rand_bin():
    w = int(((width/bin_size) - 1) * random.random())
    h = int(((height/bin_size) - 1) * random.random())
    bins[w][h] = 1

setup_bins()

#test boundaries
#bins[99][0] = 1
#bins[0][79] = 1
#these should fail
#bins[100][0] = 1
#bins[0][80] = 1

# blinker
bins[20][10] = 1
bins[21][10] = 1
bins[22][10] = 1

# block
bins[10][10] = 1
bins[10][11] = 1
bins[11][11] = 1
bins[11][10] = 1

# toad
bins[30][10] = 1
bins[31][10] = 1
bins[32][10] = 1
bins[29][11] = 1
bins[30][11] = 1
bins[31][11] = 1

# beacon
bins[40][9] = 1
bins[40][10] = 1
bins[41][10] = 1
bins[41][9] = 1
bins[42][11] = 1
bins[42][12] = 1
bins[43][12] = 1
bins[43][11] = 1

# glider
bins[10][20] = 1
bins[10][21] = 1
bins[10][22] = 1
bins[9][22] = 1
bins[8][21] = 1

if dorand:
    for i in range(1000):
       rand_bin()

frame_count = 0
# animation loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #frame_count += 1

    pygame.time.wait(stall)

    #print "count: ", frame_count
    #print "bla"
    #rand_bin()
    refresh()
    pygame.display.flip()
