x = 25
try:
    assert int(x)>= 25
    print('right age!')
except ValueError:
    print("wrong number!")
