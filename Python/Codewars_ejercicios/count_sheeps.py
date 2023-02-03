def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    print(count)

count_sheeps([True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ])