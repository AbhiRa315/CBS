from tkinter import*
import csv
import random
import time
import pyautogui
import win32print, win32ui, win32con  
from PIL import Image, ImageWin
import mysql.connector
import sqlite3


db = sqlite3.connect("sem6.db")

db.execute("""
    CREATE TABLE IF NOT EXISTS bill (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name text NOT NULL,
  menu1 integer NOT NULL,
  menu2 integer NOT NULL,
  menu3 integer NOT NULL,
  menu4 integer NOT NULL,
  menu5 integer NOT NULL,
  menu6 integer NOT NULL,
  cost_of_meal integer NOT NULL,
  sc real NOT NULL,
  sub_total real NOT NULL,
  gst real NOT NULL,
  total  NOT NULL,
  date_of_entry timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP);""")


root=Tk()
root.geometry("1600x800+0+0")
root.title("Fast Food Burgers")

text_Input=StringVar()
operator=""

Tops = Frame(root, width =1600,height = 50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width =800,height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

#================================time=========================================
localtime=time.asctime(time.localtime(time.time()))
#================================Info=========================================
p1=PhotoImage(file="fastfood.gif")
Label(Tops,image=p1).grid(row=0,column=0,sticky=W)
lblInfo = Label(Tops, font=('arial',50,'bold'),text="Fast Food Burgers",
                fg="Steel Blue",bd=10,anchor='e')
lblInfo.grid(row=0,column=1,sticky=E)
lblInfo = Label(Tops, font=('arial',20,'bold'),text=localtime, fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=1)
#=================================prices========================================
pfries=80
pburger=100
pfish=180
pChickenBurger=150
pCheeseBurger=120
pDrinks=40



    
#=================================Calculator====================================


def Ref():

 
    

    rfries=txtFries.get()   #fries
    qfries=int(rfries)
    tfries=qfries*pfries

    rburger=txtBurger.get()  #burger
    qburger=int(rburger)
    tburger=qburger*pburger

    rfish=txtFilet.get()    #filet_o_fish
    qfish=int(rfish,0)
    tfish=qfish*pfish

    rChickenBurger=txtChicken.get()    #ChickenBurger
    qChickenBurger=int(rChickenBurger)
    tChickenBurger=qChickenBurger*pChickenBurger

    rCheeseBurger=txtCheese.get()    #CheeseBurger
    qCheeseBurger=int(rCheeseBurger)
    tCheeseBurger=qCheeseBurger*pCheeseBurger

    rDrinks=txtDrinks.get()    #drinks
    qDrinks=int(rDrinks)
    tDrinks=qDrinks*pDrinks

    cost=tfries+tburger+tfish+tChickenBurger+tCheeseBurger+tDrinks #cost
    Cost.set(cost)
    
    sc=cost*0.1     #service charge
    st=cost+sc      #Subtotal
    Service.set(sc)
    SubTotal.set(st)
    
    gst=st*0.05  #tax
    bill=st+gst  #finalbill
    Tax.set(gst)
    Total.set(bill)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    
    fries.set(0)
    Burger.set(0)
    Filet.set(0)
    Drinks.set(0)
    Chicken.set(0)
    Cheese.set(0)
    
    Tax.set("")
    Cost.set("")
    SubTotal.set("")
    Total.set("")
    Service.set("")

def qPrint(self):
    pic = pyautogui.screenshot(region=(20,25, 1250, 600))        #taking screenshot
    pic.save('Screenshot.png')
    
    # Constants for GetDeviceCaps
    #
    # HORZRES / VERTRES = printable area
    HORZRES = 8
    VERTRES = 8
    #
    # LOGPIXELS = dots per inch
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    #
    # PHYSICALWIDTH/HEIGHT = total area
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111
    #
    # PHYSICALOFFSETX/Y = left / top margin
    PHYSICALOFFSETX = 0
    PHYSICALOFFSETY = 0

    printer_name = win32print.GetDefaultPrinter ()
    file_name = "Screenshot.png"
    #
    # You can only write a Device-independent bitmap
    #  directly to a Windows device context; therefore
    #  we need (for ease) to use the Python Imaging
    #  Library to manipulate the image.
    #
    # Create a device context from a named printer
    #  and assess the printable size of the paper.
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
    printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)

    #
    # Open the image, rotate it if it's wider than
    #  it is high, and work out how much to multiply
    #  each pixel by to get it as big as possible on
    #  the page without distorting.

    bmp = Image.open (file_name)
    if bmp.size[0] > bmp.size[1]:
      bmp = bmp.rotate (0)

    ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
    scale = min (ratios)

    #
    # Start the print job, and draw the bitmap to
    #  the printer device at the scaled size.
    #
    hDC.StartDoc (file_name)
    hDC.StartPage ()

    dib = ImageWin.Dib (bmp)
    scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
    x1 = 0
    y1 = 0
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height
    dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()

    #------------------------Database-----------------------------------------
    # entering score to database
    db = sqlite3.connect("sem6.db")
    self.a=self.rand.get()
    self.b=self.fries.get()
    self.c=self.Burger.get()
    self.d=self.Filet.get()
    self.e=self.Chicken.get()
    self.f=self.Cheese.get()
    self.g=self.Drinks.get()
    self.h=self.Cost()
    self.i=self.Service.get()
    self.j=self.SubTotal.get()
    self.k=self.Tax.get()
    self.l=sef.Total.get()
    

    
    cur = db.cursor()
    sql = ("INSERT INTO bill(name,menu1,menu2,menu3,menu4,menu5,menu6,cost_of_meal,sc,sub_total,gst,total) VALUES(?)",(self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i,self.j,self.k,self.l))
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()


    

