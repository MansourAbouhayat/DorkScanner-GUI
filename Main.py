import tkinter as tk
from tkinter import ttk
import datetime
import ScrapeDork
from tkinter import messagebox

DATA=[]
def scrape_dorks():
    query = query_entry.get()
    data=ScrapeDork.ScrapeDork().DuckDuckGO(query)
    
    
    # Clear previous data in the table
    clear_table()

    
    # Display the scraped results in the table
    for i, result in enumerate(data):
        table.insert('', 'end', values=(i+1, result))
    export_data(data)

def clear_table():
    for row in table.get_children():
        table.delete(row)

def export_data(data):
    filename='Results'+str(datetime.date.today())+str(datetime.datetime.now().time())+'.txt'

    with open(filename, 'w') as file:
        for url in data:
            file.write(url+'\n')
    messagebox.showinfo('DATA','SAVED')

# Create the Tkinter window
window = tk.Tk()
window.geometry("500x360")
window.title("Dork Scraper")

# Create a label and entry for the query
query_label = ttk.Label(window, text="Query:")
query_label.pack()
query_entry = ttk.Entry(window)
query_entry.pack(pady=10)

# Create a button to scrape the dorks
scrape_button = ttk.Button(window, text="Scrape Dorks", command=scrape_dorks)
scrape_button.pack()

# Create the table to display the results
table_columns = ("#","Result")
table = ttk.Treeview(window, columns=table_columns, show="headings")

table.pack(pady=10)

# Set the column headings
for column in table_columns:
    table.heading(column, text=column)

# Create a button to export the data


# Start the Tkinter event loop
window.mainloop()
