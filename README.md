# test-commit-revert
A simple example of a code written with TCR (test && commit || revert ) programming workflow.

# Intro
In TCR you write a little test and its real code, if the test pass your change is commited, if not your code is hard reverted just before starting going wrong.
This is interesting since you need to take really tiny steps in order to get things working, and also to avoid retyping so much code again. :)
Also you get instant feedback about every code decision you do.

# So...
Many people could hate this when they find themself not reaching something relevant without get the code reverted many times, me included, 
however it starts paying you once you get the workflow's point. At the end of the day it is jus TDD, but with some tweaks that leaves no 
place for errors. Try it, it is fun!

# Credits
Original tutorial here: [TCR, by Kent Beck... ](https://www.youtube.com/watch?v=Aof0F9DvTFg&list=PLlmVY7qtgT_nhLyIbeAaUlFOWbWT5y53t)


