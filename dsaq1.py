

#  program to find all pairs of an integer array whose sum is equal to a given number.


def sum_given_number(array , num , sum):
    for i in range(num):
        for j in range(i+1 , num):
            if array[i] + array[j] == sum:
                print("(",array[i],",",array[j],")")
                
                
array = [3,4,3,2,5,6,7,8,4,4,5,6]
num = len(array)
sum = 15


sum_given_number(array, num, sum)