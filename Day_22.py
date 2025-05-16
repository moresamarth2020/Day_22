#!/usr/bin/env python
# coding: utf-8

# # Docstrings in python
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

# In[1]:


def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)


# In[2]:


def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2


# ## Python Comments vs Docstrings
# ### Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.
# 
# ### Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.
# 
# We can access these docstrings using the doc attribute.
# ### Python doc attribute
# Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.

# In[3]:


def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)


# # PEP 8
# PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.
# 
# PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.
# 
# ### The Zen of Python
# Long time Pythoneer Tim Peters succinctly channels the BDFL’s guiding principles for Python’s design into 20 aphorisms, only 19 of which have been written down.
# The Zen of Python, by Tim Peters

# In[4]:


import this


# In[ ]:





# In[ ]:




