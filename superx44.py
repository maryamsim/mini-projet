
from tkinter import *
from tkinter import messagebox
from datetime import date


root = Tk()
root.geometry("1200x550")
root.title("SUPERMARKET")


img1 = PhotoImage(file='image1.png').subsample(8)
img2 = PhotoImage(file='milk1.png').subsample(8)
img3 = PhotoImage(file='mirind.png').subsample(3)
img4 = PhotoImage(file='tonik.png').subsample(3)

hawai = IntVar()
milk = IntVar()
merendina = IntVar()
tonik = IntVar()
var_total = 0
var_date = ""
var_rest = 0

price_list = [6, 7, 3, 20]

date1_label = None
total1_label = None
rest1_label = None

def cancel():
    global date1_label, total1_label, rest1_label

    hawai.set(0)
    milk.set(0)
    merendina.set(0)
    tonik.set(0)
    name_entry.delete(0, "end")
    price_entry.delete(0, "end")

    if date1_label:
        date1_label.destroy()
        date1_label = None  

    if total1_label:
        total1_label.destroy()
        total1_label = None

    if rest1_label:
        rest1_label.destroy()
        rest1_label = None 

    name_entry.focus()

# functions
def pay():
    global var_total, var_date, date1_label, total1_label

    if name_entry.get() == "":
        messagebox.showerror(title="Error", message="Please enter client name")
    else:
        var_total = hawai.get() * price_list[0] + milk.get() * price_list[1] + merendina.get() * price_list[2] + tonik.get() * price_list[3]
        var_date=date.today()
        date1_label = Label(root,width=16, text=var_date, font='arial 15 bold', foreground="#1e5d3a")
        date1_label.place(x=620, y=193)

        total1_label = Label(root, width=16, text=var_total, font='arial 15 bold', foreground="#1e5d3a")
        total1_label.place(x=620, y=123)


def confirm():
    global var_total, var_rest, rest1_label

    var_rest = int(price_entry.get()) - int(var_total)

    rest1_label = Label(root, text=var_rest,width=16, font='arial 15 bold', foreground="#1e5d3a")
    rest1_label.place(x=620, y=333)

def save():
    global var_total, var_date, var_rest

    f = name_entry.get()
    v1 = var_total
    v2 = var_date
    p = price_entry.get()
    cancel()

    all_data = f + ";" + str(v1) + ";" + str(v2) + ";" + str(p) + ";" + str(var_rest) + "\n"
    with open(r"C:\Users\HP\Desktop\market\desktop-tutorial\mini-projet\file.csv", "a") as file:
        file.write(all_data)

    label_fact=Label(root,text="BILL",font='arial 15 bold')
    label_fact.place(x=900,y=50)

    bill_text = Text(root, width=25, height=10,font="arial 15 bold")
    bill_text.insert(END, "Client: " + f + "\n")
    bill_text.insert(END, "Total: $" + str(v1) + "\n")
    bill_text.insert(END, "Date: " + str(v2) + "\n")
    bill_text.insert(END, "Price: $" + str(p) + "\n")
    bill_text.insert(END, "Rest: $" + str(var_rest) + "\n")
    bill_text.place(x=900,y=80) 

     
        
button1=Button(root, text="HAWAI",font='arial 15 bold',fg="#FFFFFF",bg="#0e1d54",width=100,height=100,image=img1,compound=TOP)
button1.place(x=30,y=50)
button2=Button(root, text="MILK",font='arial 15 bold',fg="#FFFFFF",bg="#0e1d54",width=100,height=100,image=img2,compound=TOP)
button2.place(x=300,y=50)
button3=Button(root, text="MIRINDINA",font='arial 15 bold',fg="#FFFFFF",bg="#0e1d54",width=100,height=100,image=img3,compound=TOP)
button3.place(x=30,y=270)
button4=Button(root, text="TONIK",font='arial 15 bold',fg="#FFFFFF",bg="#0e1d54",width=100,height=100,image=img4,compound=TOP)
button4.place(x=300,y=270)


sp1=Spinbox(root,from_=0,to=10,width=15,textvariable=hawai,background="#5c99ad",justify=CENTER)
sp1.place(x=35,y=180)
sp2=Spinbox(root,from_=0,to=10,width=15, textvariable=milk,background="#5c99ad",justify=CENTER)
sp2.place(x=300,y=180)
sp3=Spinbox(root,from_=0,to=10,width=15,textvariable=merendina, background="#5c99ad",justify=CENTER)
sp3.place(x=30,y=400)
sp4=Spinbox(root,from_=0,to=10,width=15,textvariable=tonik,background="#5c99ad",justify=CENTER)
sp4.place(x=300,y=400)

#client name
name_label=Label(root,text="CLIENT NAME:",font='arial 15 bold')
name_label.place(x=450,y=50)
name_entry=Entry(root,width=30,font='arial 10 bold')
name_entry.place(x=620,y=53)

#total price
total_label=Label(root,text="TOTAL PRICE :",font='arial 15 bold')
total_label.place(x=450,y=120)

#date
date_label=Label(root,text="DATE :",font='arial 15 bold')
date_label.place(x=450,y=190)


#client price
price_label=Label(root,text="CLIENT PRICE :",font='arial 15 bold')
price_label.place(x=450,y=260)
price_entry=Entry(root,width=30,font='arial 10 bold')
price_entry.place(x=620,y=263)

#rest
rest_label=Label(root,text="REST :",font='arial 15 bold')
rest_label.place(x=450,y=330)
#function hover
def hover1(event):
    event.widget.configure(bg="#66faf8")
def default1(event):
    event.widget.configure(bg="#ad64ff")


def hover2(event):
    event.widget.configure(bg="#fe4902")
def default2(event):
    event.widget.configure(bg="#ffd700")


def hover3(event):
    event.widget.configure(bg="#1b5028")
def default3(event):
    event.widget.configure(bg="#98fb98")


def hover4(event):
    event.widget.configure(bg="#f2057a")
def default4(event):
    event.widget.configure(bg="#ff91a4")



#buttons
pay_btn=Button(root,text="Pay",command=pay,width=7,font='arial 15 bold',background="#ad64ff")
pay_btn.place(x=450,y=400)

cancel_btn=Button(root,text="Cancel",command=cancel,width=7,font='arial 15 bold',background="#ffd700")
cancel_btn.place(x=620,y=400)

confirm_btn=Button(root,text="Confirm",command=confirm,font='arial 15 bold',background="#98fb98")
confirm_btn.place(x=450,y=450)

save_btn=Button(root,text="Save",width=7,command=save,font='arial 15 bold',background="#ff91a4")
save_btn.place(x=620,y=450)
  

pay_btn.bind("<Enter>",hover1)
pay_btn.bind("<Leave>",default1)

cancel_btn.bind("<Enter>",hover2)
cancel_btn.bind("<Leave>",default2)

confirm_btn.bind("<Enter>",hover3)
confirm_btn.bind("<Leave>",default3)

save_btn.bind("<Enter>",hover4)
save_btn.bind("<Leave>",default4)





root.mainloop()
