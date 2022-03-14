#Array data set
names = ["Jonathan", "jeongho", "Jane", "Bill", "Steve"];
print(names)
print(names[0])
print(names[:1]) # slicing
print(names[1:]) #slicing
print(names[1:3]) #slicing
names.append("daeun")
print(names)
names.pop()
print("pop의 결과 : " , names)
#len
len(names)
#multi array
multi_names = [[100,95,85,78,75],["Jonathan","jeongho","daeun", "yunhak","suri"]]
print(multi_names[0][0])