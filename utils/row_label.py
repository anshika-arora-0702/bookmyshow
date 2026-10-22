def row_label(row_number: int) -> str:
    if row_number < 1:
        raise ValueError("Row number must be at least 1")

    label = ""
    while row_number > 0:
        row_number -= 1
        row_number, remainder = divmod(row_number, 26)
        label = chr(ord("A") + remainder) + label

    return label