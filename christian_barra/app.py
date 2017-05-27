###############################################################
# STEP #1
###############################################################
# I've take this code from here: http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
###############################################################
# app.py #
###############################################################

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
    
###############################################################

###############################################################
# STEP #2
###############################################################
# app.py #
###############################################################

from flask import Flask
app = Flask(__name__)

@app.route('/id/<person_id>')
def hello_world(person_id):
    return 'Hello, World {person_id}!'.format(person_id)

if __name__ == '__main__':
    app.run()
    
###############################################################
# STEP #3
###############################################################
# app.py #
###############################################################

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This view is not doing something special'

@app.route('/id/<person_id>')
def api_id(person_id):
    return 'Hello, World {}!'.format(person_id)

if __name__ == '__main__':
    app.run()

###############################################################
# STEP #4
###############################################################
# I took this code from here: https://github.com/barrachri/Python-PWr/blob/master/christian_barra/Day3.ipynb
###############################################################
# Day3.ipynb #
###############################################################

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

def api_call(db, person_id):
    '''
    Returns a list of [first_name, last_name, status] in case person_id is a "Student"
    Returns a list of [first_name, last_name, status, [{"name": name, "id" : student_id}]] 
    in case person_id is a "Professor"
    
    parameters
    :db a dict like object
    :person_id a unique identifier
    
    :return a list'''
    
    if person_id in db:
        
        if db[person_id]['role'] == 'Student':
            first_name = db[person_id]['first_name']
            last_name = db[person_id]['last_name']
            status = db[person_id]['status']
            return [first_name, last_name, status]
        
        elif db[person_id]['role'] == 'Professor':
            first_name = db[person_id]['first_name']
            last_name = db[person_id]['last_name']
            status = db[person_id]['status']
            students = []
            
            for student_id in db[person_id]['students']:
                s_first_name = db[student_id]['first_name']
                s_last_name = db[student_id]['last_name']
                name = f"{s_first_name} {s_last_name}"
                students.append({"name": name, "id" : student_id})
                
            return [first_name, last_name, status, students]
    else:
        return "Your db sucks there's no id"

###############################################################
# STEP #5
###############################################################
# app.py #
###############################################################

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
    return 'Hello, World {}!'.format(person_id)

if __name__ == '__main__':
    app.run()

###############################################################
# STEP #6
###############################################################
# app.py #
###############################################################

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
        return ("Is in the db")
    else:
        return ("No is not in the db")

if __name__ == '__main__':
    app.run()

###############################################################
# STEP #7
###############################################################
# app.py #
###############################################################

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

    if person_id in db:
        if db[person_id]['role'] == 'Student':
            student = db[person_id]
            first_name = student['first_name']
            last_name = student['last_name']
            status = student['status']
            return "{},{},{}".format(first_name, last_name, status)
        
        if db[person_id]['role'] == 'Professor':
            professor = db[person_id]
            first_name = professor['first_name']
            last_name = professor['last_name']
            status = professor['status']
            
            students = []
            
            for student_id in db[person_id]['students']:
                student = db[student_id]
                s_first_name = student['first_name']
                s_last_name = student['last_name']
                name = "{} {}".format(s_first_name, s_last_name)
                students.append({"name": name, "id" : student_id})
                
            return "{}, {}, {}, {}".format(first_name, last_name, status, students)
            
    return "Your db sucks there's no id"

if __name__ == '__main__':
    app.run()