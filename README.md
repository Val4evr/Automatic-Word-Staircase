# Automatic-Word-Staircase
Datamuse API Alphabetic Word Staircase solver

# The Alphabetic Word Staircase:

This is a simple game with the following rules:
1. A letter is selected at random
2. A list of words is created, with the first entry being only that letter
3. Words beggining with the letter get continuously added to the list, in ascending length.
4. The length of the word must equal its index in the list (starting with 1). 
5. Person with longest list after a set time wins. 

## Example:
1.  u
2.  up
3.  use
4.  unit
5.  upset
6.  unique
7.  uncanny
8.  ultimate
9.  undertake
10. ubiquitous
11. unequivocal
12. unscrupulous
13. understanding
14. unconscionable
15. unprepossessing
16. ultracrepidarian
17. understandability
18. unsatisfactoriness
19. ultracrepidarianism
20. uncharacteristically
21. ureterohydronephrosis

Longer word not found.

# The solver:
It is a simple script that sends GET requests to the Datamuse API.

# Installation:
Just find a suitable location, clone the repo and run main.py:
```
cd Documents/Programming
git clone https://github.com/Val4evr/Automatic-Word-Staircase.git
cd Automatic-Word-Staircase
python main.py
```