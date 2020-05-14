#!/usr/bin/env python3
"""Module-level comments"""
print("Good morning. Welcome to the National Cheese Emporium!")
cheeses = ['Muenster','Cheddar','Red Leicester']
cheeses_lower = [x.lower() for x in cheeses]
def main():
    guest_ask = input("What would you like? ").lower()

    while True:
        if guest_ask in cheeses_lower:
            print("We have {} cheese(s)! yessir".format(guest_ask))
            break
        else:
            print("I'm afraid we don't have any {}.".format(guest_ask))
            guest_ask = input("What would you like? ")
            if guest_ask in ["You...do have some cheese, don't you","Have you in fact got any cheese here at all"]:
                print("We have three cheeses {}!".format(cheeses))
                guest_ask = input("What would you like? ")
    
if __name__ == '__main__':
    main()
