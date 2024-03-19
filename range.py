greeting='Hello, Python!'
sub_greeting=greeting[0:5]
print(sub_greeting)

###
language=greeting[7:]
print(language)

###
skip=greeting[::2]
print(skip)

###
rev_greeting=greeting[::-1]
print(rev_greeting)

###
last_chars=greeting[-7:]
print(last_chars)

###
middle_chars=greeting[2:-1]
print(middle_chars)

###
nth_chars=greeting[1:10:3]
print(nth_chars)