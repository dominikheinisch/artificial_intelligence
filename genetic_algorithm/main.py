import time

from genetic_algorithm import MultipleSimulation
from genetic_algorithm import SelectionType


def main():
    start = time.time()
    files = ['had12.dat', 'had14.dat', 'had16.dat', 'had18.dat', 'had20.dat', 'chr25a.dat', 'nug28.dat']
    result_filename = 'result.csv'
    multiple_sim = MultipleSimulation(filename=files[4], result_filename=result_filename,
                                      no_iter=2, pop_size=200, gen_size=100, prob_cross=0.8, prob_mutate=0.1,
                                      save_best=False, selection_type=SelectionType.TOURNAMENT_TYPE, tournament_size=5)
    multiple_sim.run()
    print("simulation time:")
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()
