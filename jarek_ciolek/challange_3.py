# the key of the dictionary is the ID of the person
# inside the university
db_university = { "1AEF" : {
    "first_name": "Christian", 
    "last_name": "Barra", 
    "status" : "Active",
    "role": "Student"
    },
    "2BED" : {
    "first_name": "Jolanta", 
    "last_name": "Pizza", 
    "status" : "Inactive",
    "role": "Student"
    },
    "2BEC" : {
    "first_name": "Wioletta", 
    "last_name": "", 
    "status" : "Inactive",
    "role": "Student"
    },
    "4AEF" : {
    "first_name": "Michal", 
    "last_name": "Bojano", 
    "status" : "Active",
    "role": "Professor",
    "students": ["1AEF", "2BED"]
    },
    "8ACF" : {
    "first_name": "Salvatore", 
    "last_name": "Pedalino", 
    "status" : "Inactive",
    "role": "Professor",
    "students": []
    }}


def api_call(dict_object, id_inside_db):
    '''This function takes a dict object and a id (unique identifier)
    then the function should return:

    If the id is of a student a list with 3 elements ["first_name", "last_name", "status"]
    If it's a professor a list with 4 elements ["first_name", "last_name", "status", [d_list] ]

    the 4th element is a list of dictionaries where each dict contains {"name": name, "id" : id}
    :name is a string with the fist and last name "Chritian Barra"
    :id is the id of that person "1AEF" in my case
    the list must contain a dict for each student, and should be empty in case it has no students

    '''
    if dict_object[id_inside_db]['role'] == 'Student':
        first_name = dict_object[id_inside_db]['first_name']
        last_name = dict_object[id_inside_db]['last_name']
        status = dict_object[id_inside_db]['status']
        return [first_name, last_name, status]
    elif dict_object[id_inside_db]['role'] == 'Professor':
        first_name = dict_object[id_inside_db]['first_name']
        last_name = dict_object[id_inside_db]['last_name']
        status = dict_object[id_inside_db]['status']
        students = []
        for student_id in dict_object[id_inside_db]['students']:
            s_first_name = dict_object[student_id]['first_name']
            s_last_name = dict_object[student_id]['last_name']
            name = f"{s_first_name} {s_last_name}"
            students.append({"name" : name, "id" : student_id})
        return [first_name, last_name, status, students]

print(api_call(db_university, "2BEC"))
print(api_call(db_university, "8ACF"))
print(api_call(db_university, "4AEF"))