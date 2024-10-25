import fake_math as fa, true_math as tr

print(fa.divide(5, 55))
print(fa.divide(5, 0))

print(tr.divide(5, 214))
print(tr.divide(5, 0))


print("----------- ниже пример из задания --------------")
result1 = fa.divide(69, 3)
result2 = fa.divide(3, 0)
result3 = tr.divide(49, 7)
result4 = tr.divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)