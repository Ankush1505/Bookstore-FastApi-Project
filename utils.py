from passlib.context import CryptContext

#  we want to use "bcrypt"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a password
def hash(password: str):
    return pwd_context.hash(password)

# Function to Verify a password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
