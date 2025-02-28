#Imports
import tkinter as tk

#Multi language Support
translations={
    "en":{"title":"Currency Convertor",
          "button":"Convert",},
    "de":{"title":"Währungsrechner",
          "button":"Umrechnen",},
    "fr":{"title":"Convertisseur de devises",
          "button":"Convertir",},
    "es":{"title":"Conversor de monedas",
          "button":"Convertir",},
    "it":{"title":"Convertitore di valute",
          "button":"Convertire",},
    "pt":{"title":"Conversor de moedas",
          "button":"Converter",},
    "ru":{"title":"Конвертер валют",
          "button":"Преобразовать",},} 
language="ru"
title="Currency Convertor"
button="Convert"
if language =="de":
    title=translations["de"]["title"]
    button=translations["de"]["button"]
elif language =="en":
    title=translations["en"]["title"]
    button=translations["en"]["button"]
elif language =="fr":
    title=translations["fr"]["title"]
    button=translations["fr"]["button"]
elif language =="es":
    title=translations["es"]["title"]
    button=translations["es"]["button"]
elif language =="it":
    title=translations["it"]["title"]
    button=translations["it"]["button"]
elif language =="pt":
    title=translations["pt"]["title"]
    button=translations["pt"]["button"]
elif language =="ru":
    title=translations["ru"]["title"]
    button=translations["ru"]["button"]

#Class
class CurrencyConverter:
    def __init__(self,root):
        #Result variable
        self.result = tk.StringVar()
        #Window
        self.root = root
        self.root.title(title)
        self.root.geometry("400x300")
        #Convert Button
        self.button=tk.Button(root,text=button,command=self.convert)
        self.button.grid(row=0,column=1)
        #Textfeldeingabe
        self.curr1=tk.Entry(root)
        self.curr2=tk.Entry(root,state="disabled")
        self.curr1.grid(row=0,column=0)
        self.curr2.grid(row=0,column=2)
        #Drop down menu
        self.t_curr=tk.StringVar()
        self.t_curr.set("USD")
        self.drop=tk.OptionMenu(root,self.t_curr,"USD","CHF","GBP")
        self.drop.grid(row=0,column=3)
        
    def convert(self):
        if self.t_curr.get() == "USD":
            self.result=float(self.curr1.get())*1.04
        elif self.t_curr.get() == "CHF":
            self.result=float(self.curr1.get())*1.07
        elif self.t_curr.get() == "GBP":
            self.result=float(self.curr1.get())*0.83
        self.result=round(self.result,2)
        self.curr2.config(state="normal")
        self.curr2.delete(0,"end")
        self.curr2.insert(0,str(self.result))
        self.curr2.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()


