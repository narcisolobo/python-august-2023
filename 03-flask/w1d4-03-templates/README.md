# Flask Templating and Jinja

Templates and Jinja are essential components of Flask. They allow you to build dynamic and reusable web pages by combining HTML markup with data from your Flask application.

## Templates:
Templates in Flask are HTML files with placeholders that can be dynamically filled with data. They provide a way to structure and define the visual elements of your web pages, such as headers, footers, and content sections. Flask uses a template engine called Jinja2 to render templates.
Key points:

- Templates separate presentation from application logic.
- Templates are reusable and flexible. They help us build dynamic web pages.

### Template Inheritance
- `base.html` - Jinja allows us to inherit HTML from parent templates.
- We can create child templates that extend these parent templates.
- We can include partial templates in parent and child templates.

## Jinja2
Jinja is a powerful templating engine used by Flask to render dynamic content in templates. It provides a wide range of features and syntax that allow you to insert and manipulate data within HTML templates.

**Syntax**  
Jinja employs a special syntax for variable interpolation and control flow statements.

Use double curly braces `{{ variable }}` to display the value of variables.

Use single curly braces and percent signs `{% for item in items %}...{% endfor %}` for loops and conditionals.

### Logic and Control Structures
#### For loops
```jinja
{% for product in products %}
    <p>{{ product.name }}</p>
    <p>{{ product.price }}</p>
{% endfor %}
```

#### Conditionals
```jinja
{% if product.quantity > 0 %}
    <p>{{ product.quantity }}</p>
{% else %}
    <p>Out of stock</p>
{% endif %}
```
