
class LinkedList:
    data = "test"
    next_node = None
    def __init__(self, data):
        self.data = data

    def addNode(self, data):
        self.next_node = LinkedList(data)

    def push(self, data):
        if self.next_node != None:
            return self.next_node.push(data)
        else:
            self.addNode(data) 

    def insert(self, i, data):
        i -= 1
        if i == -1:
            node_temp = self.next_node
            self.next_node = LinkedList(self.data)
            self.data = data
            self.next_node.next_node = node_temp
            return True
        else:
            return self.next_node.insert(i, data) 
        
    def removeNode(self, i):
        i -= 1
        if i == -1:
            self.data = self.next_node.data
            self.next_node = self.next_node.next_node
            return True
        else:
            return self.next_node.removeNode(i)
    
    def getLength(self, i = 0):
        i += 1
        if self.next_node == None:
            return i
        else:
            return self.next_node.getLength(i)

    def convertToPythonList(self, list = [-1]):
        if list == [-1]:
            list = [self.data]
        if self.next_node == None:
            return list
        else:
            list.append(self.next_node.data)
            return self.next_node.convertToPythonList(list)
    
    def linkNode(self, node):
        self.next_node = node

    def getNode(self, i):
        i -= 1
        if i == -1:
            return self
        elif i < -1:
            return LinkedList(None)
        else:
            if self.next_node:
                return self.next_node.getNode(i)
            else:
                return -1

    def findData(self, data, i = -1):
        i += 1
        if self.data == data:
            return i
        elif self.next_node == None:
            return -1
        else:
            return self.next_node.findData(data, i)

        


# Main function

# Declare the linked list
linked_list = LinkedList("1")
linked_list.push("2")
linked_list.push("3")
linked_list.push("4")
linked_list.push("5")
linked_list.push("6")
linked_list.push("7")


# Show the original linked list
print("Original Linked List:")
print(linked_list.convertToPythonList())
print("Length of Linked List: " + str(linked_list.getLength()))

print("\n\n")

# Remove the linked_list[4] element from the list
print("Removed linked_list[4] from the linked list!")
linked_list.removeNode(4)

# Show new linked list
print("\n")
print("New Linked List:")
print(linked_list.convertToPythonList())
print("Length of Linked List: " + str(linked_list.getLength()))


# Remove the linked_list[4] element from the list
print("Inserted \"test\" to linked_list[3] from the linked list!")
linked_list.insert(3, "test")

# Show new linked list
print("\n")
print("New Linked List:")
print(linked_list.convertToPythonList())
print("Length of Linked List: " + str(linked_list.getLength()))


# Find data
in_finddata = input("\n\nInput a string and see if it is in the linked list:\n")

item_location = linked_list.findData(in_finddata)

if item_location == -1:
    print("Item is not found!")
else:
    print("Item is found at location " + str(item_location))



