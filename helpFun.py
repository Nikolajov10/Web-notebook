def reverseDateString(s:str)->str:
    rev=""
    curr=""
    for letter in s:
        if letter == "-":
            if rev=="":
                rev=curr+rev
            else:
                rev = curr + "-" + rev
            curr=""
        else:
            curr+=letter
    rev=curr+"-"+rev
    return rev

def arrStrToArr(string_array:str):
    arr=[]
    string_array=string_array[1:len(string_array)-1]
    arr=string_array.split(',')
    for index,num in enumerate(arr):
        arr[index]=int(num)
    return arr

def compareDNAs(dna1,dna2)->float:
    matching=0
    n = len(dna2)
    for i in range(n):
        if abs(dna1[i]-dna2[i])<=32:
            matching+=1
        elif abs(dna1[i]-dna2[i])<=54:
            matching+=0.5
    return matching/n