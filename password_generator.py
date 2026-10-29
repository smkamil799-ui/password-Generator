import string 
import secrets

print("==== PASSWORD GENERATOR ====")

# Ask the user for password length
length = int(input("Enter password length: "))

#check the password length
if length < 4:
     print("please enter a length of at least 4. ")
else:
    # create a collection of char
     characters = (
     string.ascii_letters
    + string.digits
    + string . punctuation
     )
     password = "".join(
          secrets.choice(characters)
          for _ in range(length)
     )

     print("Your generated password is:")
     print(password)


