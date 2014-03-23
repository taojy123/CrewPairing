#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    import tkFileDialog
    #import tkSimpleDialog
    from ImageTk import PhotoImage
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.messagebox import *
    import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()
    from tkinter import PhotoImage

from core import Virgin

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Crew Paring Data Converter')
        self.master.geometry('481x273')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        im = PhotoImage(file='logo.gif')

        #self.Picture1 = Canvas(self.top, takefocus=1)
        #self.Picture1.create_image(0, 0, image=im)
        #self.Picture1.place(relx=0., rely=0., relwidth=1., relheight=0.179)

        #self.LabelPicture = Label(self.top, text='---', image=im, anchor='w')
        #self.LabelPicture.place(relx=0., rely=0., relwidth=1., relheight=0.179)

        self.Command4 = Button(self.top, text='Start Conversion', command=self.Command4_Cmd)
        self.Command4.place(relx=0.283, rely=0.821, relwidth=0.385, relheight=0.121)

        self.Command3 = Button(self.top, text='Choose', command=self.Command3_Cmd)
        self.Command3.place(relx=0.649, rely=0.527, relwidth=0.119, relheight=0.092)

        self.Command2 = Button(self.top, text='Choose', command=self.Command2_Cmd)
        self.Command2.place(relx=0.399, rely=0.381, relwidth=0.119, relheight=0.092)

        self.Command1 = Button(self.top, text='Choose', command=self.Command1_Cmd)
        self.Command1.place(relx=0.399, rely=0.234, relwidth=0.119, relheight=0.092)

        self.Label6 = Label(self.top, text='-', anchor='w')
        self.Label6.place(relx=0.05, rely=0.674, relwidth=0.917, relheight=0.062)

        self.Label5 = Label(self.top, text='Where do you want to save the spreadsheet?', anchor='w')
        self.Label5.place(relx=0.05, rely=0.527, relwidth=0.568, relheight=0.092)

        self.Label4 = Label(self.top, text='-', anchor='w')
        self.Label4.place(relx=0.532, rely=0.381, relwidth=0.418, relheight=0.062)

        self.Label3 = Label(self.top, text='-', anchor='w')
        self.Label3.place(relx=0.532, rely=0.234, relwidth=0.418, relheight=0.062)

        self.Label2 = Label(self.top, text='Please Choose a AOSP file', anchor='w')
        self.Label2.place(relx=0.05, rely=0.381, relwidth=0.335, relheight=0.062)

        self.Label1 = Label(self.top, text='Please Choose a prg file', anchor='w')
        self.Label1.place(relx=0.05, rely=0.234, relwidth=0.335, relheight=0.062)


        showinfo("This is the test version", "This is the test version")
        
class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command4_Cmd(self, event=None):
        pairings = Virgin.combiner(self.prg_file, self.aosp_file);
        pairings = Virgin.astrixAdder(pairings) # put the astrix in kenzie's code
        Virgin.csvWriter(pairings, self.output_file)
        for x in pairings:
            print(x)
        print("done")
        Virgin.swapper(pairings)
        choose = askquestion("Crew Paring Data Converter", "Conversion Finished!\n Do you want to continue another conversion?")
        if choose == "no":
            self.top.destroy()
        

    def Command3_Cmd(self, event=None):
        output_file = tkFileDialog.asksaveasfilename(initialdir=os.getcwd(), title="Where do you want to save the spreadsheet?")
        self.Label6["text"] = output_file
        self.output_file = output_file

    def Command2_Cmd(self, event=None):
        aosp_file = tkFileDialog.askopenfilename(initialdir=os.getcwd(), title="Please Choose a AOSP file")
        self.Label4["text"] = aosp_file.split("/")[-1]
        self.aosp_file = aosp_file
        

    def Command1_Cmd(self, event=None):
        prg_file = tkFileDialog.askopenfilename(initialdir=os.getcwd(), title="Please Choose a prg file")
        self.Label3["text"] = prg_file.split("/")[-1]
        self.prg_file = prg_file


if __name__ == "__main__":
    top = Tk()

    im = PhotoImage(file='logo.gif')
    
    #canvas = Canvas(top)
    #canvas.create_image(0, 0, image=im)
    #canvas.place(relx=0., rely=0., relwidth=1., relheight=0.179)
    
    pic = Label(top, image=im, anchor='center')
    pic.place(relx=0., rely=0., relwidth=1., relheight=0.179)
    
    Application(top).mainloop()
    
    print("Bye")
