## This is a function to conver dates for the form
## XXX BC -> -XXX
## AD XXX -> XXX

def convert_date(date: str):
    if 'BC' in date:
        date = date.strip(' BC')
        date = -int(date)
    elif 'AD' in date:
        date = date.strip('AD ')
        date = int(date)
    else: raise ValueError("Invalid input format")
    return(date)
