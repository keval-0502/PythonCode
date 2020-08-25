item = "Paints"
x = "Quantity"
y = "Price"
q = 15
p = 10
Total_amount = p*q
c = 2
item1 = "Brushes"
q1 = 12
p1 = 5
Total_amount1 = p1*q1
myorder = ("item is {}\n{} is {}\n{} is {}\nTotal amount is {}")
print(myorder.format(item, x, q, y, p, Total_amount))
print("\n")
corder = ("Customer number is {}\nitem is {}\n{} is {}\n{} is {}\nTotal amount is {} ")
print(corder.format(c, item1, x, q1, y, p1, Total_amount1))