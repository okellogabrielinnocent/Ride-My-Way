import os
from api.views import app
from api import utilities
 
app.config["SECRETE_KEY"] = "toosecrete"

if __name__ == '__main__':
    utilities.Database()
    app.run(debug=True)
