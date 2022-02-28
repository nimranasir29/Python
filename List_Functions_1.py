lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends_1= ["Kevin","Karen","Jim","Oscar","Toby"]
friends_2= ["Kevin","Karen","Jim","Oscar","Toby"]
friends_3= ["Kevin","Karen","Jim","Jim","Oscar","Toby"]

print(friends_3.count("Jim"))   # count how many times 'Jim' present in the list

print(friends.index("Kevin"))   # check at which index kevin present

friends.pop()                  # Removes the last element of the list 'Toby'
print(friends)

friends.append("creed")        # Add the item at the end of the list
print(friends)

friends_1.insert(1," Kelly")     # Push to the right one index position
print(friends_1)

friends_2.remove("Jim")        # Remove jim from list
print(friends_2)

friends_4 = friends.copy()    #copy
print(friends_4)

friends.clear()         # give us a empty list
print(friends)



lucky_numbers.sort()     # in ascending order
print(lucky_numbers)

lucky_numbers.reverse()   # reverse the list
print(lucky_numbers)

friends_2.sort()        # put it in alphabetical order
print(friends_2)

print(friends.index("Mike"))    #gives an error bcz 'Mike' is not prsent in the list


