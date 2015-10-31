## Testing python code with nosetests

Testing serves several purposes:

1. Be sure your code runs.
1. Be sure it does the right thing.
1. Be sure not to break it when you make new things.

We will focus on 'unit tests'. These are tests that consider units of code as
independent items to be tested. Ideally, no reads from disk, or from a network
are required. Other kinds of tests are 'end-to-end' tests, which exercise a
full pipeline of analysis

## Installing nose:

We will use the testing framework `nose`, which is also used by many of the
open source scientific software libraries (`numpy`/`scipy`/etc). With Anaconda
installed, installing `nose` should be as simple as:

    conda install nose

Alternatively, you can also use the `pip` package manager:

    pip install nose

Note that if `pip` is unavaliable you can install that via a : `conda install pip`. You get the picture.

## The `assert` statement

Before we start running `nose`, let's consider what software tests should
do. For now let's consider just the most generic case: a testing suite
should run every statement in your code, and check that the resulting variables
have the `correct` value.  against:

1. A result calculated using pencil and paper
1. A result calculated using an alternative (e.g. slower, but safer) method
1. A result calculated with a previous version of the software that you have
some reason to believe is true (this is called 'regression testing').

Thus, testing software relies on making specific assertions about what you
expect the code to do. This uses the python `assert` statement. This statement
evaluates the Truth of an expression, and then raises an error if the statement
is false:


    a = 1
    b = 1
    c = 2
    assert a == b  # nothing happens
    assert b == c  # raises error

If you want, you can raise an informative error:

    assert b == c, "%s is not equal to %s"%(b,c)

To use this as a test for your analysis code, consider the following function
to calculate the area of a circle:

    def area(r):
        return np.pi * (r ** 2)

We can assert our expectation that the area of a circle with radius of
1 will be equal to pi in the following python statement

    assert area(1) == np.pi

We might also expect the area of a circle with radius sqrt(pi) to be
equal to pi squared:

    assert area(np.sqrt(np.p)) == np.pi ** 2

But this raises an AssertionError. Why? This demonstrates the limitations that
computers have in representing real numbers. Often our calculations will be
approximations, or will be susceptible to this kind of floating point error.
Instead of requiring strict equality, we can instead state what level of
precision we can guarantee:

    assert np.abs(area(np.sqrt(np.pi))-(np.pi ** 2)) < 10e-15

This means that even when you are not able to provide an *exact* answer, you
can still test that your answer is *close enough*. What *enough* means, depends
on the specifics of your analysis. A particle physicist might require precision
to 15 significant digits, but most biologists are happy if they can get the
sign right...

## Using `nose` to automate tests:

The `nosetests` application seeks files named `test_*.py` in the file paths
below the pwd, and runs every function in these files that is defined as `def
test_*()`. If all these functions run with no error, and no failed assertions,
then nose reports back with the number of functions that have been
run. Otherwise, errors and assertion failures are reported.

Let's examine the simple module `circle.py` and its test file `test_circle.py`
as an example of this.

##
