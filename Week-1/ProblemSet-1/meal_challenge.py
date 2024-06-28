def main():
    get_input = convert(input('What time is it? '))
    
    if 7 <= get_input <= 8:
        print('breakfast time')
    elif 12 <= get_input <= 13:
        print('lunch time')
    elif 18 <= get_input <= 19:
        print('dinner time')
    else:
        None

def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    if time.endswith('p.m.'):
        hours = 12 + float(hours)
        minutes = minutes.rstrip('p.m.')
    else:
        minutes = minutes.rstrip('a.m.') 
    minutes = float(minutes)/60
    tot = round(hours + minutes,2)
    return tot
    
if __name__ == '__main__':
    main()


