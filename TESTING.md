# Index - Table Of Contents:

1. [Validator Testing](#Validator-Testing)
3. [Lighthouse Testing](#Lighthouse-Testing)
4. [Responsiveness and Browser Compatibility](#Responsiveness-and-Browser-Compatibility)
5. [Automated Testing](#Automated-Testing)
6. [Manual Testing](#Manual-Testing)


# Validator Testing

### HTML
I used [W3 validator](https://validator.w3.org/)

- Home page
  ![html homepage validator](/README_FILES/htmlvalidatorr.png)

- All recipes page
  ![html all recipes page validator](/README_FILES/htmlvalidatorr.png)

- Category page
  ![html category page validator](/README_FILES/htmlvalidatorr.png)

- Method page
  ![html method page validator](/README_FILES/htmlvalidatorr.png)

- Full recipe page
  ![html full recipe page validator](/README_FILES/htmlvalidatorr.png)

- Login page
  ![html login page validator](/README_FILES/htmlvalidatorr.png)

- Sign UP page
  ![html sign up page validator](/README_FILES/htmlvalidatorr.png)

- Sign Out page
  ![html sign out page validator](/README_FILES/htmlvalidatorr.png)

- 404
  ![html 404 validator](/README_FILES/htmlvalidatorr.png)

- Delete recipe page
  ![html delete recipe page validator](/README_FILES/htmlvalidatorr.png)

- Create new recipe page/Update new recipe page
   - Errors were showing for crispy form fields/summernote editor, the code was not written by me but built-in crispy form codes
 
### CSS

I used [W3C CSS validator](https://jigsaw.w3.org/css-validator/) for CSS code validation

- style.css file
  
  ![Css code](/README_FILES/cssvalidator.png)

### JavaScript

I used [JSHint validator](https://jshint.com/) for javacript code validation

- scroll.js file

<img src="/README_FILES/jshint.png" alt="jshint" width="400" height="150" />

   - There are no errors, but warning for unused variables, these variables are being used in the corresponding templates

### Python

I used [CI Python Linter](https://pep8ci.herokuapp.com/) for python code validation

- recipeblog App
  
- recipeblog/views.py

![python validator](/README_FILES/CLpython.png)

- recipeblog/forms.py

![python validator](/README_FILES/CLpython.png)

-recipeblog/urls.py 

![python validator](/README_FILES/CLpython.png)

-recipeblog/admin.py 

![python validator](/README_FILES/CLpython.png)

- recipeblog/test_views.py

![python validator](/README_FILES/CLpython.png)

- recipeblog/test_forms.py

![python validator](/README_FILES/CLpython.png)

-recipeblog/test_models.py 

![python validator](/README_FILES/CLpython.png)

- recipeblog/models.py

![python validator](/README_FILES/recipeblog-models.py.png)

  - These are lines too long errors in models.py, if the lines are broken the codes is not working that is it is left as it is.

- users App

- users/models.py
  
![python validator](/README_FILES/CLpython.png)

- users/models.py
  
![python validator](/README_FILES/CLpython.png)

- users/admin.py
  
![python validator](/README_FILES/CLpython.png)

- users/tests.py
  
![python validator](/README_FILES/CLpython.png)

# Lighthouse Testing

- Home page

  <img src="/README_FILES/lighthouse.png" alt="Lighthouse home page" width="500" height="150" />

- All recipes page

  <img src="/README_FILES/lighthouserecipes.png" alt="Lighthouse all recipe page" width="500" height="150" />

- Method page

  <img src="/README_FILES/lighthousemethod.png" alt="Lighthouse method page" width="500" height="150" />

- Full recipe page

  <img src="/README_FILES/lighthousefullrecipe.png" alt="Lighthouse full recipe page" width="500" height="150" />

- Add recipe page

  <img src="/README_FILES/lighthouseaddrecipe.png" alt="Lighthouse add recipe page" width="500" height="150" />

- Update recipe page

  <img src="/README_FILES/lighthouseupdaterecipe.png" alt="Lighthouse update page" width="500" height="150" />

- Delete recipe page

  <img src="/README_FILES/lighthousedelete.png" alt="Lighthouse delete page" width="500" height="150" />

- SignUp page

  <img src="/README_FILES/lighthousesignup.png" alt="Lighthouse sign up page" width="500" height="150" />

- SignIn page

  <img src="/README_FILES/lighthousesignup.png" alt="Lighthouse sign in page" width="500" height="150" />
  
- SignOut page

  <img src="/README_FILES/lighthousesignout.png" alt="Lighthouse sign out page" width="500" height="150" />


# Responsiveness and Browser Compatibility

- I have tested the website on various browsers including Google Chrome, Microsoft Edge, Safari, and Mozilla Firefox
   - The website is working as expected in all browsers, all the pages are responsive and behaving as expected
      on all screen sizes.
     
# Aotumated Testing

- users app testing

  - The test code for [users/tests.py](https://github.com/Sadaf-Tariq/pp4-desi-recipe-blog/blob/main/users/tests.py) can be found here

    <img src="/README_FILES/users.tests.png" alt="user app tests.py file" width="500" height="130" />

- recipeblog app testing

  - The test code for [recipeblog/test_views.py](https://github.com/Sadaf-Tariq/pp4-desi-recipe-blog/blob/main/recipeblog/test_views.py) can be found here

    <img src="/README_FILES/recipeblog-testviews.png" alt="user app tests.py file" width="500" height="130" />

  - The test code for [recipeblog/test_forms.py](https://github.com/Sadaf-Tariq/pp4-desi-recipe-blog/blob/main/recipeblog/test_forms.py) can be found here

    <img src="/README_FILES/recipeblog-testforms.png" alt="user app tests.py file" width="500" height="130" />

  - The test code for [recipeblog/test_models.py](https://github.com/Sadaf-Tariq/pp4-desi-recipe-blog/blob/main/recipeblog/test_models.py) can be found here

    <img src="/README_FILES/recipeblog-testmodels.png" alt="user app tests.py file" width="500" height="130" />

# Manual Testing


  |Feature|Action|Expected Result|Result|
  |-------|------|---------------|------|
  |Logo|When the user clicks on logo|the logo redirects to home page|Pass|
  |Header text|When the user clicks on header text|The text redirects to home page|Pass|
  |Navbar links|when the user click on any link|The link redirects to corresponding pages|Pass|
  |Recipe Cards|When the user hover on recipe card|The card changes its color to be prominent|Pass|
  |Recipe Cards|When the user click on a recipe card|The card redirects to the corresponding full recipe page|Pass|
  |Food Category Cards|When the user hover on recipe card|The card changes its color to be prominent|Pass|
  |Food Category Cards|Whe the user click on a recipe card|The card redirects to the corresponding recipe category page|Pass|
  |Food Method Cards|When the user hover on recipe card|The card changes its color to be prominent|Pass|
  |Food Method Cards|Whe the user click on a recipe card|The card redirects to the corresponding recipe method page|Pass|
  |All recipe page recipe Cards|When the user hover on recipe card|The card changes its color to be prominent|Pass|
  |All recipe page recipe Cards|Whe the user click on a recipe card|The card redirects to the corresponding recipe method page|Pass|
  |Create recipe page for logged-in user|When the user tries to add a recipe|The page should display a form to add a recipe with add/cancel button|Pass|
  |Recipe submission|When the user submits a recipe|A success message should be displayed and the added recipe should be visible on home/allrecipes page|Pass|
  |Add recipe cancel button|When the user clicks cancel button|The recipe should not be added and redirects to add recipe page|Pass|
  |Update recipe page for recipe authors|When the author tries to update a recipe|The page should display a form with prepopulated fields to update a recipe with update/cancel button|Pass|
  |Updated recipe submission|When the user submits an updated recipe|A success message should be displayed and the added recipe should be visible on home/allrecipes page|Pass|
  |Update recipe cancel button|When the user clicks cancel button|The recipe should not be updated and redirects to home page|Pass|
  |Delete recipe page for author|When the author tries to delete a recipe|The page should display a page to delete a recipe and delete/cancel button|Pass|
  |Recipedeletion|When the author deletes a recipe|A success message should be displayed and the deleted recipe should not be visible on home/allrecipes page|Pass|
  |Delete recipe cancel button|When the user clicks cancel button|The recipe should not be deleted and redirects to the home page|Pass|
  |Log In|When a user clicks on log in link|A form with email and password should be displayed|Pass|
  |Log In|When a user clicks on log in link|A success message should be displayed to the user|Pass|
  |Sign Up|When a user clicks on Sign Up link|A form with email and password and password(again) should be displayed|Pass|
  |Sign Up|When a user clicks on Sign Up link|A success message should be displayed to the user|Pass|
  |Log Out|When a user clicks on log out link|A confirmation page should be displayed|Pass|
  |Log Out|When a user clicks on log out link|A success message should be displayed to the user|Pass|

  - Success messages

    <img src="/README_FILES/delete_message.png" alt="delete success message" width="" height="" />
    
    <img src="/README_FILES/add_message.png" alt="add recipe success message" width="" height="" />

    <img src="/README_FILES/update_message.png" alt="update success message" width="" height="" />

    <img src="/README_FILES/sign-in.png" alt="sign in success message" width="" height="" />

    <img src="/README_FILES/sign-out.png" alt="sign out success message" width="" height="" />

    

  
  
  






