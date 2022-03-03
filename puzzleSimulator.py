from puzzle8 import Puzzle
from time import sleep

def main():
	puzzle8 = Puzzle([1,2,3,4,5,6,7,8,0])
	
	print('Seu puzzle embaralhado')
	puzzle8.print_matrix(puzzle8.get_initial_state())

	sleep(5)
	puzzle8.clear_terminal()

	print('Resolvendo seu puzzle')
	puzzle8.print_matrix(puzzle8.get_initial_state())

	sleep(5)
	puzzle8.clear_terminal()


	print('Resolvido em {} tentativas via busca em largura'.format(puzzle8.solve_puzzle_bfs()))
		
	
	
	best_way, attempts = puzzle8.solve_puzzle_manhattan()
	print('Resolvido em {} tentativas via distancia Manhattan\nA solucao minima necessita de {} tentativas e se encontra acima'.format(attempts, best_way))


if __name__ == "__main__":
	main()
