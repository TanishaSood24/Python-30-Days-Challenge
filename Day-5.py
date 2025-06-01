def sum_and_average(lst):
    if not lst:
        return None
    total=0
    for num in lst:
        total+=num
    avg=total/len(lst)
    return total,avg

list_elements=[10,20,30,40,50]
sum_average=sum_and_average(list_elements)
print("Sum of elements is:",sum_average[0])
print("Average of elements is:",sum_average[1])


