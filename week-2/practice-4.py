# Tuple containing city names and associated values
city_tuple = ("Ekiti", 750, "Oshogbo", 250, "Akure", 500)

# Second tuple with more city data
s_tuple = ("Abeokuta", 300, "Ogbomoso")

# Prints the complete tuple
print(city_tuple)

# Prints last element of the tuple
print(city_tuple[-1])

# Prints elements of the tuple starting from 3rd to 4th element (index 2 to 3)
print(city_tuple[2:4])

# Prints elements of the tuple starting from 4th element to the end (index 3 to end)
print(city_tuple[3:])

# Prints the contents of the second tuple three times
print(s_tuple * 3)

# Prints the concatenated tuples
print(city_tuple + s_tuple)