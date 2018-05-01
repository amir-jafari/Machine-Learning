

the_string = "Hello World!"

print( the_string[4])
print( the_string.split(' '))
print( the_string.split('r'))
# ------------------------------------------------------------------
words = ["this", "is", "a", "list", "of", "strings"]

print( ' '.join(words))
print( 'ZOOL'.join(words))
print( ''.join(words))
this_string = "there"
print( "Hello %s!" % this_string)
# ------------------------------------------------------------------
emptyTuple = ()
singleItemTuple = ("spam",)
this_tuple = (12, 89, 'a')
print( this_tuple[0])
# ------------------------------------------------------------------
emptyDict = {}
this_dict = {'a': 1, 'b': 23, 'c': "eggs"}
this_dict['a']                # accessing
del this_dict['b']            # deleting:
#                             # finding
print( this_dict. get('e'))
print( this_dict. keys())
print( this_dict. items())
print( 'c' in this_dict)
# ------------------------------------------------------------------
the_list = [5, 3, 'p', 9, 'e']

print( the_list[0])
print( the_list[1:3])
print( the_list[2:])
print( the_list[:2])
print( the_list[2:-1])
print( len(the_list))

#print( the_list. sort())
print( the_list)
print( the_list. append(37))
print( the_list)
print( the_list. pop())
print( the_list)
print( the_list. pop(1))
print( the_list)
print( the_list. insert(2, 'z'))
print( the_list)
print( the_list. remove('e'))
print( the_list)
del the_list[0]
print( the_list)
the_list = the_list + [0]
print( the_list)
a =9 in the_list
print( a)
# =============================================================
# List Comprehension

x = [x*5 for x in range(5)]
print( x)
x = [x for x in range(5) if x % 2 == 0]
print( x)

