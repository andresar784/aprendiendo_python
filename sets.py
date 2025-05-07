# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
length_of_companies = len(it_companies)
print(length_of_companies)
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
#   Insert multiple IT companies at once to the set it_companies
it_companies.update(["HP","Aiwa"])
length_of_companies = len(it_companies)
print(length_of_companies) #10
#   Remove one of the companies from the set it_companies
it_companies.remove("IBM")
length_of_companies = len(it_companies)
print(length_of_companies)
#    What is the difference between remove and discard
# Update rayses an error if not encounter a item to be removed, instaed discard do  nothing
it_companies.discard("IM")
#Excersises nivel 2
# Join A and B
C = A.union(B)
print(C)
# Find A intersection B
print(A.intersection(B)) # {19, 20, 22, 24, 25, 26}
# Is A subset of B
print(A.issubset(B)) #True
# Are A and B disjoint sets
print(A.isdisjoint(B)) # False
# Join A with B and B with A
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}      
# What is the symmetric difference between A and B
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# Delete the sets completely
# del A
# del B     
# Convert the ages to a set and compare the length of the list to the set, which one is bigger?   
ages_length = len(age)
print(ages_length)
ages_set = set(age)
print(len(ages_set))
# the list is bigger because allows multiplicates
# Explain the difference between the following data types: string, list, tuple and set
#String. 
#List. ordered, changeable, allows multiplicate
#Tuple, ordered, unchangeable, unmodifiable, can be diferente datatypes
#Set, not duplicate, unordered, not changeable

# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? #10
# Use the split methods and set to get the unique words
string = "I am a teacher and I love to inspire and teach people"
words = string.split()
unique_words = set(words)
print(len(unique_words)) # 10 words
