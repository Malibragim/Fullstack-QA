


def test_isomorphic(a,b):
 a = 'bounce'
 b = 'artist'


 if len(a) != len(b):
     return False

 map_a_b = {}
 map_b_a = {}
 for i1, i2 in zip(a,b):
    if i1 in map_a_b:
        if map_a_b[i1] != i2:
          return False
    else:
          map_a_b[i1] = i2
    if i2 in map_b_a:
        if map_b_a[i2] != i1:
          return False
    else:
         map_b_a[i2]=i1
 return True
print(test_isomorphic('artist', 'bounce'))


def test_missing_num():
    nums = [1,2,4,5,6,7,8,9,10]
    for num in range(1, 10):
        if num not in nums:
            print('Пропущено натуральное число:', num)
            break
    else:
            print('Пропущенных значений нет')















