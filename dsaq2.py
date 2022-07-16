# program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def ReverseArray(Array, first, last):
    while first < last:
        Array[first],Array[last] = Array[last],Array[first]
        
        first += 1
        last -= 1
        
        
Array = [40,50,60,70,80,90,100]
ReverseArray(Array, 0, 6)
print(Array)