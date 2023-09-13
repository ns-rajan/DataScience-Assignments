#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Solution for Moonlight Dinner Ball
# There is no import done, no inbuilt libraries used

# Example input
# 1 This is the # of Test Cases
# 4 5 This is the # of Boys and Girls
# 2 5 6 8  These are the heights of Boys
# 3 8 5 1 7  These are the heights of Girls

# The first line contains T denoting the number of test cases.
# Each test case contains three lines.
# The first line contains M and N.
# The second line contains M integers each denoting the height of boy.
# The third contains N integers each denoting the height of girl.

# T is the # of test cases
# M is the number of boys
# N is the number of girls

# Constraints:
# 1<=T<=10
# 1<=N, M<=10000
# 1<=Height<=200


# Storing the Constraints and use as needed
# 1-10 test cases, at least 1 girl, at most 10000 boys, 1-200 height units

MINTVALUE = 1
MAXTVALUE = 10

MINNVALUE = 1
MAXMVALUE = 10000

MINHVALUE = 1
MAXHVALUE = 200
errormessage = ""

try:
    # Open or Create the input and output files
    file1 = open("inputPS10.txt","r+")
    file2 = open("outputPS10.txt","w")

    # seek(n) takes the file handle to the nth
    # byte from the beginning.
    file1.seek(0) 
    T = int(file1.readline())

    if (T > MAXTVALUE or T < MINTVALUE) :
        errormessage = "T value out of range"
        #print (errormessage)
        file2.write(errormessage)
        raise Exception('UseCaseRangeError', errormessage)
    try:
        # the first T number of lines for number of test cases will be read here
        # excess lines above T value will be ignored
        for i in range(T) :
            M,N=map(int,file1.readline().split())
            if (N >= MINNVALUE and M <= MAXMVALUE and N>=M):
                #boys_height_array = [int(i) for i in file1.readline().split()]
                #girls_height_array = [int(i) for i in file1.readline().split()]
                boys_height_list = list(map(int,file1.readline().split()))
                girls_height_list = list(map(int,file1.readline().split()))
                
                # Validation for Height Min Max
                if (all(j < MAXHVALUE for j in boys_height_list) and all(j < MAXHVALUE for j in girls_height_list) ):
                    f=0
                    quick_sort(0, len(boys_height_list) - 1, boys_height_list)
                    quick_sort(0, len(girls_height_list) - 1, girls_height_list)
                    #print(boys_height_array)
                    #print(girls_height_array)
                    
                    for l in range(M):
                        if(boys_height_list[l]<=girls_height_list[l]):
                            #print("NO")
                            file2.write("NO"+ "\n") 
                            f=1
                            break
                    if(f==0):
                        #print("YES")
                        file2.write("YES"+ "\n")
                else:
                    errormessage = 'Height Input not within permissible range'
                    raise Exception('IncorrectHeight', errormessage)

            else:
                errormessage = 'Input not within permissible range'
                raise Exception('NotInteger', errormessage)

    except:
        errorstring = "Invalid/Missing data in Input file " + errormessage
        raise Exception('InvalidInput', errorstring )

    # Close the File Handles if all good
    file1.close()
    file2.close()
    


except: #catch exceptions and close if there are open Files
    errorstring = "Handling Errors and closing files " + errormessage
    #print(errorstring)
    file2.write(errorstring)
    
    if not file1.closed:
        file1.close()
    if not file2.closed:
        file2.close()
    exit()

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
     
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
     
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
         
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
             
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1
         
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
     
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end
     
# The function that implements QuickSort
def quick_sort(start, end, array):
     
    if (start < end):
         
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)
         
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

