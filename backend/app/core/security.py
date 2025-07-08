from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import settings

# Initialize password hashing context with bcrypt as the primary scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token for user authentication.

    Creates JWT containing the provided data and an exp timestamp.
    The token is signed using the application's secret key.

    Args:
        data: The payload to encode in the token, typically contains user info
        expires_delta: Custom expiration time delta. If None, uses
            the default expiration time from settings

    Returns:
        str: The encoded JWT token string

    Note:
        - Uses UTC time for expiration timestamps
        - Automatically adds 'exp' claim to the token payload
        - Signs token using the algorithm specified in settings
        - Default expiration taken from settings.access_token_expire_minutes
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.access_token_expire_minutes,
        )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify if a plain password matches its hashed version.

    Uses the configured password hashing context (bcrypt) to safely verify
    if a plain password matches its hashed counterpart.

    Args:
        plain_password (str): The plain text password to verify
        hashed_password (str): The hashed password to check against

    Returns:
        bool: True if the password matches, False otherwise

    Note:
        - Uses bcrypt for password verification
        - Timing-attack safe comparison
        - Automatically handles different bcrypt versions
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Generate a secure hash of a password.

    Creates a crypt secure hash of the provided password using bcrypt.
    The resulting hash includes the salt and algorithm information.

    Args:
        password (str): The plain text password to hash

    Returns:
        str: The complete hash string (including salt and algorithm parameters)

    Note:
        - Uses bcrypt with automatic salt generation
        - Includes algorithm version in hash string
        - Safe against rainbow table attacks
        - Automatically handles work factor from CryptContext configuration
    """
    return pwd_context.hash(password)


def verify_token(token: str) -> Optional[str]:
    """Verify and decode a JWT token.

    Validates the signature & expiration of JWT token and extracts the username
    (subject claim) if valid.

    Args:
        token (str): The JWT token string to verify and decode

    Returns:
        Optional[str]: The username from the token if valid, None otherwise

    Note:
        - Verifies token signature using application's secret key
        - Checks token expiration automatically
        - Returns None for any validation error
        - Expects 'sub' claim to contain the username
        - Uses algorithm specified in settings

    Example:
        >>> token = create_access_token({"sub": "john_doe"})
        >>> username = verify_token(token)
        >>> print(username)
        'john_doe'
    """
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except JWTError:
        return None
