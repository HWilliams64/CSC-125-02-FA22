# == equality
# >= greater than or equal to
# <= less than or equal to
# < less then
# > greater than

# and => both have to be true for the entire sequence to be true
# or => only one has to be true for the entire sequence

# LOGICAL RULES
# and -> x -> multiply
# or -> + -> addition
# true -> greater than 0 -> 1
# false -> less than or equal to 0 -> 0
# PEMDAS -> Parentheses Expontents Multiplction Devision Addditon and Substraction 

#           0    +    0    +    1 = 1 => true 
result = 3 == 2 or 2 == 1 or 1 == 1
#           0   x      0    +    (1    x    0)
#   0 + 0 
result = 3 == 2 and 2 == 1 or (1 == 1 and False)

#           0   x      (0    +    1)    x    0)
result = 3 == 2 and (2 == 1 or 1 == 1) and False
print(result)