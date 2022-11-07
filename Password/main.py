#Only import the constants
from tkinter import *
#import a another class
from tkinter import messagebox
from random import choice, randint, shuffle
#THis auto copy's to the clipboard so the password can be used anytime after being generated
# s

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    """Function will generate a password"""
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #This will receive the different characters from the different list to make a unique password
    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8,10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    #this adds the contents of the list in the the password_list 
    password_list = password_letters + password_symbols + password_numbers
    #Then we shuffle the list 
    shuffle(password_list)
    #This adds the elements in the password_list  to the empty string using join() and the string is saved to the password variable using the with elements from the password_list
    password = "".join(password_list)
    
    #This populates the password field when the generate button is hit
    password_entry.insert(0, password)
    #auto copy to the clipboard
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    """This will get the data in the fields and save it to a txt file"""
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        #Showinfo is the way you send a reminder to the user.
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} "
                                                                f"\nPassword: {password} \nIs it ok to save?")

        #This controls the entries field acceptance for better user interface
        if is_ok:#This returns a boolean    
            with open("Password\data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Create the canvas where the logo will sit
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="Password\logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
web_label = Label(text="Website: ", font=("Arial", 10, "normal"))
web_label.grid(column=0, row=1)

Email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
Email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)

#Entry
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
#this makes the cusor start at the web entry field
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
#This prepopulates the email entry field the 0 is for the being and keyword "END" would be at the end of whatever is in the field
email_entry.insert(0, "roman@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#Buttons
generate_button = Button(text="Generate Password", command=password_generator , highlightthickness=0)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()