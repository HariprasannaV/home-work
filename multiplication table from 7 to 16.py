"""
######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number up to 12 rows.
"""
for tables in range(7, 17):
    print(f'Table {tables}')
    for count in range(1, 13):
        print(f'{count} * {tables} = {count*tables}')
    print()
print("End of Tables")
