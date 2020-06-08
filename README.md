Live at: https://ayushxx7.pythonanywhere.com


ABOUT:
TMDB API BASED MOVIE DETAIL SEARCH ENGINE
uses Flask for backend


ASSUMPTIONS:

CLIENT REQUIRES SIMPLE WEBSITE WITH A SINGLE SEARCH BAR.
WILL BE USING THAT SEARCH BAR AND ENTERING MOVIE NAMES WHICH WILL BE A STRING
CLIENT EXPECTS FIRST PAGE RESULTS WILL SHOW UP ON THE SAME PAGE ITSELF
CLIENT EXPECTS MORE INFORMATION WILL BE PRESENT ON OTHER PAGE AND THERE WILL BE
A SIMPLE REDIRECT FROM NAME LIST TO DETAIL ABOUT SELECTED NAME
CLIENT DOES NOT NEED SECURTIY FEATURES FOR NOW
CLIENT DOES NOT REQUIRE ANY STORAGE OR DATABASE SOLUTION FOR NOW


CHOICE OF IMPLEMENTATION:

HTML, CSS, JS, BOOTSTRAP TEMPLATE FOR FRONT END TO MAKE THE UI LOOK CLEAN AND 
FOR FASTER CUSTOMIZATION BECAUSE CLIENT WILL NOT SEE WHAT IS GOING ON BEHIND.

FLASK FOR BACKEND BECAUSE IT IS SIMPLE TO SETUP AND RUN, IS A LOW LEVEL FRAMEWORK 
SO IT IS LIGHTWEIGHT, AND IT SATISFIES ALL REQUIREMENTS

JINJA FOR VARIABLE PASSING BETWEEN PYTHON AND HTML 


HOW TO:

git clone https://github.com/ayushxx7/tmdb_search.git
pip install -r requirements.txt
py hello.py

Server starts running

Go to localhost:5000 or http://127.0.0.1:5000 and start searching.
