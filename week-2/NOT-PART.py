n = 10

if n > 10:
    if n % 2 == 0:
        result = "Even and greater than 10"
    else:
        result = "Odd and greater than 10"
else:
    result = "5 or below"
    if n > 5:
        result = "Between 6 and 10"

print(result)