class amor_dict ():
    def __init__(self,num_list):
        self.list = num_list
        rev_binary = bin(len(num_list)).split("b")[1][::-1]
        self.amort_dictionary = self.create_dictionary(self.list,rev_binary)
        
    def create_dictionary(self,temp,rev_binary):
            amort_dictionary = { }
            levels_hold = []
            k = 0
            if len(temp) == 0:
                amort_dictionary[0] = []
            else:    
                while k < len(temp):
                    for j in range(len(rev_binary)):

                        if rev_binary[j] == "1":
                            length_of_list = 2**j
                            for i in range(0,length_of_list):
                                levels_hold.append(temp[k])
                                k +=1
                            levels_hold.sort()
                            amort_dictionary[j] = levels_hold
                            levels_hold = []
                        elif rev_binary[j] == "0":
                            amort_dictionary[j] = []
            return amort_dictionary
        
    def insert(self,num):
        initial_list = [num]
        bcd = []
        mergelist=[]
        i = 0
        for i in range(0,len(self.amort_dictionary)):
            w = 0
            j = 0
            if self.amort_dictionary[i] != []:
                    bcd = self.amort_dictionary[i]
                    self.amort_dictionary[i] = []
                    while w < len(initial_list) and j < len(bcd):
                        if initial_list[w] < bcd [j]:
                            mergelist.append(initial_list[w])
                            w += 1
                        else:
                            mergelist.append(bcd[j])
                            j += 1
                    while w < len(initial_list):
                        mergelist.append(initial_list[w])
                        w += 1
                    while j < len(bcd):
                        mergelist.append(bcd[j])
                        j += 1
                    initial_list= []
                    initial_list = mergelist
                    mergelist = []
            elif self.amort_dictionary[i] == []:
                if i == 0:
                    self.amort_dictionary[i] = [num]
                    initial_list = []
                    break;
                self.amort_dictionary[i] = initial_list
                initial_list=[]
                break;  
        if initial_list != [] and self.amort_dictionary:
             self.amort_dictionary[i+1] = initial_list
        elif not self.amort_dictionary:
            self.amort_dictionary[i] = initial_list
            
    def search(self , num):
        for i in range(0,len(self.amort_dictionary)):
            if self.amort_dictionary[i]:
                abc =[]
                abc =self.amort_dictionary[i]
                first = 0
                last = len(abc)-1
                while last - first > 1:
                    middle = (last + first)//2
                    if abc[middle] < num:
                        first = middle + 1
                    else:
                        last = middle      
                if abc[first] == num:
                    return "level "+ str(i)
                elif abc[last] == num:
                    return "level " + str(i)
        return "level "+ str(-1)
            
    def print(self):
        for i in self.amort_dictionary:
            print("Level",i,":",self.amort_dictionary[i])
        
        
if __name__ == '__main__':
    
    print("---Output Begins ---")
    amor =amor_dict([23, 12 ,24, 42])
    print("--Created Dictionary --")
    amor.print()
    print()
    print("--Insert Operation --")
    amor.insert(11)
    amor.print()
    print()
    print("-- Insert Operation 2 --")
    amor.insert(74)
    amor.print()
    print()
    print("--Search operation--")
    ans = amor.search(74)
    print(ans)
    print()
    print("--Search Operation 2--")
    ans =amor.search(77)
    print(ans)
    print()
    print("-- Insert operation 3 --")
    amor.insert(78)
    amor.print()
    print()
    print("--Insert operation 4--")
    amor.insert(15)
    amor.print()
    print()
    print("Passing empty list")
    amor1 =amor_dict([])
    amor1.print()