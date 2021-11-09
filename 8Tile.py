import numpy as np

def moveTile(grid, posx, posy, dir):
	
	oldx = posx
	oldy = posy
	if(dir == 'U' or dir == 'u'):
		posx -= 1;
	elif(dir == 'D' or dir == 'd'):
		posx += 1;
	elif(dir == 'L' or dir == 'l'):
		posy -= 1;
	elif(dir == 'R' or dir == 'r'):
		posy += 1;

	if(posx < 0 or posy < 0 or posx > 2 or posy > 2):
		print('Invalid Direction!')
		return grid, oldx, oldy
	
	temp = grid[posx][posy]
	grid[posx][posy] = grid[oldx][oldy]
	grid[oldx][oldy] = temp

	for i in range(3):
		for j in range(3):
			print(grid[i][j], end=' ')
		print()
	return grid, posx, posy


if __name__ == '__main__':
	gridArr = []
	posx = -1
	posy = -1
	print('Enter Grid:')
	for i in range(3):
		row = list(map(int, input().split(' ')))
		gridArr.append(row)

	for i in range(3):
		for j in range(3):
			if(gridArr[i][j] == 0):
				posx = i
				posy = j
	
	while(True):
		print('Enter Direction(U,D,L,R): ')
		dir = input()
		if(dir == 'U' or dir == 'D' or dir == 'L' or dir == 'R'):
			gridArr, posx, posy = moveTile(gridArr, posx, posy, dir)
		else:
			break
		
		print('\n\n')
