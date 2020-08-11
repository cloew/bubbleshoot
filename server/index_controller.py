from flask import render_template

class IndexController:
    """ Controller to return the Index Page """
    
    def perform(self):
        """ Render the template for the index page """
        return render_template('index.html')
