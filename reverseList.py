#input [2,3,5,1]
#input [1,5,3,2]

def reverse_list(numberList):
    dict=[]
    for i, number in enumerate(numberList):
        dict.append(numberList[len(numberList) - (i + 1)])
    return dict

result = reverse_list([2,3,5,1])
print(result)