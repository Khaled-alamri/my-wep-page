def powe(base_num, pow_num):
    x=1
    for index in range(pow_num):
        x=x*base_num
    return x
print(powe(2,8))