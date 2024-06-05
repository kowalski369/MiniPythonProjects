# Filtering Strings: Create a function to filter strings based on length. 
# Use filter() to keep only strings longer than a specific character count.

# this program sorts the word of prompt which is greater then 5.

def filter_str(n):
        if len(n)>5:
            return True
        else:
            return False

def main():
    lst = []
    prompt = input("Enter the prompt: ").split()
    for i in prompt:
        lst.append(i)
    result = filter(filter_str,lst)
    print(list(result))
    
main()



    