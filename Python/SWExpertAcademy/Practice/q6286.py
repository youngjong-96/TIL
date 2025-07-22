#피보나치수열 10번째까지 출력

# list=[None]*10
list = [1, 1]
imsleepy = [list.append(list[i-1]+list[i-2]) for i in range(0,10) if i>1]

# for i in range(0,len(list)):
#     if i <2:
#         list[i] = 1
#     else:
#         list[i] = list[i-1]+list[i-2]
print(list)