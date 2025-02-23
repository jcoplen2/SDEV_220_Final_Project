#final project - animal shelter
#author - jbc
#last updated 20250223
#this program will allow users to track which animals are available at the shelter. 

#import tkinter
import tkinter as tk
from tkinter import messagebox

#create class and subclasses
#animal class
class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    #string for animails
    def __str__(self):
        return f"{self.name}, {self.age}, {self.breed}"

#cat and dog class
class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed) 
        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed) 

#create main window
MainWindow = tk.Tk()
MainWindow.title("Madison Animal Shelter")
MainWindow.geometry('600x400+50+50')
MainWindow.config(bg = "sky blue")

#list to store animals
animals = []

#Label and entry for name
tk.Label(MainWindow, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(MainWindow)
name_entry.grid(row=0, column=1)

#Label and entry for age
tk.Label(MainWindow, text="Age:").grid(row=1,column=0)
age_entry = tk.Entry(MainWindow)
age_entry.grid(row=1,column=1)

#Label and entry for breed
tk.Label(MainWindow, text="Breed:").grid(row=2,column=0)
breed_entry = tk.Entry(MainWindow)
breed_entry.grid(row=2,column=1)

#display for animals
listbox = tk.Listbox(MainWindow, width=50)
listbox.grid(row=4, column=0, columnspan=2)

#add animals logic
def add_dog():
    add_animal(Dog)

def add_cat():
    add_animal(Cat)

def add_animal(animal_type):
    name = name_entry.get()
    age = age_entry.get()
    breed = breed_entry.get()

    animal = animal_type(name, age, breed)
    animals.append(animal)
    listbox.insert(tk.END, str(animal))

    #clear input boxes
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    breed_entry.delete(0, tk.END)

    #remove animal logic
def remove_animal():
    selected_animal = listbox.curselection()
        
    animals.pop(selected_animal[0])
    listbox.delete(selected_animal[0])

#buttons to add cat or dog
tk.Button(MainWindow, text="Add Dog", command=add_dog).grid(row=3,column=0)
tk.Button(MainWindow, text="Add Cat", command=add_cat).grid(row=3,column=1)

#remove animal button
tk.Button(MainWindow, text='Remove Animal', command=remove_animal).grid(row=5, column=0, columnspan=2)

#start program
if __name__ == '__main__':
    MainWindow.mainloop()