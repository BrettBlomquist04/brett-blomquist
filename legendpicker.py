import random as rn

def main():
    legends = ['Bangalore','Fuse','Mad Maggie','Ash','Ballistic','Pathfinder','Wraith','Revenant','Octane',
               'Valkyrie','Horizon','Bloodhound','Crypto','Vantage','Seer','Gibraltar','Lifeline','Mirage',
               'Loba','Conduit','Newcastle','Caustic','Wattson','Catalyst','Rampart']
    weapons = ['Havoc','Flatline','Hemlock','R-301','Nemesis','Alternator','Prowler','Volt','R-99','C.A.R',
               'Devotion','L-Star','Spitfire','Rampage','G7 Scout','Triple Take','30-30 Repeater','Bocek Bow',
               'Charge Rifle','Longbow','Sentinel','Kraber','EVA-8','Mastiff','Peacekeeper','Mozambique',
               'RE-45','P2020','Wingman']
    another = 'y'
    print('This application will give you random legend, loadout, or both.')
    print('To begin, please enter your choice of what you want generated:')
    print('For a random legend only, enter "legend" or "l" ')
    print('For a random loadout, enter "loadout" or "t" ')
    print('For both, enter "both" or "b" ')
    while another == 'y' or another == 'Y':
        choice = input('Enter your selection: ')
        if choice == "legend" or choice == "l" or choice == "L":
            legend = rn.choice(legends)
            print(f'\nYour random legend is: {legend}')
            another = input('\nEnter "y" if you would like to go again, or any other button to exit: ')
        elif choice == "loadout" or choice == 't' or choice == 'T':
            weapon1 = rn.choice(weapons)
            weapon2 = rn.choice(weapons)
            print(f'\nYour random loadout is: {weapon1} and {weapon2}')
            another = input('\nEnter "y" if you would like to go again, or any other button to exit: ')
        elif choice == "both" or choice == 'b' or choice == 'B':
            legend = rn.choice(legends)
            weapon1 = rn.choice(weapons)
            weapon2 = rn.choice(weapons)
            print(f'\nYour random legend is: \n{legend} \nAnd your random loadout is: \n{weapon1} and {weapon2}')
            another = input('\nEnter "y" if you would like to go again, or any other button to exit: ')
        else:
            print('Please enter a valid input!')
main()
input("Press Enter to exit...")