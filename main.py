def main():
    intro()
    
    try:
        miles_traveled = int(input('Please enter the number of miles traveled: '))
        miles_to_kilometers(miles_traveled)
    except:
        print('Try again. Please enter a numeric value for miles traveled.')
        print()
        main()

def intro():
    print('This program converts the number of miles traveled')
    print('into kilometers traveled.')
    print('For your reference, the formula is:')
    print('1 mile = 1.61 kilometers.')
    print()

def miles_to_kilometers(miles):
    kilometers = miles * 1.61
    print('Traveling', miles, 'miles is equal to traveling', kilometers, 'kilometers.')

main()