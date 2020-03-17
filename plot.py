#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt
from sys import argv, stderr, exit


def instr():
    """
    function for printing the general usage instructions
    """
    print('general usage: ./plot.py <csv_file(s)> [--write <png_file(s)>]')
    exit(0)


def parse_csv(file_name):
    """
    function for parsing the data from a .csv file and returning it in a way that pyplot can plot it

    parameters
    - file_name: name of the .csv file

    returns
    - x_data: list of x values
    - y_data: list of y values
    - labels: two-element list containing the name of the x label and y label

    - assumes that the first column of the .csv file represents the x values and the second column represents the
    y values
    - assumes the first row represents the x and y labels
    - writes the x values and y values in a separate list and returns both of them
    """

    x_data, y_data = [], []

    try:
        with open('csvs/{}'.format(file_name), 'r') as f:
            data = csv.reader(f)
            labels = next(data)

            for line in data:
                if len(line) != 2:
                    print('only two columns supported', file=stderr)
                    exit(1)
                for element in line:
                    if not element.isnumeric():
                        print('.csv file should only contain numbers', file=stderr)
                        exit(1)

                x_data.append(float(line[0]))
                y_data.append(float(line[1]))

            return x_data, y_data, labels

    except FileNotFoundError:
        print('file \'{}\' not found'.format(file_name), file=stderr)
        exit(1)


def plot(data, output=None):
    """
    function for plotting the graph for the data in the .csv file(s)

    parameters
    - data: a tuple containing a list of x values; a list of y values; the list of x and y labels
    - output: name of the output .png file

    - if output is not empty then the function will save the plot to a .png file
    """

    x_data = data[0]
    y_data = data[1]

    plt.figure()
    plt.xlabel(data[2][0])
    plt.ylabel(data[2][1])
    plt.plot(x_data, y_data, 'bo-')

    if output:
        plt.savefig('plots/{}'.format(output))


def parse_n_plot(csv_files, png_files=None):
    """
    wrapper function for parsing data and making the plot

    parameters
    - csv_files: list of input .csv files
    - png_files: list of output .png files

    - the function iterates through the list of input files and makes plots for each file
    - if png_files is empty, then the program will show the plot
    - if not, then the plots will be saved to .png files (by running the plot() function as it is)
    """

    if not png_files:
        for file in csv_files:
            data = parse_csv(file)
            plot(data)
        plt.show()
    else:
        for csv_file, png_file in zip(csv_files, png_files):
            data = parse_csv(csv_file)
            plot(data, png_file)


def ret_io_lists(args):
    """
    function for converting the list of arguments entered in the terminal to two lists containing all the input files
    and output files

    parameters
    - args: list of arguments

    returns
    - csv_files: list of input .csv files
    - png_files: list of output .png files
    """

    concatenated_args = ' '.join(args)
    csv_png_list = concatenated_args.split('--write')
    csv_files = csv_png_list[0].split()
    png_files = csv_png_list[1].split()

    if len(csv_files) == len(png_files):
        return csv_files, png_files
    else:
        print('input files don\'t match up with output files', file=stderr)
        exit(1)


def main(args):
    """
    main function

    parameters
    - args: list of arguments entered in the terminal
    """

    if args[1] == 'help':
        if len(args) > 2:
            print('just enter \'./plot.py help\' if you need instructions', file=stderr)
            exit(1)
        instr()

    if '--write' in args:
        if args[-1] == '--write':
            print('enter the names of the output files', file=stderr)
            exit(1)
        else:
            csv_files = ret_io_lists(args[1:])[0]
            png_files = ret_io_lists(args[1:])[1]
            parse_n_plot(csv_files, png_files)

    else:
        csv_files = args[1:]
        parse_n_plot(csv_files)


if __name__ == '__main__':
    main(argv)
