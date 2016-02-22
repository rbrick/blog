# region Authenticate
def authenticate(username, password):
    """
    Authenticates a user.
    How it works:
       Stores the authentication token the users computer.
       The authentication token expires after a certain period of time,
       If the authentication token is already created when the user logs in,
       then we reuse the authentication token.

       When the user visits the page, and has an authentication, we will check for the tokens validity
       if the token is still valid (Has not expired), we keep the user logged in, if not we log the user out.

       The user can opt to stay logged in, indefinitely, by checking the "Remember Me" button.

       The user can also opt to disallow multiple log-ins. This setting will generate a new authentication token
       every time a user logs in, and invalidate any other token
    :param username: The username
    :param password: The password
    :return: An authentication token
    """
    pass


def logout(username, password): pass

# endregion
