new_grade=0
limit = int(input())
for i in range(limit):
	grade = int(input())	
    if grade<38:
   	print(grade)
    elif grade>38 and grade%5!=0:
       	while grade%5!=0:
        	    new_grade=grade+1
            if new_grade-grade<3:
	        	print(new_grade)
	