def sum(*tuple_name): # tuple is ordered and unchangable, but we can cast it to a list to make changes (done in sum1)
    sum = 0
    # now iterate over the tuple
    for i in tuple_name:
        sum = sum + i
    return sum

def sum_casted_to_list(*tuple_name):
    sum = 0
    tuple_name = list(tuple_name)
    tuple_name[0] = 0
    for i in tuple_name:
        sum = sum + i
    return sum

# variable amount of arguments can be passed now - which get passed as tuple
print(str(sum(1, 2, 3, 4, 5)))
print(str(sum(1, 2, 3, 4, 5, 99))) 


print(str(sum_casted_to_list(101, 2, 3, 4, 5))) 