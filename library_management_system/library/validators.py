import datetime

# Error validation module
def validate_publication_year(publication_year):
    """
    Validates the publication year to ensure it is a valid number and falls between the
    earliest known printed books (1450) and the current year.
    """
    current_year = datetime.datetime.now().year
    try:
        publication_year = int(publication_year)
        if publication_year < 1450 or publication_year > current_year:
            return f"Publication year must be between 1450 and {current_year}."
        return None  # No error
    except ValueError:
        return "Publication year must be a valid number."


def validate_genre(genre):
    """
    Validates the genre to ensure it is within the accepted genres.
    Modify the list according to your needs.
    """
    accepted_genres = ['Fiction', 'Non-fiction', 'Mystery', 'Science Fiction', 'Fantasy', 'Biography']
    if genre not in accepted_genres:
        return f"Genre must be one of the following: {', '.join(accepted_genres)}."
    return None  # No error


def validate_user_data(username, email, password):
    """
    Example validation for user data.
    You can expand this function for username, email format, and password length, etc.
    """
    errors = {}
    if len(username) < 3:
        errors['username'] = "Username must be at least 3 characters long."

    if '@' not in email or '.' not in email:
        errors['email'] = "Enter a valid email address."

    if len(password) < 6:
        errors['password'] = "Password must be at least 6 characters long."

    return errors
