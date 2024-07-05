def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(license):
    return min_char(license) and first_two_char(license) and chk_spl_char(license) and validate_num(license)

def min_char(license):
    return True if 2 <= len(license) <= 6  else False

def first_two_char(license):
    return True if license[0:2].isalpha() else False

def chk_spl_char(license):
    return True if license.isalnum() else False

def validate_num(license):
    num_pos = None

    for i in range(len(license)):
        if license[i].isnumeric() and num_pos == None:
            if license[i] == "0":
                return False
            else:
                num_pos = i
        elif num_pos != None:
            if license[i].isalpha():
                return False
    """
    # Checks if there is atleast one number in the input
    if num_pos == None:
        return False
    """
    return True

main()
