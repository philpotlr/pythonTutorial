#import entire module
import greet

greet.sayHello('Tim')


#import specific module
from greet import sayGoodbye

sayGoodbye('Tom')