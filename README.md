# Python Advanced CodeMeProject 
## DNA conversion tool
Python Advanced CodeMeProject is a Python-based web application for  converting DNA sequence to corresponding DNA reverse strand sequence, RNA sequence or protein sequence. 
Python Advanced CodeMeProject was prepared as a final project for Python Advaned course on CODE:ME.

## Installation

Python Advanced CodeMeProject requires:

Python (3.6)
Flask

## Functionalities

The web application provides a simple tool useful for molecular biology and biotechnology research. It enables for converting user-defined DNA sequence into corresponding DNA reverse strand sequence, RNA sequence or protein sequence. All processed data (both input and output), together with date and time of making a query, is stored in a database.

The application can be used after login and is available for users whose data are stored in the database.  New user account can be created by administrator by running 'create_user.py' file. Alternatively, new user account can be created by admin only by direct entry to the database ('baza_zaliczenie.db', 'users' table). File 'password_hash.py' can be useful for password hashing to be uploaded to the database.

The application enables for printing out all queries made by a logged user. Admin can browse all queries available in the database.


## How to use

For the first start, a database need to be created. This can be done by running 'baza_init.py'. To start application, 'app.py' file needs to be run. The web application explains step-by-step what to do once it is run.

**_Enjoy!_**
