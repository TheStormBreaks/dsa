class BrowserSimulator:
    def __init__(self):
        self.history = []  # Stack for back navigation
        self.forward_stack = []  # Stack for forward navigation
        self.current_page = None

    def visit_page(self, page):
        if not page:
            print("Invalid Input: Please enter a valid page URL.")
            return

        if self.current_page:
            self.history.append(self.current_page)

        if len(self.history) > 10:
            self.history.pop(0)  # Limit the history to 10 entries

        self.current_page = page
        self.forward_stack.clear()  # Clear forward history on new visit

        self.update_status()

    def go_back(self):
        if not self.history:
            print("No pages in history to go back to.")
            return

        self.forward_stack.append(self.current_page)
        self.current_page = self.history.pop()

        if len(self.forward_stack) > 10:
            self.forward_stack.pop(0)  # Limit the forward stack to 10 entries

        self.update_status()

    def go_forward(self):
        if not self.forward_stack:
            print("No pages in forward history to go forward to.")
            return

        self.history.append(self.current_page)
        self.current_page = self.forward_stack.pop()

        if len(self.history) > 10:
            self.history.pop(0)  # Limit the history to 10 entries

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
