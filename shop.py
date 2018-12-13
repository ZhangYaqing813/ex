
product = {
    '1':('huawei',10000),'2':('xiaomi',5000),'3':('oppo',6000)
}

def func_list():
    print('\tq: quit\n','\td:delete sm in car\n')

def shop():
    car=[]
    maney=[]
    flag=False
# print product list number:name:price
    for key,value in product.items():
        print(key,value[0],value[1],'\n')

    func_list()

    i = 0
    while not flag:
#print func number
        product_sn= input('enter you want porduct number:\n')
#delete one of the car,also maney
        if product_sn == 'd':
            if len(car):
                for tt in car:
                    i += 1
                    print(i,':',tt)
                d_sn= input('delet number:')
                car.remove(car[int(d_sn)-1])
                maney.remove(maney[int(d_sn)-1])
            else:
                print('nothing ')
                continue
#quit this prog
        if product_sn == 'q':
            print(car,'\n',maney)
            return sum(maney)
            quit()
#add product to car and get the product pric
        if product_sn in product.keys():
            car.append(product.get(product_sn)[0])
            maney.append(product.get(product_sn)[1])

x=shop()
print(x)