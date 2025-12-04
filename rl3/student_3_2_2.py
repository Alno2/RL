#!/usr/bin/env python3
# rewards: [golden_fish, jellyfish_1, jellyfish_2, ... , step]
# Taking the shortest path to catch the King Fish.
# Make King Fish reward very high and jelly negative
rewards = [200, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -1]

# Q learning learning rate
alpha = 0.8

# Q learning discount rate
gamma = 0.9

# Epsilon initial
epsilon_initial = 1

# Epsilon final
epsilon_final = 1

# Annealing timesteps
annealing_timesteps = 1

# threshold
threshold = 1e-6
