# csv plotter

###### author: yahya ahmed adeem | date created: 2020 mar 17

### description

this program takes the data from one or more csv file and plots it
and either shows the plot or writes it into a .png file

enter `./plot.py help` in your terminal for general instructions

#### usage examples
make sure you place your files in the `csvs` folder
  
##### example 1: one .csv file, show plot
```
./plot.py file.csv
```
##### example 2: one .csv file, write to .png file
```
./plot.py file.csv --write output.png
```
##### example 3: multiple .csv files, show plots
```
./plot.py file1.csv file2.csv
```
##### example 4: multiple .csv files, write to .png files
```
./plot.py file1.csv file2.csv --write output1.png output2.png
```
the data from `file1.csv` is written to `output1.png` and the data
from `file2.csv` is written to `output2.png` and so on

#### logarithmic scales

if you want to plot a graph with a logarithmic scale, put `log_`,
`xlog_`, or `ylog_` in front of the name of the .csv file depending
on which axis you want to have a logarithmic scale

##### example 1: logarithmic scale for x axis

```
./plot.py xlog_plot.csv
```
##### example 2: logarithmic scale for y axis

```
./plot.py ylog_plot.csv
```
##### example 3: logarithmic scale for both axes

```
./plot.py log_plot.csv
```

#### tips on how to format your .csv file for this program

- you can make a .csv file using ms excel or, if you're like
me and don't want to pay microsoft for readily available
functionality, you can use google sheets or libreoffice;
generally, anything that can be used to make spreadsheets
- your spreadsheet needs to have two columns, one for the
horizontal axis and the other for the vertical axis
- the first row of the spreadsheet should always be the
axis labels
- **optional**: the first row of the third column can be used to specify a
color for the plot either by using rgb values or one of the following 
preset colors:
    - r: red
    - g: green
    - b: blue
    - c: cyan
    - m: magenta
    - y: yellow
    - k: black
    - w: white
- your spreadsheet should look something like this:

    | **$x$ | $x^2$ | 128,174,87 |
    |:---:|:---:|:---:|
    | 1 | 1 |
    | 2 | 4 |
    | 3 | 9 |
    | 4 | 16|
    | 5 | 25|
    
    _**it would help if the axis labels have LaTeX formatting
to make the labels look half-decent in the actual plot_
- finally, you can just export the spreadsheet as a .csv file
