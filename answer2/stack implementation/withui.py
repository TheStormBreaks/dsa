import tkinter as tk
from tkinter import messagebox

class BrowserSimulator:
    def __init__(self, root):
        self.history = []  # Stack for back navigation
        self.forward_stack = []  # Stack for forward navigation
        self.current_page = None

        # UI Setup
        self.root = root
        self.root.title("Browser Simulator")

        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.visit_button = tk.Button(root, text="Visit", command=self.visit_page)
        self.visit_button.grid(row=0, column=2, padx=5)

        self.back_button = tk.Button(root, text="Back", command=self.go_back, state=tk.DISABLED)
        self.back_button.grid(row=1, column=0, padx=10, pady=10)

        self.forward_button = tk.Button(root, text="Forward", command=self.go_forward, state=tk.DISABLED)
        self.forward_button.grid(row=1, column=2, padx=10, pady=10)

        self.status_label = tk.Label(root, text="No page loaded", anchor="w")
        self.status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

    def visit_page(self):
        page = self.entry.get().strip()
        if not page:
            messagebox.showwarning("Invalid Input", "Please enter a valid page URL.")
            return

        if self.current_page:
            self.history.append(self.current_page)

        if len(self.history) > 10:
            self.history.pop(0)  # Limit the history to 10 entries

        self.current_page = page
        self.forward_stack.clear()  # Clear forward history on new visit

        self.update_status()
        self.update_buttons()

    def go_back(self):
        if not self.history:
            return

        self.forward_stack.append(self.current_page)
        self.current_page = self.history.pop()

        if len(self.forward_stack) > 10:
            self.forward_stack.pop(0)  # Limit the forward stack to 10 entries

        self.update_status()
        self.update_buttons()

    def go_forward(self):
        if not self.forward_stack:
            return

        self.history.append(self.current_page)
        self.current_page = self.forward_stack.pop()

        if len(self.history) > 10:
            self.history.pop(0)  # Limit the history to 10 entries

        self.update_status()
        self.update_buttons()

    def update_status(self):
        if self.current_page:
            self.status_label.config(text=f"Current Page: {self.current_page}")
        else:
            self.status_label.config(text="No page loaded")

    def update_buttons(self):
        self.back_button.config(state=tk.NORMAL if self.history else tk.DISABLED)
        self.forward_button.config(state=tk.NORMAL if self.forward_stack else tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserSimulator(root)
    root.mainloop()
