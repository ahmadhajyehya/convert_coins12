from coins import *

print("welcome to currency converter")
print ("1.dollars to shekel")
print ("2.shekel to dollars")

class USD:
    def get_value(self):
        return 3.52
    def calculate(self, amount):
        return amount * self.get_value()
class ILS:
    def get_value(self):
        return 0.28
    def calculate(self, amount):
        return amount * self.get_value()

def get_value():
      choice = input('please choose an option 1/2')
      f = open('result.txt','a')
      try:
         if choice == '1':
            value1 = float(input("please enter amount to convert"))
            result = value1 / 3.52
            print(" the result is :", result)
            listA.append(result)



         if choice == '2':
            value2 = float(input("please enter amount to convert"))
            result = value2 * 0.28
            print(" the result is :", result)
            listA.append(result)



         restart = input("To Continue\n Type in: \n Y for Yes \n N for No\n")
         if restart == "N" or restart == "n":
            print(listA)
            print("Elements of the List:\n")
            for x in listA:
               print(x)


            print("thanks for using our currincy converter")

      except:
         ('error...')
      f.write('\nAddition ='+str(listA))
      f.close()

listA = []
while True:
   get_value()
def main():
   get_value()
main()

