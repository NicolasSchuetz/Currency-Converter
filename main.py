#Imports
import tkinter as tk

#Multi language Support
translations={
    "en":{"title":"Currency Convertor","button":"Convert",},
    "de":{"title":"Währungsrechner","button":"Umrechnen",},
    "fr":{"title":"Convertisseur de devises","button":"Convertir",},
    "es":{"title":"Conversor de monedas","button":"Convertir",},
    "it":{"title":"Convertitore di valute","button":"Convertire",},
    "pt":{"title":"Conversor de moedas","button":"Converter",},
    "ru":{"title":"Конвертер валют","button":"Преобразовать",},} 

#Class
class CurrencyConverter:
    def __init__(self,root):
        #Window
        self.root = root
        self.root.geometry("400x400")
        
        #Language
        self.language=tk.StringVar(value="en")
        self.language.trace_add("write",self.update_language) #Auto Akutalisiert
        self.lang_drop=tk.OptionMenu(root,self.language,*translations.keys())
        self.lang_drop.grid(row=0,column=4)

        #Textfeldeingabe
        self.curr1=tk.Entry(root)
        self.curr2=tk.Entry(root,state="disabled")
        self.curr1.grid(row=0,column=0)
        self.curr2.grid(row=0,column=2)
        #Drop down menu
        self.t_curr=tk.StringVar(value="USD")
        self.drop=tk.OptionMenu(root,self.t_curr,"USD","CHF","GBP")
        self.drop.grid(row=0,column=3)
        #Convert Button
        self.convert_button=tk.Button(root,command=self.convert)
        self.convert_button.grid(row=0,column=1)

        #Set language
        self.update_language()
        
    def update_language(self,*args):
        lang=self.language.get()
        self.root.title(translations[lang]["title"])
        self.convert_button.config(text=translations[lang]["button"])

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


