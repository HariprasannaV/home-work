"""
######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares
"""

for row in range(0,8):
    for column in range(0,4):
        print('\u25A0',end="")
        print('\u25B0',end="")
    print()
