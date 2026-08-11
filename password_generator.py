import secrets
import string


def generate_password(length, use_upper, use_lower, use_numbers,
     use_symbols, exclude_ambiguous):

    selected_sets = []

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits

    if exclude_ambiguous:
        uppercase = uppercase.replace("O", "")
        lowercase = lowercase.replace("l", "")
        numbers = numbers.replace("0", "").replace("1", "")

    if use_upper:
        selected_sets.append(uppercase)

    if use_lower:
        selected_sets.append(lowercase)

    if use_numbers:
        selected_sets.append(numbers)

    if use_symbols:
        selected_sets.append(string.punctuation)

    if len(selected_sets) < 2:
        raise ValueError("Select at least two character types.")

    password = []
   
    for character_set in selected_sets:
        password.append(secrets.choice(character_set))

    all_characters = "".join(selected_sets)

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)