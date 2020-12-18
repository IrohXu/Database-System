import re

class node(object):
    def __init__(self, key, index):
        """
        Node in the hashing
        """
        self.key = key
        self.pointer_index = index     #  The index will localize to the array(can be consider as a pointer)
        self.next = None

class hashing(object):
    def __init__(self, B):
        self.size = B
        self.array = []
        self.dict = {}
        for i in range(0, self.size): self.dict[i] = None
    
    def length(self):
        return len(self.array)

    def _insert(self, key, value):
        dict_key = key%self.size
        if(self.dict[dict_key] is None):
            index = self.length()
            self.array.append((key,value))
            self.dict[dict_key] = node(key, index)
            tag = 1
        else:
            head = self.dict[dict_key]
            while(head.next != None):
                if(head.key == key):
                    self.array[head.pointer_index] = (key,value)    # Update the value
                    break
                else:
                    head = head.next
            if(head.key != key):
                index = self.length()
                self.array.append((key,value))
                new_node = node(key, index)
                head.next = new_node
                tag = 1
            else:
                self.array[head.pointer_index] = (key,value)    # Update the value
                tag = 0
        return tag
    
    def insert(self, key, value):
        tag = self._insert(key, value)
        if(tag == 1):
            print("key: "+ str(key)+", value: "+str(value)+" is inserted successfully.")
        else:
            print("Duplicated key, key: "+ str(key)+", value: "+str(value)+" is updated successfully.")

    def _search(self, key):
        dict_key = key%self.size
        head = self.dict[dict_key]
        while(head != None):
            if(head.key == key):
                return head.pointer_index
            else:
                head = head.next
        return None
    
    def search(self, key):
        tag = self._search(key)
        if(tag == None):
            print("The key is not existed.")
        else:
            key = self.array[tag][0]
            value = self.array[tag][1]
            print("key|value")
            print(str(key)+"|"+str(value))

    def _delete(self, key):
        dict_key = key%self.size
        head = self.dict[dict_key]
        if(head == None):
            return None
        if(head.key == key):
            output = head.pointer_index
            self.dict[dict_key] = head.next
            return output
        while(head.next != None):
            if(head.next.key == key):
                output = head.next.pointer_index
                head.next = head.next.next
                return output
            else:
                head = head.next
        return None
    
    def delete(self, key):
        tag = self._delete(key)
        if(tag == None):
            # print("The delete operation failed.")
            print("The key is not existed.")
        else:
            k_v = self.array[tag]
            self.array[tag] = None
            print("key: "+str(k_v[0])+", and value: "+str(k_v[1])+" is removed.")
    
    def visualization(self):
        for dict_key in self.dict:
            temp_key_value = []
            head = self.dict[dict_key]
            while(head != None):
                temp_key_value.append((head.key, head.pointer_index))
                head = head.next
            print(str(dict_key)+':'+str(temp_key_value))
    
    def search_all(self):
        print("key|value")
        for dict_key in self.dict:
            head = self.dict[dict_key]
            while(head != None):
                print(str(self.array[head.pointer_index][0]) + "|" + str(self.array[head.pointer_index][1]))
                head = head.next

    def load_table(self, table_path):
        fd = open(table_path)
        first_line = fd.readline()
        while(True):
            line = fd.readline()
            if(line == ""):
                break
            info = line.split('|')
            self._insert(int(info[0]), int(info[1]))
    
    def load_command(self, command_path):
        fd = open(command_path)
        while(True):
            line = fd.readline()
            if(line == ""):
                break
            matchObj = re.match( r'[a-z]*', line)
            if(matchObj):
                command = matchObj.group()
            if(command == 'insert'):
                numberObj = re.match( r'\d*', line)
            elif(command == 'delete'):
                numberObj = re.search( r'\d*', line)
            elif(command == 'search'):
                numberObj = re.search( r'\d*', line)
            else:
                print("Wrong command, command should be insert, delete or search")
            print(numberObj.group())


if __name__ == '__main__':
    h = hashing(5000)
    input_table = './myIndex.txt'
    input_command = './myCommand.txt'
    h.load_table(input_table)
    h.load_command(input_command)
    # for i in range(0, 100000):
    #     h._insert(i, i*2)
    h.search(15)
    h.insert(15, 140)
    h.delete(15)
    h.insert(15, 140)
    h.delete(15)

    h.search(15)
