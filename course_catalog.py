import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

course_index = {}

with open("INST-courses-all.txt", "r") as file: #Opens file in read mode)
    for line in file: #Goes through each line
        line = line.strip() #removes extra spaces + the invisible \n at the end
        
        # If line is blank, move to next line
        if line == "": 
            continue
        
        # If line is not blank, split it and save the course information
        if line != "":
            parts = line.split("||") #removes "||" so the parts are distinctly seperated
            #Assigning parts based on position and removing spaces and newlines bef and after
            course_code = parts[0].strip()
            title = parts[1].strip()
            description = parts[2].strip()
            prerequisites = parts[3].strip()
            credits = parts[4].strip()

            #Formatting dictionary
            course_index[course_code] = {
                "title": title,
                "description": description,
                "prerequisites": prerequisites,
                "credits": credits
            }
#-------------------------------------------------------
# This function looks up the title and prerequisites of a course
def lookup_course_info(course_code): 
    if course_code in course_index: # if course code is in the dictionary
        course = course_index[course_code] #Assign course to the course code
        return "Course title:", course["title"], "Course prerequisite:", course["prerequisites"] # return the course title and prerequisite
    else: # If the course code is not found, return this message
        return "Course not found."
    
#-------------------------------------------------------
# This function finds all courses with no prerequisites
def no_prerequisites(): 
    no_prereq_list = [] #starting with an empty list for courses with no prereq 
    for course_code in course_index: # Loop through each course in course code
        prereq = course_index[course_code]["prerequisites"] # get the course_code value from the course_index key and then grab the associated prerequisite value of the course.

        # If prerequisites are None or blank, add the course code to the list    
        if prereq == "None" or prereq == " ":   
            no_prereq_list.append(course_code)
    
    # Return the final list of courses with no prerequisites   
    return no_prereq_list  
#-----------

# This function finds all courses with no prerequisites
def no_prerequisites(): 
    no_prereq_list = [] #starting with an empty list for courses with no prereq 
    for course_code in course_index: # Loop through each course in course code
        prereq = course_index[course_code]["prerequisites"] # get the course_code value from the course_index key and then grab the associated prerequisite value of the course.

        # If prerequisites are None or blank, add the course code to the list    
        if prereq == "None" or prereq == "":   
            no_prereq_list.append(course_code)
    
    # Return the final list of courses with no prerequisites   
    return no_prereq_list  
 
#---------------------------
# Open/create a JSON file in write mode
with open("course_index.json", "w") as json_file:
    json.dump(course_index, json_file, indent=4)  # Save the course_index dictionary into the JSON file with indent of 4 for neatness
#-------------------------------------------------------

#Test to print out the whole dictionary
####print(course_index)
#Test to see if looking up "INST126" will give title and prerequisites
print(f"Information on course: {lookup_course_info('INST126')}")
#Test to get list of courses with no prerequisites
print(f"courses with no prerequisites: {no_prerequisites()}")
