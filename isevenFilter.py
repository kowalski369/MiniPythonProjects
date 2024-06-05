# This program is related to filter function()
# Finding Even Numbers: Write a program that uses filter() to extract even numbers from a list.
#  How can you define a lambda function to check for evenness?

def filter_evenlist():
    prompt = input("Enter the number seperated by spaces: ").split()
    promptlist = []
    for i in prompt:
        promptlist.append(int(i))
    result = filter(lambda x: x%2==0,promptlist)
    return list(result)

print(filter_evenlist())