from tkinter import *
from tkinter import messagebox
import random,os,smtplib,tempfile





def print_bill():
    if script.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill is Empty")
    else:
        file= tempfile.mktemp(".txt")
        open(file,"w").write(script.get(1.0,END))
        os.startfile(file,"Print")


def send_email():

    def send_gmail():
        try:
            ob=smtplib.SMTP("smtp.gmail.com",587)
            ob.starttls()
            ob.login(sender_entry.get(),password_entry.get())
            ob.sendmail(sender_entry.get(),receiver_entry.get(),email_bill.get(1.0,END))
            ob.quit()
            messagebox.showinfo("Success","Email is successfully sent")
        except:
            messagebox.showerror("Error","Something went wrong. Try again later")
    root1= Toplevel()
    root1.grab_set()
    root1.title("Send Email")
    root1.resizable(0,0)
    root1.config(bg="gray20")
    sender= LabelFrame(root1,text="Sender",font="Times 20 bold",bd=8,relief="groove",bg="gray20",fg="gold")
    sender.grid(row=0,column=0,padx=10,pady=8)

    sender_add =Label(sender,text="Sender Address",font="Times 14 bold",bg="gray20",fg="white")
    sender_add.grid(row=0,column=0,padx=10,pady=8,sticky="w")
    sender_entry =Entry(sender,width=20,bd=4)
    sender_entry.grid(row=0,column=1,padx=10,pady=8)
    password =Label(sender,text="Password",font="Times 14 bold",bg="gray20",fg="white")
    password.grid(row=1,column=0,sticky="w",padx=10,pady=8)
    password_entry =Entry(sender,width=20,bd=4,show="*")
    password_entry.grid(row=1,column=1,padx=10,pady=8)

    receiver= LabelFrame(root1,text="Recepient",font="Times 20 bold",bd=8,relief="groove",bg="gray20",fg="gold")
    receiver.grid(row=1,column=0,padx=10,pady=8)

    receiver_add =Label(receiver,text="Receiver Address",font="Times 14 bold",bg="gray20",fg="white")
    receiver_add.grid(row=0,column=0,padx=10,pady=8,sticky="w")
    receiver_entry =Entry(receiver,width=20,bd=4)
    receiver_entry.grid(row=0,column=1,pady=8,padx=10)



    message=Label(receiver,text="Message: ",font="Times 14 bold",bg="gray20",fg="white")
    message.grid(row=1,column=0,padx=10,pady=8,sticky="w")
    email_bill =Text(receiver,font="Times 12 bold",height=12,width=40)
    email_bill.grid(row=2,column=0,columnspan=2)

    email_bill.insert(END,script.get(1.0,END).replace("=",'').replace("-",'').replace("\t\t\t",'\t\t').replace("\t\t",'\t'))


    send =Button(receiver,text="SEND",font="Times 16 bold",bd=6,relief="groove",padx=20,command=send_gmail)
    send.grid(row=3,column=0,columnspan=2,padx=10,pady=8)
    root1.mainloop()


def search_all():
    for i in os.listdir('bills/'):
        if int(i.split('.')[0]) == int(Bill_no_entry.get()):
            f=open(f"bills/{i}",'r')
            script.delete(1.0,END)
            for data in f:
                script.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror("Error","Invalid Bill Number")






def clear_all():
    Fish_entry.delete(0,END)
    Qeema_entry.delete(0,END)
    Chicken_entry.delete(0,END)
    Beef_entry.delete(0,END)
    Mutton_entry.delete(0,END)
    
    Chicken_entry.insert(0,0)
    Mutton_entry.insert(0,0)
    Beef_entry.insert(0,0)
    Qeema_entry.insert(0,0)
    Fish_entry.insert(0,0)    

    Oil_entry.delete(0,END)
    Sugar_entry.delete(0,END)
    Milk_entry.delete(0,END)
    Eggs_entry.delete(0,END)
    Rice_entry.delete(0,END)
    
    Rice_entry.insert(0,0) 
    Sugar_entry.insert(0,0)
    Eggs_entry.insert(0,0)
    Milk_entry.insert(0,0)
    Oil_entry.insert(0,0)

    Dew_entry.delete(0,END)
    Coke_entry.delete(0,END)
    Sprite_entry.delete(0,END)
    Sting_entry.delete(0,END)
    Fanta_entry.delete(0,END)


    Dew_entry.insert(0,0)
    Fanta_entry.insert(0,0)
    Coke_entry.insert(0,0)
    Sting_entry.insert(0,0)
    Sprite_entry.insert(0,0)

    cold_price_entry.delete(0,END)
    grocery_price_entry.delete(0,END)
    Meat_price_entry.delete(0,END)

    cold_tax_entry.delete(0,END)
    grocery_tax_entry.delete(0,END)
    Meat_tax_entry.delete(0,END)
    Bill_no_entry.delete(0,END)
    name_entry.delete(0,END)
    Phone_entry.delete(0,END)
    Bill_no_entry.insert(0,0)
    script.delete(1.0,END)

    messagebox.showinfo("Success","Cleared Successfully")


