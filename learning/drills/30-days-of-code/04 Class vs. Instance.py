# define person class



class Person:
    def __init__(self, initialAge):
        # add check for initialAge
        # if initial age < 0, set self.age to 0 and print error

        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0

        else:
            self.age = initialAge

    def yearPasses(self):
        self.age += 1
        return self.age

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')



# test

user_age = int(input())
t = Person(user_age)
t.amIOld()
t.yearPasses()
t.yearPasses()
t.yearPasses()

t.amIOld()
