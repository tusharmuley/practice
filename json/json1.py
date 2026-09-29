# Tasks
# Extract all customer names.
# Find all orders with completed payment.
# Find customers from Pune.
# Calculate the total amount of each order (price × quantity).
# Find all orders containing a Laptop.
# Calculate the total revenue from completed orders only.
# Find the customer who placed the highest-value order.

orders = {
    "status": "success",
    "data": {
        "orders": [
            {
                "order_id": 1001,
                "customer": {
                    "id": 1,
                    "name": "Tushar",
                    "city": "Pune"
                },
                "items": [
                    {"product": "Laptop", "price": 50000, "quantity": 1},
                    {"product": "Mouse", "price": 500, "quantity": 2}
                ],
                "payment": {
                    "status": "completed",
                    "method": "UPI"
                }
            },
            {
                "order_id": 1002,
                "customer": {
                    "id": 2,
                    "name": "Rahul",
                    "city": "Mumbai"
                },
                "items": [
                    {"product": "Keyboard", "price": 1500, "quantity": 1},
                    {"product": "Monitor", "price": 12000, "quantity": 2}
                ],
                "payment": {
                    "status": "pending",
                    "method": "Card"
                }
            },
            {
                "order_id": 1003,
                "customer": {
                    "id": 3,
                    "name": "Priya",
                    "city": "Pune"
                },
                "items": [
                    {"product": "Laptop", "price": 50000, "quantity": 2}
                ],
                "payment": {
                    "status": "completed",
                    "method": "Card"
                }
            }
        ]
    }
}


def json_practice(obj):
    orders_data = orders['data']['orders']
    customer_data = []
    completed_orders=[]
    pune_customers=[]
    total_each_order=[]
    laptop_data=[]
    total_revenue=0
    highest_order_customer=[]
    for order in orders_data:
        customer_data.append(order['customer']['name'])
        
        # Find all orders with completed payment.
        if order['payment']['status'] == "completed":
            completed_orders.append(order)
            
        # Find customers from Pune
        if order['customer']['city'] =="Pune":
            pune_customers.append(order['customer']['name'])
            
        # Calculate the total amount of each order (price × quantity).
        current_total=0
        for item in order.get('items',[]):
            # print(item)
            current_total += item['price'] * item['quantity']
            
            # Find all orders containing a Laptop.
            if item['product'] == "Laptop":
                laptop_data.append(order['order_id'])
                
        total_each_order.append({order['order_id']:current_total})
        
        
        if order['payment']['status'] == "completed":
            for item in order['items']:
                total_revenue += item['price'] * item['quantity']
            
    
        # Find the customer who placed the highest-value order.
        current_total1=0
        for item in order['items']:
            current_total1 += item['price'] * item['quantity']
        data = {
            "customer_name":order['customer']['name'],
            "total":current_total1
        }
        highest_order_customer.append(data)
    high_amount = 0
    customer=""
    print(highest_order_customer)
    for c in highest_order_customer:
        print(c)
        if c['total']>high_amount:
            high_amount = c['total']
            customer=c
        
    return customer_data, completed_orders, pune_customers, total_each_order, laptop_data, total_revenue, highest_order_customer

customer_names, completed_orders,pune_customers, total_each_order, laptop_data, total_revenue,customer =json_practice(orders)
print("all the customers are ", customer_names)
print(" all orders with completed payment.", completed_orders)
print(" customers from Pune.", pune_customers)
print("Calculate the total amount of each order (price × quantity).",total_each_order)
print("Find all orders containing a Laptop.",laptop_data)
print("Calculate the total revenue from completed orders only.",total_revenue)
print("Find the customer who placed the highest-value order.",customer)