if not os.path.exists("bills"):
    os.mkdir("bills")



def save_bill():
    global bill_number
    res=messagebox.askyesno("Confirm","Do you want to save the bill")
    if res:
        bill_content=script.get(1.0,END)
        f=open(f"bills/ {bill_number}.txt", 'w')
        f.write(bill_content)
        f.close()
        
        messagebox.showinfo("Success",f"Bill number {bill_number} saved successfully")
        bill_number =random.randint(200,999)








bill_number =random.randint(200,999)

def Bill_area():
    if name_entry.get()=='' or Phone_entry.get()=='':
        messagebox.showerror("ERROR","Customer Details Required")
    elif Meat_price_entry.get()=='' and grocery_price_entry.get()=='' and cold_price_entry.get()=='':
        messagebox.showerror("ERROR","No Product is Selected")
    elif Meat_price_entry.get()=='0 Rs' and grocery_price_entry.get()=='0 Rs' and cold_price_entry.get()=='0 Rs':
         messagebox.showerror("ERROR","No Product is Selected")
    else:
        script.delete(1.0,END)
        script.insert(END,"\t\t**WELCOME CUSTOMER**")
        script.insert(END,f"\n\nBill Number : {bill_number}")
        script.insert(END,f"\nCustomer Name : {name_entry.get().title()}")
        script.insert(END,f"\nCustomer Phone Number : {Phone_entry.get()}")
        script.insert(END,"\n\n======================================================")
        script.insert(END,"Products\t\t\tQuantity\t\tPrice")
        script.insert(END,"\n======================================================")

        if bp !='0':
            script.insert(END,f"\nBeef\t\t\t{bp}\t\t{int(bp) * 800} Rs")
        if mp !='0':
            script.insert(END,f"\nMutton\t\t\t{mp}\t\t{int(mp) * 2000} Rs")

        if cp !='0':
            script.insert(END,f"\nChicken\t\t\t{cp}\t\t{int(cp) * 600} Rs")
        
        if qp !='0':
            script.insert(END,f"\nQeema\t\t\t{qp}\t\t{int(qp) * 1100} Rs")
        
        if fp !='0':
            script.insert(END,f"\nFish\t\t\t{fp}\t\t{int(fp) * 700} Rs")

        if ep !='0':
            script.insert(END,f"\nEggs\t\t\t{ep}\t\t{int(ep) * 22} Rs")
        if mip !='0':
            script.insert(END,f"\nMilk\t\t\t{mip}\t\t{int(mip) * 210} Rs")

        if sp !='0':
            script.insert(END,f"\nSugar\t\t\t{sp}\t\t{int(sp) * 120} Rs")
        
        if op !='0':
            script.insert(END,f"\nOil\t\t\t{op}\t\t{int(op) * 560} Rs")
        
        if rp !='0':
            script.insert(END,f"\nRice\t\t\t{rp}\t\t{int(rp) * 320} Rs")

        
        if cop !='0':
            script.insert(END,f"\nCoka Cola\t\t\t{cop}\t\t{int(cop) * 200} Rs")
        if fap !='0':
            script.insert(END,f"\nFanta\t\t\t{fap}\t\t{int(fap) * 160} Rs")

        if spp !='0':
            script.insert(END,f"\nSprite\t\t\t{spp}\t\t{int(spp) * 190} Rs")
        
        if stp !='0':
            script.insert(END,f"\nSting\t\t\t{stp}\t\t{int(stp) * 100} Rs")
        
        if dp !='0':
            script.insert(END,f"\nDew\t\t\t{dp}\t\t{int(dp) * 180} Rs")
        script.insert(END,"\n\n------------------------------------------------------")
        if Meat_tax_entry.get()!='0.0 Rs':
            script.insert(END,f"\n\nMeat Tax\t\t\t\t\t{Meat_tax_entry.get()}")
        if grocery_tax_entry.get()!='0.0 Rs':
            script.insert(END,f"\nGrocery Tax\t\t\t\t\t{grocery_tax_entry.get()}\n")
        if cold_tax_entry.get()!='0.0 Rs':
            script.insert(END,f"Cold Drinks Tax\t\t\t\t\t{cold_tax_entry.get()}")
        script.insert(END,"\n\n------------------------------------------------------")

        script.insert(END,f"\nTotal Bill\t\t\t\t\t{round(total_price,3)} Rs")

        script.insert(END,"\n------------------------------------------------------")
        save_bill()










