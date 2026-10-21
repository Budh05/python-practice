
#! cresting prog to print tables from 1 to 19 in a file named tables.txt 
def tables_gen(n):
    tables=""
    for i in range (1,11):
        tables+=f"{n} x {i} = {n*i}\n"
    return tables
with open("Py projects/files/tables_gen.txt","w") as f:
    f.write("tables from 1 to 19 , done by files01.py\n")
    for i in range (1,20):
        f.write(tables_gen(i) + "\n")