import random
import time
import matplotlib.pyplot as plt

def search_in_sequence(sequence, value):
    return value in sequence

def generate_random_unique_sequence(length, target_position):
    sequence = random.sample(range(1, length + 1), length)
    
    # Place the search value at a specific position
    if target_position == 'Start':
        search_value = sequence[0]
    elif target_position == 'Middle':
        search_value = sequence[length // 2]
    elif target_position == 'End':
        search_value = sequence[-1]
    else:
        search_value = sequence[0]  # Default fallback
    
    return sequence, search_value

def plot_time_complexity(x, y, title):
    plt.plot(x, y, marker='o')
    plt.xlabel('Sequence Length')
    plt.ylabel('Average Time (seconds)')
    plt.title(title)
    plt.grid(True)
    plt.show()

sequence_lengths = [5000, 10000, 15000, 20000]
num_trials = 1000
search_positions = ['Start', 'Middle', 'End']
average_times = {position: [] for position in search_positions}

# Measure search time for each position
for position in search_positions:
    for length in sequence_lengths:
        total_time = 0
        for _ in range(num_trials):
            sequence, value = generate_random_unique_sequence(length, position)

            start_time = time.time()
            search_in_sequence(sequence, value)
            end_time = time.time()

            total_time += (end_time - start_time)

        average_time = total_time / num_trials
        average_times[position].append(average_time)

# Plot the results
for position in search_positions:
    plot_time_complexity(sequence_lengths, average_times[position], f'Time Complexity - Search at {position}')
