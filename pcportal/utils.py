def check_password(password):
    """
    This function checks if a string (password)
    is good enough to use as a password.
    Returns True or False.
    """
    if len(password) > 5:
        return True

    else:
        return False
