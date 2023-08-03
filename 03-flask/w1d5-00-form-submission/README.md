# Flask Form Submission

## POST Requests
So far, the flow of data in our Flask applications have largely been one-way, from server to client. The client requests a route (with optional route parameters), our server maps that route to the correct function, then responds with a Jinja template.

This type of request is called a GET request. Specifically, it is an *HTTP request method*. It is one of a set of several types of request methods. They are sometimes referred to as HTTP verbs. The most important ones are GET, POST, PUT, PATCH, and DELETE.

We'll learn about PUT, PATCH, and DELETE in the JavaScript stack, but for now let's talk about GET and POST.

The request described above is called a GET request because our client is requesting to *get* information from the server. But what do we do when our client must provide or give information to the server, say when creating an account or purchasing a product? In these cases, our client must make a POST request by submitting a form.

## Forms
Forms and the handling of form submission is critical to becoming a sufficient web developer.
Forms allow users to input and submit data to our back-end servers, enabling interactive and dynamic functionality in web applications.

In order for our client to make a POST request, our HTML form tags must have at least two attributes, the `action` attribute and the `method` attribute.

### The `action` attribute:
The value of the action attribute is a server-side Flask route where the form data is sent for processing. If the form is meant to create a user account, it might be something like `action="/users/register"`. If the form is meant to purchase a product, it might be `action="/products/purchase"`.

### The `method` attribute:
The value of the method attribute will be `"POST"`, i.e. `method="POST"`. The uppercase is convention, it is not required. POST requests are used to send data from the client to the server for specific actions, such as creating a user account or making a purchase.

#### Example `form` tag:
```html
<form action="/users/register" method="POST">
  ...
</form>
```

### Form inputs
Inside the form tags, our inputs must at least have `name` attributes.

***This is crucial**. It serves as the key in the key-value pair for the form data sent to the server.*

Upon form submission, a dictionary is created with key-value pairs and is sent along with the POST request as a kind of payload. The names of the keys are the inputs' `name` attributes, and the values are the data the user has entered into each input. We access these values server-side with `request.form`.

For example, say our form has a label and input that looks like this:
```html
<label for="first_name">First Name:</label>
<input type="text" name="first_name" id="first_name" />
```

If our user has entered a value of "Kermit" into this input and then submits the form, the dictionary would look like this:

```py
{ "first_name": "Kermit" }
```

We can access this value server-side using bracket notation:
```py
entered_first_name = request.form["first_name"]
# THIS KEY NAME MUST MATCH EXACTLY
# WITH THE NAME ATTRIBUTE OF THE INPUT
```
Or with the built-in `.get` dictionary method:
```py
entered_first_name = request.form.get("first_name")
``````

### Other input types
#### `number` inputs:
When we have an input of type "number" in our HTML form and we submit the form, the value of that input will be treated as a string in the `request.form` dictionary in Flask.

The HTML form submission mechanism sends all form data as strings, regardless of the input type specified in the HTML. This means that even if you have an `<input type="number" />` in your form and the user enters a numeric value, that value will be received as a string on the server side.

To handle numeric values and perform numerical operations, we will need to convert the string representation of the number to a numeric data type, such as an integer or a float. You can use Python's built-in conversion/constructor functions like `int()` or `float()` to achieve this.

For example, if your form has an input of type "number" like this:

```html
<label for="age">Age:</label>
<input type="number" name="age" id="age" />
```
And the user enters a value of "25" for the age, we can convert it to an integer in your Flask route using the `int()` constructor:

```py
age = int(request.form["age"])
# or
age = int(request.form.get("age"))
```

#### `checkbox` inputs:
```html
<form action="/users/register" method="POST">
  ...
  <label for="reading">
    <input
      type="checkbox"
      name="hobbies"
      id="reading"
      value="reading"
    />
    Reading
  </label>
  <label for="music">
    <input
      type="checkbox"
      name="hobbies"
      id="music"
      value="music"
    />
    Music
  </label>
  <label for="sports">
    <input
      type="checkbox"
      name="hobbies"
      id="sports"
      value="sports"
    />
    Sports
  </label>
  <button type="submit">Register</button>
