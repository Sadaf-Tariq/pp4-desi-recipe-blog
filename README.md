# Index - Table Of Contents:

1. [General Information](#About-everything-DESI)
3. [Data](#Data)
4. [User Experience](#User-Experience)
5. [Features](#Features)
6. [Technologies Used](#Technologies-Used)
7. [Testing](#Testing)
8. [Validator Testing](#Validator-Testing)
9. [Bugs](#Bugs)
10. [Unfixed bugs](#Unfixed-Bugs)
11. [Deployment](#Deployment)
12. [Credits](#Credits)

# About everything DESI
everythingDESI is a recipe blog web application, for people who love desi food. This website provides a platform for desi food lovers to share 
their favorite food recipes, share their opinions, like, and give ratings to help others to try the best ones available.

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
Wireframes are created on [Balsamiq](https://balsamiq.cloud/)
[Home Wireframe](/README_FILES/wirefram1.png)
[Recipe list Wireframe](/README_FILES/wirefram2.png)
[Add recipe Wireframe](/README_FILES/wirefram23.png)

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

    ![Navigation Bar for unauthenticated User](/README_FILES/navbar.png)
    ![Navigation Bar for authenticated User](/README_FILES/logged-in-navbar.png)
    ![Collapsible navigation Bar ](/README_FILES/collapsible-navbar.png)


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

    ![Food Method](/README_FILES/category.png)

​* Recipes with Food Preparation Method

  * This page displays the filtered recipe with the selected preparation method

  * The page contains the recipe cards of the filtered recipes

  * The recipe card contains the recipe image, average rating, cooking time, preparation time, method, category and number of servings
 
  * These cards help users see a list and make a decision about which recipe they want to explore more

    ![Food Method](/README_FILES/method.png)

* Add recipe

  * The users who are logged in will have the opportunity to add their favorite recipe by using the 'Create New Recipe' page

  * This page has a form which enables the user to input everything they need for a good recipe
 
  * These inputs are then saved to the database and added to the list of recipes
 
  * The forms fields are title, category , method, author_name, featured_iamge, ingredients, instructions, prep_time,
    cooking_time, servings and calories
 
  * There are two buttons available to 'Add' or 'Cancel'

    ![Add Recipe](/README_FILES/add-recipe-form.png)
    ![Add Recipe button](/README_FILES/add_recipe_submit.png)

* Full Recipe

  * When the users click on the recipes cards on the home page or recipes page, the page redirects to a full recipe page
 
  * This page contains all the information of that recipe in detail
 
  * All the information from database title, category, method, author_name, featured_iamge, ingredients, instructions, prep_time,
    cooking_time, servings, and calories are displayed
    
   ![Full Recipe header](/README_FILES/full-recipe-header.png)

  * If the user is not logged in, they will not be able to like, rate, or comment

   ![Like and rate for non-logged users](/README_FILES/like-rate-com.png)

  * If the user is logged in, the options to like and rate will appear
 
    ![Like and rate for logged-in users](/README_FILES/logged-in-like-rating-comments.png)

  * The ingredients and Instruction section of the recipe is also available in detail
    
    ![Ingredients](/README_FILES/ingredients.png)![Instructions](/README_FILES/instructions.png)

  * The list of comments from the database is available for all the users but a user cannot comment if not logged in

     ![Comments not logged-in user](/README_FILES/comments.png)
     ![Comments logged-in user](/README_FILES/comments_loggedin.png)
 
* Edit Recipe

  * The users who have created their own recipes will be able to edit their own recipes

  * When the user clicks the edit button a form with prepopulated fields will appear so that a user can update the recipe
 
  *  There are two buttons available to 'Edit' or 'Cancel'

    ![Edit Recipe](/README_FILES/edit_Recipe.png)
    ![Edit Recipe](/README_FILES/submit-edit-recipe.png)

* Delete Recipe

  * The users who have created their own recipes will be able to delete their own recipes

  * When the user clicks the delete button, a confirmation message will appear to confirm the deletion process
 
  *  There are two buttons available to 'Delete' or 'Cancel'

    ![Delete REcipe](/README_FILES/delete-recipe.png)

​* Authentication
   I used the django-allauth package to implement authentication and the Custom User model. The user can sign up with an email address & password..

  * **Sign In** process is straightforward, when the user clicks on the Log In link, the page will be redirected to a form

  * The user will input an email address and password to complete the process

    ![Sign-In](/README_FILES/sign-in.png)

  * If the user is not already registered, they can opt to sign up

  * **Sign Up** process is also straightforward, when the user clicks on the Sign Up link, the page will be redirected to a form

  * The user will input an email address, password ans password(again) for confirmation and to complete the process

    ![Sign-In](/README_FILES/sign-up.png)

   * If the user decides to **Log Out**, the logout link from the nav bar lets the user to log out

   * It redirects the user to a sign put page to confirm the process

     ![Sign-Out](/README_FILES/sign-out.png)

* 404

  * A 404 page is available for the user to guide if the page requested is not available

    ![404](/README_FILES/404.png)


    
# Technologies Used

#### Languages Used

- Python: Using the Django framework and other plugins to develop the app
- HTML5
- CSS3
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


# Bugs
* When I tested my HTML code for the index.html page on html validator, I got the error that one of the div element was unclosed which was causing another section to give another error, I solved the problem by removing that div element
* Another error I found for the menu.html page, where I put an anchor element inside a button element, I solved that error by replacing the button to form 
* For the style.css for the header element in a media query, I got an error because there was a margin selector that had a negative value, I solved that error by removing that selector

# Unfixed Bugs
There is no unfixed bugs but there is a warning indicated by html validator for gallery.html page of the website, for my design I do not need any header for this section of the page that is why this warning was not entertained
![Warning Image](/images/warning.png)

# Validator Testing


# Deployment
- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - https://sadaf-tariq.github.io/pp1-everythingdesi/

# Credits
* Content
  * [Font awesome](https://fontawesome.com/) provided the icon for my header and cover text on the hero-image element
  * [w3schools](https://www.w3schools.com/) helped me in creating my form
  * [w3schools](https://www.w3schools.com/) helped me in creating my button for the menu page
  * [StackOverflow](www.stackoverflow.com) helped me to create a custom bottom border on the speciality section heading
  * [StackOverflow](www.stackoverflow.com) helped me to remove the error I was getting for an anchor element inside the button element
  * The code for the social media link for the footer was taken from Code Institute [Love Running](https://github.com/Sadaf-Tariq/love-running/blob/main/index.html) project
  * The text for the home page was taken from [Wikipedia](www.wikipedia .com) and some open-source sites
  * The logo image for the website was taken from [Wix](www.wix.com)
  * I got the inspiration for the website from Zouq restaurant, Koyla restaurant, and David Smyth Catering
  * [w3schools](https://www.w3schools.com/), [StackOverflow](www.stackoverflow.com),  and Code Institute's walkthrough project [Love Running](https://github.com/Sadaf-Tariq/love-running) helped me so much throughout my project

* Media
  * The images used in the website were taken from [Pexels](https://www.pexels.com/) and [pngTree](https://pngtree.com/)
