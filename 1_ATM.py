'''
ATM Problem Code: HS08TEST

Link: https://www.codechef.com/problems/HS08TEST
'''

withdrawal = int(input(""))
total = float(input(""))
commisioned = withdrawal + 0.50
if commisioned > 0 and commisioned <=total and total <= 2000:
    print(total - commisioned)
else:
    print(total)
