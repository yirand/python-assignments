#!/usr/bin/env python3
"""Module-level comments"""

def main():
    bird = float(input("How many ounces of birds are carrying the coconuts? "))
    coconuts = float(input("How many pounds of coconuts are there? "))
    if bird/coconuts >= 5.5:
        print('Yes! Carrying the coconuts is possible.')
    else:
        print('No. Carrying the coconuts is impossible.')

if __name__ == '__main__':
    main()




