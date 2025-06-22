from pydantic import BaseModel, EmailStr, conint

class UserProfile(BaseModel):
    """
    Represents a user profile with basic validation.
    """
    name: str                      # Must be a string (no special rules here)
    email: EmailStr                # Automatically validates correct email format
    age: conint(ge=18, le=100)     # Age must be an integer between 18 and 100

    def display_profile(self):
        """
        Nicely prints the user profile details.
        """
        print("👤 User Profile")
        print(f"Name : {self.name}")
        print(f"Email: {self.email}")
        print(f"Age  : {self.age}")

# Create a user profile with valid details
try:
    user1 = UserProfile(name="Aisha Verma", email="aisha.verma@example.com", age=28)
    user1.display_profile()
except Exception as e:
    print("Validation Error:", e)