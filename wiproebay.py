#ebay wants to sell several products
#price of products are given
#shipping distance is given from fulfillment zone to delivery point
#SKUs- ordered product is available or not in fulfilment zone
#Find max discount price if certain product can be shipped

num_of_products = int(input())
products_price= list(map(int,input().split()))
distance = list(map(int,input().split()))
sku =list(map(int,input().split()))

for product in range(num_of_products):
    if sku[product] > 0:
        print(products_price[product]*distance[product],end=" ")

#or using zip method
for product_price, dist, s in zip(products_price, distance, sku):
    if s > 0:
        print(product_price * dist, end=" ")

#use zip for iterating in multiple lists
#search ennumerate