
# ADS Lab 03 - Pipelines
Authors : Felix Breval, Anthony David, Timothée Van HOve
Group : Lab_3_C
Date: 2024-03-24

## Task 1 : Exercices on redirection
> Compile the following C++ program, called out.cpp , into an executable. The program writes a series of O characters on the stdout stream and a series of E characters
on the stderr stream:

```c++
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    for (int i = 0; i < 5; ++i) {
        cout << "O";
        cerr << "E";
    }
    return EXIT_SUCCESS;
}

```
> Run the executable with ./out
> 1. Run the following commands and tell where stdout and stderr are redirected to.
> 1. Run the following commands and tell where stdout and stderr are redirected to.
> a. ./out > file 

// todo

> b. ./out 2> file 

// todo

> c. ./out > file 2>&1 

// todo

> d. ./out 2>&1 > file

// todo

> e. ./out &> file


## Task 2 :



## Task 3 : Conversion to CSV
> In this task you will use the command line to summarize the log entries and convert the summary into a CSV file that can be read by a spreadsheet program. A CSV (Comma-Separated Values) file is a file containing a table in text format. It starts with a line containing the column names. Each name is speparated by a comma ,. The remaining lines contain the rows of the table, one line per row. Each line contains the cells of the corresponding row, again separated by commas. Here is an example of a CSV file:
```
Element, Atomic Mass
H, 1.008
He, 4.002602
Li, 6.94
Be, 9.0121831
```
>Note: Spreadsheet software typically tolerates spaces between the values and the commas and removes them. In a spreadsheet the order of columns is not important. Depending on the language of your computer, your spreadsheet may use another character than comma , to separate the columns, for example Excel in French expects semicolon ;.
>
>Produce a CSV file named accesses.csv that contains for each day (given by its date)the number of accesses on that day. Transfer that file to your workstation and use spreadsheet software to import the CSV file. Plot the data in a graph and produce a file named accesses.pdf .
>
>Notes :
>
>- Make sure the spreadsheet software correctly interprets the date fields as
>  dates and not as text.
>- The dates in the file will not be continuous, i.e. there are days without any
>  accesses which will not appear in the file. Choose a type of plot appropriate
>  for this case.

// todo

## Task 3

Command used: 

```bash
grep -o '\[[0-9]*/[A-Z][a-z]*/[0-9]*:[0-9]*:[0-9]*' ads_website.log | cut -d'/' -f1-2 | sort | uniq -c | tr -d  '[' | sed -e 's/^ *//;s/ /,/'> accesses.csv
```

To create the csv, I used python. it can be easily run by doing:

```bash
python3 script.py
```