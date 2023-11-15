# Index - Table Of Contents:

1. [General Information](#About-everything-DESI)
3. [Data](#Data)
4. [User Experience](#User-Experience)
5. [Features](#Features)
6. [Technologies Used](#Technologies-Used)
7. [Agile Methodology](#Agile-Methodology)
8. [Testing](#Testing)
12. [Deployment](#Deployment)
13. [Credits](#Credits)

# About everything DESI
everythingDESI is a recipe blog web application, for people who love desi food. This website provides a platform for desi food lovers to share 
their favorite food recipes, share their opinions, like, and give ratings to help others try the best ones available.

The website is interactive and responsive and also allows users to register themselves. 
![Responsive image](/README_FILES/respponsive.png)

# Data
## Database Diagram
The Database diagram shows the relationship between the tables created by the model. The user custom table that was created by the custom model is shown 
in the diagram as this was directly connected with the model.

The 'Recipe' model is the main model which contains most of the details. The main purpose of the application is to display the recipe details and add new recipes,
which is done by the recipe model. To filter the recipes by 'category' and 'method' I created two separate models 'RecipeCategory' and 'RecipeMethod'. This one-to-many relationship enables to create recipes with different methods and categories. 

The application also allows the user to comment and rate the recipes. The 'Comment' and 'Rating' models allow the user to fulfill this task. The one-to-many relationship between these models allows the user to comment and rate multiple recipes. 

I used [DrawSQL](https://drawsql.app/) to draw and visualize the database schema.

![Database Diagram](/README_FILES/DatabaseDiagram.png)

 ## User Custom Model

 The user model is customized to take 'email' and 'password' rather than the built-in 'username' field. The email field is set to 'Unique' and the username is 
 set to none. This custom user model is used with the recipe and comment model as one-to-many relationships.

# User Experience

### User Requirements and Expectations:

- A user-friendly and self-explanatory landing page 

- Easy navigation to the whole site

- Responsive and interactive design

- Feedback as the user takes action

- Properly working features

### Target Audience

* The target audience is people like me, who love desi food. There are thousands of websites available for food lovers but I wanted to make a blogging website only for desi food lovers.
* People who already cook and want to learn new recipes or the people who are new to cooking, this website welcomes everyone

### User Stories
|EPIC|User Stories|Role|Functionality|Benefit|MosCoW|
|--------|------------|----|-------------|-------|------|
|Authentication|Account Registration|As a **Site User** | I can register an account| so that I can publish a recipe, comment, like, and rate any recipe|Must-Have|
|Authentication|Sign In|As a **Site User**| I can **sign in** with my email and password|so that I can publish a recipe, comment, like, and rate any recipe|Must-Have|
|Authentication|Sign Out|As a **logged-in** user| I can log out of my account| so that no one can see my confidential information|Must-Have|
|Administration|Approve comments|As a **Site Admin**| I can approve or disapprove comments | so that I can filter out any inappropriate content|Should-Have|
|Administration|Manage posts|As a **Site Admin**| I can create, read, update, and delete posts| so that I can manage my blog content|Must-Have|
|CRUD Functionality|Read full recipe|As a **Site User**|  I can click on a recipe card| so that I can read the full recipe|Must-Have|
|CRUD Functionality|Add a recipe|As a **Site User**| I can add recipes| so that I can share my favourite recipes with othersMust-Have|
|CRUD Functionality| Update recipes|As a **Site User**|  I can update my published recipes| so that I can add or correct information|Must-Have|
|CRUD Functionality|Delete recipe|As a **Site User**|  I can delete my published| so that I can remove them from the recipe list|Must-Have|
|CRUD Functionality| Recipe cards list|As a **Site User**|  I can view recipe cards on the home page| so that I can select one to read|Must-Have|
|CRUD Functionality|View comments|As a **Site User/Admin**|I can view comments on an individual post| so that I can read the conversationn|Should-Have|
|CRUD Functionality|Comment on recipe blogs|As a **Site User**| I can leave comments on a post| so that I can be involved in the conversation and ask questions|Should-Have|
|CRUD Functionality|View ratings|As a **Site User**| I can view the average rating on each recipe blog| so that I can see which is the most popular or viral|Could-Have|
|CRUD Functionality|Rate recipes|As a **Site User**| I can rate recipes| so that I can help other users choose the right content|Could-Have|
|User features|Choose method|As a **Site User**| I can select the method| so that I can choose what type of recipe I want to see|Should-Have|
|User features|Choose category|As a **Site User**| I can select the category| so that I can choose what type of recipe I want to see|Should-Have|
|User features|View likes|As a **Site User/Admin**| I can view the number of likes on each recipe blog| so that I can see which is the most popular or viral|Should-Have|
|User features|Like/Unlike|As a **Site User**| I can like or unlike a post| so that I can interact with the content|Should-Have|
|User features|Footer social media links |As a **Site User**| I can click on social media links| so that I can stay updated by following the platform|Could-Have|

[Acceptance Criteria and Tasks](https://github.com/users/Sadaf-Tariq/projects/2)

### WireFrames
* Wireframes are created on [Balsamiq](https://balsamiq.cloud/)

<img src="/README_FILES/wireframe1.png" alt="Home Wireframe" width="400" height="400"/>


- The home page planning is done using this wireframe as a guide, there is another row was added during the development of food preparation methods.

<img src="/README_FILES/wirefram3.png" alt="Add recipe form Wireframe" width="400" height="400"/>

- This is a general recipe list page wireframe, the same planning is used for the category and method recipes list.

<img src="/README_FILES/wirefram2.png" alt="RecipeList Wireframe" width="400" height="400"/>

- This wireframe is made for adding a recipe page, the same is used for editing recipes and similar for login, sign up, and sign out pages.

### Color Scheme

- The color palette was chosen by me and generated by [color hex](https://www.color-hex.com/)

![Color Palette](/README_FILES/colorpallette.png)

- #E6BEAE is the primary color used in the whole project, for the header, footer, navbar, and form background.

### Typography

- Montez and Hind Siliguri are the fonts that I used throughout the project. The fonts are taken from [Google Fonts](https://fonts.google.com/)

### Imagery/Icons

- The logo image for the website was taken from [WIX](https://www.wix.com/logo/maker)
- The images used in the website were taken from [Pexels](https://www.pexels.com/) and [pngTree](https://pngtree.com/)
- The icons used are taken from [Font Awesome](https://fontawesome.com/v4/get-started/)

# Features
* The Header

  * Featured at the top of the page, the header shows the logo of the website at the right of the right corner: everything DESI that links to the home page

  * The logo image is present at the left corner of the header and also links to the home page

  * The header clearly shows the name of the website with a font easy to understand and a color that contrasts with the background

    ![Header](/README_FILES/header-logo.png)

* Navigation

  * Featured after the header, it contains the navigation links for the website present at the center of the navigation bar

  * The navigation links are: Home, Recipes, Sign Up, and Log In for unauthenticated users, which link to the different pages of the website

  * The navigation links for authenticated users are Home, Recipes, Create New Recipe, and Sign Out

  * The navbar collapses when the screen size is smaller and contains all the same links

  * The navigation links make it easy for the user to find the different pages of the website and use the same color theme but a different font

  
    <img src="/README_FILES/navbar1.png" alt="Navigation Bar for unauthenticated User" width="650" />
    <img src="/README_FILES/logged-in-navbar.png" alt="Navigation Bar for authenticated User" width="650"/>
    <img src="/README_FILES/collapsible-navbar.png" alt="Collapsible navigation Bar" width="650"/>


* Recipe Cards

  * The recipe card lists are shown after the nav bar, these are the recipes that are already available in the database created by users and the admin
 
  * These cards contain the recipe image, average rating, number of likes, and number of comments
 
  * These cards help users see a list and make a decision about which recipe they want to explore more

    ![Recipe Cards](/README_FILES/recipe-cards.png)

* Food Category Options

  * After the recipe cards, there is a scroll list of food categories available for users

  * Each category filters a list of recipes of that category and makes it easy for the users

  * There are arrow buttons available on each side for the user to see the full list of categories

    ![Food Category](/README_FILES/food-category.png)

   
* Food Method Options

  * After the categories option, there is a scroll list of food methods available for users

  * Each method filters a list of recipes of that method and makes it easy for the users

  * There are arrow buttons available on each side for the user to see the full list of methods

    ![Food Method](/README_FILES/food-method.png)

* The Footer

  * The footer section encourages the user to keep in contact and updated

  * The footer section includes social media icons so that users can find the blogging page on Facebook, Twitter, YouTube, and Instagram

  * The information on the footer section is valuable to the users as it helps them to find or see any updates if available

    ![The footer](/README_FILES/footer.png)

* Recipes Page

  * The recipes page is available for all the users 

  * The page contains a detailed list of recipe cards and has all the recipes available in the database
 
  * The recipe card contains the recipe image, average rating, cooking time, preparation time, method, category and number of servings
 
  * These cards help users see a list and make a decision about which recipe they want to explore more

    ![Recipes Cards](/README_FILES/recipes-recipe-card.png)

​* Recipes with Food Category

  * This page displays the filtered recipe with the selected category

  * The page contains the recipe cards of the filtered recipes

  * The recipe card contains the recipe image, average rating, cooking time, preparation time, method, category and number of servings
 
  * These cards help users see a list and make a decision about which recipe they want to explore more

    <img src="/README_FILES/category.png" alt="Food Category" width="500" height="400"/>

​* Recipes with Food Preparation Method

  * This page displays the filtered recipe with the selected preparation method

  * The page contains the recipe cards of the filtered recipes

  * The recipe card contains the recipe image, average rating, cooking time, preparation time, method, category and number of servings
 
  * These cards help users see a list and make a decision about which recipe they want to explore more

    <img src="/README_FILES/method.png" alt="Food Method" width="500" height="400"/>
    
* Add recipe

  * The users who are logged in will have the opportunity to add their favorite recipe by using the 'Create New Recipe' page

  * This page has a form which enables the user to input everything they need for a good recipe
 
  * These inputs are then saved to the database and added to the list of recipes
 
  * The forms fields are title, category , method, author_name, featured_iamge, ingredients, instructions, prep_time,
    cooking_time, servings and calories
 
  * There are two buttons available to 'Add' or 'Cancel'

    <img src="/README_FILES/add-recipe-form.png" alt="Add Recipe" width="500" height="450"/>
    <img src="/README_FILES/add_recipe_submit.png" alt="Add Recipe button" width="500" height="450"/>

* Full Recipe

  * When the users click on the recipes cards on the home page or recipes page, the page redirects to a full recipe page
 
  * This page contains all the information of that recipe in detail
 
  * All the information from database title, category, method, author_name, featured_iamge, ingredients, instructions, prep_time,
    cooking_time, servings, and calories are displayed
    
   <img src="/README_FILES/full-recipe-header.png" alt="Full Recipe header" width="800"/>

  * If the user is not logged in, they will not be able to like, rate, or comment

   <img src="/README_FILES/like-rate-com.png" alt="Like and rate for non-logged users" width="800"/>

  * If the user is logged in, the options to like and rate will appear
 
   <img src="/README_FILES/logged-in-like-rating-comments.png" alt="[Like and rate for logged-in users" width="800"/>

  * The ingredients and Instruction section of the recipe is also available in detail
    
    ![Ingredients](/README_FILES/ingredients.png)
     <img src="/README_FILES/instructions.png" alt="Instructions" width="480" height="450"/>

  * The list of comments from the database is available for all the users but a user cannot comment if not logged in

     ![Comments not logged-in user](/README_FILES/comments.png)
     ![Comments logged-in user](/README_FILES/comments_loggedin.png)
    
* Edit Recipe

  * The users who have created their own recipes will be able to edit their own recipes

  * When the user clicks the edit button a form with prepopulated fields will appear so that a user can update the recipe
 
  *  There are two buttons available to 'Edit' or 'Cancel'

     <img src="/README_FILES/edit_Recipe.png" alt="Edit Recipe" width="500" height="450"/>
     <img src="/README_FILES/submit-edit-recipe.png" alt="Edit Recipe button" width="500" height="450"/>

* Delete Recipe

  * The users who have created their own recipes will be able to delete their own recipes

  * When the user clicks the delete button, a confirmation message will appear to confirm the deletion process
 
  *  There are two buttons available to 'Delete' or 'Cancel'

     <img src="/README_FILES/delete-recipe.png" alt="Delete Recipe" width="550" height="450"/>


​* Authentication
   I used the django-allauth package to implement authentication and the Custom User model. The user can sign up with an email address & password..

  * **Sign In** process is straightforward, when the user clicks on the Log In link, the page will be redirected to a form

  * The user will input an email address and password to complete the process

    <img src="/README_FILES/sign-in.png" alt="Sign-In" width="550" height="450"/>


  * If the user is not already registered, they can opt to sign up

  * **Sign Up** process is also straightforward, when the user clicks on the Sign Up link, the page will be redirected to a form

  * The user will input an email address, password ans password(again) for confirmation and to complete the process

    <img src="/README_FILES/sign-up.png" alt="Sign-Up" width="550" height="450"/>

   * If the user decides to **Log Out**, the logout link from the nav bar lets the user to log out

   * It redirects the user to a sign put page to confirm the process

    <img src="/README_FILES/sign-out.png" alt="Sign-out" width="550" height="450"/>
     
* 404

  * A 404 page is available for the user to guide if the page requested is not available

    <img src="/README_FILES/404.png" alt="404" width="550" height="450"/>


# Agile Methodology
  * Agile methodology is used for project planning and development. Start from the planning until development user stories were created and implemented according to the order to stay organized. I used GitHub and its project features, Milestone, Labels, and Kanban Board to apply agile methodology.
  * User stories with acceptance criteria and tasks were defined and prioritized using MosCoW prioritization
  * The [user stories](https://github.com/users/Sadaf-Tariq/projects/2) can be found here
    
    
# Technologies Used

#### Languages Used

- Python: Using the Django framework and other plugins to develop the app
- HTML5
- CSS3
- Bootstrap5
- JavaScript

#### Frameworks, Libraries, and Packages

- django: Full-stack Python Framework
- Django-allauth: Django package for authentication
- Crispy-forms: Django package for form management
- Cloudinary: Cloud platform to host static and media file
- Google Fonts: Text fonts
- Summernote: JavaScript library to create WYSIWYG editors online
- dj-database-url: Parses database URLs for Django.
- gunicorn: Web server to run on Heroku.
- psycopg2: Adapter for PostgreSQL Database.

#### Hosting Platforms

- Heroku: For deployment/production
- ElephantSQL: For database
- Cloudinary: For static/media files

#### Other tools

- [RealFaviconGenerator](https://favicon.io/): To generate favicons
- Gitpod/Codeanywhere: For local development
- Git & Github: For version control and deployment
- Google Dev Tools: For testing and troubleshooting
- DrawSql: For database model 
- Random Key Generator: To generate a secret key.

# Testing

 * Testing document can be found in [TESTING.md](https://github.com/Sadaf-Tariq/pp4-desi-recipe-blog/blob/main/TESTING.md)

# Deployment
* The projects is deployed on **Heroku**, the database used is **ElephantSQL** and static/media files are hosted by **Cloudinary**
  
#### Installing Django and supporting libraries
- Install Gunicorn(django server for heroku): pip3 install 'django<4' gunicorn

- Install dj_database_url and pyscopg2(connect to PostegreSQL): pip3 install dj_database_url==0.5.0 psycopg2

- Install Cloudinary (Static/media hosting cloud platform): pip3 install dj3-Cloudinary-storage, pip3 install urllib3==1.26.15

- Install summernote (online editor): pip3 install summernote


#### Create App
- Create Project -> django-admin startproject PROJ_NAME . 

- Create App -> python3 manage.py startapp APP_NAME

- Add App to installed apps in settings.py:

            INSTALLED_APPS = [
              ...
              'APP_NAME',
            ]
             
#### Create an external database
- Navigate to ElephantSQL.com and create a free account

- Create an instance using the free plan(free turtle) with the instance name and region.

- Get the database URL from the instance info page

- Migrate the database
  
- In settings.py
  
  add

  import dj_database_url
  
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL', ''))
    }
  
  and comment out:
  
    DATABASES = {
            'default': {
                'ENGINE': 'Django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

#### Create the Heroku app
* Sign up for Heroku 

* Click the "Create a new app" button.

* Give your app a name and select the region 

 #### Django secret key
 
* Create a django secret key from [Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)

#### Create an env.py file
- Create an env.py file, the file should be added to .gitignore file
- Import os library: **import os**

- Set environment variables:

   - DATABASE_URL  ElephantSQL URL from the instance : os.environ["DATABASE_URL"]="<copiedURL>
   - SECRET_KEY: os.environ["SECRET_KEY"] = "randomSecretKey" (from key generator)

#### Update settings.py
    import os
    import dj_database_url
    if os.path.isfile('env.py'):
        import env

  SECRET_KEY = os.environ.get('SECRET_KEY')

- Save all files and make migrations: python3 manage.py makemigrations
  then migrate: python3 manage.py migrate

- Update heroku config Values

  |Key|Values|
  |---|------|
  |PORT|8000|
  |SECRET_KEY|randomsecretkey|
  |DATABASE_URL|Elephant_SQL URL|
  |DISABLE_COLLECTSTATIC|1(to prevent Heroku form collecting static files)|


#### Update setting.py for static and media files

- Create a Cloudinary account from [Cloudinary](cloudinary.com)

- Copy the URL from Cloudinary dashboard.

- Update env.py
  os.environ["CLOUDIANRY_URL"] = "Cloudinary URL from dashboard(remove CLOUDINARY_URL in the beginning)"

- Add a new Config Var in Heroku with the KEY CLOUDINARY_URL, and the same value(URL) 

- Tell Django to use Cloudinary to store media and static files and Update template directory:

       STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
       STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
       STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
       
       MEDIA_URL = '/media/'
       DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
       
       TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

        TEMPLATES = [
               {
                 ...,
                 'DIRS': [TEMPLATES_DIR],
                 ...,
                     ],
                   },
                 },
               ]


- Add Heroku Hostname to ALLOWED_HOSTS
  
  ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']

- Create a Profile
  
  web: gunicorn whatscooking.wsgi

- Commit and push changes to GitHub
  
- Under the deploy section of Heroku, deploy the project using GitHub

- Remove DISABLE_COLLECSTATIC = 1 from Heroku config vars, before final deployment when the the static files are ready to be collected


# Credits
* Content
  * [Font awesome](https://fontawesome.com/) provided the icon for my header, like, comment, rating and arrows
  * [w3schools](https://www.w3schools.com/) helped me in creating collapsible navbar
  * [Medium](https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c) helped me creating rating(reviews)
  * [Medium](https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318) helped me custom user model for authentication
  * [StackOverflow](www.stackoverflow.com) helped me to create multiple queryset in a view
  * [StackOverflow](www.stackoverflow.com) helped me to test using custom user model
  * [StackOverflow](www.stackoverflow.com) helped me to create custom summernote editor
  * Filter list_view for category and method were helped by the [github](https://github.com/veryacademy/YT-Django-Simple-Blog-App-Part3-SimpleCategories/blob/master/blog/views.py)
  * [ProgrammingBasic](https://www.programmingbasic.com/horizontal-scrolling-div-with-arrows) helped me to create an arrow scroll list
  * [OpenclassRooms](https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page)helped to create and sub,it 
     multiple forms on a page
  * The logo image for the website was taken from [Wix](www.wix.com)
  * I got the inspiration for the website from [pinchOfyum](https://pinchofyum.com/)
  * [w3schools](https://www.w3schools.com/), [StackOverflow](www.stackoverflow.com),  and Code Institute's walkthrough projects helped me so much throughout my project
  * Special thanks to Martin from tutor support for resolving a test error

* Media
  * The images used in the website were taken from [Pexels](https://www.pexels.com/) and [pngTree](https://pngtree.com/)
