# WAP to print table from 11 to 20.
print("Table from 11 to 20.")
for i in range(11,21):
    for j in range(1,11):
        table = i*j
        print(i,'*',j,'=',table,end='\t')
        #print(f"{i}*{j}={table}")
    print() 