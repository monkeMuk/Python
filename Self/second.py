from flask import Blueprint, render_template

second = Blueprint(
    'second',
    __name__,
    static_folder='static',
    template_folder='templates'
    )

'''
good practice, 
    name of file == name of variable == name of Blueprint, in this case it's 'second'

'''
