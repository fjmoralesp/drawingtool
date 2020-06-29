## Drawing tool

### `Install dependencies`
Before running the current program, be sure to intall all the dependencies.

Please make sure to have python3 and pip installed in your OS, then run the following command:

NOTE: The installation script has been tested on MacOS, if installing on Linux or Windows, make sure to review the dependencies and install prerequisites, you may need to install dependencies by your own

`source install.sh`

### `Run the program`

Modify the **input.txt** file in the root directory with the desired params, e.g

```
C 20 4
L 1 2 6 2
L 6 3 6 4
R 16 1 20 3
B 10 3 o
```

Then run:

`./run.sh`

NOTE: The first run might take a while since python needs to generate all the __pycache__ from the second run, it should be faster

An **o​utput.txt** file will be created in the root directory with the program results

### `Run Unit tests and Code Coverage`
To excecute the tests and generate the code coverage run:

`./runTests.sh`

`./runCoverage.sh`
