# test-commit-revert
A simple example of a code written with TCR (test && commit || revert ) programming workflow.

# Intro
In TCR  a little test and its real code is written, if the test pass the code is commited, if not the code is hard reverted just before starting going wrong.
This is interesting because this asks for very tiny steps in order to get things working, and also to avoid retyping so much code again when there's failure. 

Also the programmer gets instant feedback about every code decision made. :)

# So...
Many people could hate this when they find themselves not reaching something relevant without getting the code reverted many times, me included.
However it starts paying you once you get it smoothly. At the end of the day it is TDD, but with some twists that closes much 
more the place for errors, bugs and ideally bad code design.

# Source
Original tutorial here if you want to give it a try: 
[TCR, by Kent Beck... ](https://www.youtube.com/watch?v=Aof0F9DvTFg&list=PLlmVY7qtgT_nhLyIbeAaUlFOWbWT5y53t)


