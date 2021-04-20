#minimum length 8 and maximum number 15
import re

n=input("enter a string:")
rule='([a-zA-Z]{8,15}$)'
match=re.fullmatch(rule,n)
if match is not None:
    print("valid")
else:
    print("invalid")