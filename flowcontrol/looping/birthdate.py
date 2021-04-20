birth_d=int(input("enter your birth date"))
birth_m=int(input("enter birth month"))
birth_y=int(input("enter your birth year"))

t_d=int(input("enter today date"))
t_m=int(input("enter today month"))
t_y=int(input("enter today year"))

age_y=(t_y-birth_y)+1
if(t_m>birth_m):
    print("age is:",age_y)
else:
    print("age is",age_y-1)