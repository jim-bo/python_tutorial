# imports
from time import sleep

# errant function
print("0: Hello, I am here!")

# function
def load_data():

    # this is a block comment
    print("2: ... now I am here, going to sleep")
    data = "Data loading"
    
    sleep(3)        # this is an inline comment
    
    # another block comment
    print("3: ..waking up, loaded the data")
    return data

# entrypoint
if __name__ == "__main__":

    print("1: This is the second print statement")

    # load the data
    d = load_data()

    # print the results
    print("4: here is your data: ", d)