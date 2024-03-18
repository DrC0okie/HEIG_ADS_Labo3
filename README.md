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



## Task 3 : Concersion to CSV


