from tkinter import *
import random,math,os
from  tkinter import messagebox
root=Tk()
root.geometry("1350x750+0+0")
root.title("BILLING SOFTWARE")
bg_color="deep sky blue"
        #adding title
title=Label(root,text="Sarthak Super Shopee",font="lucida 30 bold",bd=12,bg=bg_color,fg="white",relief=GROOVE,pady=2).pack(fill=X)


        #adding functions
def total():
    c_s_p = soap.get() * 40
    c_fc_p = face_cream.get() * 120
    c_fw_p = face_wash.get() * 60
    c_hs_p = spray.get() * 180
    c_hg_p = gell.get() * 140
    c_bl_p = loshan.get() * 180
    total_cosmetic_price=float(
        c_s_p+
        c_fc_p+
        c_fw_p+
        c_hs_p+
        c_hg_p+
        c_bl_p
        )
    cosmetic_price.set("Rs. "+str(total_cosmetic_price))        #setting cosmetic price
    c_tax=round((total_cosmetic_price*0.05),2)
    cosmetic_tax.set("Rs. "+str(c_tax))

    g_r_p = rice.get() * 80
    g_f_p = food_oil.get() * 180
    g_d_p = daal.get() * 60
    g_w_p = wheat.get() * 240
    g_s_p = sugar.get() * 45
    g_t_p = tea.get() * 150


    total_grocery_price=float(
        g_r_p+
        g_f_p+
        g_d_p+
        g_w_p+
        g_s_p+
        g_t_p
        )
    grocery_price.set("Rs. "+str(total_grocery_price))  #setting grocery price
    g_tax=round((total_grocery_price*0.1),2)
    grocery_tax.set("Rs. "+str(g_tax))

    d_m_p = maza.get() * 80
    d_c_p = cock.get() * 180
    d_f_p = frooti.get() * 60
    d_t_p = thumbsup.get() * 240
    d_l_p = limca.get() * 45
    d_s_p = sprite.get() * 150

    total_drinks_price = float(
        d_m_p+
        d_c_p +
        d_f_p+
        d_t_p+
        d_l_p +
        d_s_p
        )
    cold_drink_price.set("Rs. "+str(total_drinks_price))
    d_tax=round((total_drinks_price*0.05),2)
    cold_drink_tax.set("Rs. "+str(d_tax))

    Total_bill=float(total_cosmetic_price+total_grocery_price+total_drinks_price+c_tax+d_tax+g_tax)
    #welcome_bill()

def welcome_bill():
    txtarea.delete('1.0',END)
    txtarea.insert(END,"\tWelcome to sarthak shop\n")
    txtarea.insert(END,f"\nBill Number: {bill_no.get()}")
    txtarea.insert(END,f"\n Customer Name:{c_name.get()}")
    txtarea.insert(END,f"\n Phone Number:{c_phon.get()}")
    txtarea.insert(END,"\n======================================")
    txtarea.insert(END,"\n Products\t\tQTY\t\tPrice")
    txtarea.insert(END,"\n======================================")


