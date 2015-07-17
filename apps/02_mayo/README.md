# Connecting Client to Server

Remember the link in the setup about `telnet towel.blinkenlights.nl`?

Well, in that case, we were using ` towel.blinkenlights.nl` as a *server* and our command line was the *client*.

Every time you connect to a web site, you're doing the same thing. The only difference is that your browser is decoding those characters into a visual web page.

To send things to the browser we have a bunch of different methods. Sending things to the browser is known as a `REQUEST`. There are 2 primary types of `requests`. `GET` and `POST`.

 * `GET`: The primary request your browser makes — you can see the entire `GET` request in your browser.

 eg: `http://127.0.0.1/hello/world/?q=foo`. Every part of the url is a `GET` request. Anything that follows a `?` is a *parameter*.

 Multiple paramters are sent with `&`. For example the url: `http://127.0.0.1/?q=1&date=2015` has the parameters `q` and `date` which equal `1` and `2015` respectively.

 You can capture parameters in the `app.route` of a flask web application:
 ```python
 @app.route("/hola/<string:elephants>/<int:a>/<int:b>")
 def index(elephants, a, b):
   return elephants, a, b
 ```

 * `POST`: A special one-off send to the browser. Whenever you submit a form on the web, you are using a `POST` to send the data. If you've ever tried to hit "back" on a site unsuccessfully, this is why — `POST` is essentially a one-time request. We send these variables via a web form:

 ```html
 <form method='POST' action='.'>
   <input name='title' type='text' />
 </form>
 ```
 In this form, we can capture the `title` in flask by using `request.form['title']`
