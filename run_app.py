import os
from api.views import app
from api import utilities
 

app.config['DEBUG']= True

if __name__ == '__main__':
    utilities.Database()
    app.run()
