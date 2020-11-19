import tkinter as tk
from tkinter import messagebox
import integrate
from tkinter import *
from os import remove
from PIL import ImageTk, Image

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Numerical integration by Sillavich V.0.9 (Error pop up not included)")
        self.geometry("1280x720")
        self.make_topmost()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.label= Label(self,
                         text="Rectangle integral:\nTrapezoidal integral:\nSimpson integral:",
                         font="Times 10")
        self.label.place(x=100, y=600)
        self.inputValue1=''
        self.inputValue2=''
        self.inputValue3=''
        self.rectangle=''
        self.trapezoidal=''
        self.simpson=''
      #  self.show_image()
        label1=Label(self,text="Enter your function here",font="Times 10")
        label1.place(x=700,y=50)
        label2 = Label(self, text="Enter your interval here", font="Times 10")
        label2.place(x=700, y=250)
        label3 = Label(self, text="Enter number of partitions", font="Times 10")
        label3.place(x=700, y=450)
        self.T=Text(self,height=1,width=30,wrap=NONE)
        self.T.place(x=700,y=100)
        self.T2 = Text(self, height=1, width=30)
        self.T2.place(x=700, y=300)
        self.T3 = Text(self, height=1, width=30)
        self.T3.place(x=700, y=500)



        buttonCommit=Button(self,height=1,width=10,text='commmit',command=lambda: self.retrieve_input())
        buttonCommit.place(x=800,y=600)

        self.T.bind('<Return>', self.func)
        self.T.bind("<Tab>", self.focus_next_widget)
        self.T2.bind("<Tab>", self.focus_next_widget)
        self.T2.bind('<Return>', self.enterfunc)
        self.T3.bind('<Return>',self.retrieve_input_event)


    def focus_next_widget(self,event):
        event.widget.tk_focusNext().focus()
        return ("break")
    def enterfunc(self,event):
        return('break')
    def func(self,event):
     # try:
        inputValue = self.T.get("1.0", "end-1c")
        integrate.numericalIntegration(inputValue, '-5 5', 5).plot_graphic('asd')
        self.show_image()
        return('break')

   #   except Exception as e:
     #     print(e)

     # finally:
     #   return('break')

    def retrieve_input(self):
        try:
            self.inputValue1=self.T.get("1.0","end-1c")
            self.inputValue2 = self.T2.get("1.0", "end-1c")
            self.inputValue3 = self.T3.get("1.0", "end-1c")

            self.calculate_input()

            integrate.numericalIntegration(self.inputValue1, str(self.inputValue2), int(self.inputValue3)).plot_graphic('asd')
            self.show_image()
          #  labelres = Label(self, text=f"Rectangle integral: {self.rectangle}\nTrapezoidal integral: {self.trapezoidal}\nSimpson integral:{self.simpson}", font="Times 10")
           # labelres.place(x=100, y=600)
            self.label['text']=f"Rectangle integral: {self.rectangle}\nTrapezoidal integral: {self.trapezoidal}\nSimpson integral:{self.simpson}"

        except Exception as e:
            print(e)
            pass
        return('break')
    def retrieve_input_event(self,event):
        try:
            self.inputValue1=self.T.get("1.0","end-1c")
            self.inputValue2 = self.T2.get("1.0", "end-1c")
            self.inputValue3 = self.T3.get("1.0", "end-1c")

            self.calculate_input()

            integrate.numericalIntegration(self.inputValue1, str(self.inputValue2), int(self.inputValue3)).plot_graphic('asd')
            self.show_image()
          #  labelres = Label(self, text=f"Rectangle integral: {self.rectangle}\nTrapezoidal integral: {self.trapezoidal}\nSimpson integral:{self.simpson}", font="Times 10")
            #labelres.place(x=100, y=600)
            self.label['text']=f"Rectangle integral: {self.rectangle}\nTrapezoidal integral: {self.trapezoidal}\nSimpson integral:{self.simpson}"
        except Exception as e:
            print(e)
        return('break')


    def calculate_input(self):

        self.rectangle=integrate.numericalIntegration(self.inputValue1, str(self.inputValue2), int(self.inputValue3)).rectangle()
        self.trapezoidal = integrate.numericalIntegration(self.inputValue1, str(self.inputValue2),
                                                        int(self.inputValue3)).trapezoidal()
        self.simpson = integrate.numericalIntegration(self.inputValue1, str(self.inputValue2),
                                                        int(self.inputValue3)).simpson()




    def on_exit(self):

        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.destroy()
            remove('asd.png')

    def show_image(self):



        with Image.open("asd.png") as image:
            photo = ImageTk.PhotoImage(image, master=self)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.grid(row=0, column=0)
    def make_topmost(self):

        self.lift()
        self.attributes("-topmost", 1)
        self.attributes("-topmost", 0)


if __name__ == '__main__':
    App().mainloop()
