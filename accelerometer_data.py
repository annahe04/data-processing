import pandas
from pathlib import Path
import matplotlib

directory_path = Path("results/acceleration_results")

def results_function(result_file, csv_file):
    file_path = directory_path / result_file
    file = open(file_path, "a")
    data = pandas.read_csv(csv_file)
    data = data.rolling(5, step = 1).mean()
    
    mean = data["x"].mean()
    standard_deviation = data["x"].std()
    max = data["x"].max()
    min = data["x"].min()
    max_to_min = max - min
    root_mean_square = (data["x"] ** 2).mean() ** 0.5
    string = f"[{mean}, {standard_deviation}, {max}, {min}, {max_to_min}, {root_mean_square}]"
    file.write(string + "\n")
    
    mean = data["y"].mean()
    standard_deviation = data["y"].std()
    max = data["y"].max()
    min = data["y"].min()
    max_to_min = max - min
    root_mean_square = (data["y"] ** 2).mean() ** 0.5
    string = f"[{mean}, {standard_deviation}, {max}, {min}, {max_to_min}, {root_mean_square}]"
    file.write(string + "\n")
    
    mean = data["z"].mean()
    standard_deviation = data["z"].std()
    max = data["z"].max()
    min = data["z"].min()
    max_to_min = max - min
    root_mean_square = (data["z"] ** 2).mean() ** 0.5
    string = f"[{mean}, {standard_deviation}, {max}, {min}, {max_to_min}, {root_mean_square}]"
    file.write(string + "\n")
    
    file.close()
    
    
    

if __name__ == "__main__":
    # results_function("dws_6.txt", "C_Gyroscope_data/dws_1/sub_6.csv")
    # results_function("dws_7.txt", "C_Gyroscope_data/dws_1/sub_7.csv")
    # results_function("dws_8.txt", "C_Gyroscope_data/dws_1/sub_8.csv")
    # results_function("dws_9.txt", "C_Gyroscope_data/dws_1/sub_9.csv")
    # results_function("dws_10.txt", "C_Gyroscope_data/dws_1/sub_10.csv")
    
    # results_function("jog_6.txt", "C_Gyroscope_data/jog_9/sub_6.csv")
    # results_function("jog_7.txt", "C_Gyroscope_data/jog_9/sub_7.csv")
    # results_function("jog_8.txt", "C_Gyroscope_data/jog_9/sub_8.csv")
    # results_function("jog_9.txt", "C_Gyroscope_data/jog_9/sub_9.csv")
    # results_function("jog_10.txt", "C_Gyroscope_data/jog_9/sub_10.csv")
    
    # results_function("sit_6.txt", "C_Gyroscope_data/sit_5/sub_6.csv")
    # results_function("sit_7.txt", "C_Gyroscope_data/sit_5/sub_7.csv")
    # results_function("sit_8.txt", "C_Gyroscope_data/sit_5/sub_8.csv")
    # results_function("sit_9.txt", "C_Gyroscope_data/sit_5/sub_9.csv")
    # results_function("sit_10.txt", "C_Gyroscope_data/sit_5/sub_10.csv")
    
    # results_function("std_6.txt", "C_Gyroscope_data/std_6/sub_6.csv")
    # results_function("std_7.txt", "C_Gyroscope_data/std_6/sub_7.csv")
    # results_function("std_8.txt", "C_Gyroscope_data/std_6/sub_8.csv")
    # results_function("std_9.txt", "C_Gyroscope_data/std_6/sub_9.csv")
    # results_function("std_10.txt", "C_Gyroscope_data/std_6/sub_10.csv")
    
    # results_function("ups_6.txt", "C_Gyroscope_data/ups_3/sub_6.csv")
    # results_function("ups_7.txt", "C_Gyroscope_data/ups_3/sub_7.csv")
    # results_function("ups_8.txt", "C_Gyroscope_data/ups_3/sub_8.csv")
    # results_function("ups_9.txt", "C_Gyroscope_data/ups_3/sub_9.csv")
    # results_function("ups_10.txt", "C_Gyroscope_data/ups_3/sub_10.csv")
    
    # results_function("wlk_6.txt", "C_Gyroscope_data/wlk_7/sub_6.csv")
    # results_function("wlk_7.txt", "C_Gyroscope_data/wlk_7/sub_7.csv")
    # results_function("wlk_8.txt", "C_Gyroscope_data/wlk_7/sub_8.csv")
    # results_function("wlk_9.txt", "C_Gyroscope_data/wlk_7/sub_9.csv")
    # results_function("wlk_10.txt", "C_Gyroscope_data/wlk_7/sub_10.csv")
    
    
    results_function("dws_6.txt", "B_Accelerometer_data/dws_1/sub_6.csv")
    results_function("dws_7.txt", "B_Accelerometer_data/dws_1/sub_7.csv")
    results_function("dws_8.txt", "B_Accelerometer_data/dws_1/sub_8.csv")
    results_function("dws_9.txt", "B_Accelerometer_data/dws_1/sub_9.csv")
    results_function("dws_10.txt", "B_Accelerometer_data/dws_1/sub_10.csv")
    
    results_function("jog_6.txt", "B_Accelerometer_data/jog_9/sub_6.csv")
    results_function("jog_7.txt", "B_Accelerometer_data/jog_9/sub_7.csv")
    results_function("jog_8.txt", "B_Accelerometer_data/jog_9/sub_8.csv")
    results_function("jog_9.txt", "B_Accelerometer_data/jog_9/sub_9.csv")
    results_function("jog_10.txt", "B_Accelerometer_data/jog_9/sub_10.csv")
    
    results_function("sit_6.txt", "B_Accelerometer_data/sit_5/sub_6.csv")
    results_function("sit_7.txt", "B_Accelerometer_data/sit_5/sub_7.csv")
    results_function("sit_8.txt", "B_Accelerometer_data/sit_5/sub_8.csv")
    results_function("sit_9.txt", "B_Accelerometer_data/sit_5/sub_9.csv")
    results_function("sit_10.txt", "B_Accelerometer_data/sit_5/sub_10.csv")
    
    results_function("std_6.txt", "B_Accelerometer_data/std_6/sub_6.csv")
    results_function("std_7.txt", "B_Accelerometer_data/std_6/sub_7.csv")
    results_function("std_8.txt", "B_Accelerometer_data/std_6/sub_8.csv")
    results_function("std_9.txt", "B_Accelerometer_data/std_6/sub_9.csv")
    results_function("std_10.txt", "B_Accelerometer_data/std_6/sub_10.csv")
    
    results_function("ups_6.txt", "B_Accelerometer_data/ups_3/sub_6.csv")
    results_function("ups_7.txt", "B_Accelerometer_data/ups_3/sub_7.csv")
    results_function("ups_8.txt", "B_Accelerometer_data/ups_3/sub_8.csv")
    results_function("ups_9.txt", "B_Accelerometer_data/ups_3/sub_9.csv")
    results_function("ups_10.txt", "B_Accelerometer_data/ups_3/sub_10.csv")
    
    results_function("wlk_6.txt", "B_Accelerometer_data/wlk_7/sub_6.csv")
    results_function("wlk_7.txt", "B_Accelerometer_data/wlk_7/sub_7.csv")
    results_function("wlk_8.txt", "B_Accelerometer_data/wlk_7/sub_8.csv")
    results_function("wlk_9.txt", "B_Accelerometer_data/wlk_7/sub_9.csv")
    results_function("wlk_10.txt", "B_Accelerometer_data/wlk_7/sub_10.csv")
    
    
    