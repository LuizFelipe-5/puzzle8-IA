from random import randint
from copy import deepcopy
from time import sleep
import os


class Puzzle():
	def __init__(self, puzz):
		self.__finalState = puzz
		self.__initialState = deepcopy(puzz)
		self.__movesList = ['13', '024', '15', '046', '1357', '248', '37', '468', '57']
		
		self.__distanceDict = {
		0: [4, 3, 2, 3, 2, 1, 2, 1, 0],
		1: [0, 1, 2, 1, 2, 3, 2, 3, 4],
		2: [1, 0, 1, 2, 1, 2, 3, 2, 3],
		3: [2, 1, 0, 3, 2, 1, 4, 3, 2],
		4: [1, 2, 3, 0, 1, 2, 1, 2, 3],
		5: [2, 1, 2, 1, 0, 1, 2, 1, 2],
		6: [3, 2, 1, 2, 1, 0, 3, 2, 1],
		7: [2, 3, 4, 1, 2, 3, 0, 1, 2],
		8: [3, 2, 3, 2, 1, 2, 1, 0, 1],
		}
		
		self.__level = 0

		self.__visited = {}
		self.__visitedAUX = {}
		
		print('Sua configuracao inicial')
		self.printMatrix(self.__finalState)
		sleep(5)
		self.clearTerminal()
		self.shufflePuzzle(self.__initialState, 10)
		print('Seu puzzle embaralhado')
		self.printMatrix(self.__initialState)
		
		self.__initialStateAUX = deepcopy(self.__initialState)
		
		self.__visited[tuple(self.__initialState)] = 0
		self.__visitedAUX[tuple(self.__initialStateAUX)] = 0
		
	
	
	def getFinalState(self):
		return self.__finalState
		
	def getInitialState(self):
		self.printMatrix(self.__initialState)
	
	def getInitialStateAUX(self):
		self.printMatrix(self.__initialStateAUX)
		
	def getFinalLevel(self):
		return self.__level
	
	def clearTerminal(self):
		os.system('cls' if os.name == 'nt' else 'clear')
	
	def printMatrix(self, m):
		print()
		pos = deepcopy(m)
		
		if type(pos[0]) == int:
			i = pos.index(0)
			
			pos[i] = ' '
			
			valor =('| {} | {} | {} |\n'+
					 '| {} | {} | {} |\n'+
					 '| {} | {} | {} |\n').format(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8])
			print(valor)
			sleep(0.5)
		else:
			for item in pos:
				i = item.index(0)
			
				item[i] = ' '
				
				valor =('| {} | {} | {} |\n'+
						 '| {} | {} | {} |\n'+
						 '| {} | {} | {} |\n').format(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8])
				print(valor)
				sleep(0.5)
				
				
		

	def swap(self, m, pos_1, pos_2):
		
		m[int(pos_1)], m[int(pos_2)] = m[int(pos_2)], m[int(pos_1)]
		
		return m

	def getIndex_zero(self, m):
		return m.index(0)


	def shufflePuzzle(self, p, n):
		for i in range(n):
			print('Embaralhando seu puzzle')
			j = self.getIndex_zero(p)
			rand = randint(0, len(self.__movesList[j])-1)
			move = self.__movesList[j]
			p = self.swap(p, j, move[rand])
			
			self.printMatrix(p)
			self.clearTerminal()
	
	def solvePuzzle(self):
		accept = False
		index = 0
		result = 0
		print()
		
		if tuple(self.__finalState) in self.__visited.keys():
			print(self.__finallState)
			print(len(self.__visited))
			return 0
		
		while not accept:
			sons = [son for son in self.__visited if self.__visited[son] == index]
			self.__level+=1

			for son in sons:
				z = self.getIndex_zero(list(son))
				for x in self.__movesList[z]:
					new_son = self.swap(list(son), z, x)
					result+= 1
					
					
					if tuple(new_son) not in self.__visited:
						self.__visited[tuple(new_son)] = index + 1
					
					if new_son == self.__finalState:
						accept = True
						return result
			index+= 1
	
	def getManhattanD(self, m):
		dist = 0
		
		for i in m:
			index = m.index(i)
			d_vector = self.__distanceDict[i]
			dist+= d_vector[index]
		
		return dist
		
	def sort_func(element):
		return element[1]

	def solvePuzzleManhattan(self):
		accept = False
		result = 0
		index = 0
		way = {}
		print()
		distance_now = 10000000000
		sorted_list = [tuple([tuple(son), self.getManhattanD(son)]) for son in self.__visitedAUX if self.__visitedAUX[son] == index]
		sorted_list.sort(key=Puzzle.sort_func)
		
		
		while not accept:			
	
			if list(sorted_list[0][0]) == self.__finalState:
				accept = True
				tree = []
				result+=1
				item =  list(way.keys())
				item = item[-1]
				
				root = False
				
				while not root:
					tree.append(list(item))
					item = way[tuple(item)]
					if list(item) == self.__initialState:
						root = True
					

				
				tree.append(self.__initialState)
				tree.reverse()
				self.printMatrix(tree)
				
					
				return len(tree)-1, result
			
			z = self.getIndex_zero(list(sorted_list[0][0]))
			
			for x in self.__movesList[z]:
				new_son = tuple(self.swap(list(sorted_list[0][0]), z, x))
				if new_son in self.__visitedAUX:
					continue
				self.__visitedAUX[new_son] = index + 1
				way[deepcopy(new_son)] = list(deepcopy(sorted_list[0][0]))

				sorted_list.append(tuple([new_son, self.getManhattanD(list(new_son))]))
			

			sorted_list.pop(0)
			result+=1	
			
			sorted_list.sort(key=Puzzle.sort_func)
	
