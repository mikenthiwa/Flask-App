# Hello-Book(Flask-App)
Hello-Books is a simple application that helps manage a library and its processes like stocking, tracking and renting books. With this application users are able to find and rent books. The application also has an admin section where the admin can do things like add books, delete books, increase the quantity of a book etc.

### Getting Started
To access the project:
Go to: https://github.com/mikenthiwa/Flask-App/README.md
Clone it to your computer.


### Prerequisites
*Browse
*Python
*IDE

### Installing virtual enviroment
Open cmd.


Navigate to your project folder and open it using the commandprompt.


Create a virtual enviroment.
  *virtualenv name_of_virtual_enviroment.
  
 
Folder with the 'name_of_virtual_enviroment' will be created and that is out enviroment.


Navigate inside the folder, open folder called Scripts and run the script activate.
 *Type activate

### Running the test

Create a simple flask application that return 'hello world' for testing.
This is good example since flask requires to be run under virtualenviroment
example;
import flask from Flask


app = Flask(__name__)

@app.route('/')

def index():

    return 'Hi'
  
if __name__ == '__main__':

    app.run()
  
 if the webpage return Hi, this shows that the virtual enviroment has been created properly

### Author
Michael Mutua


