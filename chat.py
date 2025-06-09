import os
from fileinput import filename

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            #if '商品,價格' in line:
            #    continue  # 遇到"商品,價格"字串，則跳過此行
            chat = line.strip().split(',')
            products.append([chat])
    return products

#讀取檔案

#印出所有購買記錄
def print_products(products):
    for p in products:
        print(p[0])

#寫入檔案
#def write_file(filename, products):
#    with open(filename,'w', encoding='utf-8') as f:
#        f.write('商品,價格\n')
#        for p in products:
#            f.write(p[0]+','+p[1]+'\n')

#def main():
#    filename = 'products.csv'
#    if os.path.isfile(filename): #檢查檔案是否存在
#        print('file exist')
#        products = read_file(filename)
#
#    else:
#        print('file is not exist')
#
#    products = user_input(products)
#    print_products(products)
#    write_file('products.csv', products)

#main()