numbers=[4,6,7,9,8,10,13,14,5]

if len(numbers)<2:
    print("List must have atleast two elements")
second_largest=float('-inf')
largest=second_largest

for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num !=largest:
        second_largest=num

if second_largest ==float('-inf'):
    print("There is no second largest element")
else:
    print(second_largest)