def bill_area():
    if c_name.get() == "" or c_phon.get() == "":
        messagebox.showerror("Error", "Customer details are must")
    elif cosmetic_price.get()=="Rs. 0.0" and grocery_price.get()=="Rs. 0.0" and cold_drink_price.get()=="Rs. 0.0":
        messagebox.showerror("Error", "no product selected ")

    else:
        c_s_p = soap.get() * 40
        c_fc_p = face_cream.get() * 120
        c_fw_p = face_wash.get() * 60
        c_hs_p = spray.get() * 180
        c_hg_p = gell.get() * 140
        c_bl_p = loshan.get() * 180

        g_r_p = rice.get() * 80
        g_f_p = food_oil.get() * 180
        g_d_p = daal.get() * 60
        g_w_p = wheat.get() * 240
        g_s_p = sugar.get() * 45
        g_t_p = tea.get() * 150

        d_m_p = maza.get() * 80
        d_c_p = cock.get() * 180
        d_f_p = frooti.get() * 60
        d_t_p = thumbsup.get() * 240
        d_l_p = limca.get() * 45
        d_s_p = sprite.get() * 150

        total_cosmetic_price = float(
            c_s_p +
            c_fc_p +
            c_fw_p +
            c_hs_p +
            c_hg_p +
            c_bl_p
        )
        c_tax = round((total_cosmetic_price * 0.05), 2)

        total_grocery_price = float(
            g_r_p +
            g_f_p +
            g_d_p +
            g_w_p +
            g_s_p +
            g_t_p
        )
        g_tax = round((total_grocery_price * 0.1), 2)

        total_drinks_price = float(
            d_m_p +
            d_c_p +
            d_f_p +
            d_t_p +
            d_l_p +
            d_s_p
        )
        cold_drink_price.set("Rs. " + str(total_drinks_price))
        d_tax = round((total_drinks_price * 0.05), 2)

        Total_bill = float(total_cosmetic_price + total_grocery_price + total_drinks_price + c_tax + d_tax + g_tax)

        welcome_bill()
        # cosmetics
        if soap.get() != 0:
            txtarea.insert(END, f"\n Bath Soap\t\t {soap.get()}\t\t {c_s_p}")
        if face_cream.get() != 0:
            txtarea.insert(END, f"\n Face Cream\t\t {face_cream.get()}\t\t {c_fc_p}")
        if face_wash.get() != 0:
            txtarea.insert(END, f"\n Face Wash\t\t {face_wash.get()}\t\t {c_fw_p}")
        if spray.get() != 0:
            txtarea.insert(END, f"\n Spray\t\t {spray.get()}\t\t {c_hs_p}")
        if gell.get() != 0:
            txtarea.insert(END, f"\n Hair gell\t\t {gell.get()}\t\t {c_hg_p}")
        if loshan.get() != 0:
            txtarea.insert(END, f"\n Loshan\t\t {loshan.get()}\t\t {c_bl_p}")
            # grocery
        if rice.get() != 0:
            txtarea.insert(END, f"\n rice\t\t {rice.get()}\t\t {g_r_p}")
        if food_oil.get() != 0:
            txtarea.insert(END, f"\n Food oil\t\t {food_oil.get()}\t\t {g_f_p}")
        if daal.get() != 0:
            txtarea.insert(END, f"\n daal\t\t {daal.get()}\t\t {g_d_p}")
        if wheat.get() != 0:
            txtarea.insert(END, f"\n wheat\t\t {wheat.get()}\t\t {g_w_p}")
        if sugar.get() != 0:
            txtarea.insert(END, f"\n sugar\t\t {sugar.get()}\t\t {g_s_p}")
        if tea.get() != 0:
            txtarea.insert(END, f"\n Tea\t\t {tea.get()}\t\t {g_t_p}")
            # colddrinks
        if maza.get() != 0:
            txtarea.insert(END, f"\n Maza\t\t {maza.get()}\t\t {d_m_p}")
        if cock.get() != 0:
            txtarea.insert(END, f"\n Cock\t\t {cock.get()}\t\t {d_c_p}")
        if frooti.get() != 0:
            txtarea.insert(END, f"\n Frooti\t\t {frooti.get()}\t\t {d_f_p}")
        if thumbsup.get() != 0:
            txtarea.insert(END, f"\n thumbsup\t\t {thumbsup.get()}\t\t {d_t_p}")
        if limca.get() != 0:
            txtarea.insert(END, f"\n limca\t\t {limca.get()}\t\t {d_l_p}")
        if sprite.get() != 0:
            txtarea.insert(END, f"\n sprite\t\t {sprite.get()}\t\t {d_s_p}")

        txtarea.insert(END, "\n======================================")
        if cosmetic_tax.get() != "Rs. 0.0":
            txtarea.insert(END, f"\n Cosmetic tax\t\t\t{cosmetic_tax.get()}")
        if grocery_tax.get() != "Rs. 0.0":
            txtarea.insert(END, f"\n Grocery tax\t\t\t{grocery_tax.get()}")
        if cold_drink_tax.get() != "Rs. 0.0":
            txtarea.insert(END, f"\n Cold Drink tax\t\t\t{cold_drink_tax.get()}")

        txtarea.insert(END, f"\n Total Bill \t\t\t Rs.{Total_bill}")

        txtarea.insert(END, "\n======================================")
        save_bill()

def save_bill():
    op=messagebox.askyesno("Save bill","do you want to save bill")
    if op>0:
        bill_data=txtarea.get('1.0',END)
        f1=open("bill/"+str(bill_no.get())+".txt","w")
        f1.write(bill_data)
        f1.close()
        messagebox.showinfo("saved",f"bill no: {bill_no.get()} saved succesfully")
    else:
        return

def find_bill():
    present="no"
    for i in os.listdir("bill/"):
        if i.split('.')[0]==search_bill.get():
            f1=open(f"bill/{i}","r")
            txtarea.delete('1.0',END)
            for d in f1:
                txtarea.insert(END,d)
            f1.close()
            present="yes"
    if present=="no":
        messagebox.showerror("error","invalidbill no")

