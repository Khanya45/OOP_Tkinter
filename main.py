from tkinter import *
import tkinter.ttk
from tkinter import messagebox

root = Tk()
root.geometry("450x400")
root.title("Get Tickets")
root.config(bg="#EBB3DC")

class clsTicketSales:
    cellNumber = StringVar()
    price = StringVar()
    nr_tickets = IntVar()

    def __init__(self, window):
        self.lblcellnum = Label(window, text="Enter your cellphone number", bg="#EBB3DC")
        self.lblcellnum.place(x=20, y=50)
        self.edtcellnum = Entry(window)
        self.edtcellnum.place(x=230, y=50)

        self.lblcategory = Label(window, text="Select category", bg="#EBB3DC")
        self.lblcategory.place(x=100, y=90)
        self.cbCategory = tkinter.ttk.Combobox(window)
        self.cbCategory['values'] = ("Soccer", "Movie", "Theater")
        self.cbCategory.place(x=230, y=90)

        self.lbltickets = Label(window, text="Select number of tickets", bg="#EBB3DC")
        self.lbltickets.place(x=50, y=130)
        self.spnTickets = Spinbox(window, from_=0, to=100)
        self.spnTickets.place(x=230, y=130)

        self.btnCalc = Button(window, text="Calculate Ticket",borderwidth="6", command=self.CalcPayment)
        self.btnCalc.place(y=170, x=150)

        self.lblResult1 = Label(window, text="", textvariable=self.price, bg="#EBB3DC")
        self.lblResult1.place(y=250, x=50)

        self.lblResult2 = Label(window, text="", textvariable=self.cellNumber, bg="#EBB3DC")
        self.lblResult2.place(y=270, x=50)

        self.lblResult3 = Label(window, text="", textvariable=self.nr_tickets, bg="#EBB3DC")
        self.lblResult3.place(y=290, x=50)

        self.btnClear = Button(window, text="Clear", command=self.clear)
        self.btnClear.place(x=150, y=350)

        self.btnExit = Button(window, text="Exit", command=self.exit)
        self.btnExit.place(x=220, y=350)


    def CalcPayment(self):
        if self.edtcellnum.get().isdigit() == False or len(self.edtcellnum.get()) < 10:
            messagebox.showerror("warning", "write the correct cellphone number")
        elif int(self.spnTickets.get()) == 0:
            messagebox.showerror("Warning", "Please select the number of tickets")
        elif self.cbCategory.get() == "":
            messagebox.showerror("Warning", "Please select the Category")
        else:
            if self.cbCategory.get() == "Soccer":
                prize = 40
                cost = float(self.spnTickets.get()) * prize + 14/100
                self.price.set("Amount payable: R" + str(cost))
                self.cellNumber.set("Reservation for " + self.cbCategory.get() + " for " + str(self.spnTickets.get()))
                self.nr_tickets.set("was done by " + str(self.edtcellnum.get()))
            elif self.cbCategory.get() == "Movie":
                prize = 75
                cost = float(self.spnTickets.get()) * prize + 14/100
                self.price.set("Amount payable: R" + str(cost))
                self.cellNumber.set("Reservation for " + self.cbCategory.get() + " for " + str(self.spnTickets.get()))
                self.nr_tickets.set("was done by " + str(self.edtcellnum.get()))
            elif self.cbCategory.get() == "Theater":
                prize = 100
                cost = float(self.spnTickets.get()) * prize + 14/100
                self.price.set("Amount payable: R" + str(cost))
                self.cellNumber.set("Reservation for " + self.cbCategory.get() + " for " + str(self.spnTickets.get()))
                self.nr_tickets.set("was done by " + str(self.edtcellnum.get()))

    def clear(self):
        self.edtcellnum.delete(1, END)
        st = ""
        self.price.set(st)
        self.cellNumber.set(st)
        self.nr_tickets.set(st)
        self.nr_tickets.set(st)
        self.spnTickets.delete(0, END)
        self.cbCategory.delete(0, END)

    def exit(self):
         root.destroy()



objTicketSales = clsTicketSales(root)

root.mainloop()






