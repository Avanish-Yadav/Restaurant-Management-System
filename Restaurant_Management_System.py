from tkinter import *
from tkinter import messagebox


root=Tk()
root.title('Python Project')
root.geometry('1280x720')
bg_color='green'

#=====================variable=======================
Pizza=IntVar()
Berger=IntVar()
Chicken=IntVar()
Dhokla=IntVar()
total=IntVar()

cb=StringVar()
cr=StringVar()
cs=StringVar()
cm=StringVar()
total_cost=StringVar()

#================functions=================
def Total():
    if Pizza.get()==0 and Berger.get()==0 and Chicken.get()==0 and Dhokla.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Pizza.get()
        r=Berger.get()
        s=Chicken.get()
        m=Dhokla.get()

        t=float(b*99.0+r*200.0+s*85.0+m*70.0)
        total.set(b+r+s+m)
        total_cost.set('Rs'+str(round(t,2)))

        cb.set('Rs'+str(round(b*99.0,2)))
        cr.set('Rs'+str(round(r*200.0,2)))
        cs.set('Rs'+str(round(s*85.0,2)))
        cm.set('Rs'+str(round(m*70.0,2)))

def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,"Items\tNumber of Items\tCost of Items")
    textarea.insert(END,f'\n\nPizza\t\t{Pizza.get()}\t{cb.get()}')
    textarea.insert(END,f'\n\nBerger\t\t{Berger.get()}\t{cr.get()}')
    textarea.insert(END,f'\n\nChicken\t\t{Chicken.get()}\t{cs.get()}')
    textarea.insert(END,f'\n\nDhokla\t\t{Dhokla.get()}\t{cm.get()}')
    textarea.insert(END,'\n\n======================================')
    textarea.insert(END,f'\n\nTotal Price\t\t{total.get()}\t {total_cost.get()}')
    textarea.insert(END,'\n\n======================================')


def reset():
    textarea.delete(1.0,END)
    Pizza.set(0)
    Berger.set(0)
    Chicken.set(0)
    Dhokla.set(0)
    total.set(0)

    cb.set('')
    cr.set('')
    cs.set('')
    cm.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()


title=Label(root,text='RESTAURANT MANAGEMENT SYSTEM',bg=bg_color,fg='white',font=('times new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)
#===========Product details=========
F1=LabelFrame(root,text='MENU DETAILS',font=('times new romman',18,'bold'),fg='black',bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=5,y=90,width=825,height=500)

#=============Heading==================
itm=Label(F1,text='ITEMS',font=('Helvetic',21,'bold','underline'),fg='black',bg=bg_color)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='NUMBERS OF ORDERS',font=('Helvetic',21,'bold','underline'),fg='black',bg=bg_color)
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text='COST OF FOOD',font=('Helvetic',21,'bold','underline'),fg='black',bg=bg_color)
cost.grid(row=0,column=2,padx=20,pady=15)

#========================Product==============
bread=Label(F1,text='PIZZA',font=('times new roman',18,'bold'),fg='yellow',bg=bg_color)
bread.grid(row=1,column=0,padx=12,pady=7)
b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pizza)
b_txt.grid(row=1,column=1,padx=12,pady=7)
cb_txt=Entry(F1,text='PIZZA',font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cb)
cb_txt.grid(row=1,column=2,padx=12,pady=7)

rice=Label(F1,text='BERGER',font=('times new roman',18,'bold'),fg='yellow',bg=bg_color)
rice.grid(row=2,column=0,padx=12,pady=7)
r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Berger)
r_txt.grid(row=2,column=1,padx=12,pady=7)
cr_txt=Entry(F1,text='Berger',font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cr)
cr_txt.grid(row=2,column=2,padx=12,pady=7)

soap=Label(F1,text='CHICKEN',font=('times new roman',18,'bold'),fg='yellow',bg=bg_color)
soap.grid(row=3,column=0,padx=12,pady=7)
s_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Chicken)
s_txt.grid(row=3,column=1,padx=12,pady=7)
cs_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cs)
cs_txt.grid(row=3,column=2,padx=12,pady=7)

milk=Label(F1,text='DHOKLA',font=('times new roman',18,'bold'),fg='yellow',bg=bg_color)
milk.grid(row=4,column=0,padx=12,pady=7)
m_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Dhokla)
m_txt.grid(row=4,column=1,padx=12,pady=7)
cm_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=cm)
cm_txt.grid(row=4,column=2,padx=12,pady=7)





t=Label(F1,text='TOTAL PRICE',font=('times new roman',18,'bold'),fg='yellow',bg=bg_color)
t.grid(row=5,column=0,padx=12,pady=7)
t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total)
t_txt.grid(row=5,column=1,padx=12,pady=7)
ct_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=total_cost)
ct_txt.grid(row=5,column=2,padx=12,pady=7)

#======================bill area====================
F2=Frame(root,relief=GROOVE,bd=7)
F2.place(x=840,y=90,width=500,height=500)
bill_title=Label(F2,text='RECEIPT',font='arial 15 bold',bd=7,relief=GROOVE,bg='yellow')
bill_title.pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15 ',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview())

#===================Button==========================
F3=Frame(root,relief=GROOVE,bd=10,bg=bg_color)
F3.place(x=5,y=593,width=1350,height=104)

btn1=Button(F3,text='Total',font='arial 25 bold',bg='green',fg='black',width=10,command=Total)
btn1.grid(row=0,column=0,padx=13,pady=3)

btn2=Button(F3,text='Receipt',font='arial 25 bold',bg='green',fg='black',width=10,command=receipt)
btn2.grid(row=0,column=1,padx=13,pady=3)



btn3=Button(F3,text='Reset',font='arial 25 bold',bg='green',fg='black',width=10,command=reset)
btn3.grid(row=0,column=3,padx=13,pady=3)

btn4=Button(F3,text='Exit',font='arial 25 bold',bg='green',fg='black',width=10,command=exit)
btn4.grid(row=0,column=4,padx=13,pady=3)

root.mainloop()