from passlib.context import CryptContext

# 1. Tell passlib we want to use "bcrypt" (the industry standard algorithm)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. Function to Hash a password
def hash(password: str):
    return pwd_context.hash(password)

# 3. Function to Verify a password (we will use this later for Login)
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)