def Display():

    global bp,mp,fp,qp,cp
    global op,mip,sp,rp,ep
    global cop,stp,spp,fap,dp
    global total_price
    bp= Beef_entry.get()
    mp= Mutton_entry.get()
    fp= Fish_entry.get()
    qp= Qeema_entry.get()
    cp= Chicken_entry.get()

    total_meat= int(bp) * 800 + int(qp) * 1100 + int(fp) * 700 + int(mp)*2000 + int(cp)*600
    Meat_price_entry.delete(0,END)
    Meat_price_entry.insert(0,f"{total_meat} Rs")

    total_tax = total_meat * 0.05
    Meat_tax_entry.delete(0,END)
    Meat_tax_entry.insert(0,f"{round(total_tax,2)} Rs")




    op= Oil_entry.get()
    mip= Milk_entry.get()
    sp= Sugar_entry.get()
    rp= Rice_entry.get()
    ep= Eggs_entry.get()

    total_grocery = int(mip)*210+int(rp)*320+int(op)*560+int(ep)*22+int(sp)*120
    grocery_price_entry.delete(0,END)
    grocery_price_entry.insert(0,f"{total_grocery} Rs")


    total_tax1 = total_grocery * 0.02
    grocery_tax_entry.delete(0,END)
    grocery_tax_entry.insert(0,f"{round(total_tax1,2)} Rs")


    cop= Coke_entry.get()
    fap= Fanta_entry.get()
    stp= Sting_entry.get()
    spp= Sprite_entry.get()
    dp = Dew_entry.get()

    total_cold=int(cop)*200+int(fap)*160+int(stp)*100+int(dp)*180+int(spp)*190
    cold_price_entry.delete(0,END)
    cold_price_entry.insert(0,f"{total_cold} Rs")

    total_tax2 = total_cold * 0.01
    cold_tax_entry.delete(0,END)
    cold_tax_entry.insert(0,f"{round(total_tax2,2)} Rs")


    total_price = total_cold + total_grocery + total_meat + total_tax + total_tax1 + total_tax2

root = Tk()

root.title("Retail bill System")


root.geometry("1366x768")



head= Label(root,text="Retail Billing System",font="Times 25 bold",bd=10,relief= "sunken",bg="gray15",fg="gold",pady=10)
head.pack(fill="x")

detail = LabelFrame(root,text="Customer Details",font="Times 25 bold",bd=10,relief= "sunken",bg="gray15",fg="gold",pady=8)

detail.pack(fill="x")


