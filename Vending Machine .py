https://edabit.com/challenge/dKLJ4uvssAJwRDtCo



products = [
  { 'number': 1, 'price': 100, 'name': 'Orange juice' },
  { 'number': 2, 'price': 200, 'name': 'Soda' },
  { 'number': 3, 'price': 150, 'name': 'Chocolate snack' },
  { 'number': 4, 'price': 250, 'name': 'Cookies' },
  { 'number': 5, 'price': 180, 'name': 'Gummy bears' },
  { 'number': 6, 'price': 500, 'name': 'Condoms' },
  { 'number': 7, 'price': 120, 'name': 'Crackers' },
  { 'number': 8, 'price': 220, 'name': 'Potato chips' },
  { 'number': 9, 'price': 80,  'name': 'Small snack' }
]
Result={}
money=250
product_number=4
change=[500, 200, 100, 50, 20, 10]
for istenen_urun in products:
    if product_number==istenen_urun['number']:
      if istenen_urun['price']>money:
        print('Not enough money for this product')
      else:
        Result.update(product=istenen_urun['name'])
        A=[]
        kalan=money-istenen_urun['price']
        for para in change:
          while kalan>=para:
            kalan -= para
            A+=[para]
        Result.update(change=A)
        print(Result)
if product_number not in list(range(1,len(products))):
        print('Enter a valid product number')


          




#Test.assert_equals(vending_machine(products, 500, 8), { 'product': 'Potato chips', 'change': [ 200, 50, 20, 10 ] })
#Test.assert_equals(vending_machine(products, 500, 1), { 'product': 'Orange juice', 'change': [ 200, 200 ] })
#Test.assert_equals(vending_machine(products, 200, 7), { 'product': 'Crackers', 'change': [ 50, 20, 10 ] })
#Test.assert_equals(vending_machine(products, 100, 9), { 'product': 'Small snack', 'change': [ 20 ] })
#Test.assert_equals(vending_machine(products, 1000, 6), { 'product': 'Condoms', 'change': [ 500 ] })
#Test.assert_equals(vending_machine(products, 250, 4), { 'product': 'Cookies', 'change': [] })
#Test.assert_equals(vending_machine(products, 500, 0), 'Enter a valid product number')
#Test.assert_equals(vending_machine(products, 90, 1), 'Not enough money for this product')
#Test.assert_equals(vending_machine(products, 0, 0), 'Enter a valid product number')