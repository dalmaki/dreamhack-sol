# Solution

Use stack smashing method.

The variable `name` is allocated to the stack. Note that the return pointer is also allocated at the lower part of the stack; The catch is to change this _return pointer value_ to `win`.

Variable `name` can be anything.
Set the hex value to 40125B (position of `win` void pointer)
And integer to 16 (Change all of the visible stack values)
