# Purpose
This is a tiny script for grabbing the croud level from [https://www.boulderwelt-muenchen-ost.de/]. Basically just to satisfy my curiosity.

# Installation
After cloning the repository, make sure that the following is installed:
- bs4
- pathlib
- lxml

# Usage
Just type
```
./log_level.py
```
into the shell of your choice. This will start logging into LOG_DIR, every INTERVAL seconds. Those values are configurable in code in `log_level.py`.  
