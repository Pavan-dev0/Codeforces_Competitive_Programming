# CHOSE INDEX I AND REPLACE AI WITH AI+1 if 1<=i <n
# CHOSE INDEX I AND REPLACE AI WITH BI+1 if 1<=i <=n
#has q queries
#query described by 2 numbers l and r his task 
#find max value of sum(al+al+1............an) for each query

# At beginning it contains number of test cases
#1st line contains n(range of a and b) and the q is the query that later contains l and r 
#second line of each test case ocontains n ints a1,a2,a3..........an
#third line of each test case(b1,b2......bn)
#q line contains two ints l and r


main=int(input())


for _ in range(main):

    n,q=map(int,input().split())
    a=map(int,input().split())
    b=map(int,input().split())


    
