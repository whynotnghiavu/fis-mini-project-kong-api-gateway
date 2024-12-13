import settings
from datetime import timedelta
from loguru import logger
from fastapi import HTTPException
from database import get_db

from app.auth.models.user import User
from app.auth.schema.auth import RegisterUserRequest

from app.auth.utils.password_manager import PasswordManager
from app.auth.utils.auth_handler import AuthHandler


async def create_admin_default():
    """
    Called on application startup.  Currently just creates the admin
    user if it doesn't already exist.
    """
    logger.info("Creating admin default user...")

    is_admin_default_exists = await check_admin_default()

    if not is_admin_default_exists:
        logger.info("Creating admin default user...")
        await create_user(
            name=settings.ADMIN_DEFAULT_NAME,
            age=settings.ADMIN_DEFAULT_AGE,
            username=settings.ADMIN_DEFAULT_USERNAME,
            email=settings.ADMIN_DEFAULT_EMAIL,
            password=settings.ADMIN_DEFAULT_PASSWORD,
            is_admin=True
        )
    else:
        logger.info("Admin default user already exists...")


async def check_admin_default():
    """
    Check if the admin default user exists.

    Returns:
        bool: True if the admin default user exists, False otherwise.
    """
    logger.info("Check admin default user...")
    return await get_user_by_username(settings.ADMIN_DEFAULT_USERNAME)


async def get_user_by_username(username: str):
    """
    Get user by username.

    Args:
        username (str): The username of the user to fetch.

    Returns:
        User: The user object if the user exists, None otherwise.
    """
    logger.info(f"Get user by username={username}")
    with get_db() as session:
        user = session.query(User).filter(User.username == username).first()
    return user


async def get_user_by_email(email: str):
    """
    Get user by email.

    Args:
        email (str): The email of the user to fetch.

    Returns:
        User: The user object if the user exists, None otherwise.
    """
    logger.info(f"Get user by email={email}")
    with get_db() as session:
        user = session.query(User).filter(User.email == email).first()
    return user


async def create_user(
        name: str,
        age: int,
        username: str,
        email: str,
        password: str,
        is_admin: bool
):
    """
    Create a user.

    Args:
        name (str): The name of the user.
        age (int): The age of the user.
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        is_admin (bool): Is the user an admin.

    Returns:
        User: The created user object.
    """

    logger.info(f"Creating user with username={username}")

    password = PasswordManager().get_password_hash(password)

    with get_db() as session:
        user = User(
            name=name,
            age=age,
            username=username,
            email=email,
            password=password,
            is_admin=is_admin
        )
        session.add(user)
        session.commit()
        session.refresh(user)
    return user


async def authenticator(username: str, password: str):
    """
    Authenticate a user with the given username and password.

    Args:
        username (str): The username of the user to authenticate.
        password (str): The password of the user to authenticate.

    Returns:
        str: The JWT token if the authentication is successful, None otherwise.
    """
    logger.info(f"User logged in with username={username}")

    user = await get_user_by_username(username)

    if not user or not PasswordManager().verify_password(password, user.password):
        logger.error("Invalid username or password")
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return await AuthHandler().encode_token(
        user=user,
        access_token_expires=timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    )


async def register(request: RegisterUserRequest):
    """
    Register a user.

    Args:
        request (RegisterUserRequest): The request body containing the username, password, email, name, and is_admin of the user to register.

    Returns:
        str: The JWT token if the registration is successful.

    Raises:
        HTTPException: If the username already exists.
    """

    check_exists_user_with_username = await get_user_by_username(request.username)
    if check_exists_user_with_username:
        logger.error(f"User with username={request.username} already exists")
        raise HTTPException(
            status_code=400,
            detail=f"User with username={request.username} already exists"
        )

    check_exists_user_with_email = await get_user_by_username(request.email)
    if check_exists_user_with_email:
        logger.error(f"User with email={request.email} already exists")
        raise HTTPException(
            status_code=400,
            detail=f"User with email={request.email} already exists"
        )

    new_user = await create_user(
        name=request.name,
        age=request.age,
        username=request.username,
        email=request.email,
        password=request.password,
        is_admin=request.is_admin
    )

    return await AuthHandler().encode_token(
        user=new_user,
        access_token_expires=timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    )
