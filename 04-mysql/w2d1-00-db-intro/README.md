# MySQL

MySQL is a free and open-source relational database system. It was created by a Swedish company and first released in 1995. It is written in C and C++. MySQL ranks as the second-most widely used database. It powers many of the most accessed applications, including Facebook, Twitter, Netflix, Uber, Airbnb, Shopify, and Booking.com.

## Relational Databases
Relational databases are a type of database management system (DBMS) that organizes and stores data in a tabular form, consisting of rows and columns. The foundation of relational databases is based on the relational model, which defines relationships between tables using keys and constraints. These databases are designed to efficiently manage large amounts of structured data and provide powerful mechanisms for querying, manipulating, and retrieving data.

The purpose of relational databases is to provide a reliable, scalable, and flexible solution for storing and managing data. They offer a structured approach to organizing data by breaking it down into logical entities (tables) and defining relationships between them. This enables the representation of complex real-world scenarios and allows for efficient data retrieval and manipulation operations.

## MySQL Server

When we install MySQL, we have the option to spin up the included MySQL Server on our local machines. I recommend that you start it up and leave this instance up and running for the duration of this stack.

We will primarily be interacting with our instance of MySQL Server through an application called MySQL Workbench. It is also possible to interact with the instance through a shell in our terminal. You may have already done this. The command to enter the mysql shell is `mysql -uroot -p` (Mac) and `mysql.exe -uroot -p (Windows)`.

**Please note:** After executing the above command, you will be prompted for your password. As you type, there will be no visual confirmation that you're pressing any keys. Continue typing your password as normal and press enter when complete.

