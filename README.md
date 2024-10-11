1.How It Works:
Criteria Checks:

The check_password_strength function checks for:

Length of at least 8 characters.

At least one lowercase letter.

At least one uppercase letter.

At least one number.

At least one special character.

2.Strength Assessment:

It counts how many criteria are met.

If 4 or more criteria are met, the password is considered "Strong."

If 3 criteria are met, it's "Moderate."

Otherwise, it's "Weak."

3.Feedback:

Provides feedback on which criteria were not met to help users improve their password.

4.User Interaction:

The main function prompts the user to enter a password, checks its strength, and provides feedback.
