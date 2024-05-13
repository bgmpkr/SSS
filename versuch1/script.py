import numpy as np
import glob
import matplotlib.pyplot as plt



def read_data(file_path):
    # Read data from file
    data = np.genfromtxt(file_path, delimiter=';', skip_header=1000, usecols=(0, 1), dtype=str)

    float_data = np.zeros((len(data), 2))
    for i in range(len(data)):
        float_data[i, 0] = float(data[i, 0].replace(',', '.'))
        float_data[i, 1] = float(data[i, 1].replace(',', '.'))

    return float_data

def calculate_statistics(data):
    # Calculate mean and standard deviation
    mean = np.mean(data[:, 1])
    std_dev = np.std(data[:, 1])

    return mean, std_dev

def plot_data(data):
    plt.plot(data[:, 0], data[:, 1])
    plt.xlabel('Zeit [ms]')
    plt.ylabel('Kanal A [V]')
    plt.show()

def main():
    file_paths = glob.glob('*.csv')
    data = read_data(file_paths[0])
    for file_path in file_paths:
        next_data = read_data(file_path)
        if 'data' in locals():
            data = np.concatenate((data, next_data))
        else:
            data = next_data

    plot_data(data)
    mean, std_dev = calculate_statistics(data)
    print("Mean:", mean)
    print("Standard Deviation:", std_dev)

if __name__ == '__main__':
    main()