name = Label(detail,text="Name",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
name.grid(row=0,column=0,padx=13)

name_entry=Entry(detail,width=22,bd=6)
name_entry.grid(row=0,column=1)


Phone = Label(detail,text="Phone Number",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Phone.grid(row=0,column=2,padx=13)
Phone_entry=Entry(detail,width=22,bd=6)
Phone_entry.grid(row=0,column=3)



Bill_no = Label(detail,text="Bill Number",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Bill_no.grid(row=0,column=4,padx=13)
Bill_no_entry=Entry(detail,width=22,bd=6)
Bill_no_entry.grid(row=0,column=5)
Bill_no_entry.insert(0,0)
search=Button(detail,text="SEARCH",bg="gray20",font="arial 15 bold",fg= "gold",bd=8,relief="groove",padx=6,command=search_all)
search.grid(row=0,column=6,padx=20)

items= Frame(root)
items.pack(fill="x")

meat = LabelFrame(items,text="Meat Items",font="Times 20 bold",bd=10,relief= "sunken",bg="gray15",fg="gold")
meat.grid(row=0,column=0)


Mutton = Label(meat,text="Mutton",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Mutton.grid(row=0,column=0,padx=13,pady=6,sticky="w")
Mutton_entry=Entry(meat,width=16,font="Times 10 bold",bd=6)
Mutton_entry.grid(row=0,column=1,padx=12)
Mutton_entry.insert(0,0)

Beef = Label(meat,text="Beef",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Beef.grid(row=1,column=0,padx=13,pady=6,sticky="w")
Beef_entry=Entry(meat,width=16,font="Times 10 bold",bd=6)
Beef_entry.grid(row=1,column=1,padx=12)
Beef_entry.insert(0,0)


Fish = Label(meat,text="Fish",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Fish.grid(row=2,column=0,padx=13,pady=6,sticky="w")
Fish_entry=Entry(meat,width=16,font="Times 10 bold",bd=6)
Fish_entry.grid(row=2,column=1,padx=12)
Fish_entry.insert(0,0)



Chicken = Label(meat,text="Chicken",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Chicken.grid(row=3,column=0,padx=13,pady=6,sticky="w")
Chicken_entry=Entry(meat,width=16,font="Times 10 bold",bd=6)
Chicken_entry.grid(row=3,column=1,padx=12)
Chicken_entry.insert(0,0)


Qeema = Label(meat,text="Qeema",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Qeema.grid(row=4,column=0,padx=13,pady=6,sticky="w")
Qeema_entry=Entry(meat,width=16,font="Times 10 bold",bd=6)
Qeema_entry.grid(row=4,column=1,padx=12)
Qeema_entry.insert(0,0)




grocery = LabelFrame(items,text="Grocery Items",font="Times 20 bold",bd=10,relief= "sunken",bg="gray15",fg="gold")
grocery.grid(row=0,column=1)


Rice = Label(grocery,text="Rice",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Rice.grid(row=0,column=0,padx=13,pady=6,sticky="w")
Rice_entry=Entry(grocery,width=16,font="Times 10 bold",bd=6)
Rice_entry.grid(row=0,padx=12,column=1)
Rice_entry.insert(0,0)

Oil = Label(grocery,text="Oil",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Oil.grid(row=1,column=0,padx=13,pady=6,sticky="w")
Oil_entry=Entry(grocery,width=16,font="Times 10 bold",bd=6)
Oil_entry.grid(row=1,column=1,padx=12)
Oil_entry.insert(0,0)


Sugar = Label(grocery,text="Sugar",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Sugar.grid(row=2,column=0,padx=13,pady=6,sticky="w")
Sugar_entry=Entry(grocery,width=16,font="Times 10 bold",bd=6)
Sugar_entry.grid(row=2,column=1,padx=12)
Sugar_entry.insert(0,0)



Milk = Label(grocery,text="Milk",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Milk.grid(row=3,column=0,padx=13,pady=6,sticky="w")
Milk_entry=Entry(grocery,width=16,font="Times 10 bold",bd=6)
Milk_entry.grid(row=3,column=1,padx=12)
Milk_entry.insert(0,0)


Eggs = Label(grocery,text="Eggs",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Eggs.grid(row=4,column=0,padx=13,pady=6,sticky="w")
Eggs_entry=Entry(grocery,width=16,font="Times 10 bold",bd=6)
Eggs_entry.grid(row=4,column=1,padx=12)
Eggs_entry.insert(0,0)







Cold_Drinks = LabelFrame(items,text="Cold_Drinks",font="Times 20 bold",bd=10,relief= "sunken",bg="gray15",fg="gold")
Cold_Drinks.grid(row=0,column=2)


Coke = Label(Cold_Drinks,text="Coka Cola",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Coke.grid(row=0,column=0,padx=13,pady=6,sticky="w")
Coke_entry=Entry(Cold_Drinks,width=16,font="Times 10 bold",bd=6)
Coke_entry.grid(row=0,column=1,padx=12)
Coke_entry.insert(0,0)

Fanta = Label(Cold_Drinks,text="Fanta",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Fanta.grid(row=1,column=0,padx=13,pady=6,sticky="w")
Fanta_entry=Entry(Cold_Drinks,width=16,font="Times 10 bold",bd=6)
Fanta_entry.grid(row=1,column=1,padx=12)
Fanta_entry.insert(0,0)


Sprite = Label(Cold_Drinks,text="Sprite",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Sprite.grid(row=2,column=0,padx=13,pady=6,sticky="w")
Sprite_entry=Entry(Cold_Drinks,width=16,font="Times 10 bold",bd=6)
Sprite_entry.grid(row=2,column=1,padx=12)
Sprite_entry.insert(0,0)



Sting = Label(Cold_Drinks,text="Sting",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Sting.grid(row=3,column=0,padx=13,pady=6,sticky="w")
Sting_entry=Entry(Cold_Drinks,width=16,font="Times 10 bold",bd=6)
Sting_entry.grid(row=3,column=1,padx=12)
Sting_entry.insert(0,0)


Dew = Label(Cold_Drinks,text="Dew",bg="gray20",font="arial 15 bold",fg= "white",bd=8,relief="groove",padx=6)
Dew.grid(row=4,column=0,padx=20,pady=6,sticky="w")
Dew_entry=Entry(Cold_Drinks,width=16,font="Times 10 bold",bd=6)
Dew_entry.grid(row=4,column=1,padx=12)
Dew_entry.insert(0,0)

bill = Frame(items,bd=8,relief="groove",bg="gray20")
bill.grid(row=0,column=4)

text = Label(bill,text="Bill Area",font="Times 15 bold",bg="silver",bd=8,relief="ridge",fg="Black",padx=10,pady=8)
text.pack(fill="x")


scroll= Scrollbar(bill,orient=VERTICAL)
scroll.pack(side="right",fill=Y)

script=Text(bill,height=14.5,width=54,yscrollcommand=scroll.set)
script.pack()

scroll.configure(command = script.yview)


prices = LabelFrame(root,text="Prices",font="Times 20 bold",bd=10,relief= "sunken",bg="gray15",fg="gold")
prices.pack(fill="x")


Meat_price = Label(prices,text="Meat Price",bg="gray20",font="arial 15 bold",fg= "white",bd=4,relief="groove",padx=6)
Meat_price.grid(row=0,column=0,padx=13,pady=8)
Meat_price_entry=Entry(prices,width=16,font="Times 10 bold",bd=6)
Meat_price_entry.grid(row=0,column=1)


grocery_price = Label(prices,text="Grocery Price",bg="gray20",font="arial 15 bold",fg= "white",bd=4,relief="groove",padx=6)
grocery_price.grid(row=1,column=0,padx=13,pady=8)
grocery_price_entry=Entry(prices,width=16,font="Times 10 bold",bd=6)
grocery_price_entry.grid(row=1,column=1)


cold_price = Label(prices,text="Cold drink Price",bg="gray20",font="arial 15 bold",fg= "white",bd=4,relief="groove",padx=6)
cold_price.grid(row=2,column=0,padx=13,pady=8)
cold_price_entry=Entry(prices,width=16,font="Times 10 bold",bd=6)
cold_price_entry.grid(row=2,column=1)



Meat_tax = Label(prices,text="Meat Tax",bg="gray20",font="arial 15 bold",fg= "white",bd=4,relief="groove",padx=6)
Meat_tax.grid(row=0,column=2,padx=13,pady=8)
Meat_tax_entry=Entry(prices,width=16,font="Times 10 bold",bd=6)
Meat_tax_entry.grid(row=0,column=3)


grocery_tax = Label(prices,text="Grocery Tax",bg="gray20",font="arial 15 bold",fg= "white",bd=4,relief="groove",padx=6)
grocery_tax.grid(row=1,column=2,padx=13,pady=5)
grocery_tax_entry=Entry(prices,width=16,font="Times 10 bold",bd=6)
grocery_tax_entry.grid(row=1,column=3)

cold_tax = Label(prices,text="Cold drink Tax",bg="gray20",font="arial 15 bold",fg= "white",bd=4,relief="groove",padx=6)
cold_tax.grid(row=2,column=2,padx=13)
cold_tax_entry=Entry(prices,width=16,font="Times 10 bold",bd=6)
cold_tax_entry.grid(row=2,column=3)

total = Button(prices,text="Total",font="Times 20 bold",bd=8,relief="groove",padx=6,command=Display)
total.grid(row=0,column=4,rowspan=3,padx=20)


billbtn =Button(prices,text="Bill",font="Times 20 bold",bd=8,relief="groove",padx=6,command=Bill_area) 
billbtn.grid(row=0,column=5,rowspan=3,padx=20)

email = Button(prices,text="Email",font="Times 20 bold",bd=8,relief="groove",padx=6,command=send_email)
email.grid(row=0,column=6,rowspan=3,padx=20)

print= Button(prices,text="Print",font="Times 20 bold",bd=8,relief="groove",padx=6,command=print_bill)
print.grid(row=0,column=7,rowspan=3,padx=20)

clear = Button(prices,text="Clear",font="Times 20 bold",bd=8,relief="groove",padx=6,command=clear_all)
clear.grid(row=0,column=8,rowspan=3,padx=12)





root.mainloop()