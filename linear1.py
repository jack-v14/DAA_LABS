import random
import time
import matplotlib.pyplot as plt

def search_in_sequence(sequence, value):
    return value in sequence

def generate_random_unique_sequence(length):
    return random.sample(range(1, length+1), length)

def plot_time_complexity(x, y, title):
    plt.plot(x, y, marker='o')
    plt.xlabel('Sequence Length')
    plt.ylabel('Average Time (seconds)')
    plt.title(title)
    #plt.grid(True)
    plt.show()

sequence_lengths = [5000,10000,15000,20000]  # Vary the sequence lengths as desired
num_trials = 1000

search_positions = ['Start', 'Middle', 'End']
search_values = []


for length in sequence_lengths:
    sequence = generate_random_unique_sequence(length)
    search_values.append([random.choice(sequence) for _ in range(num_trials)])
    #print(search_values)

average_times = {position: [] for position in search_positions}

for position in search_positions:
    for length, values in zip(sequence_lengths, search_values):
       total_time = 0
        for value in values:
            sequence = generate_random_unique_sequence(length)
           # sequence.sort()  # Simulating unordered sequence

            start_time = time.time()
            search_in_sequence(sequence, value)
            end_time = time.time()

            total_time += (end_time - start_time)
        average_time = total_time / num_trials
        average_times[position].append(average_time)

for position in search_positions:
    plot_time_complexity(sequence_lengths, average_times[position], f'Time Complexity - Search at {position}')
