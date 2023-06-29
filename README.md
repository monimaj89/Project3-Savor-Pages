# Savor Pages

## Welcome
Savor Pages is a user friendly website for a food lovers, where you can easily add you recipe, share it with other, edit or delete it. See the live site [here](https://savor-pages.herokuapp.com/).

Mockup image

## Table content

## Project Overwiev
Savor Pages is a recipe sharing and management Application built using Python, Flask+SQLAlchemy, Materialize, Jinja2 and Java Script jQuery. It uses Cloudinary API to manage user-uploaded images.

User Authentication is handled using relational database (PostgreSQL using Flask+SQLAlchemy).
Standard CRUD data manipulation is handled using a relational database Flask+PyMongo.
Savor Pages is my third milestone project for Code Institute's Level 5 Diploma in Web Application Development.

As a lfood lover, but not necessarily cooking chef, the choice of this project was quite an easy decision. A site where everyone can share their ideas for recipes along with ingredients and preparations steps seems to be the perfect idea for someone who loves to eat and is not necessarily a chef, like me.


# User Experience
## Project Goals
* To develop a site where users can easily find food recipes.
* Guest users will be able to view and look through recipes, even without having their own account.
* Registered users will also be able to share and manage their own recipes.
* Use Mobile First design principle in building a responsive site.
* Present the available information in a user friendly way.
* Provide users the option to register and create an account.
* Provide registered users access to a full CRUD functionality.
* Provide all registered users access to a custom user dashboard with read functionality.
* Include defensive programming to enable users to make an informed decision when deleting recipes.
* Handle any errors to help the users understand the issue.
## User stories
### First time User
* Immediately understand the main purpose and use of the site and how to use it.
* Look through all recipes.
* Register/ create a user account.
### Registered User
* Learn more about what I can do on the Savor Pages site.
* Add, edit, retrieve and delete my own recipes.
* Add my own recipes, based on categories.
* Upload an image with my recipes.
* Be able to add additional information about my recipe.
* Have access to tools I may need in order to add, update or delete my recipes.
* Be warned of the consequences of deleting a recipe.
* Have my own member user dashboard (read functionality).
### Admin Goals
* Have the ability to maintain the recipes, in particular the categories
* Add, edit and delete my own recipes
* Add, edit, and delete any recipe by category
## Scope
### Feature Ideas Planning
When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

| # | Feature | Importance | Difficulty |
| --- | --- | --- | --- |
| 1 | View, create, edit and delete recipes | 5 | 5 |
| 2 | View, create, edit and delete images with recipes | 5 | 5 |
| 3 | View, create, edit and delete recipe's category | 5 | 5 |
| 4 | Create, edit and delete account | 5 | 3 |
| 5 | Login and logout to account | 5 | 5 |
| 6 | Moderate content submitted by registered users | 5 | 1 |
| 7 | Send message and/ or feedback to Admin | 5 | 2 |
| 8 | Receive Notifications on users activities | 2 | 2 |
| 9 | Search for Recipes | 5 | 5 |
| 10 | Search Recipes by Ingredients | 3 | 1 |
| 11 | Search Recipes by Category | 5 | 2 |
| 12 | Share Recipes on Social Media | 3 | 3 |
| 13 | Display Suggested Recipes | 3 | 2 |
| 14 | Access to Custom User Dashboard (Read Functionality) | 4 | 5 |
| 15 | User Action Validation | 5 | 5 |

Based on the results of the Feature Ideas Planning, I have decided to attempt to implement features numbers 1, 2, 3, 5, 14 and 15 for this production release and postpone the remaining features due to time limitations.

### Functionality Requirements
* Clean and themed presentation of recipe details.
* Intuitive site navigation.
* Fresh-looking, appetising and themed use of images across the site.
* Full CRUD functionality.
* Use of Defensive Programming to safeguard logged in users againts any unintended result of their actions.
* Solid error handling provide information as well as a much better user experience for any user who may encounter errors when using the site.

## Structure Plan
The yellow elements in these diagrams illustrate the pages that are always accessible from the navbar for all visitors.
The grey elements in these diagrams are the pages not accessible to a particular user.
The view recipes function is available to all visitors.
The add, edit and delete elements are only available to logged in users. The delete functions will return to:
 * A registered user deleting his own recipe will return to a recipe page.
 * An admin deleting the category associated with the recipe will return to a category page.
### Guest user
![Guest user journey across the site](docs/quest.png)
### Registered User
![Registered user's journey across the site](docs/register.png)
### Admin user
![Admin user's permission and journey across the site](docs/admin.png)
## Skeleton
### Wireframes
* [DESKTOP - Index page](docs/wireframes/dhome.png)
* [DESKTOP - Recipe page](docs/wireframes/dhome.png)
* [DESKTOP - Category page](docs/wireframes/dhome.png)
* [DESKTOP - Add recipe page](docs/wireframes/dhome.png)
* [DESKTOP - Edit recipe page](docs/wireframes/dhome.png)
* [DESKTOP - Edit category page](docs/wireframes/dhome.png)
* [TABLET - Index page](docs/wireframes/dhome.png)
* [TABLET - Recipe page](docs/wireframes/dhome.png)
* [TABLET - Category page](docs/wireframes/dhome.png)
* [MOBILE - Index page](docs/wireframes/dhome.png)
* [MOBILE - Recipe page](docs/wireframes/dhome.png)
* [MOBILE - Category page](docs/wireframes/dhome.png)
# Design
[Materialize](https://materializecss.com/) was used and customised for the front-end development.
## Colour
The colors used on my website are white, gray and yellow, the background color is usually white and gray, so to brighten up the look of the page, I decided to add yellow details for headings, and buttons border.
![Colour Palette](docs/palette.png)
## Typography
Fonts was imported from [Google Fonts](https://fonts.google.com/)
* Rock Salt font has been used for heading across the page.
![Rock salt](docs/rocksalt.png)
* Sora has been used as a main body font.
![Sora](docs/sora.png)
* Sans serif is set as a backup if any of the fonts fail to load.
## Images and icons
* Main hero image has been borrowed from Pixabay from [Pexel](https://www.pexels.com/)
![Hero image](savorpages/static/images/hero.webp)
* Page logo has been created by myself using [Canva](https://www.canva.com/)
* On desktop screen logo is clickable and redirect to a home page.
![Logo](docs/logo1.webp)
* Every image used for a recipe has been provided from [Pexel](https://www.pexels.com/)
* Icons used across the page has been provided from [Font Awesome](https://fontawesome.com/)
# Features
## Favicon 
* As a favicon I wanted to use my own page logo, but it was barely visible, so I decides to use one of the Favicon Emoji from [Favicon](https://favicon.io/).

![Avocado](docs/avocado.png)
## Multi Page Element
### Navbar
![Navbar](docs/navbar.png)

A Navbar displays on every page, contains:
* Logo
* Home
* Recipes
* Account

### Footer
* Page name
* Page Author
* Current year

![Footer](docs/footer.png)

### Home/Index page
* Link for recipes
* Link to create an account

### Recipe page
* Look through recipes added by other users
* Add recipe button only for logged users

![Recipe page](docs/recipe.png)

### An account
* Register page - with the link to login page for already registered users
![Register form](docs/registerform.png)

* Login page - with the link to register page for user without an account
![Login](docs/login.png
)
## For Registered Users
### Profile page
* All information needed to move around the page
* Recipes added by user
![Profile](docs/profile.png)

### Add recipe page
* A form contains:
    * Category
    * Recipe name
    * Recipe description
    * Ingredients
    * Preparation
    * Cook Time
    * Image
![Add recipe](docs/addrecipe.png)

### Edit a recipe
* Allows the user edit his own recipe (excluding an image, which will be added in the future)
![Edit recipe](docs/edit.png)

### Delete a recipe
* Allows the user delete his own recipe supported by the defensive function against deleting by the mistake.
![Delete recipe](docs/delete.png)

### Log out 
* Log out the user and return to login page

## For Admin user only
### Manage categories
* Add a category
* Edit a category 
* Delete a category, which also delete all recipes associated with this category
![Category](docs/category.png)

## Error page
![Error page](docs/error.png)
* 404 Error - Page not found 
* 400 Error - Bad Request
* 500 Error - Internal Server error

## CRUD Table
This shows what CRUD functionality is available from each page
| Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| Home |  | read intro about the app |  |  |
| Recipes |  | look through recipes | edit and update recipe (requires log in & only if owner of the recipe) | delete recipe (requires log in) & only if owner of the recipe |
| Add recipe | choose a category, create a new recipe, upload an image |  |  |  |
| Register | user profile |  |  |  |
| Login |  | username for password check |   |  |  |
| Edit recipe |  | all information about the recipe and image | all information about the recipe |  |
| Categories, only for admin user | categories | all available categories | all available categories | all available categories plus all recipes associated with the deleted category |
| Profile |  | user dashboard, custom information for registered users, view all available recipes shared by the logged in user | edit own recipe functionality available to logged in users from their dashboard | delete own recipe functionality available to logged in users from their dashboard |
## Future Features
I would like to expand the project in the future with following features:
* Allow user delete his own account
* Edit the image along with recipe
* Voting functionality for user's favourite recipe
* Recipe search functionality  
* Add page animation for better UX when viewing the site
# Technologies used
* Language
    * HTML5 - for content and structure of the site
    * CSS3 - for styling the site
    * Vanilla JavaScript - to get current year for the footer
    * jQuery 
        * Mobile side nav
        * Navbar collapsible
        * Navbar dropdown
        * Floating action button
        * Modal pop up window
        * Form dropdown select
    * Python - for the core of the backend of the site 
        * Python Modules Used:
            * blinker==1.6.2
            * click==8.1.3
            * cloudinary==1.33.0
            * Flask==2.3.2
            * Flask-SQLAlchemy==2.5.1
            * greenlet==2.0.2
            * gunicorn==20.1.0
            * importlib-metadata==6.6.0
            * itsdangerous==2.1.2
            * Jinja2==3.1.2
            * MarkupSafe==2.1.2
            * psycopg2==2.9.6
            * SQLAlchemy==1.4.46
            * urllib3==1.26.16
            * Werkzeug==2.3.4
            * zipp==3.15.0
* Tools 
    * [GitHub](https://github.com/) - used to host the site
    * [Git](https://git-scm.com/) -  used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.
    * [Heroku](https://id.heroku.com/login) - used to deploy the site
    * [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) was used for debugging and testing with Lighthouse
    * [Materialize](https://materializecss.com/) - used for the styling as well as the responsivness of the site
    * [Cloudinary API](https://cloudinary.com/) - used to enable user add his own image to the recipe
    * [Balsamiq](https://balsamiq.com/wireframes/) - used to create a wireframes for this project
    * [Goolge Fonts](https://fonts.google.com/) - Used to select and import font for the project (Rock Salt & Sora)
    * [Font Awesome](https://fontawesome.com/) - used for icons across the site
    * [Favicon](https://favicon.io/) - used for a browser tab icon
    * [Canva](https://www.canva.com/) - used to create a page logo
    * [Convertio](https://convertio.co/) - used to convert images into webp
    * [Lucid Chart](https://www.lucidchart.com/) - used to create a structure diagram for REDAME
    * [MockUp Generator](https://techsini.com/multi-mockup/) - used to create mockup image

# Testing
## All testing undertaken for this project can be found in the [Testing documentation](/TESTING.md)

# Bugs

# Deployment

# Credits


