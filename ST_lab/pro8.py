"""
8. Design, develop, code and run the program in any suitable language to solve
the commission problem. Analyze it from the perspective of decision table-based
testing, derive different test cases, execute these test cases and discuss the
test results.

"""

flag = 0
locks = int(input("Enter the total number of locks : "))
barrels = int(input("Enter the total number of barrelss : "))
stocks = int(input("Enter the total number of stocks : "))

if locks <= 0 or locks > 70:
    print("Invalid Locks Input")
    flag = 1

if stocks <= 0 or stocks > 80:
    print("Invalid Stocks Input")
    flag = 1

if barrels <= 0 or barrels > 90:
    print("Invalid Barrels Input")
    flag = 1

if flag == 0:
    t_sales = (locks * 45) + (stocks * 30) + (barrels * 25)

    if (t_sales <= 1000):
        commission = 0.10 * t_sales

    elif (t_sales < 1800):
        commission = 0.10 * 1000
        commission = commission + (0.15 * (t_sales - 1000))

    else:
        commission = 0.10 * 1000
        commission = commission + (0.15 * 800)
        commission = commission + (0.20 * (t_sales - 1800))

    print(f"The total sales is {t_sales} \nThe commission is {commission}")
