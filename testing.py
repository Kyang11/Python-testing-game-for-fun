"""alien = {
    "color": "green",
    "point": 5
    }
new_point = alien["point"]
access = alien["color"]
print("User just earn " +str(new_point) +" point and the color is " + access)"""



"""alien = {
    "speed": "low",
    "x_position": 0,
    "y_position": 25
    }


print("The original x-position: "+str(alien["x_position"]))

if alien["speed"]=="low":
    x_increment =1
elif alien["speed"] == "medium":
    x_increment =2
else:
    x_increment = 3

alien["x_position"] =alien['x_position'] + x_increment
print("new x-position: "+ str(alien['x_position']))"""


"""favorite_languge = {
    "ku": 'python',
    'neng': "SQL",
    'lydia': "c",
    'nathen': 'python'
}
for name, language in favorite_languge.items():
    print(name.title() + "'s favorite language is " + language.title())"""
   # print("Ku favorite language is "+ favorite_languge['ku'].title()+ ".")""""

"""favorite_languge = {
    "ku": 'python',
    'neng': "SQL",
    'lydia': "c",
    'nathen': 'python'
}
for name, language in favorite_languge.items():
    print(name.title() + " 's favorite language is " + language.title())"""


"""user ={
    'username': 'Kyang',
    'first':'Ku',
    'last': 'Yang'
}
for key, value in user.items():
    print("\nKey: " +key)
    print("Value: " +value)
    """

"""favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in favorite_languages:
 print(name.title()) """


"""favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['sarah', 'phil', 'jen']
for name in favorite_languages.keys():
 print(name.title())
 if name in friends:
    print(" Hi " + name.title() +
 ", I see your favorite language is " +
 favorite_languages[name].title() + "!")"""
 
 
"""favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(name.title() + ", thank you for taking the poll.")"""
 

"""favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
  'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
 print(language.title())"""
 
"""allia= []
for alian_number in range(30):
    new_alian = {'color': 'green', 'points': 5, 'speed': 'slow'}
    allia.append(new_alian)
for alian in allia[:30]:
    print(alian)
    print("\n")
print("Total number of allia: " +str(len(allia)))"""

        
"""my_dict = {
    "name": "Tryi Aikham",
    "position": "QB",
    "team": "Dallas Cowboys",
    "age": 54,
    "weight": 220,
    "superbowls": ["XXVII", "XXVIII", "XXX"],
    "awards": {
        "super_bowls_mvp": "XXVII",
        "probowl": [1991,1992,1993,1994,1995,1996],
        "man_of_the_year"
: 1997    }
}


print(my_dict.get("awards", "age")["probowl"][len(my_dict["position"])])"""

"""number = input(" Enter a nuber and I will telll you itf it's enven or odd: ")
number = int(number)

if number %2 ==0:
    print("The number " +str(number)+ "is even")
else:
    print(" The number "+str(number)+ " is odd")"""
    
    
"""user = input(" Can you give me a nuber ? ")
user = int(user)
if user %10 ==0:
    print(f"{user } is multiple of 10")
else:
    print(f"{user}  is not mutiple of 10")"""

"""prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
 message = input(prompt)
 
 if message != 'quit':
    print(message)"""
    
"""prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input("Enter the text: ")
    if message == 'quit':
        break
    else:
        print(message)"""


"""current = 0
while current <10:
    current+=1
    if current %2 ==0:
        continue
    print(current)"""
    
"""pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)"""


"""responses={}
polling_active=True
while polling_active:
    name= input("\n What is your name? ")
    response = input("\nWhich moutain would you like to climb someday? ")
    
    responses[name] = response
    repeat = input("Would ypou like to let another person response? yes/no: ")
    if repeat =='no':
        polling_active = False
print("\n-- poll result--")
for name, response in responses.items():
    print(name+ " would like to clime " + response+ ". ")
    """

"""num = 1
new_num = 0
while num < 10:
    for i in range(3):
        new_num+=1
    num+=2
print(new_num)"""


"""def say_hello(name, age):
    print(f" hello {name} you are {age} year old")
    
def say_bye():
    print(" goodblye")
    
def greet_back(feeling):
    if feeling == "good":
        print(" I feel good too")
    elif feeling == "bad":
        print(" I am so sorry")
    elif feeling == 'streesed':
        print("coding is hard to learn")
    else:
        print("Well, have a good day")
    
#drive code 
while True:
    response = input("What do you want to do? Say hello[h] Say goodble [g] talk to me [t] quit [q]: ")
    if response.lower() == 'q':
        break
    elif response.lower()=='h':
        n = input("What is ypour name? ")
        a = input("What is ypour nage? ")
        say_hello(n, a)
    elif response.lower()=='g':
        say_bye()
    elif response.lower()=='t':
         f = input(" how are yout today? ")
         greet_back(f)
    else:
        print(" invallid input")"""
        
"""def myfunction(num):
    while num<10:
        print(num)
        if num==6:
            return
        num+=1
myfunction(1)"""


"""def dory(fish, nuber):
    if nuber >10:
        print("Who are you? ", end = " ")
    else:
        if fish=="Nemo":
            print("Just keep swimming", end = " ")
        else:
            print("I dont know you", end = " ")
print(dory("Nemo", 90))"""

"""x=5
def some_function(x):
    print(x, end = " ")
print(x, end = " ")
some_function(1)
x=x-1
print(x, end = " ")
some_function(1)"""


        