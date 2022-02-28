print(2**3)        #   first Method

def raise_to_power(base_num, pow_num):    # second Method
    
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result



print(raise_to_power(3,2))
