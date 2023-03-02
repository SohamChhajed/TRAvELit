# SAMPLE CODE
person1=input("Enter your Name : ")
place1=input("Enter where you are headed to : ")
date1=input("Enter date in dd-mm-yyyy format : ")
person2=input("Enter your Name : ")
place2=input("Enter where you are headed to : ")
date2=input("Enter date in dd-mm-yyyy format : ")
person3=input("Enter your Name : ")
place3=input("Enter where you are headed to : ")
date3=input("Enter date in dd-mm-yyyy format : ")
d1=date1.split("-")
d2=date2.split("-")
d3=date3.split("-")
if (place1==place2==place3) and (d1[0]==d2[0]==d3[0]) and (d1[1]==d2[1]==d3[1]):
    print(person1,"and",person2,'and',person3,"are matched")
elif (place1==place2==place3) and (d1[1]==d2[1]==d3[1]) and (d1[0]!=d2[0]!=d3[0]):
    print("Hey",person1,"and",person2,'and',person3,"are travelling in the same month to the same place")
elif (place1==place2) and (d1[0]==d2[0]) and (d1[1]==d2[1]):
    print(person1,"and",person2,"are matched")
elif (place1==place3) and (d1[0]==d3[0]) and (d1[1]==d3[1]):
    print(person1,"and",person3,"are matched")
elif (place2==place3) and (d2[0]==d3[0]) and (d2[1]==d3[1]):
    print(person2,"and",person3,"are matched") 
elif (place1==place2) and (d1[1]==d2[1]) and (d1[0]!=d2[0]):
    print("Hey",person1,"and",person2,"are travelling in the same month to the same place")
elif (place2==place3) and (d2[1]==d3[1]) and (d2[0]!=d3[0]):
    print("Hey",person2,'and',person3,"are travelling in the same month to the same place")
elif (place1==place3) and (d1[1]==d3[1]) and (d1[0]!=d3[0]):
    print("Hey",person1,'and',person3,"are travelling in the same month to the same place")
else:
    print("Sorry no matches found for now")
    
    