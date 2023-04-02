# testing-py-game
Example of unit testing on pyGame

 * unittest is a built-in framework in python 3
 * the software under test is a simple class ( MovableCircle) that moves a circle using basic gaming keys ( wasd )
 * the circle class contains an additional feature when pressing key "q" for exiting will help showing the testing the behaviour of running flag.
 * the unit test class ( MovableCircleTest ) has an example of mocking function for modeling the pressing of "q" key.

## running
```
python3 circle.py
```
## unit testing
```
python3 -m unittest
```

## further reading
unittest [framework](https://docs.python.org/3/library/unittest.html)
