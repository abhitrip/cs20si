import time

def timetest(input_func):

    def timed(*args,**kwargs):
        start_time = time.time()
        result = input_func(*args,**kwargs)
        end_time = time.time()
        print "Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
        input_func.__name__,
        args,
        kwargs,
        end_time - start_time
        )
        return result
    return timed

@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print "inside foobar"

    print args, kwargs

foobar(["hello, world"], foo=2, bar=5)

"""
inside foobar
(['hello, world'],) {'foo': 2, 'bar': 5}
Method Name - foobar, Args - (['hello, world'],), Kwargs - {'foo': 2, 'bar': 5}, Execution Time - 0.30296087265

Inside decorator, function foobar is referenced as variable input_func. The result, post execution of input_func is referred as result.
"""

# Method Decorator
def method_decorator(method):

    def inner(city_instance):
        if city_instance.name=='SFO':
            print "It's a cool place to live in"
        else:
            method(city_instance)
    return inner

class City(object):
    """docstring for City"""
    def __init__(self, name):
        self.name = name

    @method_decorator
    def print_test(self):
        print self.name

p1 = City("LAX")
p1.print_test()
"""
Method decorators allow overriding class properties by decorating, without having to find the calling function.
In the snippet shown above, we decorate the class method print_test. The method_decorator prints the name of the city, if the name of city instance is not SFO.
"""

# Class Decorators
class decoclass(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        # before f actions
        print 'decorator initialised'
        self.f(*args, **kwargs)
        print 'decorator terminated'
        # after f actions

@decoclass
def klass():
    print 'class'

klass()
"""
If you want to create a callable returning another callable, the function decorator approach is easier. If you want the return to be a function, function decorators should be preferred, however if you want the decorator to return a custom object that does something different to what a function does, in that case a class decorator should be used.

With a class, you can add methods and properties to the decorated callable object, or implement operations on them. You can create descriptors that act in a special way when placed in classes (e.g. classmethod, property)
"""

# Chaining Decorator
def makebold(f):
    return lambda: "<b>" + f() + "</b>"
def makeitalic(f):
    return lambda: "<i>" + f() + "</i>"

@makebold
@makeitalic
def say():
    return "Hello"

print say()
