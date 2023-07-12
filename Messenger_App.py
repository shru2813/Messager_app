from abc import ABC,abstractclassmethod

class MessagingService(ABC):
    def sendmessage(self):
        pass

class SMSMessagingService(MessagingService):

    def __init__(self,mobile,message):
        self.mobile=mobile
        self.message=message

    def sendmessage(self):
        print("The Mobile Number:",self.mobile)
        print("The Message:",self.message)

class EmailMessagingService(MessagingService):

    def __init__(self,email,subject,message):
        self.email=email
        self.subject=subject
        self.message=message

    def sendmessage(self):
        print("The email ID:",self.email)
        print("The Subject of the email:",self.subject)
        print("The Message:",self.message)

class WhatsAppMessagingService(MessagingService):

    def __init__(self,mobile,valid,message):
        self.mobile=mobile
        self.valid=valid
        self.message=message

    def sendmessage(self):
        if self.valid:
            print("The mobile Number:",self.mobile)
            print("The user is available in whatsapp")
            print("The Message:",self.message)
        else:
            print("The user in not available in Whatsapp")

while True:
    print("Enter the number of the action to perform:")
    print("1. SMS")
    print("2. Email")
    print("3. Whatsapp")
    print("4. Exit")
    action = int(input())
    if action == 1:
        mobile_number=int(input("Enter the mobile number: "))
        if str(mobile_number)[0] in "6789" and len(str(mobile_number))==10:
            message=input("Enter the meassage: ")
            sms=SMSMessagingService(mobile_number,message)
            sms.sendmessage()
            print("Message sent Sucessfully!!")
        else:
            print("Enter a valid Mobile Number!!")
    elif action == 2:
        email=input("Enter Email: ")
        if "@" in email and email.split(".")[-1] in ("com","in"):
            subject=input("Enter subject of the email: ")
            message=input("Enter the meassage: ")
            email=EmailMessagingService(email,subject,message)
            email.sendmessage()
            print("Message sent Sucessfully!!")
        else:
            print("Enter a valid Email address!!")
    elif action == 3:
        mobile_number=int(input("Enter the mobile number: "))
        if str(mobile_number)[0] in "6789" and len(str(mobile_number))==10:
            valid=input("If whatsapp available enter 'T' else enter'F': ")
            if valid=='T':
                message=input("Enter the meassage: ")
                wp=WhatsAppMessagingService(mobile_number,valid,message)
                wp.sendmessage()
                print("Message sent Sucessfully!!")
            else:
                print("The user not vailable in Whatsapp!!")
        else:
            print("Enter a valid Mobile Number!!")
    elif action == 4:
        break
    else:
        print("Invalid Action")
