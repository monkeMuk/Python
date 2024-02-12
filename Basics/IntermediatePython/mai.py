#first class functions = https://www.youtube.com/watch?v=kr0mpwqttM0
def logger(msg):
    def log_message():
        print("log: ",msg)
    return log_message 

log = logger("Hallo")
log()
#log() is essentially the same as log_message()


def enter_name(name):
    def insert_name():
        print("My name is ", name)
    return insert_name

ali = enter_name("Ali")
ali()


def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}<\{0}>".format(tag,msg))
    return wrap_text

print_h1 = html_tag("h1")
print_h1("Big asss headline!")
print_h1("Sub headline")

print_p = html_tag("p")
print_p("Dis the paragraph")



# starts with hi! and ends with <3

def func(intro):
    def wrapper(end):
        print("{0} {1} {0}".format(intro,end))
    return wrapper

love = func("<3")
love("You suck asf!")

#Closures

def OuterFunction():
    msg = 'ni de mama'

    def InnerFunction():
        print(msg)
    return InnerFunction()

OuterFunction()


def OuterFunction(message):
    msg = message

    def InnerFunction():
        print(msg)
    return InnerFunction

yo = OuterFunction("yo")
wo = OuterFunction("wo")

yo()
wo()

def a(func_b):
    def c():
        return func_b()
    return c

def Obama():
    print("Obama")

decorated_obama = a(Obama)
decorated_obama() 

@a
def show():
    print("Showing")
#same as show = a(Show)








