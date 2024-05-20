import random
import string
import tkinter as tk

#defining letters, digits and special characters that can be used. 
#Creating function to generate password
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

#create a string that contains all characters that can be selected from.
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

#pwd empty, do not meet criteria (no number, special characters)
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char  in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        #meets criteria set to true, but
        meets_criteria = True
        #if we should include a number, but we don't, meet_criteria gets set to false. If we do have a number and we need a number, stays true.
        if numbers:
            #but we dont have a number
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
        
    return pwd


def on_yes_number():
    global has_number #accesses global variable has_numbers
    has_number = True #sets has_number to true when "Yes" button is clicked

def on_no_number():
    global has_number
    has_number = False

def on_yes_special():
    global has_special
    has_special = True

def on_no_special():
    global has_special
    has_special = False

def main():
    root = tk.Tk()
    root.title("Random Password Generator")

    #entry field for min length
    tk.Label(root, text="Enter the minimum length:").pack()
    length_entry = tk.Entry(root) #creating entry field for min length
    length_entry.pack()


    global has_number
    has_number = False

    global has_special
    has_special = False

    #create "Yes" and "No" buttons for selecting numbers
    tk.Label(root, text="Do you want to have numbers?:").pack()
    yes_number_button = tk.Button(root, text = "Yes", command=on_yes_number, activebackground="blue")
    yes_number_button.pack()
    no_number_button = tk.Button(root, text="No", command=on_no_number)
    no_number_button.pack()

    tk.Label(root, text="Do you want to have special characters?:").pack()
    #create Yes No buttons
    yes_special_button = tk.Button(root, text="Yes", command=on_yes_special)
    yes_special_button.pack()
    no_special_button = tk.Button(root, text="No", command=on_no_special)
    no_special_button.pack()

#function to generate pwd and display it
    def on_generate():
        min_length = int(length_entry.get())
    #generate pwd based on choices and input
        pwd = generate_password(min_length, has_number, has_special)
        result_label.config(text="The generated password is: " + pwd)
        
    #creating result_label widget
    result_label = tk.Label(root, text="")
    result_label.pack()    
        
#create the gen password button and bind it to the on_generate function
    generate_button = tk.Button(root, text="Generate Password", command=on_generate)
    generate_button.pack() #displays generate pwd button

    root.mainloop()

if __name__ == "__main__":
    main()



    #yes

#Prompts for user - Min length int converts string to integers with int( (will crash program if something other than numbers used)
#.lower converts input to lower case, and checks with == "y" if it is y (true)
#min_length = int(input("Enter the minimum length: "))
#has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
#has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
#pwd = generate_password(min_length, has_number, has_special)

#print("The generated password is:", pwd)



