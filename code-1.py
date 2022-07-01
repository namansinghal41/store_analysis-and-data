#!/usr/bin/env python
# coding: utf-8

# In[17]:


from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
 
HEIGHT = 700
WIDTH = 600
root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
canvas.pack()

def homewindow():
    l1 = Label(text="Rajasthan Store", fg="white", bg="black", bd=10,font=('Courier', 18))
    l1.place(relx=0.5, rely=0, anchor='n', )
    frame = Frame(root, bg='#7788dc', bd=5)
    frame.place(relx=0.5, rely=0.1,relwidth=1, relheight=1, anchor='n')
    button1 = Button(frame, text="Products List",font=('Courier', 17), command= plist)
    button1.place(x=170,y=30,relwidth=0.4)
    salesbutton = Button(frame, text="Sales",font=('Courier', 17), command=sales)
    salesbutton.place(x=170,y=80,relwidth=0.4)
    l2 = Label(frame, text='''About: \n Rajasthan stores, since 2005. 
                                    \nWe have been a succesfull business 
                                    \nsince 17 years, with 
                                    \ncontinuosly growing profits day by 
                                    \nday. We are known for our products 
                                    \nquality and cutomer loyalty.''',font=('Courier', 14))
    l2.place(x=100,y=130,relwidth=0.7,relheight=0.4)
    l3 = Label(frame, text='''Project by:-
-Naman Singhal-(36)
-Tanika Goyal-(53)
-Rishita Bohra-(46)
-Kriti Bhatnagar-(30)
-Jiya Gupta-(27)
-Abhinav Singh Chauhan-(3)''',font=('Courier', 14))
    l3.place(x=0,y=520,relwidth=0.5,relheight=0.3,anchor='w')
    button4 = Button(frame, text="Exit",font=('Courier', 17), command=root.destroy )
    button4.place(x=300,y=500,relwidth=0.4)
    
def plist(): #products list window
    win2 = Toplevel(root)
    win2.geometry("700x500")
    win2.title("Products List")
    canvas = Canvas(win2, height=500, width=700, bg="black")
    canvas.pack()
    l2 = Label(win2,text="Products list",fg="white", bg="black", bd=10,font=('Courier', 18))
    l2.place(relx=0.4,rely=0)
    
    def drinks():
        win3 = Toplevel(root)
        win3.geometry("700x550")
        win3.title("drinks")
        exit = Button(win3, text="Exit",font=('Courier', 17), command=root.destroy )
        exit.place(x=600,y=400)
        back = Button(win3, text="back",font=('Courier', 17),  command = win3.destroy)
        back.place(x=0, y=400)
        
        tree = ttk.Treeview(win3, column=("name", "price", "availability"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="price")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="avalability")
        tree.insert('', 'end', text="1", values=("coca-cola   ","150" , "1 in stock"))
        tree.insert('', 'end', text="1", values=('sprite', '160', '5 in stock'))
        tree.insert('', 'end', text="1", values=('limca', '200', '10 in stock'))
        tree.insert('', 'end', text="1", values=('mountain dew', '180', 'out of stock'))
        tree.pack() 
        

        headphones={'coca-cola':150,'sprite':160, 'limca':200, 'mountain dew':180}
        x_axis = list(headphones.keys())
        y_axis = list(headphones.values())
        fig = plt.figure(figsize = (5, 4))
        plt.bar(x_axis, y_axis, color ='powderblue',width = 0.3)
        plt.xlabel("Drink name")
        plt.ylabel("Price")
        plt.title("Price Comparison Of Drinks")
        figure_canvas = FigureCanvasTkAgg(fig, win3)
        toolbar = NavigationToolbar2Tk(figure_canvas, win3)
        figure_canvas.get_tk_widget().pack( )
        toolbar.update()

        
    headphones = Button(win2, text="drinks",font=('Courier', 17), command=drinks)
    headphones.place(x=300,y=100)
    
    def snacks():
        win4 = Toplevel(root)
        win4.geometry("700x550")
        win4.title("snacks")
        exit = Button(win4, text="Exit",font=('Courier', 17), command=root.destroy )
        exit.place(x=600,y=400)
        back = Button(win4, text="back",font=('Courier', 17),  command = win4.destroy)
        back.place(x=0, y=400)
        
        tree = ttk.Treeview(win4, column=("name", "price", "availability"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="price")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="avalability")
        tree.insert('', 'end', text="1", values=("chips   ","70" , "150 in stock"))
        tree.insert('', 'end', text="1", values=('biscuits', '30', '5000 in stock'))
        tree.insert('', 'end', text="1", values=('chocolates', '100', '2000 in stock'))
        tree.insert('', 'end', text="1", values=('pastry', '500', '100 in stock'))
        tree.pack()
        
        snacks={'chips':70,'biscuits':30,'chocolates':100,'pastry':500,}
        x_axis = list(snacks.keys())
        y_axis = list(snacks.values())
        fig = plt.figure(figsize = (5, 4))
        plt.plot(x_axis,y_axis,color='purple')
        plt.xlabel("Snacks Name")
        plt.ylabel("Price")
        plt.title("Price Comparison Of snacks")
        figure_canvas = FigureCanvasTkAgg(fig, win4)
        toolbar = NavigationToolbar2Tk(figure_canvas, win4)
        figure_canvas.get_tk_widget().pack( )
        toolbar.update()
        
    snacks = Button(win2, text="snacks",font=('Courier', 17), command=snacks)
    snacks.place(x=300,y=150)
    
    def soaps():
        win5 = Toplevel(root)
        win5.geometry("700x500")
        win5.title("soaps")
        exit = Button(win5, text="Exit",font=('Courier', 17), command=root.destroy )
        exit.place(x=600,y=400)
        back = Button(win5, text="back",font=('Courier', 17),  command = win5.destroy)
        back.place(x=0, y=400)
        
        tree = ttk.Treeview(win5, column=("name", "price", "availability"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="price")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="avalability")
        tree.insert('', 'end', text="1", values=("lux   ","70" , "15 in stock"))
        tree.insert('', 'end', text="1", values=('lifebuoy', '30', '500 in stock'))
        tree.insert('', 'end', text="1", values=('medimix', '100', '100 in stock'))
        tree.insert('', 'end', text="1", values=('pearls', '500', '10 in stock'))
        tree.pack()     
        
        soaps={'lux':70,'lifebuoy':30,'medimix':100,'pearls':500,}
        x_axis = list(soaps.keys())
        y_axis = list(soaps.values())
        fig = plt.figure(figsize = (5, 5))
        plt.pie(y_axis,labels=x_axis)
        plt.title("Price Comparison Of soaps")
        figure_canvas = FigureCanvasTkAgg(fig, win5)
        toolbar = NavigationToolbar2Tk(figure_canvas, win5)
        figure_canvas.get_tk_widget().pack( )
        toolbar.update()
        
    soaps = Button(win2, text="soaps",font=('Courier', 17), command=soaps)
    soaps.place(x=300,y=200)
    
    exit = Button(win2, text="Exit",font=('Courier', 17), command=root.destroy )
    exit.place(x=600,y=400)
    back = Button(win2, text="back",font=('Courier', 17),  command = win2.destroy)
    back.place(x=0, y=400)
    
