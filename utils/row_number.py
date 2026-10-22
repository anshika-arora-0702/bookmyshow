def row_number(row_char: str) -> int:
    if not row_char or not row_char.isascii() or not row_char.isalpha():
        raise ValueError("Row label must contain only letters A-Z")

    number = 0
    for char in row_char.upper():
        number = number * 26 + ord(char) - ord("A") + 1

    return number