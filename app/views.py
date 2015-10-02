from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'proj'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Prof1'}, 
            'body': 'Call for research assistance' 
        },
        { 
            'author': {'nickname': 'Stud1'}, 
            'body': 'Interested in doing research for X' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)