</form>

```
In this example, we have three checkboxes with the same `name` attribute value of "hobbies". This allows the user to select one or more hobbies. The `value` attribute for each checkbox represents the value associated with the corresponding hobby.

When the form is submitted, the selected hobby values will be sent to the server as a list in the `request.form` dictionary. You can access this list server-side by using `getlist()` method on `request.form`:

```py
selected_hobbies = request.form.getlist("hobbies")
```
The `selected_hobbies` list will contain the selected hobby values, for example `['reading', 'music']` if the user selected "Reading" and "Music". You can then process this list on the server side as needed.

#### `radio` inputs:
```html
<form action="/orders/create" method="POST">
  ...
  <label for="hawaiian">
    <input
      type="radio"
      name="pizza"
      id="hawaiian"
      value="hawaiian"
    />
    Hawaiian
  </label>
  <label for="margherita">
    <input
      type="radio"
      name="pizza"
      id="margherita"
      value="margherita"
    />
    Margherita
  </label>
  <label for="pepperoni">
    <input
      type="radio"
      name="pizza"
      id="pepperoni"
      value="pepperoni"
    />
    Pepperoni
  </label>
  <button type="submit">Place Order</button>
</form>
```
In this example, we have radio buttons for each pizza option. The `name` attribute is set to "pizza" to group the radio buttons together. Each radio button has a unique id and a corresponding label for better accessibility.

When the form is submitted, the selected pizza option will be sent to the server as a single value in the `request.form` dictionary. You can access this value using the name of the radio button group:

```py
selected_pizza = request.form["pizza"]
# or
selected_pizza = request.form.get("pizza")
```
The `selected_pizza` variable will contain the value of the selected pizza option, such as "hawaiian", "margherita", or "pepperoni", depending on the user's selection.

#### `select` elements
```html
<form action="/orders/create" method="POST">
  ...
  <label for="shirt_size">Shirt Size:</label>
  <select id="shirt_size" name="shirt_size">
    <option value="small">Small</option>
    <option value="medium">Medium</option>
    <option value="large">Large</option>
  </select>
  <button type="submit">Place Order</button>
</form>
```
In this example, we have a `<select>` element with an `id` of "tee-shirt-size" and a `name` of "size". The `<select>` element contains three `<option>` elements with different values and display text for each tee-shirt size.

When the form is submitted, the selected tee-shirt size will be sent to the server as the value in the `request.form` dictionary. You can access this value using the name of the select element:

```py
selected_size = request.form["shirt_size"]
# or
selected_size = request.form.get("shirt_size")
```

The `selected_size` variable will contain the value of the selected tee-shirt size, such as "small", "medium", or "large", depending on the user's selection.

## Server-Side Form Processing
Next week, we will be adding a MySQL database to our Flask applications. When that happens, we will be processing our forms server-side and mutating the data in our database accordingly. After the appropriate database operation takes place, our routes will finally `redirect` to another view function.

**We never want to `render_template` on a POST handler.** We will always `redirect` to a GET route. We will discuss this topic further in the afternoon.

### Example Server-Side POST Request Handler:

```py
@app.route("/orders/create", methods=["POST"])
def create_pizza_order():
  # save the user in the database
  # we'll learn how to do that soon!

  # if we would like to inspect the
  # form data, we can print it like so:
  print(request.form)

  # or individual values like so:
  print(request.form["pizza"])
  # or using .get()
  print(request.form.get("pizza"))

  return redirect("/success")
```

Notice the new addition of `methods=["POST"]` in our `@app.route()` decorator. This is how we allow specific HTTP methods for specific routes. The `methods` argument must be plural, and its value is an array of strings. If the `methods` argument is not specified, it defaults to `["GET"]`.

Flask gives us shortcut decorators, as well. If you would like to save a little typing, you can also use `@app.get()` for GET routes or `@app.post()` for POST routes. The shortcut decorator below is an identical configuration to the one above.

```py
@app.post("/orders/create")
```
