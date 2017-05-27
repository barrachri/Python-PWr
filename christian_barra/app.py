
from flask import Flask

app = Flask(__name__)

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


@app.route('/')
def index():
    return 'This view is not doing something special'

@app.route('/id/<person_id>')
def api_id(person_id):

    if person_id in db_university:
        if db_university[person_id]['role'] == 'Student':
            student = db_university[person_id]
            first_name = student['first_name']
            last_name = student['last_name']
            status = student['status']
            return "{},{},{}".format(first_name, last_name, status)

        if db_university[person_id]['role'] == 'Professor':
            professor = db_university[person_id]
            first_name = professor['first_name']
            last_name = professor['last_name']
            status = professor['status']

            students = []

            for student_id in db_university[person_id]['students']:
                student = db_university[student_id]
                s_first_name = student['first_name']
                s_last_name = student['last_name']
                name = "{} {}".format(s_first_name, s_last_name)
                students.append({"name": name, "id" : student_id})

            return "{}, {}, {}, {}".format(first_name, last_name, status, students)
    return "Your db sucks there's no id"

if __name__ == '__main__':
    app.run()