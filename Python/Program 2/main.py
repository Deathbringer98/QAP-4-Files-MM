# Program Author: Matthew Menchinton
# Date: 2023-07-25
import matplotlib.pyplot as plt

def get_sales_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = []
    for month in months:
        while True:
            try:
                sales_amount = float(input(f"Enter the total sales for {month}: $"))
                if sales_amount < 0:
                    raise ValueError("Sales amount cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input. {e}")
        sales.append(sales_amount)
    return months, sales

def create_sales_graph(months, sales):
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales, color='skyblue')
    plt.xlabel("Months")
    plt.ylabel("Total Sales ($)")
    plt.title("Total Sales by Month")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    print("Enter the total amount of sales for each month from January to December.")
    months, sales = get_sales_data()
    create_sales_graph(months, sales)

if __name__ == "__main__":
    main()
