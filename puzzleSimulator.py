from puzzle8 import Puzzle

def main():
	puzzle8 = Puzzle([1,2,3,4,5,6,7,8,0])
	#print('Resolvido em {} tentativas'.format(puzzle8.solvePuzzle()))
	print(puzzle8.solvePuzzleManhattan())


if __name__ == "__main__":
	main()