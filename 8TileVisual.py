import pygame 
import os
from pygame.constants import WINDOWHITTEST
import copy


# bfs variables
solution = []
flag = False
direction = [[-1,0],[1,0],[0,-1],[0,1]]
help = ['U', 'D', 'L', 'R']
visited = []
final = [
    [1,2,3],
    [4,5,6],
    [7,8,-1]]

# pygame variables
crashed=False
path = ""
width,height = 318,500
solve_pos = [50, 444]
solve_box = [25, 430, 105, 50]
quit_pos = [210, 444]
quit_box = [180, 430, 105, 50]
left_pos = [20, 344]
left_box = [20, 344, 80, 43]
right_pos = [210, 344]
right_box = [210, 344, 80, 43]
curIndex = 0
board=[
    [4,1,3],
    [2,-1,5],
    [7,8,6]]
blankX=1
blankY=1
n=3

def swapVal(b, x, y, move):
    newx = x + move[0]
    newy = y + move[1]
    newBoard = copy.deepcopy(b)
    temp = newBoard[x][y]
    newBoard[x][y] = newBoard[newx][newy]
    newBoard[newx][newy] = temp
    return newBoard


def convertGridArray(initial, x, y, moves):
    if(len(moves) == 0):
        return []
    ret = []
    ret.append(initial)
    board = copy.deepcopy(initial)
    for i in range(len(moves)):
        if(moves[i] == 'U'):
            board = swapVal(board, x, y, direction[0])
            x = x + direction[0][0]
            y = y + direction[0][1]
        elif(moves[i] == 'D'):
            board = swapVal(board, x, y, direction[1])
            x = x + direction[1][0]
            y = y + direction[1][1]
        elif(moves[i]) == 'L':
            board = swapVal(board, x, y, direction[2])
            x = x + direction[2][0]
            y = y + direction[2][1]
        elif(moves[i] == 'R'):
            board = swapVal(board, x, y, direction[3])
            x = x + direction[3][0]
            y = y + direction[3][1]
        else:
            return []

        ret.append(board)
    return ret



def bfs(board, blankx, blanky):
    queue = []
    queue.append([board, blankx, blanky, ""])
    initial = copy.deepcopy(board)
    count = 0
    while(len(queue) != 0):
        cur = queue.pop(0)
        print(cur)
        if(cur[0] == final):
            arr = convertGridArray(initial, blankx, blanky, cur[3])
            return cur[3], arr

        visited.append(cur)

        for i in range(len(direction)):
            newx = cur[1] + direction[i][0]
            newy = cur[2] + direction[i][1]
            
            if(newx >= 0 and newy >=0 and newx < 3 and newy < 3):
                newBoard = swapVal(cur[0], cur[1], cur[2], direction[i])
                if(newBoard not in visited):
                    queue.append([newBoard, newx, newy, cur[3] + help[i]])

    return []



def move(direction,blankX,blankY):
    if(direction=="D"):
        if(blankX+1<n):
            t=board[blankX+1][blankY]
            board[blankX+1][blankY]=board[blankX][blankY]
            board[blankX][blankY]=t
            blankX+=1
            
    elif(direction=="U"):
        if(blankX-1>=0):
            t=board[blankX-1][blankY]
            board[blankX-1][blankY]=board[blankX][blankY]
            board[blankX][blankY]=t
            blankX-=1
    elif(direction=="L"):
        if(blankY-1>=0):
            t=board[blankX][blankY-1]
            board[blankX][blankY-1]=board[blankX][blankY]
            board[blankX][blankY]=t
            blankY-=1
    elif(direction=="R"):
        if(blankY+1<n):
            t=board[blankX][blankY+1]
            board[blankX][blankY+1]=board[blankX][blankY]
            board[blankX][blankY]=t
            blankY+=1
    return blankX,blankY

pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("8 Tiles")
application_path = os.path.dirname(__file__)
application_path=application_path.replace('\\','/')
tile=pygame.image.load(application_path+"/tile.jpeg")
blank=pygame.image.load(application_path+"/Empty.jpeg")
left=pygame.image.load(application_path+"/arrow2.jpeg")
left = pygame.transform.scale(left, (80, 43))
right=pygame.image.load(application_path+"/arrow1.jpeg")
right = pygame.transform.scale(right, (80, 43))

while crashed==False:
    gameDisplay.fill((0,0,0))   
    if flag == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if(solve_box[0] <= mouse[0] <= (solve_box[0] + solve_box[2]) and solve_box[1] <= mouse[1] <= (solve_box[1]+solve_box[3])):
                    path, solution = bfs(board, blankX, blankY)
                    flag = True
                    break
                if(quit_box[0] <= mouse[0] <= (quit_box[0]+quit_box[2]) and quit_box[1] <= mouse[1] <= (quit_box[1]+quit_box[3])):
                    crashed = True
                
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        blankX,blankY=move("U",blankX,blankY)
                    if event.key == pygame.K_LEFT:
                        blankX,blankY= move("L",blankX,blankY)
                    if event.key == pygame.K_RIGHT:
                        blankX,blankY=move("R",blankX,blankY)
                    if event.key == pygame.K_DOWN:
                        blankX,blankY=move("D",blankX,blankY)
    else:
        if(len(solution) == 0 and board != final):
            print("invalid tile configuration!")
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()

                    if(quit_box[0] <= mouse[0] <= (quit_box[0]+quit_box[2]) and quit_box[1] <= mouse[1] <= (quit_box[1]+quit_box[3])):
                        crashed = True

                    if(left_box[0] <= mouse[0] <= (left_box[0] + left_box[2]) and left_box[1] <= mouse[1] <= (left_box[1]+left_box[3])):
                        if(curIndex == 0):
                            continue
                        curIndex -= 1
                        board = copy.deepcopy(solution[curIndex])
                    
                    if(right_box[0] <= mouse[0] <= (right_box[0] + right_box[2]) and right_box[1] <= mouse[1] <= (right_box[1]+right_box[3])):
                        if(curIndex == len(solution) - 1):
                            continue
                        curIndex += 1
                        board = copy.deepcopy(solution[curIndex])
    counter=-1
    for y in range(0,n):
        submitfont = pygame.font.Font('freesansbold.ttf', 22)
        solve = submitfont.render('Solve', True, (255, 255, 255))
        quit = submitfont.render('Quit', True, (255, 255, 255))  
        pathstr = submitfont.render(str(len(path)+ 1) + " Steps", True, (255, 255, 255))  
        gameDisplay.blit(pathstr, (110, 354))

        pygame.draw.rect(gameDisplay, (36,236,213), (solve_box[0], solve_box[1], solve_box[2], solve_box[3]))
        pygame.draw.rect(gameDisplay, (36,236,213), (quit_box[0], quit_box[1], quit_box[2], quit_box[3]))
        gameDisplay.blit(solve, (solve_pos[0], solve_pos[1]))
        gameDisplay.blit(quit, (quit_pos[0], quit_pos[1]))  
        gameDisplay.blit(left, (left_pos[0], left_pos[1]))
        gameDisplay.blit(right, (right_pos[0], right_pos[1]))
        for x in range(0,n):
            font = pygame.font.Font('freesansbold.ttf', 22)
            tileNum=font.render(str(board[y][x]), True, (0, 0, 0)).convert_alpha()
            counter+=1
            if board[y][x]==-1:
                gameDisplay.blit(blank, (x*100+10,y*100+10))
                continue
            else:
                gameDisplay.blit(tile, (x*100+10,y*100+10))
            gameDisplay.blit(tileNum,(x*100+30,y*100+30))
    pygame.display.update()


