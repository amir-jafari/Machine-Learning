()# Example 3.1. Defining a Dictionary
d = {"server": "mpilgrim", "database": "master"}   # Creating Dictionary.

print( d)
print( d["server"]   )   # Accessing the dictionary with the Keys.
print( d["database"] )   # server and database is a key.
# -------------------------------------------------------------------------------
# Example 3.2. Modifying a Dictionary
# Dictionaries have no concept of order among elements
d["database"] = "pubs"  # Modifying the key values.
print( d)

d["uid"] = "sa"        # Adding new key with the value it is same as modifying
print (d)
# -------------------------------------------------------------------------------
# Example 3.3. Dictionary Keys Are Case-Sensitive
d = {}
d["key"] = "value"
d["key"] = "othervalue"

print (d)

d["Key"] = "thirdvalue"

print( d)
# -------------------------------------------------------------------------------
# Example 3.4. Mixing Datatypes in a Dictionary

d = {"server": "mpilgrim", "uid": "sa", "database": "pubs"}
print( d)

d["retrycount"] = 3

print (d)

d[42] = "douglas"

print(d)
# -------------------------------------------------------------------------------
# Example 3.5. Deleting Items from a Dictionary
del d[42]

print(d)

d["database"] = ("amir", "amir1")

print (d)
a = d["database"][1]

print (a)
d.clear()

print (type(a))

del a
# -------------------------------------------------------------------------------
# Example 3.6. Defining a List

li = ["a", "b", "mpilgrim", "z", "example"]

print (li[0])

print (li[4])
# -------------------------------------------------------------------------------
# Example 3.7. Negative List Indices

print (li[-1])
print (li[-3])

print (li[1:-1])

print (li[0:3])
# -------------------------------------------------------------------------------
# Example 3.9. Slicing Shorthand

print( li[:3])
print( li[3:])

print (li[:])
# -------------------------------------------------------------------------------
# Example 3.10. Adding Elements to a List

li.append("new")

print (li)

li.insert(2, "new")

print (li)

li.extend(['two', 'elements'])

print (li)
# -------------------------------------------------------------------------------
# Example 3.11. The Difference between extend and append

li = ['a', 'b', 'c']
print (li)

li.extend(['d', 'e', 'f'])
print (li)
print (len(li))
print (li[-1])

li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])

print (li)

print( li[-1])
# -------------------------------------------------------------------------------
# Example 3.12. Searching a List

li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

print (li.index("a"))

print ("a" in li)

# -------------------------------------------------------------------------------
# Example 3.13. Removing Elements from a List

li.remove("new")
print (li)

# It does two things: it removes the last element of the list, and it returns the value that it removed
print( li.pop())

print (li)
# -------------------------------------------------------------------------------
# Example 3.14. List Operators

li = ['a', 'b', 'mpilgrim']

li = li+["example", "new"]

print (li)

li += ['two']

print (li)

li = [1, 2] * 3

print (li)

# -------------------------------------------------------------------------------
# Example 3.15. Defining a tuple

t = ("a", "b", "mpilgrim", "z", "example")

print (t)

print (type(t))

print (t[0], t[-1], t[1:3])
# -------------------------------------------------------------------------------
# Example 3.16. Tuples Have No Methods


# 1	You can't add elements to a tuple. Tuples have no append or extend method.
# 2	You can't remove elements from a tuple. Tuples have no remove or pop method.
# 3	You can't find elements in a tuple. Tuples have no index method.
# 4 You can, however, use in to see if an element exists in the tuple.

# Tuples are faster than lists.
# Tuples are used in string formatting, as you'll see shortly.
# -------------------------------------------------------------------------------
# Example 3.17. Defining the myParams Variable

if __name__ == "__main__":
    myParams = {"server": "mpilgrim",
                "database": "master",
                "uid": "sa",
                "pwd": "secret"
                }
print (myParams, type(myParams))

# -------------------------------------------------------------------------------
# Example 3.18. Referencing an Unbound Variable
x = 1
print (x)
# -------------------------------------------------------------------------------
# Example 3.19. Assigning multiple values at once
v = ('a', 'b', 'c')

(x, y, z) = v

print( x, y, z)
print (v[0], v[1], v[2])
# -------------------------------------------------------------------------------
# Example 3.20. Assigning Consecutive Values

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)

print (MONDAY, TUESDAY, WEDNESDAY)
# -------------------------------------------------------------------------------
# Example 3.21. Introducing String Formatting

k = "uid"
v = "sa"

print ("%s=%s" % (k, v))
# -------------------------------------------------------------------------------
# Example 3.22. String Formatting vs. Concatenating

uid = "sa"
pwd = "secret"

print (pwd + " is not good password for " + uid)

print ("%s is not good password for %s" % (pwd, uid))

usercount = 6

print ("user connected: %d" % (usercount, ))()

# -------------------------------------------------------------------------------
# Example 3.23. Formatting Numbers

print ("Today's stock price: %f" % 50.4625)
print ("Today's stock price: %.2f" % 50.4625)
print ("Change since yesterday: %+.2f" % 1.5)

# -------------------------------------------------------------------------------
# Example 3.24. Introducing List Comprehensions

li = [1, 9, 8, 4]

print([elem*2 for elem in li])

li = [elem*2 for elem in li]

print (li)

# -------------------------------------------------------------------------------
# Example 3.25. The keys, values, and items Functions

params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}

a = params.keys()
b = a.sort()

print( b)
print( params.keys())
print( params.keys()[0])
print( params.values())
print( params.items())
# -------------------------------------------------------------------------------
# Example 3.26. List Comprehensions in buildConnectionString, Step by Step

print ([k for k, v in params.items()])
print ([v for k, v in params.items()])
print (["%s=%s" % (k, v) for k, v in params.items()])

# -------------------------------------------------------------------------------
# Example 3.27. Output of odbchelper.py
dummy = ";".join(["%s=%s" % (k, v) for k, v in params.items()])

print (dummy, type(dummy), len(dummy))
print (dummy[0])

# -------------------------------------------------------------------------------
#Example 3.28. Splitting a String

li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

print (li)
print (type(li))

s = ";".join(li)

print (s)

s1 = s.split(";")

print (s1)

s2 = s.split(";", 1)

print (s2)