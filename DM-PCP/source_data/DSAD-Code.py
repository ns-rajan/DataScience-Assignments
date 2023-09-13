t=int(input())
for i in range(t):
    b,g=map(int,input().split())
    bb=list(map(int,input().split()))
    gg=list(map(int,input().split()))
    if(b>g):
        print("NO")
    else:
        f=0
        bb.sort()
        gg.sort()
        for i in range(b):
            if(bb[i]<=gg[i]):
                print("NO")
                f=1
                break
        if(f==0):
            print("YES")
            
            
            
            
            
            
            
            
            
            
----------------------

# There is no import calls, no inbuilt libraries used

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

# Example input
# 1 This is the # of Test Cases
# 4 5 This is the # of Boys and Girls
# 2 5 6 8  These are the heights of Boys
# 3 8 5 1 7  These are the heights of Girls

# Store the MIN and MAX values and use as needed
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
    file1 = open("../source_data/inputPS10.txt","r+")
    file2 = open("../source_data/outputPS10.txt","w")

    # seek(n) takes the file handle to the nth
    # bite from the beginning.
    file1.seek(0) 
    T = int(file1.readline())
    #print (T);
    if (T > MAXTVALUE or T < MINTVALUE) :
        errormessage = "T value out of range"
        #print (errormessage)
        file2.write(errormessage)
        raise Exception('UseCaseRangeError', errormessage)

    allOrders = []
    numOfCustomers = 0
    try:
        # the first T number of lines for number of test cases will be read here
        # excess lines above T value will be ignored
        for i in range(T) :
            numOfUseCases = numOfUseCases+1
            line = file1.readline().split()
            MValue = line[0]
            NValue = line[1]
            if (MValue.isdigit() and NValue.isdigit() ):
                MValue = int(line[0])
                NValue = int(line[1])
                if (MValue >= MINMVALUE and NValue <= MAXNVALUE):
                    b,g=map(int,input().split())
		    bb=list(map(int,input().split()))
		    gg=list(map(int,input().split()))
		    if(b>g):
		        print("NO")
		    else:
		        f=0
		        bb.sort()
		        gg.sort()
		        for i in range(b):
		            if(bb[i]<=gg[i]):
		                print("NO")
		                f=1
		                break
		        if(f==0):
		            print("YES")
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
        print ("Min average waiting time:", end =" ") 
        print (minWaitTime)
        print ("Dosas served in the following order:", end =" ")
        print (customerQOrder)

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

