## Flask
****
*from flask import Flask*
*from flask import request*

`app = Flask(__name__)`
 - Makes a flask app with the current namespace

`def index():`
  `return "page contents"`
 - Acts as a view for whatever route we link it to

`@app.route('/')`
 - Comes right before a function declaration, wrapper links it to '/'

`app.run(debug=True, port=8000, host='0.0.0.0')`
 - Starts the app with debugger on port 8000 to any host
 - Debug reloads the server when data changes

`name = request.args.get('name', name)`
 - Gets the name variable from the query string if available
 - If not, uses preset name variable


## Templating
****
*from flask import render_template*
 - Templates get saved in a folder named *templates*

```
@app.route('/<name>')
def index(name='Treehouse'):
    context = {
        'name': name }
    return render_template('index.html', **context)
```
`render_template('templatename.html', **context)`
 - Where context is a dict of all our variables
 - Templates work similarly to angular and swig:

`{{ variablename }}`
 - On the template substitutes for our variable

`{% extends 'layout.html' %}`
 - This is used to make a template for the templates for drier programming

`{% block blockname %}{% endblock %}`
 - Used to denote blocks. blocks are ended with endblock.
 - Blocks from the views will be inserted into views they extend from.

`{% block title%}pagecontent | {{super()}}{% endblock %}`
 - Super() is used to copy content from the layout block

`<link rel="stylesheet" href="/static/styles.css">`
 - Static files get saved in a folder named *static*
 - They are used with /static/file like above

`{{ url_for('save') }}`
 - Links it to the url for the save function

## Cookies
****
*from flask import (Flask, redirect, render_template,*
									 *request, url_for, make_response)*

`response = make_response(redirect(url_for('index')))`
 - Pass into make_response whatever you would have returned for page render

`response.set_cookie('cookiename', json.dumps(dict(request.forms.items())))`
 - Sets the cookie names cookiename to all of the postdata from the request

`data = json.loads(request.cookies.get('character'))`
 - Loads the character cookie as a dictionaty into data

`data.update(dict(request.form.items()))`
 - Updates the data dict with any new request data

`response.set_cookie('character', json.dumps(data))`
 - Sets the response to save the data dict as a json to the cookie