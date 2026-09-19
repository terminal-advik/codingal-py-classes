




alph = "abcdefghijklmnopqrstuvwxyz"
# print(alph)

# P Y T H O N
# 0 1 2 3 4 5
#-6-5-4-3-2-1

# a b c d e f g h i j k  l m n o p q r s t u v w x y z
# 0 1 2 3 4 5 6 7 8 9 10 

# print(alph[0:5])

# variable_name[start : stop : jump] 

# start : start from here , default = 0
# stop : stop before here , default = len(string_name)
# jump : 

# print(alph[ : ]) #is equal to alph[0 : 26 : 1]

# print(alph[0 : 26 : 3]) #alph[::3]


# print( alph[15] )

#Negative Indexing

name = "ADVIK"
      # 01234
      # 54321 -------> all indexes are negative
      
print(name[-4 : -1]) #DVI
print(name[-4 : ])   #DVIK name[-4:5]

#How to reverse a string

print(name[::-1]) 

#Positive step means: name[0 : 4 : 1] --> 0->1->2->3->4

#Negative step : name[4 : 0 : 1] ---> 4->3->2->1
print(alph[-5 : ])