# Coursera Dump

The programm used for searching information (like name, rating, duration, language) about courses from [coursera.org](https://coursera.org) and saving it into excel file.

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash

pip install -r requirements.txt # alternatively try pip3

```

# Quickstart

Specify filepath to script called like coursera.py into console by following:

```bash

$ python coursera.py

```

For detailed information use [-h]:

```bash

$python coursera.py -h
usage: coursera.py [-h] [--total TOTAL] [--datafile DATAFILE]

Get info about curses from coursera.org

optional arguments:
  -h, --help           show this help message and exit
  --total TOTAL        How many courses check.
  --datafile DATAFILE  File for saving information about courses

```

After the script is executed, a file with the results is created, which is called courses_info.xlsx by default.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
