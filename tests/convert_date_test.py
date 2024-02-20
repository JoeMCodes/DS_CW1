### TEST PAGE FOR FUNCTION
### NOTE: It would be better practice to import relative function
### But there is issues with trying to import using parent directory
### 'from ..src.data_cleaning.convert_dates import convert_date' 
### gives 'ImportError: attempted relative import with no known parent package'

def convert_date(date: str):
    if 'BC' in date:
        date = date.strip(' BC')
        date = -int(date)
    elif 'AD' in date:
        date = date.strip('AD ')
        date = int(date)
    else: raise ValueError("Invalid input format")
    return(date)


def test_convert_date():
    # Test BC dates
    assert convert_date("500 BC") == -500
    assert convert_date("1 BC") == -1 
    assert convert_date("1000 BC") == -1000

    # Test AD dates
    assert convert_date("AD 500") == 500
    assert convert_date("AD 1") == 1
    assert convert_date("AD 1000") == 1000

    # Test mixed cases
    assert convert_date("500 AD") == 500
    assert convert_date("1 AD") == 1
    assert convert_date("1000 AD") == 1000
    assert convert_date("500 BC") == -500
    assert convert_date("1 BC") == -1
    assert convert_date("1000 BC") == -1000

    # Test edge cases
    assert convert_date("AD 0") == 0
    assert convert_date("BC 0") == 0
    assert convert_date("AD 2024") == 2024
    assert convert_date("BC 2024") == -2024

 # Test invalid input
    try:
        convert_date("Invalid")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError for invalid input"

    try:
        convert_date("")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError for invalid input"

    try:
        convert_date("AD")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError for invalid input"

    try:
        convert_date("BC")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError for invalid input"

    try:
        convert_date("X AD")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError for invalid input"

    try:
        convert_date("500ABC")
    except ValueError:
        pass  # This is expected
    else:
        assert False, "Expected ValueError for invalid input"


    print("All test cases passed successfully.")

test_convert_date()
