# OR, AND ,XOR


a = True
b = False

# or ( False + True = True, False + False = False)
print(a ,'or', a, '  = ',  a or a)
print(a ,'or', b, ' = ',  a or b)
print(b ,'or', a, ' = ',  b or a)
print(b ,'or', b, '= ',  b or b)

# AND ( False x True = False, False x False = False
print(a ,'and', a, '  = ',  a and a)
print(a ,'and', b, ' = ',  a and b)
print(b ,'and', a, ' = ',  b and a)
print(b ,'and', b, '= ',  b and b)

# XOR ( same as OR but TRUE X TRUE is TRUE, False x False is False)
print(a ,'xor', a, '  = ',  a ^ a)
print(a ,'xor', b, ' = ',  a ^ b)
print(b ,'xor', a, ' = ',  b ^ a)
print(b ,'xor', b, '= ',  b ^ b)