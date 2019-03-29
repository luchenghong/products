import os # operating system

# 读取档案
def read_file():
    products = []
    if os.path.isfile('products.csv'): # 检查档案在不在
        print('找到档案了')
        with open('products.csv', 'r', encoding = 'utf-8') as f:
            for line in f:
                if '商品, 价格\n' in line:
                    continue #继续
                name,price = line.strip().split(',')
                products.append([name, price])
                # s = line.strip().split(',')
                # print(s)
        print(products)
    else:
        print('找不到档案')

# 让使用者输入
def user_input():
    while True:
        name = input('请输入商品名称：')
        if name == 'q':
            break
        price = input('请输入商品价格：')
        p = []
        # p = [name, price]
        # p.append(name)
        # p.append(price)
        products.append([name, price])
    print(products)
    # print(products[0][0]) # index

# 印出购买记录
def print_products():
    for p in products:
        print(p[0], '的价格是' , p[1])

# 写入档案
def write_file():
    with open('products.csv', 'w', encoding = 'utf-8') as f:   
        f.write('商品, 价格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] +'\n')

read_file()
user_input()
print_products()
write_file()
