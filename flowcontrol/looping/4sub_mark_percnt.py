sub1=int(input("enter malayalam score"))
sub2=int(input("enter maths score"))
sub3=int(input("enter english score"))
sub4=int(input("enter science score"))
sum=sub1+sub2+sub3+sub4
print("sum=",sum)
per=(sum/200)*100
print(per)
if(per>90):
   print("A+")
   if((per>80)&(per<90)):
    print("A")
       if((per>=70)&(per<=80)):
          print("B+")
          if ((per >60) & (per <70)):
              print("B")
         #       if ((per > 50) & (per <60)):
          #          print("c+")
           #     else:
            #        print("failed")