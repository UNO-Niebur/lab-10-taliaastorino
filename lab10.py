import matplotlib.pyplot as plt
import csv

trials = []
reaction_times = []

with open('reaction_time_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            trial = int(row['Trial'])
            time = float(row['ReactionTime_ms'])
            
            if time > 0:
                trials.append(trial)
                reaction_times.append(time)
        except:
            continue

plt.plot(trials, reaction_times, marker='o')

plt.xlabel('Trial Number')
plt.ylabel('Reaction Time (ms)')
plt.title('Reaction Time Across Trials')

plt.savefig('reaction_time_graph.png')
plt.show()