def clear_data():
    op=messagebox.askyesno("clear","do you want to clear")
    if op>0:
        # cosematics variables
        soap.set(0)
        face_cream.set(0)
        face_wash.set(0)
        spray.set(0)
        gell.set(0)
        loshan.set(0)

        # grocery variables
        rice.set(0)
        food_oil.set(0)
        daal.set(0)
        wheat.set(0)
        sugar.set(0)
        tea.set(0)

        # colddrink variable
        maza.set(0)
        cock.set(0)
        frooti.set(0)
        thumbsup.set(0)
        limca.set(0)
        sprite.set(0)

        # total product price and tax vaiables
        cosmetic_price.set("")
        grocery_price.set("")
        cold_drink_price.set("")

        cosmetic_tax.set("")
        grocery_tax.set("")
        cold_drink_tax.set("")

        # customer
        c_name.set("")
        c_phon.set("")
        bill_no.set("")
        x = random.randint(1000, 9999)
        bill_no.set(str(x))
        search_bill.set("")
        welcome_bill()


def exit_app():
    op = messagebox.askyesno("exit", "do you really want to exit")
    if op > 0:
        root.destroy()

    #cosematics variables
soap=IntVar()
face_cream=IntVar()
face_wash=IntVar()
spray=IntVar()
gell=IntVar()
loshan=IntVar()

        #grocery variables
rice=IntVar()
food_oil=IntVar()
daal=IntVar()
wheat=IntVar()
sugar=IntVar()
tea=IntVar()

        #colddrink variable
maza=IntVar()
cock=IntVar()
frooti=IntVar()
thumbsup=IntVar()
limca=IntVar()
sprite=IntVar()

        #total product price and tax vaiables
cosmetic_price=StringVar()
grocery_price=StringVar()
cold_drink_price=StringVar()

cosmetic_tax=StringVar()
grocery_tax=StringVar()
cold_drink_tax=StringVar()

        #customer
c_name=StringVar()
c_phon=StringVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))
search_bill=StringVar()

############################allvariables###############
        #cosematics variables
soap=IntVar()
face_cream=IntVar()
face_wash=IntVar()
spray=IntVar()
gell=IntVar()
loshan=IntVar()

        #grocery variables
rice=IntVar()
food_oil=IntVar()
daal=IntVar()
wheat=IntVar()
sugar=IntVar()
tea=IntVar()

        #colddrink variable
maza=IntVar()
cock=IntVar()
frooti=IntVar()
thumbsup=IntVar()
limca=IntVar()
sprite=IntVar()

        #total product price and tax vaiables
cosmetic_price=StringVar()
grocery_price=StringVar()
cold_drink_price=StringVar()

cosmetic_tax=StringVar()
grocery_tax=StringVar()
cold_drink_tax=StringVar()

        #customer
c_name=StringVar()
c_phon=StringVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))
search_bill=StringVar()

       #customwer details frame
F1=LabelFrame(root,text="Customer Details",bd=10,relief=GROOVE,font="lucida 15 bold",fg="gold",bg=bg_color)
F1.place(x=0,y=80,relwidth=1)
#adding labels and entries inframe f1 for customer name
cname_lbl=Label(F1,text="Customer name",bg=bg_color,fg="white",font="lucida 18 bold").grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

