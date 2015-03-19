from frysauce import app
app.static_folder = '../static'
app.static_url_path = 'static'
app.run(debug=True)
