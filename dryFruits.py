# Dictionary ##
def printBill():
    bill=0
    print('*'*50)
    print('Product\t\tQuantity\t\tPrice')
    print('*'*50)
    for p,q in invoice.items():
        print(f'{p}\t\t{q}\t\t{products[p]*q}')
        bill+=products[p]*q
    print('*'*50)
    print(f'Total Bill\t\t\t{bill}')
products={'walnuts':1500,'cashew':1800,'almond':2000,'pine nuts':8000}
invoice={} #product:quantity
while(True):
    p=input('Enter the product to buy [blank to quit]:')
    if(p==''):
        break
    uPrice=products.get(p)
    if(uPrice is None):
        print('Sorry, requested item is not availble.')
        continue
    q=eval(input('Enter the quantity:'))
    if(p not in invoice.keys()):
        invoice[p]=q
    else:
        invoice[p]+=q
printBill()