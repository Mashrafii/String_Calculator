import re
class Calculator:

    def add(self,numberString):
        '''
        The method takes in a numberString of different format and add those number
        :param numberString: A String of Numbers
        :return: The sum of the numbers in the numberString
        '''
        if(len(numberString)==0): #Check if the string is empty.
            return 0
        string1=numberString.replace('\n',"") #remove the \n that appears in the string

        if(re.match("[0-9]+",string1)): #Check if the String is in usual format of comma separated number
                                        #It solves the coding challenge related to Question 1 and 2
            number_list=string1.split(",")
        else:                           # this else condition works to manage string in the format //[delimiter]\n delimter seperated numbers

            number_list = re.split("[^0-9a-zA-Z-]+", string1[2:]) #Split the string at any delimiter of any size
            number_list = list(filter(None, number_list))         #remove the empty strings from the list
        total = 0

        for number in number_list:                             #add all the numbers in the list number_list
            if (int(number) < 0):                              #Check if it's a negative number and raise ValueError
                raise ValueError("Negative Numbers are not allowed. Negative numbers are " + ','.join(
                    [num for num in number_list if int(num) < 0]))
            if (int(number) > 1000):                           #Check if the number exceed 1000
                number = 0
            total += int(number)
        return total                                    #return the total number

if __name__=='__main__':
    Calculator=Calculator()
    if(Calculator.add('')!=0):
        print("Error! Expected the result as 0 for the empty string but got "+ Calculator.add(''))
    if(Calculator.add('1,2,3,5')!=11):
        print("Error! Expected the result as 11 for the empty string but got " + Calculator.add('1,2,3,5'))
    if (Calculator.add('1\n\n\n,2,9') != 12):
        print("Error! Expected the result as 12 for the empty string but got " + Calculator.add('1\n\n\n,2,9'))
    if (Calculator.add('//@\n2@3@8') != 13):
        print("Error! Expected the result as 13 for the empty string but got " + Calculator.add('//@\n2@3@8'))
    if (Calculator.add('//*\n2*3*8') != 13):
        print("Error! Expected the result as 13 for the empty string but got " + Calculator.add('//*\n2*3*8'))
    if (Calculator.add('//*@\n2*3@8') != 13):
        print("Error! Expected the result as 13 for the empty string but got " + Calculator.add('//@\n2@3@8'))

    try:
        if (Calculator.add('//@\n-2@-3@8') != 13):
            print("Error! Expected the result as 13 for the empty string but got " + Calculator.add(''))
        print("Error! Expected Value Error")

    except ValueError:
        pass

    if (Calculator.add("//***\n1***2***3") != 6):
        print("Error! Expected the result as 6 for the empty string but got " + Calculator.add("//***\n1***2***-3"))
    if (Calculator.add("//$,@\n1@$$***2@$@@@3||9") != 15):
        print("Error! Expected the result as 15 for the empty string but got " + Calculator.add("//$,@\n1@$$***2@$@@@3||9"))

    print("Test Succesful")

    numberStrings=input("Please enter the number string along with quotation:")
    print("Result from the add method: "+ str(Calculator.add(eval(numberStrings))))


