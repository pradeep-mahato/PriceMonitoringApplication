import tkinter as tk
from tkinter import filedialog, Text
import os
import matplotlib.pyplot as plt
import xlrd


root = tk.Tk()
root.title("Price Monitoring Application")

canvas = tk.Canvas(root, height=1080, width=1920)
canvas.pack()

label1 = tk.Label(root, text = 'PRICE MONITORING APPLICATION')
label1.config(font = ('helvetica', 40,'underline'))
canvas.create_window(960, 50, window=label1)

label2 = tk.Label(root, text = 'Link')
label2.config(font = ('helvetica', 10))
canvas.create_window(160, 300, window = label2)

link = tk.Entry(root)
link.config(width = 100)
canvas.create_window(500, 300, window=link)

label14 = tk.Label(root, text = 'Target Price')
label14.config(font = ('helvetica', 10))
canvas.create_window(160, 270, window = label14)

tp = tk.Entry(root)
link.config(width = 100)
canvas.create_window(300, 270, window=tp)

def linkval():
    lv = link.get()

    label11 = tk.Label(root, text = 'Tracking Under Process...')
    label11.config(font = ('helvetica', 20))
    canvas.create_window(500, 400, window=label11)

    def flag():
        flag=1
        label13 = tk.Label(root, text = 'Price Monitoring Succesfull...')
        label13.config(font = ('helvetica', 20))
        canvas.create_window(500, 500, window=label13)

    button3 = tk.Button(text = 'Stop Tracking', command = flag )
    canvas.create_window(480, 460, window=button3)

    

button1 = tk.Button(text = 'Track', command = linkval )
canvas.create_window(480, 350, window=button1)

canvas.create_line(960, 960, 960, 200, dash=(4, 2))

label3 = tk.Label(root, text = 'Product Report')
label3.config(font = ('helvetica', 20, "underline"))
canvas.create_window(1250, 220, window=label3)

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

    label13 = tk.Label(root, text = "Title - ")
    label13.config(font = ('helvetica', 15))
    canvas.create_window(1120, 280, window=label13)

    title_op = inputWorksheet.cell_value(0,0)
    label12 = tk.Label(root, text = title_op)
    label12.config(font = ('helvetica', 15))
    canvas.create_window(1380, 280, window=label12)

    #print("Minimum price till now :",int(min(price)))
    label5 = tk.Label(root, text = "Minimum price till now : ")
    label5.config(font = ('helvetica', 15))
    canvas.create_window(1200, 330, window=label5)

    min_price = int(min(price))
    label6 = tk.Label(root, text = min_price)
    label6.config(font = ('helvetica', 15))
    canvas.create_window(1340, 330, window=label6)

    #print("Maximum price till now :",int(max(price)))
    label7 = tk.Label(root, text = "Maximum price till now : ")
    label7.config(font = ('helvetica', 15))
    canvas.create_window(1200, 370, window=label7)

    max_price = int(max(price))
    label8 = tk.Label(root, text = max_price)
    label8.config(font = ('helvetica', 15))
    canvas.create_window(1340, 370, window=label8)

    #print("Average price till now :",int(sum(price)/len(price)))
    label9 = tk.Label(root, text = "Average price till now : ")
    label9.config(font = ('helvetica', 15))
    canvas.create_window(1200, 410, window=label9)

    avg_price = int(sum(price)/len(price))
    label10 = tk.Label(root, text = avg_price)
    label10.config(font = ('helvetica', 15))
    canvas.create_window(1340, 410, window=label10)

    def ShowGraph():
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

    button2 = tk.Button(text = 'Show Graph', command = ShowGraph )
    canvas.create_window(1200, 470, window=button2)



data_report()
root.mainloop()