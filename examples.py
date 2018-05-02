#strings Declaration in Python depiction

double_quote_multiple_characters = "Raster"
single_quote_multiple_characters = 'Raster'
triple_quote_multiple_characters = '''Raster'''

#keyword is
print(double_quote_multiple_characters is single_quote_multiple_characters)
#check type
print(type(triple_quote_multiple_characters))


for s in double_quote_multiple_characters:
   print(s) 

#OUTPUT:
True
<class 'str'>
R
a
s
t
e
r
