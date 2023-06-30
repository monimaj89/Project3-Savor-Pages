![MockUp](docs/mockup.png)

This is the testing documentation for my web application Savor Pages. Full [README available here](/README.md)
See the live site [here](https://savor-pages.herokuapp.com/).
# Validation 
## HTML Validation
The initial test of the page validated by URL using [W3C HTML Validator](https://validator.w3.org/#validate_by_uri) showed two errors:
* Empty id and class attribuite for an "ul" element - which was unnecessary and has been deleted.
* Stray "ul" and "li" element - were misplaced in the code and were fixed

And two warnings:
* Section lacks heading - which has been change to a div element withouth any changes to page layout
* The "type" attribute unnecessary for JavaScript resources - which concerned my jquery script from materialize and has been deleted

Every other page was run through the HTML validator using source code, and all pages passed, except as desribes by the pages below
* [Home](docs/htmlhome.png)
* [Recipes](docs/htmlrecipes.png)
* [Add Recipe](docs/htmladdrecipe.png) - 1 error - fix - added an alt attribute to the image
* [Edit Recipe](docs/htmleditrecipe.png)
* [Category](docs/htmlcategory.png)
* [Add Category](docs/htmladdcategory.png)
* [Edit Category](docs/htmleditcategory.png)
* [Profile](docs/.png) - 1 error - fix - added an alt attribute to the image
* [Register](docs/htmlregister.png)
* [Login](docs/htmllogin.png)
* [Error](docs/htmlerror.png)

## CSS Validation
I run the CSS code through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) and showed no errors
* [CSS Validation result](docs/cssvalidate.png)
* [CSS Validation warnings](docs/csswarning.png) - Added quotation marks to font names

## JavaScript Linting
I ran the JavaScript code through [JSHint](https://jshint.com/), which showed no errors or warnings
* [JavaScript test result](docs/jshint.png)

## Python Linting
I ran the code through [CI Python Liner](https://pep8ci.herokuapp.com/), which showed one error:
* [Line 189: E117 over-indented](docs/python.png) - I am aware of that error since I build the Login functionality, unfortunatelly I couldn't find any solution for that, I've tried to different approach with indentation, and also search for help online, but as long as code is working I've decided leave it like that

# Manual Testing
| **Test**| **Goal** | **Result** |
| :--- | :--- | :--- |
| savorpages logo renders across all possible device | Logo displays on the top left side of the navbar on desktop, and on tablet, and mobile logo is hidden in the sidenav menu  | Pass |
| Clickable logo | On desktop logo is clickable and redirect to the home page | Pass
| Responsiveness | Site to be responsive across all device | Pass |
| Flash Messages | Messages successfully display with relevant information for user  | Pass |
| Choose Category from dropdown | Categories should be available to choose from | Pass |
| Main Navlinks | Navlinks to work and not hiding a 500 internal server error | Pass |
| Category ID | This gets stored as category_id and display for every recipe added | Pass |
| Associated Recipes | These get deleted when a category relevant to them is deleted by admin | Pass |
| Modal is semantically correct | All HTML Validation to Pass and modal works with out causing a 500 Internal Server Error | Pass |
