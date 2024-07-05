import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    print("\t\t\t\"GENERATE YOUR PASSWORD BY OUR CODE\"")

    try:
        len = int(input("ENTER THE PASSWORD LENGTH:"))
        if len < 0:
            print("NEGATIVE NUMBER INSERTED!!!!")
        else:
            s = []
            s = s+list(s1)+list(s2)+list(s3)+list(s4)
            print("PASSWORD IS: "+ "".join(random.sample(s, len)))
            
    except ValueError:
        print("WRONG INPUT")    