def Be():
    r=Tk()
    r.geometry("1600x800+0+0")
    r.title("Sales Records")
    db = sqlite3.connect("sem6.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM bill")
    result = cur.fetchall()
    Label(r,text="Transaction Id").grid(row=1,column=1)
    Label(r,text="Name").grid(row=1,column=2)
    Label(r,text="Cost Of Meal").grid(row=1,column=3)
    Label(r,text="Service Charge").grid(row=1,column=4)
    Label(r,text="Sub total").grid(row=1,column=5)
    Label(r,text="GST").grid(row=1,column=6)
    Label(r,text="Final Bill").grid(row=1,column=7)
    Label(r,text="Time").grid(row=1,column=8)

    rc=2
    for x in result:
        tid = str(x[0])
        cname = str(x[1])
        com = str(x[8])
        ser = str(x[9])
        sub = str(x[10])
        GST = str(x[11])
        Bill = str(x[12])
        Time = str(x[13])
        Label(r,font=('arial',12,'bold'),text=tid).grid(row=rc,column=1)
        Label(r,font=('arial',12,'bold'),text=cname).grid(row=rc,column=2)
        Label(r,font=('arial',12,'bold'),text=com).grid(row=rc,column=3)
        Label(r,font=('arial',12,'bold'),text=ser).grid(row=rc,column=4)
        Label(r,font=('arial',12,'bold'),text=sub).grid(row=rc,column=5)
        Label(r,font=('arial',12,'bold'),text=GST).grid(row=rc,column=6)
        Label(r,font=('arial',12,'bold'),text=Bill).grid(row=rc,column=7)
        Label(r,font=('arial',12,'bold'),text=Time).grid(row=rc,column=8)

        rc=rc+1
    cur.close()
    db.close()
    btnExit=Button(r,padx=16,pady=8,width=10
                ,text="Exit",bg="powder blue",command=r.destroy).grid(row=rc+1,column=4)
    


#========================================Restaurant Info 1=================================
rand=StringVar()
fries=StringVar()
Burger=StringVar()
Filet=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken=StringVar()
Cheese=StringVar()



fries.set(0)
Burger.set(0)
Filet.set(0)
Drinks.set(0)
Chicken.set(0)
Cheese.set(0)

lblReference=Label(f1,font=('arial',16,'bold'),text="Customer Name",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,
                   bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="Fries @80",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=fries,bd=10,insertwidth=4,
                   bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="Veg Burger @100",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,
                   bg="powder blue",justify='right')
txtBurger.grid(row=2,column=1)

lblFilet=Label(f1,font=('arial',16,'bold'),text="Filet_O_Meal @180",bd=16,anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,
                   bg="powder blue",justify='right')
txtFilet.grid(row=3,column=1)


lblChicken=Label(f1,font=('arial',16,'bold'),text="Chicken Burger @150",bd=16,anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken,bd=10,insertwidth=4,
                   bg="powder blue",justify='right')
txtChicken.grid(row=4,column=1)

lblCheese=Label(f1,font=('arial',16,'bold'),text="Veg Cheese Burger @120",bd=16,anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese,bd=10,insertwidth=4,
                   bg="powder blue",justify='right')
txtCheese.grid(row=5,column=1)

lblDrinks=Label(f1,font=('arial',16,'bold'),text="Drinks @40",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,
                   bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

#========================================Restaurant Info 2=================================

lblCost=Label(f1,font=('arial',16,'bold'),text="Cost of Meal",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,
                   justify='right')
txtCost.grid(row=1,column=3)

lblService=Label(f1,font=('arial',16,'bold'),text="Service Charge-10%",bd=16,anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=Service,bd=10,insertwidth=4,
                   justify='right')
txtService.grid(row=2,column=3)

lblTax=Label(f1,font=('arial',16,'bold'),text="GST-5%",bd=16,anchor='w')
lblTax.grid(row=4,column=2)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,
                   justify='right')
txtTax.grid(row=4,column=3)

lblSubTotal=Label(f1,font=('arial',16,'bold'),text="SubTotal",bd=16,anchor='w')
lblSubTotal.grid(row=3,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,
                   justify='right')
txtSubTotal.grid(row=3,column=3)

lblTotal=Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,
                   justify='right')
txtTotal.grid(row=5,column=3)


#========================================= Buttons =========================================
btnTotal=Button(f1,padx=16,pady=8,font=('arial',16,'bold'),width=10
                ,text="Total",bg="powder blue",command=Ref).grid(row=7,column=0)

btnReset=Button(f1,padx=16,pady=8,font=('arial',16,'bold'),width=10
                ,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=1)

btnPrint=Button(f1,padx=16,pady=8,font=('arial',16,'bold'),width=10
                ,text="Print Reciept",bg="powder blue",command=qPrint).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,font=('arial',16,'bold'),width=10
                ,text="Sales Record",bg="powder blue",command=Be).grid(row=7,column=3)

btnExit=Button(f1,padx=16,pady=8,font=('arial',16,'bold'),width=10
                ,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=4)
root.mainloop()
