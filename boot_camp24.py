#Accessing text files in python.
# w- write, a- append, r- read, x- create.
#with open("my_file.txt", mode= "a") as file:
#    file.write("\nThis is very effective.")


#with open("my_file.txt", mode= "r") as file:  
   # for text in file:
   #     print(text)


with open("invited_names.txt", mode= "r") as names_file:
    names = names_file.readlines()

with open("starting_letter.txt", mode= "r") as my_latter:
    content = my_latter.read()
    for name in names:
        striped_name = name.strip()
        finishhed_letter =  content.replace("[name]", striped_name)
        print(finishhed_letter)

    

