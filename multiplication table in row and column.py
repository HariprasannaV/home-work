"""
######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers.
#the following example uses 1 to 5.

     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25

"""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("  ", end=" ")
for table in range(start, end+1):
    print(table, end="  ")
print("\n")
print('*'*20)

for table in range(start, end+1):
    print(table, end="  | ")
    for count in range(start, end+1):
        print(table*count, end="  ")
    print("\n")
