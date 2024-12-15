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

    def remove_last(self):
        if self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

    def remove_first(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def is_empty(self):
        return self.head is None

class BrowserSimulator:
    def __init__(self):
        self.history = DoublyLinkedList()  # Doubly linked list for back navigation
        self.forward_stack = DoublyLinkedList()  # Doubly linked list for forward navigation
        self.current_page = None

    def visit_page(self, page):
        if not page:
            print("Invalid Input: Please enter a valid page URL.")
            return

        if self.current_page:
            self.history.append(self.current_page)

        if len(self.history) > 10:
            self.history.pop_first()  # Limit the history to 10 entries

        self.current_page = page
        self.forward_stack = DoublyLinkedList()  # Clear forward history on new visit

        self.update_status()

    def go_back(self):
        if self.history.is_empty():
            print("No pages in history to go back to.")
            return

        self.forward_stack.append(self.current_page)
        self.current_page = self.history.pop_last()

        if len(self.forward_stack) > 10:
            self.forward_stack.pop_first()  # Limit the forward stack to 10 entries

        self.update_status()

    def go_forward(self):
        if self.forward_stack.is_empty():
            print("No pages in forward history to go forward to.")
            return

        self.history.append(self.current_page)
        self.current_page = self.forward_stack.pop_last()

        if len(self.history) > 10:
            self.history.pop_first()  # Limit the history to 10 entries

        self.update_status()

    def update_status(self):
        if self.current_page:
            print(f"Current Page: {self.current_page}")
        else:
            print("No page loaded.")

if __name__ == "__main__":
    browser = BrowserSimulator()

    while True:
        print("\nOptions:")
        print("1. Visit a page")
        print("2. Go back")
        print("3. Go forward")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            page = input("Enter the URL of the page to visit: ")
            browser.visit_page(page)
        elif choice == "2":
            browser.go_back()
        elif choice == "3":
            browser.go_forward()
        elif choice == "4":
            print("Exiting browser simulator.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
