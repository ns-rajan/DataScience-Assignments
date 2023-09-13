
# coding: utf-8

# In[2]:


import heapq

# Store the MIN and MAX values and use as needed
# The Max values could be 109, 105 or 10^9, 10^5, we can change the values here as needed.
MINNVALUE = 1
MAXNVALUE = 109
MINTIVALUE = 0
MAXTIVALUE = 105
MINLIVALUE = 1
MAXLIVALUE = 105
errormessage = ""

try:
    # Open or Create the input and output files
    file1 = open("inputPS10.txt","r+")
    file2 = open("outputPS10.txt","w")

    # seek(n) takes the file handle to the nth
    # bite from the beginning.
    file1.seek(0) 
    n = int(file1.readline())
    #print (n);
    if (n > MAXNVALUE or n < MINNVALUE) :
        errormessage = "n value out of range"
        #print (errormessage)
        file2.write(errormessage)
        raise Exception('NotInteger', errormessage)

    allOrders = []
    numOfCustomers = 0
    try:
        # the first n number of lines for customer/bake time will be read here
        # excess lines above n value will be ignored
        for i in range(n) :
            numOfCustomers = numOfCustomers+1
            line = file1.readline().split()
            TiValue = line[0]
            LiValue = line[1]
            if (TiValue.isdigit() and LiValue.isdigit() ):
                TiValue = int(line[0])
                LiValue = int(line[1])
                if (TiValue >= MINTIVALUE and TiValue <= MAXTIVALUE and LiValue >= MINLIVALUE and LiValue <= MAXLIVALUE):
                    l, t = int(TiValue), int(LiValue)
                    heapq.heappush(allOrders, (l, t))
                else:
                    errormessage = 'Input not within permissible range'
                    raise Exception('NotInteger', errormessage)
                    
            else:
                errormessage = 'Input data is not Integer'
                raise Exception('NotInteger', errormessage)
    except:
        errorstring = "Invalid/Missing data in Input file " + errormessage
        raise Exception('InvalidInput', errorstring )
        
    file1.close()

    def minWait(allOrders) :
        customerQOrder = ""
        totalWaitTime = 0
        numOrders = len(allOrders)
        if numOrders == 0 :
            return 0
        pendingOrders = []
        currentTime = allOrders[0][0]
        loop = True
        while loop :
            while len(allOrders) != 0 and allOrders[0][0] <= currentTime :
                order = heapq.heappop(allOrders)   
                heapq.heappush(pendingOrders, (order[1], order[0]))
            if len(pendingOrders) != 0 :
                minWaitOrder = heapq.heappop(pendingOrders)
                waitTime = currentTime - minWaitOrder[1] + minWaitOrder[0]
                totalWaitTime += waitTime
                currentTime += minWaitOrder[0]
                customerQOrder += "Customer " + str(minWaitOrder[1]) + ", "
            else :
                currentTime += 1
            if len(pendingOrders) == 0 and len(allOrders) == 0 :
                loop = False

        minWaitTime = str(int( totalWaitTime/numOrders))
        #print ("Min average waiting time:", end =" ") 
        #print (minWaitTime)
        #print ("Dosas served in the following order:", end =" ")
        #print (customerQOrder)

        # \n is placed to indicate EOL (End of Line)
        file2.write("Min average waiting time: ") 
        file2.write(minWaitTime + "\n")
        file2.write("Dosas served in the following order: ")
        file2.write(customerQOrder + "\n")
        file2.close() #to change file access modes

    # This is the main function call
    minWait(allOrders)

except: #catch exceptions and close if there are open Files
    errorstring = "Handling Errors and closing files " + errormessage
    #print(errorstring)
    file2.write(errorstring)
    
    if not file1.closed:
        file1.close()
    if not file2.closed:
        file2.close()
    exit()

