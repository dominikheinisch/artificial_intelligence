import matplotlib.pyplot as plt
import os


def print_results(filename, title, sides, times):
    fig, ax = plt.subplots()
    ax.plot(sides, times)
    ax.set(xlabel='graph side', ylabel='time solving [seconds]',
           title=title)
    ax.grid()
    fig.savefig(os.path.abspath(os.path.join('results', filename)))


def print_results_log(filename, title, sides, times):
    fig, ax = plt.subplots()
    ax.semilogy(sides, times)
    ax.set(xlabel='graph side', ylabel='time solving [seconds]',
           title=title)
    ax.grid()
    fig.savefig(os.path.abspath(os.path.join('results', filename)))


def print_possible_results(filename, title, sides, results):
    fig, ax = plt.subplots()
    ax.plot(sides, results)
    ax.set(xlabel='graph side', ylabel='possible results',
           title=title)
    ax.grid()
    fig.savefig(os.path.abspath(os.path.join('results', filename)))