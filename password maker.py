# first collect what u need in the password
# generate the password
# collect the username of the password
# Collect the description of the password
# collect the date the password was created
# store the password in a file

from random import choice
import datetime as dt

print("")
print("Select your prefered unicodes!")
print("")

caps_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
small_letters = list("abcdefghijklmnopqrstuvwxyz")
symbols = list("!@#$%^&*()_-")
numbers = list("1234567890")


def pass_len():
	"""
	Collecting the total number of password in digit.
	If none given, the default int '10' will be the 
	total number of password
	"""
	length = 10
	try:
	    length = int(
	        input(
	            "password length in digit: "
	        )
	    )

	except ValueError:
	    print(
	        "You'er just stubborn, INPUT A DIGIT!!"
	    )

	return length


length = pass_len()


def collect_pass(c_l, s_l, sym, num):
	"""
	collect the list of unitext to be in 
	password, if none is given it returns
	an empty list and if some unitext are 
	specified it returns list of the unitexts.
	"""

	password = []
	if c_l:
		if c_l[0].lower() == "y":
		    password.extend(caps_letters)
		elif c_l[0].lower() == "n":
		    print("Capital letters in your password makes it more secure")
		else:
			print("Don't be stubborn. Select one of this (y/n) next time.")		
	if s_l:
		if s_l[0].lower() == "y":
			password.extend(small_letters)
		elif s_l[0].lower() == "n":
			print("Small letters in your password makes it more secure")
		else:
			print("Don't be stubborn. Select one of this (y/n) next time.")
	if sym:
		if sym[0].lower() == "y":
		    password.extend(symbols)
		elif sym[0].lower() == "n":
		    print("Symbols in your password makes it more secure")
		else:
			print("Don't be stubborn. Select one of this (y/n) next time.")
	if num:
		if num[0].lower() == "y":
		    password.extend(numbers)

		elif num[0].lower() == "n":
		    print("Numbers in your password makes it more secure")
		else:
		    print("Don't be stubborn. Select one of this (y/n) next time.")
	return password

c_l = input("caps letter(y/n): ")
s_l = input("smalls letter(y/n): ")
sym = input("symbols(y/n): ")
num = input("numbers(y/n): ")

collect_pass = collect_pass(c_l, s_l, sym, num)



def generate_pass(gen_pass, length):
	"""
	Using the length given in the function
	pass_len(), password generates unitexts of the
	length given.
	If list of password is empty, it returns a 
	string 'no password given.'
	"""

	final_pass = "No password given"
	if gen_pass:
	    final_pass = ""
	    for x in range(length):
	        password = choice(gen_pass)

	        final_pass += password

	    # bell rings to indicate sucessful creation
	    # of password
	    print("\a")

	return final_pass

final_password = generate_pass(collect_pass, length)
print(final_password)


def username():
	"""
	Collecting USERNAME coressponding 
	to the password generated.
	"""

	username_ = input(
	    'What username do you intend using?\n'
	)

	return username_.title()


get_username = username()


def get_date():
	date_time = dt.datetime.now()

	return date_time.strftime(
		"%m/%d/%Y, %H:%M:%S"
	)

date = get_date()

def get_about():
    about = input("Name of account: ")
    return about.title()


about = get_about()


def get_file(final_password, get_username, date, about):
    with open("Passwords.txt", "a") as file:
        file.write(
            f"password: '{final_password}'\t----\tusername: {get_username}"
        )
        file.write(f"\t---- Date: {date}\t----\tAbout: {about}")
        file.write("\n")


get_file(final_password, get_username, date, about)
