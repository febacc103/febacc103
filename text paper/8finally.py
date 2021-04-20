# 8. When is the finally block executed.Explain with example?
#===========================================================
#finally block is always executed after leaving the try statement.
# In case if some exception was not handled by except block,
# it is re-raised after execution of finally block.
# finally block is used to deallocate the system resources.

lst=[5,6,7]
a=int(input("enter a number:"))
try:
    print(lst[a])
except:
    print("exception occured")
finally:
    print("inside finally")