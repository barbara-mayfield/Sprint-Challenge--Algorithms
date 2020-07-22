#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) This a single loop. As n increases runtime increases linearly.

b) O(n^2) The inner loop is executed i times. Outer is executed n times.

c) O(n) The function will be called n times. The recursion calls the function again.

## Exercise II

We have an n-story building (1 to n) and e = lots of eggs.

An egg gets broken if it is thrown off a floor f or higher, but does not get broken if dropped off a floor less than floor f.

We are trying to find the value of f (the highest floor
an egg can be dropped without breaking).

What comes to mind is a binary search. Keep dividing n in half until we find the point where the egg does not break, but any higher and it will.
