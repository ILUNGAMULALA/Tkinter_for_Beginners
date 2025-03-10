import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, messagebox
import requests


# the main window
root = tk.Tk()
root.title("My App")
root.geometry("400x400")



def send_message():
    def open_file():
        file_path = filedialog.askopenfilename(title="Open File", defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)  # Clear text area
                text_area.insert(tk.END, content)

    # Function to save a file
    def save_file():
        file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".pdf",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get("1.0", tk.END))
            messagebox.showinfo("Success", "File saved successfully!")


    clear_screen()
    text_area = tk.Text(root, font=("Arial", 20), height=10, width=40)
    text_area.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    save_button = tk.Button(root, text="save", command=save_file)
    save_button.grid(row=5, column=1, columnspan=2, pady=5, padx=5)

    open_button = tk.Button(root, text="open", command=open_file)
    open_button.grid(row=6, column=1, columnspan=2, pady=5, padx=5)


# Function to fetch and display news
def getting_news ():
    clear_screen()
    def get_news():
        API_KEY = "374fa488677d488e94dac9ff312e0a8e"  # Replace with your NewsAPI key
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

        try:
            response = requests.get(url)
            news_data = response.json()

            if news_data["status"] == "ok":
                articles = news_data["articles"][:10]  # Get top 10 news articles
                news_text = "\n\n".join([f"{i+1}. {article['title']}" for i, article in enumerate(articles)])
                news_area.delete("1.0", tk.END)  # Clear previous news
                news_area.insert(tk.END, news_text)
            else:
                messagebox.showerror("Error", "Failed to fetch news. Try again.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # GUI Setup
    # root = tk.Tk()
    # root.title("Latest News")

    news_area = tk.Text(root, wrap="word", font=("Arial", 12))
    news_area.pack(expand=True, fill="both", padx=10, pady=10)

    refresh_btn = tk.Button(root, text="Get News", command=get_news)
    refresh_btn.pack(pady=5)






def main_function():
    clear_screen()
    # Main window
    #root = tk.Tk()
    #root.title("assignment 5 now on tkinterr")
    #root.geometry("1000x1000")

    def validate_inputs():
        name = name_entryspace.get().strip()
        age = age_entryspace.get().strip()
        id_number = id_entryspace.get().strip()

        # ValidatE NAME
        def validateName(name):
            if not name or len(name) < 5:
                name_error_text.config(text="Name must be at least 5 letters.", fg="red")
                return
            else:
                name_error_text.config(text=f"Welcome {name}", fg="green")
        validateName(name)

        # Validate Age
        def validate_age(age):
            if not age.isdigit() or int(age) <= 18:
                age_error_text.config(text="You must be older than 18.", fg="red")
                return
            else:
                age_error_text.config(text=f"Your age is {age}", fg="green")
        validate_age(age)


        # Validate ID Number
        def validate_id_number(id_number):
            if not id_number.isdigit() or len(id_number) != 8:
                id_error_text.config(text="Enter a valid 8-digit Kenyan ID number.", fg="red")
                return
            else:
                id_error_text.config(text="Click the Enter button below.", fg="green")
        validate_id_number(id_number)

    def submit():
        name = name_entryspace.get().strip()
        age = age_entryspace.get().strip()
        id_number = id_entryspace.get().strip()


        #messagebox.showinfo("added in the list", "User registered successfully!")

        # Clear entry fields for new input
        name_entryspace.delete(0, tk.END)
        age_entryspace.delete(0, tk.END)
        id_entryspace.delete(0, tk.END)

        # Reset error messages
        name_error_text.config(text="")
        age_error_text.config(text="")
        id_error_text.config(text="")




    # Labels and Input Fields
    name_display_text = tk.Label(root, text="Name:")
    name_display_text.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    name_entryspace = tk.Entry(root)
    name_entryspace.grid(row=0, column=1, padx=10, pady=5)
    name_error_text = tk.Label(root, text="", fg="red")
    name_error_text.grid(row=1, column=1)

    age_display_text = tk.Label(root, text="Age:")
    age_display_text.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    age_entryspace = tk.Entry(root)
    age_entryspace.grid(row=2, column=1, padx=10, pady=5)
    age_error_text = tk.Label(root, text="", fg="red")
    age_error_text.grid(row=3, column=1)

    id_display_text = tk.Label(root, text="ID Number:")
    id_display_text.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    id_entryspace = tk.Entry(root)
    id_entryspace.grid(row=4, column=1, padx=10, pady=5)
    id_error_text = tk.Label(root, text="", fg="red")
    id_error_text.grid(row=5, column=1)

    # Buttons
    validate_button = tk.Button(root, text="Validate", command=validate_inputs)
    validate_button.grid(row=6, column=0, columnspan=2, pady=10)

    submit_button = tk.Button(root, text="Enter", command=submit)
    submit_button.grid(row=7, column=0, columnspan=2, pady=5)



def clear_screen():

    for widget in root.winfo_children():
        widget.destroy()
    createMenu()


def createMenu():

    # creating the menu bar
    my_menu = tk.Menu(root)
    # setting the start
    file_menu=tk.Menu(my_menu, tearoff=0)

    # adding things , the files  to the menu
    file_menu.add_command(label="identity", command=main_function)
    file_menu.add_separator()

    file_menu.add_command(label="send messages", command=send_message)
    file_menu.add_separator()

    file_menu.add_command(label="news from kenya", command=getting_news)
    file_menu.add_separator()

    file_menu.add_command(label= "exit_app", command=root.quit)

    my_menu.add_cascade(label="DATA STORE AND NEWS", menu=file_menu)

    root.config(menu=my_menu)
createMenu()


root.mainloop()