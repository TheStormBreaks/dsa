import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, page=None):
        self.page = page
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def append(self, page):
        new_node = Node(page)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_last(self):
        if not self.tail:
            return None
        page = self.tail.page
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return page

    def pop_first(self):
        if not self.head:
            return None
        page = self.head.page
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return page

    def is_empty(self):
        return self.head is None

class BrowserSimulator:
    def __init__(self, root):
        self.history = DoublyLinkedList()  # Doubly linked list for back navigation
        self.forward_stack = DoublyLinkedList()  # Doubly linked list for forward navigation
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
            self.history.pop_first()  # Limit the history to 10 entries

        self.current_page = page
        self.forward_stack = DoublyLinkedList()  # Clear forward history on new visit

        self.update_status()
        self.update_buttons()

    def go_back(self):
        if self.history.is_empty():
            return

        self.forward_stack.append(self.current_page)
        self.current_page = self.history.pop_last()

        if len(self.forward_stack) > 10:
            self.forward_stack.pop_first()  # Limit the forward stack to 10 entries

        self.update_status()
        self.update_buttons()

    def go_forward(self):
        if self.forward_stack.is_empty():
            return

        self.history.append(self.current_page)
        self.current_page = self.forward_stack.pop_last()

        if len(self.history) > 10:
            self.history.pop_first()  # Limit the history to 10 entries

        self.update_status()
        self.update_buttons()

    def update_status(self):
        if self.current_page:
            self.status_label.config(text=f"Current Page: {self.current_page}")
        else:
            self.status_label.config(text="No page loaded")

    def update_buttons(self):
        self.back_button.config(state=tk.NORMAL if not self.history.is_empty() else tk.DISABLED)
        self.forward_button.config(state=tk.NORMAL if not self.forward_stack.is_empty() else tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserSimulator(root)
    root.mainloop()
