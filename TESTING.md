# Index - Table Of Contents:

1. [Validator Testing](#Validator-Testing)
3. [Lighthouse Testing](#Lighthouse-Testing)
4. [Responsiveness and Browser Compatibility](#Responsiveness-and-Browser-Compatibility)
5. [Automated Testing](#Automated-Testing)
6. [Manual Testing](#Manual-Testing)
7. [Fixed Bugs](#Fixed-Bugs)
8. [Known Bugs](#Knows-Bugs)


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

  <img src="/README_FILES/lighthouse.png" alt="Lighthouse home page" width="400" height="150" />

- All recipes page

  <img src="/README_FILES/lighthouserecipes.png" alt="Lighthouse all recipe page" width="400" height="150" />

- Method page

  <img src="/README_FILES/lighthousemethod.png" alt="Lighthouse method page" width="400" height="150" />

- Full recipe page

  <img src="/README_FILES/lighthousefullrecipe.png" alt="Lighthouse full recipe page" width="400" height="150" />

- Add recipe page

  <img src="/README_FILES/lighthouseaddrecipe.png" alt="Lighthouse add recipe page" width="400" height="150" />

- Update recipe page

  <img src="/README_FILES/lighthouseupdaterecipe.png" alt="Lighthouse update page" width="400" height="150" />

- Delete recipe page

  <img src="/README_FILES/lighthousedelete.png" alt="Lighthouse delete page" width="400" height="150" />

- SignUp page

  <img src="/README_FILES/lighthousesignup.png" alt="Lighthouse sign up page" width="400" height="150" />

- SignIn page

  <img src="/README_FILES/lighthousesignup.png" alt="Lighthouse sign in page" width="400" height="150" />
  
- SignOut page

  <img src="/README_FILES/lighthousesignout.png" alt="Lighthouse sign out page" width="400" height="150" />



# Responsiveness and Browser Compatibility

- I have tested the website on various browsers including Google Chrome, Microsoft Edge, Safari, and Mozilla Firefox
   - The website is working as expected in all browsers, all the pages are responsive and behaving as expected
      on all screen sizes.









