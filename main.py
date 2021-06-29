from pyfiglet import Figlet

def email_slicer():
    print(Figlet().renderText("Email   Slicer"))
    email = str(input("Enter your Email:\n>>> "))
    if ('@' in email) and (email.endswith(".com")):
        user_name,domain_name = email.split('@')
        print("User name: ",user_name)
        print("Domain name: ",domain_name)
    else:
        print("Enter a Valld Mail")

if __name__ == "__main__":
    email_slicer()