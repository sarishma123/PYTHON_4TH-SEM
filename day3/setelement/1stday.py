s={1,2,34}
s.add(12)
print("the addition is:", s )

s.remove(2)
print("the removeable of that element is: ",s )

array1 = [
    [1, "ram", "bkt", "bca"],
    [2, "rama", "bkt1", "bca"],
]

print("The array is:", array1)

array1.append(
    [3, "sita", "ktm", "bca"]
)

print("The new edited array is:", array1)

# union and intersection
a={1,2,3,45}
b={2,3,4,5,6,7}
c=a.union(b)
print("the new array is ",c)
