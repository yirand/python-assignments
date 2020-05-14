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
            guest_ask = input("What would you like? ").lower()
            if guest_ask in ["You...do have some cheese, don't you","Have you in fact got any cheese here at all"]:
                print(f"We have {len(cheeses)} cheeses!\n {cheeses[0]} \n {cheeses[1]}\n {cheeses[2]}")
                guest_ask = input("What would you like? ").lower()
    
if __name__ == '__main__':
    main()
