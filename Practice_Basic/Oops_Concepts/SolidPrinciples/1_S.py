# 👉 Single Responsibility Principle (SRP)
# 👉 Ek class = ek hi kaam

class User:
    def save(self):
        print("Save to DB")

    def send_email(self):
        print("Send email")
        
u = User()
u.save()
u.send_email()



# #############################################################################
# #############################################################################
class UserRepository:
    def save(self, user):
        print(f"Saved {user} to DB")


class EmailService:
    def send_email(self, user):
        print(f"Email sent to {user}")
        
u = UserRepository()
u.save("User data")

e = EmailService()
e.send_email("User data")
