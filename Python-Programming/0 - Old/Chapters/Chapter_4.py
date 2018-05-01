# -------------------------------------------------------------------------------
# Example 4.2. Sample Usage of apihelper.py
def info(object, spacing = 10, collapse = 1):
    """print( methods and doc strings.

    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print( "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList]))

if __name__ == "__main__":
    print( info.__doc__)


li = []

info(li)
# -------------------------------------------------------------------------------
# Example 4.3. Advanced Usage of apihelper.py
import odbchelper

info(odbchelper)

info(odbchelper, 30)

# -------------------------------------------------------------------------------
# Example 4.5. Introducing type
print( type(1))

print( type(li))

print( type(odbchelper))

# -------------------------------------------------------------------------------
# Example 4.6. Introducing str

print( str(1))

horseman = ['war', 'pestilence', 'famine']

print( horseman)

horseman.append('Powerbuilder')

print( horseman)

print( str(None))

# -------------------------------------------------------------------------------
# Example 4.7. Introducing dir

li=[]

print( dir(li))

d ={}

print( dir(d))

# -------------------------------------------------------------------------------
# Example 4.8. Introducing callable

import string

print( string.punctuation)

print( callable(string.punctuation))

print( callable(string.join))

print( string.join.__doc__)
# -------------------------------------------------------------------------------
# Example 4.8. Introducing callable

li = ["Larry", "Curly"]

print( li)
li.pop()

print( li)

print( getattr(li, "pop"))
# -------------------------------------------------------------------------------
# Example 4.11. The getattr Function in apihelper.py

import odbchelper

print( odbchelper.buildConnectionString)
print( getattr(odbchelper, "buildConnectionString"))

object = odbchelper
method = "buildConnectionString"

print( getattr(object, method))
# -------------------------------------------------------------------------------
# Example 4.12. Creating a Dispatcher with getattr

import statsout

def output(data, format="text"):
    output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
    return output_function(data)

# -------------------------------------------------------------------------------
# Example 4.14. Introducing List Filtering

li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]

print( [elem for elem in li if len(elem) > 1])

print( [elem for elem in li if elem != "b"])
print( [elem for elem in li if li.count(elem) == 1])

# -------------------------------------------------------------------------------
# Example 4.15. Introducing and

print( "a" and "b")
print( "" and "b")
print( "a" and "b" and "c")

print( "" or [] or {})
# -------------------------------------------------------------------------------
# Example 4.17. Introducing the and-or Trick
a = "first"
b = "second"

print( 1 and "a" or "b")
print( 0 and "a" or "b")
# -------------------------------------------------------------------------------
# Example 4.18. When the and-or Trick Fails

a = ""
b = "second"

print( 1 and a or b)

# -------------------------------------------------------------------------------
# Example 4.19. Using the and-or Trick Safely

print( (1 and [a] or [b])[0])

# -------------------------------------------------------------------------------
# Example 4.20. Introducing lambda Functions
def f(x):
    return x*2

print( f(3))

g = lambda x: x * 2

print( g(3))

print( (lambda x: x * 2)(3))
# -------------------------------------------------------------------------------
# Example 4.21. split With No Arguments

s = "this   is\na\ttest"
print( s)

print( s.split())

print( " ".join(s.split()))

