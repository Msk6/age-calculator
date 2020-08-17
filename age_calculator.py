import datetime


def check_birthdate(year, month, day):
	# write code here
	x = datetime.datetime.now()
	y = datetime.datetime(year, month, day)
	return y < x

def calculate_age(year, month, day):
    # write code here
	x = datetime.datetime.now()
	y = datetime.datetime(year, month, day) 
	print ("You are %s years old." %((x-y).days/365))
	return

def main():
	# write main code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))

	if check_birthdate(year, month, day):
		calculate_age(year, month, day)
		
	else:
		print ("please enter valid date")

	

if __name__ == '__main__':
	main()