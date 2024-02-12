#Different ways to make a list using another list


#1
def times_five(nums):
    result = []
    for i in nums:
        result.append(i*5)
    return result

fivey = times_five([1,2,3])
print(fivey)

#2
x_five = [1,2,3]
print(list(map(lambda x:x*5,x_five)))

#3
print([i*3 for i in [1,2,3,4,5]]) 


#yield = generator
#4
def times_four(nums):
    for i in nums:
        yield (i*4)

fourey = times_four([1,2,3,4])
print(next(fourey))

#The execption I get when the [] is finished is the StopUteration
print("for loop starts here")
for fro in fourey:
    print(fro)
#prints out everything in fourey

def logger(msg):
    def log_msg():
        print("log:",msg)
    print(log_msg)

logger("Hellloooo")
