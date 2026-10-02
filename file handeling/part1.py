#file = open("demo.txt", "r")

#print(file.read())



#file = open("demo.txt", "a") # Opening the file in append mode to add new content without overwriting existing data

#file.write("Automation ka main kaam kya hota hai? Data ko ek jagah se uthana, process karna, aur dusri jagah save karna. (Jaise hazaro emails nikalna, ya excel sheets ko automatically update karna)..\n") # Writing a new line to the file

#file.close() # Closing the file after writing to it is important to ensure that all data is properly saved and resources are released.




import os

# Ye line tumhari .py file ka exact folder dhundhegi
script_dir = os.path.dirname(__file__) 

# Ye line us folder ke raste mein 'demo.txt' ka naam jod degi
file_path = os.path.join(script_dir, "demo.txt")

# 1. Pehle usi address (file_path) par kuch likhte hain
with open(file_path, "a") as file:
    file.write("Hello JARVIS, I am learning Automation!\n")

# 2. Ab usi address (file_path) se data padhte hain
with open(file_path, "r") as file_read:
    data = file_read.read()  # Saara text read karke 'data' variable mein daal diya
    print("Meri File ka Data:")
    print(data)             # Ab usko terminal par print kar diya