import pandas
from pathlib import Path
import matplotlib
import csv
import os

data_dict = {
    'g_x_mean': [],
    'g_x_std': [],
    'g_x_max': [],
    'g_x_min':[],
    'g_x_max_to_min': [],
    'g_x_median': [],
    'g_y_mean': [],
    'g_y_std': [],
    'g_y_max': [],
    'g_y_min': [],
    'g_y_max_to_min': [],
    'g_y_median': [],
    'g_z_mean': [],
    'g_z_std': [],
    'g_z_max': [],
    'g_z_min': [],
    'g_z_max_to_min': [],
    'g_z_median': [],
    'a_x_mean': [],
    'a_x_std': [],
    'a_x_max': [],
    'a_x_min':[],
    'a_x_max_to_min': [],
    'a_x_median': [],
    'a_y_mean': [],
    'a_y_std': [],
    'a_y_max': [],
    'a_y_min': [],
    'a_y_max_to_min': [],
    'a_y_median': [],
    'a_z_mean': [],
    'a_z_std': [],
    'a_z_max': [],
    'a_z_min': [],
    'a_z_max_to_min': [],
    'a_z_median': [],
    'motion': []
}

def gyroscope_function(directory_path, result_file):
    filepath = os.path.join(directory_path, result_file)
    data = pandas.read_csv(filepath)
    data = data.rolling(10, step = 5).mean()
    
    x_mean = data["x"].mean()
    x_standard_deviation = data["x"].std()
    x_max = data["x"].max()
    x_min = data["x"].min()
    x_max_to_min = x_max - x_min
    x_median = data["x"].median()
    data_dict['g_x_mean'].append(x_mean)
    data_dict['g_x_std'].append(x_standard_deviation)
    data_dict['g_x_max'].append(x_max)
    data_dict['g_x_min'].append(x_min)
    data_dict['g_x_max_to_min'].append(x_max_to_min)
    data_dict['g_x_median'].append(x_median)
    
    y_mean = data["y"].mean()
    y_standard_deviation = data["y"].std()
    y_max = data["y"].max()
    y_min = data["y"].min()
    y_max_to_min = y_max - y_min
    y_median = data["y"].median()
    data_dict['g_y_mean'].append(y_mean)
    data_dict['g_y_std'].append(y_standard_deviation)
    data_dict['g_y_max'].append(y_max)
    data_dict['g_y_min'].append(y_min)
    data_dict['g_y_max_to_min'].append(y_max_to_min)
    data_dict['g_y_median'].append(y_median)
    
    z_mean = data["z"].mean()
    z_standard_deviation = data["z"].std()
    z_max = data["z"].max()
    z_min = data["z"].min()
    z_max_to_min = z_max - z_min
    z_median = data["z"].median()
    data_dict['g_z_mean'].append(z_mean)
    data_dict['g_z_std'].append(z_standard_deviation)
    data_dict['g_z_max'].append(z_max)
    data_dict['g_z_min'].append(z_min)
    data_dict['g_z_max_to_min'].append(z_max_to_min)
    data_dict['g_z_median'].append(z_median)

    
def accelerometer_function(directory_path, result_file):
    filepath = os.path.join(directory_path, result_file)
    data = pandas.read_csv(filepath)
    data = data.rolling(10, step = 5).mean()
    
    x_mean = data["x"].mean()
    x_standard_deviation = data["x"].std()
    x_max = data["x"].max()
    x_min = data["x"].min()
    x_max_to_min = x_max - x_min
    x_median = data["x"].median()
    data_dict['a_x_mean'].append(x_mean)
    data_dict['a_x_std'].append(x_standard_deviation)
    data_dict['a_x_max'].append(x_max)
    data_dict['a_x_min'].append(x_min)
    data_dict['a_x_max_to_min'].append(x_max_to_min)
    data_dict['a_x_median'].append(x_median)
    
    y_mean = data["y"].mean()
    y_standard_deviation = data["y"].std()
    y_max = data["y"].max()
    y_min = data["y"].min()
    y_max_to_min = y_max - y_min
    y_median = data["y"].median()
    data_dict['a_y_mean'].append(y_mean)
    data_dict['a_y_std'].append(y_standard_deviation)
    data_dict['a_y_max'].append(y_max)
    data_dict['a_y_min'].append(y_min)
    data_dict['a_y_max_to_min'].append(y_max_to_min)
    data_dict['a_y_median'].append(y_median)
    
    z_mean = data["z"].mean()
    z_standard_deviation = data["z"].std()
    z_max = data["z"].max()
    z_min = data["z"].min()
    z_max_to_min = z_max - z_min
    z_median = data["z"].median()
    data_dict['a_z_mean'].append(z_mean)
    data_dict['a_z_std'].append(z_standard_deviation)
    data_dict['a_z_max'].append(z_max)
    data_dict['a_z_min'].append(z_min)
    data_dict['a_z_max_to_min'].append(z_max_to_min)
    data_dict['a_z_median'].append(z_median)
    

if __name__ == "__main__":
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/dws_1"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/dws_1"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Downstairs")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/jog_9"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/jog_9"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Jog")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/sit_5"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/sit_5"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Sit")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/std_6"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/std_6"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Stand")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/ups_3"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/ups_3"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Upstairs")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/wlk_7"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/wlk_7"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Walk")
    
    
    
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/dws_2"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/dws_2"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Downstairs")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/jog_16"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/jog_16"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Jog")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/sit_13"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/sit_13"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Sit")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/std_14"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/std_14"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Stand")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/ups_4"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/ups_4"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Upstairs")
    for i in range(1, 25):
        filename = f'sub_{i}.csv'
        directoryname = "C_Gyroscope_data/wlk_8"
        gyroscope_function(directoryname, filename)
        directoryname = "B_Accelerometer_data/wlk_8"
        accelerometer_function(directoryname, filename)
        data_dict['motion'].append("Walk")
        
    with open('finalresults.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_dict.keys())
        rows = zip(*data_dict.values())
        writer.writerows(rows)