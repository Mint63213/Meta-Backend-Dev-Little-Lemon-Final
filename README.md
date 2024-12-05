#Little Lemon Web Application-Peer Graded Assignment

1) Evaluate the following: 
Does the web application use Django to serve static HTML content?

2) Has the learner committed the project to a Git repository?

3) Does the application connect the backend to a MySQL database?

4) Are the menu and table booking APIs implemented?

5) Is the application set up with user registration and authentication?

6) Does the application contain unit tests?

7) Can the API be tested with the Insomnia REST client?
-----------------------------------------------------
#Requirements

django 5.1.2<br>
djangorestframework 3.15.2<br>
djangorestframework-simplejwt 5.3.1<br>
mysqlclient 2.2.6<br>
djoser 2.3.1<br>
bleach 6.2.0<br>
-----------------------------------------------------
#Peer-review Instructions

1) Fix settings.py for your personal DB location<br>

2) Add database in MySQL:<br>
(Drop DATABASE littlelemon;)(*if needed)<br>

a) CREATE DATABASE LittleLemon;<br>

b) (make migrations to create the tables)<br>

c) Paste this script into your sql terminal to add appropriate menu items:<br>
/*<br>
INSERT INTO restaurant_menu (name, menu_item_description, price) VALUES
('Greek salad', 'Our famous Greek salad of crispy lettuce, peppers, olives,
 and our Chicago-style feta cheese. Garnished with crispy onion and salty
 capers.', 12),
('Grilled fish', 'The fish is swiftly grilled over medium- or high-heat coals
 or over medium- or high-heat gas grill burners. Thinner fillets and steaks are
 grilled over direct fire.', 9),
('Bruschetta', 'An Italian antipasto called bruschetta is made of grilled bread
 that has been smeared with garlic and seasoned with salt and olive oil. Toppings
 of tomato, veggies, beans, cured pork, or cheese are examples of variations. In
 Italy, a brustolina grill is frequently used to create bruschetta.', 11),
('Lemon dessert', 'This cake is adored not only for its flavor but also for its
 texture and simplicity. A base of creamed butter and sugar, eggs, lemon, milk,
 and flour are among the most basic ingredients. We omitted the brown sugar and
 substituted extra granulated sugar instead.', 7),
('Lamb ribs', 'Ribs of a lamb. Sauced. Tender. Enjoy with our Mediterranean Loaf.', 17);<br>
*/

#Add users:
 Username | password | user settings<br>

a) admindjango | lemon@789!  | superuser<br>
b) ManagerOne  | lemon@789! | Staff status<br>
c) ManagerTwo | lemon@789! | Staff status<br>
d) CustomerOne | lemon@789! | Active<br>
e) CustomerTwo | lemon@789! | Active<br>
-----------------------------------------------------
#Project Notes

I have the following recommendations:<br>

1) Users must be Staff status. Configure staff user using the Admin Console, 
selecting a User, and checking the box "Staff status", and saving. First, 
Test using manually generated tokens through API testing client.
for API calls.<br>

2) Second, uncomment the authentication_classes = [SessionAuthentication, 
BasicAuthentication] from the API views in views.py, and login through the 
webpage to generate a session using a Staff user or Super user, and visit the
 api endpoints from the browser.<br>

3) Users may register through the link on the login page. New users will be 
only 'Active' by default, not 'Staff status'. Users may only make bookings 
if they're registered and logged in.<br>

------------------------------------------------------
#API Endpoints
Authorized users may search individual menu items and bookings through the api 
using the following urls:

http://127.0.0.1:8000/apis/menu-items-api/<br>
http://127.0.0.1:8000/apis/menu-items-api/str:name<br>
http://127.0.0.1:8000/apis/booking-api/<br>
http://127.0.0.1:8000/apis/booking-api/str:last_name<br>
--------------------------------------------------------
#Test
The tests can be executed after by commenting out from settings:<br>
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
<br>
and commenting out from the API views in views.py:<br>
permission_classes
authentication_classes 
<br>
The execution codes are commented into the test.py<br>
(I need to study more testing)
------------------------------------------------------------
Originally, I chose to leave out the "'api-token-auth/', obtain_auth_token"
after realizing it has the same functionality of djoser's
built-in "auth/token/login/".<br>
(needs more research)
