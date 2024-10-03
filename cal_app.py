import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display frame
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        # Input field inside the frame
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Buttons frame
        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()

        # First row of buttons
        clear = tk.Button(btns_frame, text="C", width=32, height=3, bg="#eee", cursor="hand2", command=lambda: self.clear())
        clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        divide = tk.Button(btns_frame, text="/", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click("/"))
        divide.grid(row=0, column=3, padx=1, pady=1)

        # Second row
        seven = tk.Button(btns_frame, text="7", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(7))
        seven.grid(row=1, column=0, padx=1, pady=1)

        eight = tk.Button(btns_frame, text="8", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(8))
        eight.grid(row=1, column=1, padx=1, pady=1)

        nine = tk.Button(btns_frame, text="9", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(9))
        nine.grid(row=1, column=2, padx=1, pady=1)

        multiply = tk.Button(btns_frame, text="*", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click("*"))
        multiply.grid(row=1, column=3, padx=1, pady=1)

        # Third row
        four = tk.Button(btns_frame, text="4", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(4))
        four.grid(row=2, column=0, padx=1, pady=1)

        five = tk.Button(btns_frame, text="5", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(5))
        five.grid(row=2, column=1, padx=1, pady=1)

        six = tk.Button(btns_frame, text="6", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(6))
        six.grid(row=2, column=2, padx=1, pady=1)

        subtract = tk.Button(btns_frame, text="-", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click("-"))
        subtract.grid(row=2, column=3, padx=1, pady=1)

        # Fourth row
        one = tk.Button(btns_frame, text="1", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(1))
        one.grid(row=3, column=0, padx=1, pady=1)

        two = tk.Button(btns_frame, text="2", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(2))
        two.grid(row=3, column=1, padx=1, pady=1)

        three = tk.Button(btns_frame, text="3", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(3))
        three.grid(row=3, column=2, padx=1, pady=1)

        add = tk.Button(btns_frame, text="+", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click("+"))
        add.grid(row=3, column=3, padx=1, pady=1)

        # Fifth row
        zero = tk.Button(btns_frame, text="0", width=21, height=3, bg="#fff", cursor="hand2", command=lambda: self.click(0))
        zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        decimal = tk.Button(btns_frame, text=".", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: self.click("."))
        decimal.grid(row=4, column=2, padx=1, pady=1)

        equals = tk.Button(btns_frame, text="=", width=10, height=3, bg="#eee", cursor="hand2", command=lambda: self.evaluate())
        equals.grid(row=4, column=3, padx=1, pady=1)

    def click(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.clear()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
