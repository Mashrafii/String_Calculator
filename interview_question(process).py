import re
class String_Calculator:

    def add_1(self,string):

        if(len(string)==0):
            return 0
        else:
            number_list=string.split(",")
            total=0
            for number in number_list:
                total+=int(number)
            return total
    def add_2(self,string):
        if (len(string) == 0):
            return 0
        else:
            number_list = string.replace('\n','').split(",")
            total = 0
            for number in number_list:
                total += int(number)
            return total

    def add_3(self,numberString):
        if (len(numberString) == 0):
            return 0
        else:
            delimiter=numberString[2]
            number_list = numberString[4:].split(delimiter)
            total = 0
            for number in number_list:
                total += int(number)
            return total

    def add_4(self,numberString):
        if (len(numberString) == 0):
            return 0
        else:
            delimiter=numberString[2]
            number_list = numberString[4:].split(delimiter)
            total = 0
            for number in number_list:
                if(int(number)<0):
                    raise ValueError("Negative Numbers are not allowed. Negative numbers are "+','.join([num for num in number_list if int(num)<0]))
                total += int(number)
            return total
    def bonus_add_1(self,numberString):
        if (len(numberString) == 0):
            return 0
        else:
            delimiter=numberString[2]
            number_list = numberString[4:].split(delimiter)
            total = 0
            for number in number_list:
                if(int(number)<0):
                    raise ValueError("Negative Numbers are not allowed. Negative numbers are "+','.join([num for num in number_list if int(num)<0]))
                if(int(number)>1000):
                    number=0
                total += int(number)
            return total

    def bonus_add_2(self,numberString):
        if (len(numberString) == 0):
            return 0
        else:
            delimiter=numberString[2]
            string1=numberString.replace("\n","")
            delim_exp= "\\"+delimiter+"+"
            number_list = re.split(delim_exp,string1[2:])
            number_list.pop(0)
            total = 0
            for number in number_list:
                if(int(number)<0):
                    raise ValueError("Negative Numbers are not allowed. Negative numbers are "+','.join([num for num in number_list if int(num)<0]))
                if(int(number)>1000):
                    number=0
                total += int(number)
            return total
    def bonus_add_3(self,numberString):
        if (len(numberString) == 0):
            return 0
        else:
            string1=numberString.replace("\n","")
            number_list = re.split("[^0-9a-zA-Z]",string1[2:])
            number_list=list(filter(None,number_list))
            total = 0
            for number in number_list:
                if(int(number)<0):
                    raise ValueError("Negative Numbers are not allowed. Negative numbers are "+','.join([num for num in number_list if int(num)<0]))
                if(int(number)>1000):
                    number=0
                total += int(number)
            return total

    def bonus_add_4(self,numberString):
        if (len(numberString) == 0):
            return 0
        else:
            string1=numberString.replace("\n","")
            number_list = re.split("[^0-9a-zA-Z]+",string1[2:])
            number_list=list(filter(None,number_list))
            total = 0
            for number in number_list:
                if(int(number)<0):
                    raise ValueError("Negative Numbers are not allowed. Negative numbers are "+','.join([num for num in number_list if int(num)<0]))
                if(int(number)>1000):
                    number=0
                total += int(number)
            return total



if __name__=='__main__':
    Calculator=String_Calculator()
    print(Calculator.add_2('1,2,3,5'))
    print(Calculator.add_2(''))
    print(Calculator.add_2('1\n,2,3'))
    print(Calculator.add_2('1\n\n\n,2,9'))
    print(Calculator.bonus_add_4('//@\n2@3@8'))
    print(Calculator.bonus_add_4('//*\n1*2*3'))
    #print(Calculator.add_4('//*\n1*-2*-3'))
    print(Calculator.bonus_add_4("//***\n1***2***3"))

    print(Calculator.bonus_add_4("//$,@\n1@$$***2@$@@@3||9"))

