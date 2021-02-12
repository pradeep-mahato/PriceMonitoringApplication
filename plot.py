import matplotlib.pyplot as plt
import xlrd

# this function generates a graph for tracked price
def read_and_plot():
    #taking input from the xlsx file
    inputWorkbook = xlrd.open_workbook("D:\\Knowledge & Learn\\Programs\\Price Monitoring Application\\out.xlsx")
    inputWorksheet = inputWorkbook.sheet_by_index(0)

    date=[]
    price=[]

    n = inputWorksheet.nrows

    for y in range(2,n):
        date.append(inputWorksheet.cell_value(y,0))
        price.append(inputWorksheet.cell_value(y,1))

    plt.plot(date,price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Graph for product price record (Date vs Price)')
    plt.show()
def data_report():
    #taking input from the xlsx file
    inputWorkbook = xlrd.open_workbook("D:\\Knowledge & Learn\\Programs\\Price Monitoring Application\\out.xlsx")
    inputWorksheet = inputWorkbook.sheet_by_index(0)

    date=[]
    price=[]

    n = inputWorksheet.nrows

    for y in range(2,n):
        date.append(inputWorksheet.cell_value(y,0))
        price.append(inputWorksheet.cell_value(y,1))
    print("Product Report")
    print("Minimum price till now :",int(min(price)))
    print("Maximum price till now :",int(max(price)))
    print("Average price till now :",int(sum(price)/len(price)))



data_report()
read_and_plot()
