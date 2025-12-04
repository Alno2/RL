#!/usr/bin/env python3
# rewards: [golden_fish, jellyfish_1, jellyfish_2, ... , step]
# Never catching any Fish, including the King Fish
# Make catching fish strongly negative so avoiding them is optimal
rewards = [-100, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -50, -1]

# Q learning learning rate
alpha = 0.6

# Q learning discount rate
gamma = 0.3

# Epsilon initial
epsilon_initial = 1

# Epsilon final
epsilon_final = 1

# Annealing timesteps
annealing_timesteps = 1

# threshold
threshold = 1e-6
