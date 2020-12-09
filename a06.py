## IMPORTS GO HERE
import os
## END OF IMPORTS


#### YOUR CODE FOR text_count FUNCTION GOES HERE ####
def text_count(directory,file_name,lowercase = False,number_of_characters = False):
    counter = 0
    Names_File = os.path.join(directory,file_name)
    if lowercase == False and number_of_characters == False:
        with open(Names_File , "r") as f:
            for i in f:    
                i = i.strip().split(" ")
                for n in i:
                    if len(n) == 0:
                        continue
                    counter = counter + 1
            return ( counter)
    if lowercase == True and number_of_characters == False:
        with open(Names_File , "r") as f:
            for i in f:    
                i = i.strip().split(" ")    
                for n in i:
                    m = n.islower()
                    if m == True:
                        counter = counter + 1
            return (counter)           
    if lowercase == False and number_of_characters == True:
        with open(Names_File , "r") as f:
            for i in f:    
                for n in i:
                    for m in n:
                        counter = counter + 1
            return (counter)

#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####
def copy_lines(input_path,output_path,lines):  
    count = 0
    with open(output_path , "w") as s:
        with open(input_path , "r") as f:
            for i in f:
                i = i.strip()
                count = count + 1
                if count < lines:
                    s.write(i)
                    s.write("\n")
                elif count == lines:
                    s.write(i)
                if count == lines:
                    break

#### End OF MARKER



