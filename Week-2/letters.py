def main():
    guest_list = ['Mario', 'Lugi', 'Daisy', 'Yoshi','Bowser']
    #print(write_letter('Mario', 'Princess Peachs'))
    """
    for i in range(len(guest_list)):
        print(write_letter(guest_list[i], "Princess Peach"))
    """
    for i in guest_list:
        print(write_letter(i, "Princess Peach"))

def write_letter(reciever, sender):
    return f'''
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {reciever},
        
        You are cordially invited to a ball 
        at Peach's Castle this evening, 7:00 PM. 
        
        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    '''

main()