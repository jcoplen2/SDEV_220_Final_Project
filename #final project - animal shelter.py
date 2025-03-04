#final project - animal shelter
#author - jbc
#last updated 20250223
#this program will allow users to track which animals are available at the shelter. 

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

#cat class
class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed) 

#dog class        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed) 

#create main window
MainWindow = tk.Tk()
MainWindow.title("Madison Animal Shelter")
MainWindow.config(bg = "sky blue")

#list to store animals
animals = []

#count for animals
animal_count = 0
dog_count = 0
cat_count = 0

#create title label
WindowName = tk.Label(MainWindow, text = "Animal Management", font = ("Arial", 20),bg = "Sky blue", fg = "black")
WindowName.grid(row=0, column=2, padx=20, pady=20)

#Label and entry for name
tk.Label(MainWindow, text="Name:", bg= 'sky blue').grid(row=1, column=1, padx=5, pady=5)
name_entry = tk.Entry(MainWindow)
name_entry.grid(row=1, column=2, padx=5, pady=5)

#Label and entry for age
tk.Label(MainWindow, text="Age:", bg='sky blue').grid(row=2,column=1, padx=5, pady=5)
age_entry = tk.Entry(MainWindow)
age_entry.grid(row=2,column=2, padx=5, pady=5)

#Label and entry for breed
tk.Label(MainWindow, text="Breed:", bg='sky blue').grid(row=3,column=1, padx=5, pady=5)
breed_entry = tk.Entry(MainWindow)
breed_entry.grid(row=3,column=2, padx=5, pady=5)

#display for animals
listbox = tk.Listbox(MainWindow, width=50)
listbox.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

#add animals logic
def add_dog():
    add_animal(Dog)

def add_cat():
    add_animal(Cat)

def add_animal(animal_type):
    global animal_count, dog_count, cat_count

    name = name_entry.get()
    age = age_entry.get()
    breed = breed_entry.get()

    if name == '':
        messagebox.showwarning("Input error","Please enter a name for the animal")
        return
    
    try:
        age = int(age)
        if age <0 or age > 30:
            messagebox.showwarning("Input error","Age must be between 0-30")
            return
    except ValueError:
        messagebox.showwarning("Input error","Please enter a valid number for age")

    if breed == '':
        messagebox.showwarning("Input error","Please enter the animals breed")    
        return
    
    else:
        animal = animal_type(name, age, breed)
        animals.append(animal)
        listbox.insert(tk.END, str(animal))
        messagebox.showwarning("Success","Animal added successfully!")

        #update counts
        animal_count += 1
        if isinstance(animal, Dog):
            dog_count += 1
        else:
            cat_count += 1
        
        update_counts()

    #clear input boxes
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    breed_entry.delete(0, tk.END)

    #remove animal logic
def remove_animal():
    global animal_count, dog_count, cat_count

    selected_animal = listbox.curselection()
    
    if selected_animal:  
        animal = animals[selected_animal[0]]  
        animals.pop(selected_animal[0])  
        listbox.delete(selected_animal[0])

    animal_count -= 1
    if isinstance(animal, Dog):
            dog_count -= 1
    else:
            cat_count -= 1

    update_counts()

def update_counts():
    CountDisplay.config(text=str(animal_count))
    DogCountDisplay.config(text=str(dog_count))
    CatCountDisplay.config(text=str(cat_count))
    
#buttons to add cat or dog
tk.Button(MainWindow, text="Add Dog", command=add_dog).grid(row=4,column=1, padx=5, pady=5)
tk.Button(MainWindow, text="Add Cat", command=add_cat).grid(row=4,column=2, padx=5, pady=5)

#remove animal button
tk.Button(MainWindow, text='Remove Animal', command=remove_animal).grid(row=6, column=2, columnspan=2, padx=5, pady=5)

#display current animal count
AnimalCountLabel = tk.Label(MainWindow, text = "Total Animals:", font = ("Arial", 12),bg = "sky blue", fg = "black")
AnimalCountLabel = AnimalCountLabel.grid(row=7, column=2, padx=5, pady=5)
CountDisplay = tk.Label(MainWindow, text=str(animal_count),height=1, width=3, font=("Arial", 15))
CountDisplay.grid(row=8, column=2, padx=5, pady=5)

#display current dog count
DogCountLabel = tk.Label(MainWindow, text = "Total Dogs:", font = ("Arial", 12),bg = "sky blue", fg = "black")
DogCountLabel = DogCountLabel.grid(row=9, column=2, padx=5, pady=5)
DogCountDisplay = tk.Label(MainWindow, text=str(dog_count),height=1, width=3, font=("Arial", 15))
DogCountDisplay.grid(row=10, column=2, padx=5, pady=5)

#display current cat count
CatCountLabel = tk.Label(MainWindow, text = "Total Cats:", font = ("Arial", 12),bg = "sky blue", fg = "black")
CatCountLabel = CatCountLabel.grid(row=9, column=1, padx=5, pady=5)
CatCountDisplay = tk.Label(MainWindow, text=str(cat_count),height=1, width=3, font=("Arial", 15))
CatCountDisplay.grid(row=10, column=1, padx=5, pady=5)

#start program
if __name__ == '__main__':
    MainWindow.mainloop() 