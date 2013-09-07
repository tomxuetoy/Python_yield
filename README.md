Python_yield
============

Python yield: to show how to use yield in Python


RTFM

generator.send(value) 
Resumes the execution and “sends” a value into the generator function. The value argument becomes the result of the
current yield expression. The send() method returns the next value yielded by the generator, or raises StopIteration if
the generator exits without yielding another value. When send() is called to start the generator, it must be called with
None as the argument, because there is no yield expression that could receive the value.
