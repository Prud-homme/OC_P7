# AlgoInvest&Trade - Algorithm for investment


## Menu

* [Overview](#overview)
* [Program setup](#program-setup)
* [Program execution](#program-execution)
* [flake8](#flake8)

## Program setup

### Creation of a virtual environment

**On Windows**
```
$ python3 -m venv c:\path\to\myenv
$ myenv\Scripts\activate.bat
```

**On Unix or MacOS**
```
$ python3 -m venv /path/to/myenv
$ source myenv/bin/activate
```

**To install packages from the requirements.txt file**
```
(myenv) $ pip3 install -r requirements.txt
```

**To disable the virtual environment, run:**
```
(myenv) $ deactivate
```

## Program execution

When the virtual environment is activated and you are placed in the folder where the main file is located, launch the program with the command:
```
(myenv) $ python3 __main__.py
```

Then a window will appear to select your file with shares. Once the program is finished, the recommended investment appears in the console but is also available in a text file.
This text file is located in the same place as your data.

🗒️ *Note: Depending on the installation of python it is possible that the `python3` command is not recognized under windows. In this case, you will have to replace `python3` by `python`.*

⚠️ The shares should be represented as below:

| name     | price   | profit  |
| -------- | ------- | ------- |
| Share-1  | 10.40   | 14.23   |
| Share-2  | 6.05    | 25.48   |
| Share-3  | 20.96   | 3.76    |
| ...      | ...     | ...     |

## flake8

flake8 allows you to validate your Python code against the PEP 8 coding conventions and pyflakes.

The .flake8 file allows to configure flake8 and thus it will be enough to launch the `flake8` command to generate the report.
The report is generated in the *flake-report* folder under the name *index.html*. To open the report open the *index.html* file with a web browser.