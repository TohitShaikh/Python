#Program for calculating area and perimeter of rectangle
#Accepting the value
length=float(input('Enter Length:'))
breadth=float(input('Enter Breadth:'))
#Calculating the area and perimeter of rectangle
area_rect=length*breadth
peri_rect=2*(length+breadth)
#Displaying the result
print('-'*50)
print('length{}'.format(length))
print('breadth{}'.format(breadth))
print('Area of rect = {}'.format(area_rect))
print('Perimeter of area is {}'.format(peri_rect))
print('*'*50)