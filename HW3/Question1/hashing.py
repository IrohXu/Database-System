class node(object):
    def __init__(self, key, value):
        """
        Node in the hashing
        """
        self.key = key
        self.value = value
        self.next = None

class hashing(object):
    def __init__(self, B):
        self.size = B
        self.dict = {}
        for i in range(0, self.size):   self.dict[i] = None
    
    def insert(self, key, value):
        dict_key = key%self.size
        if(self.dict[dict_key] is None):
            self.dict[dict_key] = node(key, value)
        else:
            head = self.dict[dict_key]
            while(head.next != None):
                if(head.key == key):
                    head.value = value    # Update the value
                    break
                else:
                    head = head.next
            if(head.key != key):
                new_node = node(key, value)
                head.next = new_node

    def search(self, key):
        dict_key = key%self.size
        head = self.dict[dict_key]
        while(head != None):
            if(head.key == key):
                return head.value
            else:
                head = head.next
        print("The key is not exist.")
        return None

    def delete(self, key):
        dict_key = key%self.size
        head = self.dict[dict_key]
        if(head == None):
            return None
        if(head.key == key):
            output = (head.key, head.value)
            self.dict[dict_key] = head.next
            return output
        while(head.next != None):
            if(head.next.key == key):
                output = (head.next.key, head.next.value)
                head.next = head.next.next
                return output
            else:
                head = head.next
        print("The key is not exist.")
        return None
    
    def visualization(self):
        for dict_key in self.dict:
            temp_key_value = []
            head = self.dict[dict_key]
            while(head != None):
                temp_key_value.append((head.key, head.value))
                head = head.next
            print(str(dict_key)+':'+str(temp_key_value))
    
    def search_all(self):
        print("key | value")
        for dict_key in self.dict:
            head = self.dict[dict_key]
            while(head != None):
                print(str(head.key) + " | " + str(head.value))
                head = head.next