##adding labels and entries inframe f1 for phone no
cphn_lbl=Label(F1,text=" Phone No",bg=bg_color,fg="white",font="lucida 18 bold").grid(row=0,column=2,padx=20,pady=5)
cphn_txt=Entry(F1,width=15,textvariable=c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

##adding labels and entries inframe f1 for bill
cbill_lbl=Label(F1,text="Bill  No",bg=bg_color,fg="white",font="lucida 18 bold").grid(row=0,column=4,padx=20,pady=5)
cbill_txt=Entry(F1,width=15,textvariable=search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

    #adding button
bill_btn=Button(F1,text="Search",command=find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #coosematics frame
F2=LabelFrame(root,text="Cosmetics",bd=10,relief=GROOVE,font="lucida 15 bold",fg="gold",bg=bg_color)
F2.place(x=5,y=180,width=325,height=380)

    #adding labels
bath_lbl=Label(F2,text="Bath soap",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
bath_txt=Entry(F2,width=10,textvariable=soap,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

Face_cream_lbl=Label(F2,text="Face Cream",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
Face_cream_txt=Entry(F2,width=10,textvariable=face_cream,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

Face_w_lbl=Label(F2,text="Face Wash",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
Face_w_txt=Entry(F2,width=10,textvariable=face_wash,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

Hair_s_lbl=Label(F2,text="Hair Spray",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
Hair_s_txt=Entry(F2,width=10,textvariable=spray,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

Hair_g_lbl=Label(F2,text="Hair Gel",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
Hair_g_txt=Entry(F2,width=10,textvariable=gell,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

Body_lbl=Label(F2,text="Body lotion",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
Body_txt=Entry(F2,width=10,textvariable=loshan,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


            #grocery frame
F3=LabelFrame(root,text="Grocery",bd=10,relief=GROOVE,font="lucida 15 bold",fg="gold",bg=bg_color)
F3.place(x=340,y=180,width=325,height=380)

    #adding labels
g1_lbl=Label(F3,text="Rice",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
g1_txt=Entry(F3,width=10,textvariable=rice,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

g2_lbl=Label(F3,text="Food Oil",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
g2_txt=Entry(F3,width=10,textvariable=food_oil,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

g3_lbl=Label(F3,text="Daal",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
g3_txt=Entry(F3,width=10,textvariable=daal,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

g4_lbl=Label(F3,text="Wheat",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
g4_txt=Entry(F3,width=10,textvariable=wheat,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

g5_lbl=Label(F3,text="Sugar",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
g5_txt=Entry(F3,width=10,textvariable=sugar,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

g6_lbl=Label(F3,text="Tea",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
g6_txt=Entry(F3,width=10,textvariable=tea,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

            #colddrink frame
F4=LabelFrame(root,text="Cold Drink",bd=10,relief=GROOVE,font="lucida 15 bold",fg="gold",bg=bg_color)
F4.place(x=670,y=180,width=325,height=380)

    #adding labels
c1_lbl=Label(F4,text="Maza",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
c1_txt=Entry(F4,width=10,textvariable=maza,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

c2_lbl=Label(F4,text=" Cock",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
c2_txt=Entry(F4,width=10,textvariable=cock,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

c3_lbl=Label(F4,text="Frooti",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
c3_txt=Entry(F4,width=10,textvariable=frooti,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

c4_lbl=Label(F4,text="Thumps up",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
c4_txt=Entry(F4,width=10,textvariable=thumbsup,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

c5_lbl=Label(F4,text="Limca",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
c5_txt=Entry(F4,width=10,textvariable=limca,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

c1_lbl=Label(F4,text="Sprite",font="lucida 16 bold",bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
c6_txt=Entry(F4,width=10,textvariable=sprite,font="lucida 16 bold",bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

            #bill area frame
F5=LabelFrame(root,bd=10,relief=GROOVE)
F5.place(x=1010,y=180,width=350,height=380)

bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        #adding scrollbar
scrol_y=Scrollbar(F5,orient=VERTICAL)
txtarea=Text(F5,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH,expand=1)

        #button frame

F6=LabelFrame(root,text="Bill Menu",bd=10,relief=GROOVE,font="lucida 15 bold",fg="gold",bg=bg_color)
F6.place(x=0,y=600,relwidth=1,height=180)
    #adding labels
m1_lbl=Label(F6,text="Total Cosmetic price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
m1_txt=Entry(F6,width=18,textvariable=cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

m2_lbl=Label(F6,text="Total Grocery price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
m2_txt=Entry(F6,width=18,textvariable=grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)


m3_lbl=Label(F6,text="Total Cold Drinks price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
m3_txt=Entry(F6,width=18,textvariable=cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


m4_lbl=Label(F6,text=" Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
m4_txt=Entry(F6,width=18,textvariable=cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

m5_lbl=Label(F6,text=" Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
m5_txt=Entry(F6,width=18,textvariable=grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

m6_lbl=Label(F6,text=" Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
m6_txt=Entry(F6,width=18,textvariable=cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        #making button frame inf6
btn_F=Frame(F6,bd=7,relief=GROOVE)
btn_F.place(x=780,width=630,height=105)
total_btn=Button(btn_F,command=total,text="Total",bg="cadetblue",fg="white",pady=15,width=11,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
GBill_btn=Button(btn_F,command=bill_area,text="generate bill",bg="cadetblue",fg="white",pady=15,width=11,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
Clear_btn=Button(btn_F,text="clear",command=clear_data,bg="cadetblue",fg="white",pady=15,width=11,bd=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
Exit_btn=Button(btn_F,text="Exit",command=exit_app,bg="cadetblue",fg="white",pady=15,width=11,bd=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
welcome_bill()
root.mainloop()