import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator")
        self.root.geometry("450x540")  # Adjusted height to ensure it fits perfectly
        self.root.configure(bg="#2C3E50")

        self.expression = ""
        self.history = []
        self.operator = ""  # To store the comparison operator
        self.first_number = None  # To store the first number before comparison

        self.display = tk.Entry(self.root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right', bg="black", fg="white")
        self.display.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=15, pady=20, padx=10, sticky='nsew')
        
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            ('ON/OFF', 1, 0), ('C', 1, 1), ('History', 1, 2), ('=', 1, 3),
            ('<', 1, 4), ('>', 2, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2),
            ('(', 5, 3), (')', 5, 4)  # Parentheses on the same row
        ]
        
        for btn_text, row, col in buttons:
            if btn_text in ('ON/OFF', 'C', 'History', '=', '/', '*', '-', '+', '(', ')', '<', '>'):
                font_size = 14  # Smaller font for blue buttons
                width = 5  # Narrow width for blue buttons
            else:
                font_size = 18  # Normal size for number buttons
                width = 6  # Standard width for number buttons

            # Set the color for arithmetic operators and parentheses to Royal Blue
            if btn_text in ('+', '-', '*', '/', '(', ')', '.', '<', '>'):
                color = "#4169E1"  # Royal Blue color
            else:
                color = "#E67E22" if btn_text in ('C', 'ON/OFF', 'History', '=') else ("gray" if btn_text.isdigit() else "#3498DB")
            
            btn = tk.Button(self.root, text=btn_text, font=("Arial", font_size, "bold"),
                            bg=color, fg="white", height=2, width=width,  
                            command=lambda txt=btn_text: self.on_button_click(txt))
            
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        for i in range(6):  # Ensure all rows resize properly
            self.root.grid_rowconfigure(i, weight=1)
        
        for j in range(5):  # Adjust column configuration to fit all buttons
            self.root.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.operator = ""
            self.first_number = None
        elif char == "ON/OFF":
            self.expression = ""
            self.display.delete(0, tk.END)
            return
        elif char == "=":
            try:
                if self.first_number is not None and self.operator:  # If comparison operator and first number exist
                    result = eval(self.expression)
                    if self.operator == "<":
                        self.expression = str(result < self.first_number)
                    elif self.operator == ">":
                        self.expression = str(result > self.first_number)
                else:
                    result = str(eval(self.expression))  # Normal evaluation
                    self.expression = result
                self.history.append(f"{self.expression} = {result}")
            except:
                self.expression = "Error"
        elif char == "History":
            self.expression = "\n".join(self.history[-5:])
        elif char == "<>":
            self.operator = "<>"  # Store the operator for comparison
            if self.expression:  # Save the first number if it's available
                self.first_number = eval(self.expression)
            self.expression += "<>"
        elif char == "<>":
            self.operator = "<>"  # Store the operator for comparison
            if self.expression:  # Save the first number if it's available
                self.first_number = eval(self.expression)
            self.expression += "<>"
        else:
            self.expression += char
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()