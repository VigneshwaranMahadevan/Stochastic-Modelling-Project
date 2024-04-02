import itertools
from typing import Iterator
import numpy as np
from collections import deque

class Umbrellas:
    def __init__(self , r , p):
        self.r = r
        self.p = p

        # Let states be defined as  ( number of umbrellas at home , place you are at )
        # So , number of states is 2*(r+1)
        # [ (0,h) , (0,o) , (1,h) , ... (r-1,o)  , (r,h)   , (r,o) ]
        #    S0   ,  S1   ,  S2         S_{2r-1} ,  S_{2r} , S_{2r+1}
        # self.P is the probability distribution of the states
        
        # Intiialise pi_0 randomly
        self.pi = np.zeros((r+1)*2).reshape(-1,(r+1)*2)
        self.pi[0,:] = 1/(2*(r+1))
        
        # Transition Probability Matrix P
        self.P = np.zeros((2*(r+1),2*(r+1)))

        even_indices = np.arange(2,2*r+1,2)
        self.P[even_indices, even_indices + 1] = 1 - self.p
        self.P[even_indices, even_indices - 1] = self.p
        odd_indices = np.arange(1,2*r+1,2)
        self.P[odd_indices, odd_indices + 1] = self.p
        self.P[odd_indices, odd_indices - 1] = 1 - self.p

        self.P[0,1] = 1
        self.P[2*r+1,2*r] = 1

        #Steady State Probabilities
        self.pi = self.converge(self.one_step_transition(self.pi), 0.001)
        self.pi = itertools.islice(self.pi, 10000)
        self.pi = list(deque(self.pi)[-1])[0]

    def converge(self, pi: Iterator[np.ndarray], threshold: float) -> Iterator[np.ndarray]:
        for a, b in itertools.pairwise(pi):
            yield a 
            if (np.abs(a - b) < threshold).all():
                break

    def one_step_transition(self, pi: np.ndarray):
        while True:
            pi = np.matmul(pi, self.P)
            yield pi
    
    def part1(self):
        # Man gets wet when
        # there are no umbrellas at home and raining -> (0,h) 
        # there are no umbrellas at office and raining -> (r,o)
        # So total probab is p * ( P(0,h) + P(r,o) )
        return self.p * (self.pi[0] + self.pi[2*self.r+1])

