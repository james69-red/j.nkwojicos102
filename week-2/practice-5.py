# Returns false as game_1 is not equal to game_2
game_1 = 2
game_2 = 4
print(bool(game_1 == game_2))  # False
# Or
print(game_1 == game_2)

# Returns False as val is None
val = None
print(bool(val))  # False

# Returns False as num is an empty sequence
num = ()
print(bool(num))  # False

# Returns True as age is boolean and already True
age = True
print(bool(age))  # True