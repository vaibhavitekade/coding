#first way
'''import module1
module1.welcome("vaibhavi","tekade")
module1.login("vaibhavi","vaibhavi")
module1.square(5)
print(module1.pi)
module1.addition(10)
module1.chk_even_odd(4)
module1.chk_even_odd(5)
module1.func(-3)
module1.msg(20)
module1.number(2,3)
module1.mark()
module1.large()
module1.func()
module1.func()
module1.chk_vowel()
module1.chk_equal()
module1.vote()'''
#==================================================================

#second way
'''import module1 as mod
mod.square(4)
mod.login("vaibhavi","vaibhavi")
mod.welcome("vaibhavi","tekade")
print(mod.pi)'''
#==================================================================

# third way
'''from module1 import pi,square,login,welcome
print(pi)
square(4)
login("vaibhavi","vaibhavi")
welcome("vaibhavi","tekade")'''
#==================================================================

# fourth way
'''from module1 import*
square(4)
login("vaibhavi","tekade")
print(pi)
welcome("vaibhavi","tekade")'''
#==================================================================

