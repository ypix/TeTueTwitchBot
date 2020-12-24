# Building a Python Twitch bot


This repository contains all the code for the bot constructed over the course of my series "Building a Python Twitch bot", which can be found here: https://www.youtube.com/playlist?list=PLYeOw6sTSy6ZFDkfO9Kl8d37H_3wLyNxO.

## Installation of required components

### You will need:
- Python 3.8.0 or greater;
- `irc` 18.0.0 or greater;
- `requests` 2.22.0 or greater.

### To install Python:
Download the latest version from here: https://www.python.org/downloads/.

### Pip installs:
#### On Unix based systems:
`python3.x -m pip install irc requests` (replace "x" with your subversion).
#### On Windows:
`pip install irc requests` or `py -m pip install irc requests`.

## Notes

Feel free to fork this repository and make changes as you please, but do not distribute it beyond what is stated in the copyright information in the `twitch_tut.py` file. The code in this repository is designed to be taken as a guide.

## Help

For help and enquiries, join the Carberra Discord server: https://bit.ly/carb-discord.

## References

This repository has been folked from 
* https://github.com/Technik-Tueftler/TeTueTwitchBot

This version uses rasa and tensorflow to detect abusing messages.
A simple example can be found in the file [*test_rasa.py*](./test\test_rasa.py)  

Before running example make sure the models directory in the rasa subfolder contains a trained model file. 
To create
* open a terminal
* move to folder ``rasa`` with *cd* 
* run  ``rasa train`` in the terminal

To start a test, open a terminal and execute
* ``test\test_rasa.py``

Expected oucome:

``{'text': 'Du blödes A***', 'intent': {'id': ..., 'name': 'abuse', 'confidence': 0.7838521599769592}, 'entities': ...``

The NLU data for training can be found in [nlu.yml](rasa/data/nlu.yml)

The part for abuse data starts with
```
- intent: abuse
  examples: |
    - you fucker
    - you asshole
    - sucker
```
