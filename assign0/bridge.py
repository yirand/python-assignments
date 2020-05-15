#!/usr/bin/env python3
"""Module-level comments"""
def main():
    with open("answers.txt") as f:
        for line in f:
            print("KEEPER: Stop! Who would cross the Bridge of Death must answer me these questions three, 'ere the other side he see.")
            name = input("KEEPER: What is your name? ").strip("!. ")
            if name.find('?') >= 0:
                print("KEEPER: Auuuuuuuugh!")
                break
            quest = input("KEEPER: What is your quest? ").strip("!. ")
            if quest.find('?') >= 0:
                print("KEEPER: Auuuuuuuugh!")
                break
            data = line.split("?")
            question = data[0]
            answer = data[1].strip().split('|')
            answer[-1] = answer[-1].strip(' \n')
            trick_answer = input(f"KEEPER: What is {question}? ").lower()
            if trick_answer.find('?') >= 0:
                print("KEEPER: Auuuuuuuugh!")
                break
            for i,item in enumerate(answer):
                if trick_answer.find(item) >= 0:
                    print("KEEPER: Right. Off you go.")
                    break
                elif i+1 == len(answer):
                    print(name.upper()+": Auuuuuuuugh!")

if __name__ == '__main__':
    main()
