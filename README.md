# Printr

Printr is a simple PyPi module that allows for print statements to be replaces with a new line. Particularly useful for displaying progress messages.


## Installation
Installation can be done using pip in the standard way:
```
pip install python-printr
```
If you have python 3 installed, then install using `pip3`. There are no dependancies for this package, so installation should go ahead fine.

Alternatively, you can download directly from Pypi [here](https://pypi.python.org/pypi/Python-Printr/).

## Usage
```
import printr

printr.get_version()
>>> 0.0.3
```
The printr module contains various different printrs to assist you. You can find more information about these printrs on the wiki.

The main reason I wrote this project was to simplify status output for my projects, and because I'd never written a PyPi package before.