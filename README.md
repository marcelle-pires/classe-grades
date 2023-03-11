# Students grades

This is a Python CLI developed during my studies. The idea is to explore the multiple funcionalities of pandas library and manipulate dataframes.

## Getting started

All required dependencies are declared in requirements.txt file, you can install of them by executing:

```bash
python -m pip install -r requirements.txt
```

This script has a virtual environment, you can activate it executing:

```bash
source env/bin/activate
```

## Installing new packages

You can install new packages using pip, as normal, but remember to include this new packages in requirements file:

```bash
python -m pip freeze > requirements.txt
```

## Run
To execute this cli, based in [fire library](https://google.github.io/python-fire/guide/), you will execute following the stardard:

```bash
python -m main [name_of function] [param1] [param2] 
```

If you need help, execute the command below and find options:
```bash
python -m main --help
```

## Test

To execute all tests generated in this script, you can execute:

```bash
python -m pytest
```

## Interesting Links

[More about me - Linkeding: Marcelle Pires](www.linkedin.com/in/marcelle-reis-pires)


