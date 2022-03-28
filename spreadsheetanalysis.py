import csv


with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))


import csv

with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)
    sales = []
    for row in spreadsheet:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
print('Total sales across all months: {}'.format(total))


with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)
    months = []
    for row in spreadsheet:
        monthly_sales = int(row['sales'])
        sales.append(monthly_sales)
    monthly_sales = sales
print('Sales for each month: {}'.format(monthly_sales))


average_month = total/12
biggest_month = (max(monthly_sales))
smallest_month = (min(monthly_sales))
number_of_months = (len(sales))
print('Average sales in a month:{}'.format(average_month))
print('Month with highest sales:{}'.format(biggest_month))
print('Month with lowest sales:{}'.format(smallest_month))
print('Number of months:{}'.format(number_of_months))
