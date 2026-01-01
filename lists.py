#lists slicing
marks = [10,10,15,12,40,80,90,50,70]
marks[2]=20
print(marks[2:5])
marks.append(100)
print(marks)
print(len(marks))

marks.reverse()
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)