L = [4, 5, 1, 3, 9, 7, 10, 8, 6, 2]
print("Original list: ", L)

count = 0

for i in L:
    count += 1

avg = count/len(L)

print("sum =", count)
print("Average =", avg)

L.sort()
print("Smallest element is: ", L[0])
print("Largest element is: ", L[-1])