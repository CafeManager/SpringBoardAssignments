### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
 
    Some important difference are the way you create classes and what different tools are available to you. Dictionaries are used more often in Python.  
    
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming crashing.

    You can used .get on the dictionary. You can use a conditioner "if('c' in dict):" before you access it through "dict['c']" 

- What is a unit test?

    A unit test is a block of code that tests to see if a function is working.

- What is an integration test?

    An integration test tests to see if blocks of code works together properly together. 

- What is the role of web application framework, like Flask?

    The role of a web application framework is to make front end development easier.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    Route url is generally more dynamic than url query param. 
  Ex: Say there are 5000 comments that have the url /comment/[comment number]
  This is a lot more readable than making a route render based on a route like 
  [/comment?id=comment number]  
  
    URL Query Param can pass a lot more data when navigating to a certain page.
  Ex: Say you are sorting posts on the home page. [/home?sortBy=date&theme=darkmode]
  The alternative to this url would be [/home/sortByData/themeDarkMode]
  The alternative necessitates a lot more rewritten code and is less dynamic that the original.


- How do you collect data from a URL placeholder parameter using Flask?
  
    The placeholder syntax is encapsulated with "<>". So for example, to make a route that takes the information of the last part of a route would be: [/home/<variableName>]

  - Format:  
  @app.route("/home/<id>")  
  def home_page(id):  
    return render_template("home.html" id=id)


- How do you collect data from the query string using Flask?  
  - First you have to import it from flask:  
  from flask import request

    Then you access the information using one of these two methods.

    Method 1:

    > myVariable = request["myVariable"]

    Method 2:

     > myVariable = request.get("myVariable", [valueIfUnaccessible])

    Note: Method 2 will not return an exception if there is the data has not been defined. If the data is not defined, then the second argument will be the value that gets returned.

- How do you collect data from the body of the request using Flask?
  
    from flask import request
    data = request.get_data()


- What is a cookie and what kinds of things are they commonly used for?    

    A cookie is a piece of data that a server tells a clients to save. After the cookie is saved, the cookie is sent with every single request to the server incase the server needs to use the data.

- What is the session object in Flask?  
  A session object is something that keeps track of user information like cookies, but expires once the user exits the browser.

- What does Flask's `jsonify()` do?  
  jsonify() turns python data types into JSON.
