from frysauce import app
app.static_folder = '../static'
app.static_url_path = 'static'
app.secret_key = 'some_secret'
app.run(debug=True)
