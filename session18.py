class Silly:
   """This class does nothing, but we use it to
 illustrate instances and members"""

print "Silly has type ", type(Silly) #prints type class obj
x1 = Silly()
print "x1 has type ", type(x1) #prints type instanceobj
x1.foo = 3
print type(x1.foo) #3
print x1.__class__.__name__ #print Silly
print x1.__class__ == Silly #prints True
x2 = Silly() #creates another instance of the class Silly
x2.foo = 4 
print x2.foo #4
print x1.foo #3
print Silly.__name__ #prints Silly
# What will happen if you uncomment the following?
# print Silly.foo #Error occurs

class Dog:
    """A slobbering friend"""

    def __init__ (self, n, sound = "Woof"):
        """Initialize with number of woofs"""
        self.woofcount = n
        self.noise = sound  
    def bark (self):
        """Bark out loud"""
        for i in range(self.woofcount):
            print self.noise
    def __str__(self):
        """Called whenever a printed representation of self is needed"""
        return "Barks %d times say %s" % (self.woofcount, self.noise)
print '-------------------'
print "Dog has type", type(Dog) #classobj
print "Dog.bark has type", type(Dog.bark) #instance method

Iorek = Dog(23)

print type(Iorek) #instance 
print Iorek.__class__.__name__ #prints Dog
print Iorek.__class__ == Dog #prints True
print Iorek.woofcount #prints 23
print '________________________ Woofus'
Woofus = Dog(1)
print Woofus.woofcount #prints 1
Woofus.bark() #prints Woof once
print "-----"
Woofus.woofcount = 2
print Woofus.woofcount #prints 2
Woofus.bark() #prints woof twice

Iorek.bark() #prints 23 woofs

Fluffy = Dog(1, "Ruff")
Woofus = Dog(3, "Woof")
Rover = Dog(4, "Arf")

for d in [Fluffy, Woofus, Rover]:
    d.bark()
    print "---"
#prints Ruff, Woof*3, Arf*4

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __str__(self):
        return str(self.x)+","+str(self.y)


p = Point(7,6)
print(p) #7, 6
p.move(5,10)
print(p) #12, 16
    

