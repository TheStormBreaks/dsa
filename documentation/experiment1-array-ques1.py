class SportspersonArray:
    def __init__(self, initial_list):
        self.sportspersons = initial_list

    def get_length(self):
        return len(self.sportspersons)  # O(1)

    def add_at_end(self, sportsperson):
        self.sportspersons.append(sportsperson)  # O(1)

    def add_after_second(self, sportsperson):
        if len(self.sportspersons) < 2:
            print("Not enough elements to add after the second position.")
            return
        # Remove the sportsperson first
        self.sportspersons.remove(sportsperson)  # O(n)
        # Insert it after the second sportsperson
        self.sportspersons.insert(2, sportsperson)  # O(n)

    def replace_two_sportspersons(self, remove_list, new_list):
        for person in remove_list:
            if person in self.sportspersons:
                self.sportspersons.remove(person)  # O(n)
        self.sportspersons.extend(new_list)  # O(m), where m = len(new_list)

    def sort_sportspersons(self):
        self.sportspersons.sort()  # O(n log n)

    def print_sportspersons(self):
        print("Sportspersons:", self.sportspersons)

# Create the array with your favorite five sportspersons
favourite_sportspersons = SportspersonArray(["Hamilton", 
                        "Vettel", "Leclerc", "Sainz", "Ricciardo"])

# Task 1(a): Length of the list
print("Length of list:", favourite_sportspersons.get_length())

# Task 1(b): Add a sixth sportsperson at the end
favourite_sportspersons.add_at_end("Yuki")
favourite_sportspersons.print_sportspersons()

# Task 1(c): Add the sixth sportsperson after the second sportsperson
favourite_sportspersons.add_after_second("Yuki")
favourite_sportspersons.print_sportspersons()

# Task 1(d): Remove two sportspersons and replace them with two others
favourite_sportspersons.replace_two_sportspersons(["Ricciardo",
                             "Leclerc"], ["Schumacher", "Senna"])
favourite_sportspersons.print_sportspersons()

# Task 1(e): Sort the list alphabetically
favourite_sportspersons.sort_sportspersons()
favourite_sportspersons.print_sportspersons()
