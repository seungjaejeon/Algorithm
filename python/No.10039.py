total=0
for i in range(5):
    student=int(input())
    if student<40:
        total+=40
    else: total+=student
print(total//5)