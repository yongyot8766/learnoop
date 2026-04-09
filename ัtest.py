'''class People:
      def __init__ (self,name,age):
            self.name=name
            self.age=age
      
      def introduce(self):
            print(f'My name is {people1.name}.I\'am {people1.age} years old')

people1=People('John',23)

people1.introduce()    '''              

'''class Human:
      def __init__(self,name,age):
          self.name=name
          self.age=age  
            
      def aging(self,years):
            print(f'Before {human1.age} years old')
            human1.age=human1.age+years      
            print(f'After {human1.age} years old')

human1=Human('John',22)            
human1.aging(3)'''

class Human:
      def __init__(self,name,age):
            self.name=name
            self.age=age
      def aging(self,years):
            print(f'Before {human1.age}years old')
            human1.age=human1.age+years
            print(f'After {human1.age}years old')

human1=Human('John',23)
human1.aging(3)            