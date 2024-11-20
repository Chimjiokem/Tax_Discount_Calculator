name_of_customer = input('Enter your name: ')
print(f'Hello, {name_of_customer}! Thank you for shopping with us.')
purchase_amount = float(input('Enter the purchase amount of items: $'))
print(f'Your purchase amount is ${purchase_amount:.2f}')

#Discount
if purchase_amount < 100:
    discount = 0
elif purchase_amount >=100 and purchase_amount <=500:
    discount = 0.1 * purchase_amount
    print(f'You have received a discount of ${discount:.2f}')
elif purchase_amount > 500:
    discount = 0.2 * purchase_amount
    print(f'You have received a discount of ${discount:.2f}')
else:
    print('Sorry, no discount today.')

x = purchase_amount - discount
print(f'Your discounted price before tax is ${x:.2f}')

#Tax
if x < 200:
    tax = 0.05 * x
    print(f'A tax deduction of ${tax:.2f} will be applied at a rate of 5%.')
elif x > 200:
    tax = 0.08 * x
    print(f'A tax deduction of ${tax:.2f} will be applied at a rate of 8%.')

#Total price calculation
total_price = x + tax
print(f'PAY ${total_price:.2f}')
y = purchase_amount - total_price
print(f'You have saved ${y:.2f} in total.')
print('Thank you.')