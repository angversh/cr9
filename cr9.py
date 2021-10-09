try:  
    print('Insert a')
    a = float(input())
    print('Insert b')
    b = float(input())
    print('Insert c')
    c = float(input())
    print('Insert d')
    d = float(input())
except ValueError:
    print('Invalid data') 
    exit()
def sides():
    if (a, b, c, d> 0) and ((a<c) and (b<d)) or ((b<c) and (a<d)):
        print('Yes')
    else:
        print('No')
sides()
 