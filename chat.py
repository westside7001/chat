import os
from fileinput import filename

#讀取檔案
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat

def convert(chats):
    new = []
    person = None
    for gpt in chats:
        if gpt == 'Allen':
            person = "Allen"
            continue
        elif gpt == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': '+gpt)
    return new

def write_file(filename, chat):
    with open(filename,'w') as f:
        for line in chat:
            f.write(line + '\n')


def main():
    chats = read_file('input.txt')
    chats = convert(chats)
    write_file('output.txt',chats)


main()


#讀取檔案

#印出所有購買記錄
#def print_products(products):
#    for p in products:
#        print(p)
#


