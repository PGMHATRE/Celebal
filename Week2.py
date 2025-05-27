
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None     



class LinkedList:
    def __init__(self):
        self.head = None      

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node   # First node becomes the head
        else:
            current = self.head
            while current.next:   
                current = current.next
            current.next = new_node   # Link the new node at the end

    def print_list(self):
        if not self.head:
            print("The list is empty.")
        else:
            current = self.head
            print("Linked List:")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise IndexError("List is empty. Cannot delete any node.")

            if n <= 0:
                raise IndexError("Index must be a positive integer.")

            # If the user wants to delete the first node
            if n == 1:
                print(f"Deleting node with value: {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            # If the next node is None, index is out of range
            if not current or not current.next:
                raise IndexError("Index out of range. Cannot delete node.")

            print(f"Deleting node with value: {current.next.data}")
            current.next = current.next.next

        except IndexError as e:
            print(f"Error: {e}")


# Function to display the menu
def display_menu():
    print("\nSelect From Below Options")
    print("1. Add node")
    print("2. Print list")
    print("3. Delete nth node")
    print("4. Exit")


# Main program starts here
if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                value = int(input("Enter value to add: "))
                linked_list.add_node(value)
                print("Node added successfully.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == '2':
            linked_list.print_list()

        elif choice == '3':
            try:
                position = int(input("Enter node position to delete (1-based index): "))
                linked_list.delete_nth_node(position)
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == '4':
            print("Exiting program....")
            break

        else:
            print("Please select a valid option (1-4).")