def sales():
    win6 = Toplevel(root)
    win6.geometry("700x900")
    win6.title("sales")
    exit = Button(win6, text="Exit",font=('Courier', 17), command=root.destroy )
    exit.place(x=600,y=400)
    back = Button(win6, text="back",font=('Courier', 17),  command = win6.destroy)
    back.place(x=0, y=400)
    
    tree = ttk.Treeview(win6, column=("year", "income", "profit"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="year")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="income")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="profit")
    tree.insert('', 'end', text="1", values=('2017',"345680" , "456700"))
    tree.insert('', 'end', text="1", values=('2018', '368910', '324500'))
    tree.insert('', 'end', text="1", values=('2019', '213450', '678900'))
    tree.insert('', 'end', text="1", values=('2020', '324560', '125600'))
    tree.insert('', 'end', text="1", values=('2021', '234560', '154600'))
    tree.pack() 
    
    sales={'2017':345680,'2018':368910,'2019':213450,'2020':324560,'2021':234560}
    x_axis = list(sales.keys())
    y_axis = list(sales.values())
    fig = plt.figure(figsize = (5, 3))
    plt.bar(x_axis, y_axis, color ='DarkOliveGreen',width = 0.3)
    plt.xlabel("Year")
    plt.ylabel("Income")
    plt.title("Year Vs Income")
    figure_canvas = FigureCanvasTkAgg(fig, win6)
    toolbar = NavigationToolbar2Tk(figure_canvas, win6)
    figure_canvas.get_tk_widget().pack( )
    toolbar.update()
    
    
    years=[2017,2018,2019,2020,2021]
    income=[345680,368910,213450,324560,234560]
    profit=[45670,32450,67890,125600,154600]
    y=np.arange(len(years))

    fig = plt.figure(figsize = (5, 3))
    plt.bar(y - 0.2,income,0.4,label="Income")
    plt.bar(y + 0.2,profit,0.4,label="Profit")
    width=0.25
    plt.xticks(y + width/2,['2017','2018','2019','2020','2021'])
    plt.xlabel("Year")
    plt.ylabel("Income and Profit")
    plt.title("Income and Profit through Years")
    plt.legend()
    figure_canvas = FigureCanvasTkAgg(fig, win6)
    toolbar = NavigationToolbar2Tk(figure_canvas, win6)
    figure_canvas.get_tk_widget().pack( )
    toolbar.update()

homewindow()
root.mainloop()


# In[ ]:




