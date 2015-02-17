## Animal is-a object (yes, sort of confusing look at extra credit)
class Animal(object):
    def __init__(self, motile):
      ## has-a motile
      self.motile = []

## Dog is-a Animal 
class Dog(Animal):

  def __init__(self, name):
    ## has-a name
    self.name = name

    ## has-a bark
    self.bark = None 

## Cat is-a Animal
class Cat(Animal):
  def __init__(self, name):
    ## has-a name
    self.name = name
    ## has-a meow
    self.meow = None

## Person is-a object
class Person(object):
  def __init__(self, name):
    ## has-a name
    self.name = name

    ## has-a pet
    self.pet = None

    ## has-a greeting
    self.greeting = "Hi there!"

## Employee is-a Person

class Employee(Person):
  def __init__(self, name, salary):
    ## has-a name, salary. Huh? What is super??
    super(Employee, self).__init__(name)
    self.salary = salary
    
## Fish is-a object

class Fish(object):
  def __init__(self):
    ## has-a gills
    self.gills = None

## Salmon is-a Fish

class Salmon(Fish):
  def __init__(self):
    ## has-a spawns 
    self.spawns = None

## Halibut is-a Fish

class Halibut(Fish):
  def __init__(self):
    ## has-a flat body
    self.flat = None

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a satan
mary.pet = satan

## Frank is-a Employee with attributes set to self and 120000

frank = Employee("Frank", 120000)

## Frank has-a rover

frank.pet = rover

## Flipper is-a Fish

flipper = Fish()

## Crouse is-a Salmon

crouse = Salmon()

## harry is-a Halibut

harry = Halibut()

## harry has-a gills
harry.gills = True

## rover is motile
rover.motile = ['walks', 'runs']

## mary greeting
print mary.greeting

print harry.gills

rover.bark = "bark!"

print rover.bark

print rover.motile