# Problem 1
def analyze_orders(orders):
    total = 0
    largest = orders[0]
    smallest = orders[0]
    over_100 = 0

    for elm in orders:
        total += elm
        if elm > largest:
            largest = elm
        if smallest > elm:
            smallest = elm
        if elm > 100:
            over_100 +=1

    result = {
        'total':total,
        'largest': largest,
        'smallest':smallest,
        'over_100': over_100
    }

    return result
analyze_data1 = analyze_orders([120, 45, 300, 80, 300, 25, 150])

# Problem 2
def count_order_statuses(orders):
    result = {}
    for status in orders:
        if status in result:
            result[status] +=1
        else:
            result[status] = 1

    return result
count_order_statuses([
    "pending",
    "paid",
    "pending",
    "shipped",
    "paid",
    "pending",
    "cancelled",
    "paid",
    'refunded'
])

# Problem 3
def customer_totals(orders):
    result = {}
    for transfer in orders:
        customer_name = transfer['customer']
        if customer_name in result:
            result[customer_name] += transfer['amount']
        else:
            result[customer_name] = transfer['amount']

    return result
customer_totals(orders = [
    {"customer": "Sara", "amount": 120},
    {"customer": "Ali", "amount": 50},
    {"customer": "Sara", "amount": 80},
    {"customer": "John", "amount": 200},
    {"customer": "Ali", "amount": 30},
])

# Problem 4
def paid_customers_totals(orders):
    result = {}
    for transfer in orders:
        customer_name = transfer['customer']
        if transfer['status'] == 'paid':
            if customer_name in result:
                result[customer_name] += transfer['amount']
            else:
                result[customer_name] = transfer['amount']
    return result

paid_customers_totals(orders = [
    {"customer": "Sara", "amount": 120, "status": "paid"},
    {"customer": "Ali", "amount": 50, "status": "pending"},
    {"customer": "Sara", "amount": 80, "status": "paid"},
    {"customer": "John", "amount": 200, "status": "cancelled"},
    {"customer": "Ali", "amount": 30, "status": "paid"},
])

# Problem 5
def customer_summary(orders):
    result = {}
    for transfer in orders:
        customer_name = transfer['customer']
        paid_order = 0

        if transfer['status'] == 'paid':
            if customer_name in result:
                paid_order +=1
                result[customer_name]['total_paid'] += transfer['amount']
                result[customer_name]['paid_orders'] += paid_order
            
            else:
                result[customer_name] = {
                    'total_paid': transfer['amount'],
                    'paid_orders': 1
                }

    
    return result
customer_summary = customer_summary([
    {"customer": "Sara", "amount": 120, "status": "paid"},
    {"customer": "Ali", "amount": 50, "status": "pending"},
    {"customer": "Sara", "amount": 80, "status": "paid"},
    {"customer": "John", "amount": 200, "status": "cancelled"},
    {"customer": "Ali", "amount": 30, "status": "paid"}
    ])

def unique_words(sentence):
    result = []
    sentence = sentence.split()
    for x in sentence:
        if not x in result:
            result.append(x)

    return result
unique_words("python is great and python is powerful")

# Problem 7
def product_info(product):
    name, price, stock = product
    return {
        'Name':name,
        'Price':price,
        'Stock':stock,
        'Value': price * stock
    }
pp = product_info(("Rose Gift Box", 29.99, 5))


# Final Problem
def sales_report(orders):
    result = {}
    total_revenue = 0
    paid_orders = 0
    result['customer'] = dict()

    for transfer in orders:
        if transfer['status'] == 'paid':
            total_revenue += transfer['amount']
            paid_orders += 1
            result['total_aveneue'] = total_revenue
            result['paid_orders'] = paid_orders
            
            # customer name
            customer_name = transfer['customer']

            if not customer_name in result['customer']:
                result['customer'][customer_name] = transfer['amount']
            else:
                result['customer'][customer_name] += transfer['amount']

            

    return result
            

sales_report(orders = [
    {"customer": "Sara", "amount": 120, "status": "paid"},
    {"customer": "Ali", "amount": 50, "status": "pending"},
    {"customer": "Sara", "amount": 80, "status": "paid"},
    {"customer": "John", "amount": 200, "status": "cancelled"},
    {"customer": "Ali", "amount": 30, "status": "paid"},
    {"customer": "John", "amount": 100, "status": "paid"},
])