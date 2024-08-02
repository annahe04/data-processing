import pandas as pd
import os
import csv

directory = 'acceleration_results_copy'

data = {
    'x_mean': [],
    'x_std': [],
    'x_max': [],
    'x_min':[],
    'y_mean': [],
    'y_std': [],
    'y_max': [],
    'y_min': [],
    'z_mean': [],
    'z_std': [],
    'z_max': [],
    'z_min': []
}

def assignment_function(filename):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as file:
        x = 1
        for line in file:
            line = line.strip()
            if x == 1:
                data['x_mean'].append(float(line))
            elif x == 2:
                data['x_std'].append(float(line))
            elif x == 3:
                data['x_max'].append(float(line))
            elif x == 4:
                data['x_min'].append(float(line))
            elif x == 5:
                data['y_mean'].append(float(line))
            elif x == 6:
                data['y_std'].append(float(line))
            elif x == 7:
                data['y_max'].append(float(line))
            elif x == 8:
                data['y_min'].append(float(line))
            elif x == 9:
                data['z_mean'].append(float(line))
            elif x == 10:
                data['z_std'].append(float(line))
            elif x == 11:
                data['z_max'].append(float(line))
            elif x == 12:
                data['z_min'].append(float(line))
            x = x + 1

if __name__ == "__main__":
    for i in range(1, 11):
        filename = f'dws_{i}.txt'
        assignment_function(filename)
    for i in range(1, 11):
        filename = f'jog_{i}.txt'
        assignment_function(filename)
    for i in range(1, 11):
        filename = f'sit_{i}.txt'
        assignment_function(filename)
    for i in range(1, 11):
        filename = f'std_{i}.txt'
        assignment_function(filename)
    for i in range(1, 11):
        filename = f'ups_{i}.txt'
        assignment_function(filename)
    for i in range(1, 11):
        filename = f'wlk_{i}.txt'
        assignment_function(filename)
    
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        rows = zip(*data.values())
        writer.writerows(rows)