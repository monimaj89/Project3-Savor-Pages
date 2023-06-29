![MockUp](docs/mockup.png)

This is the testing documentation for my web application Savor Pages. Full [README available here](/README.md)
See the live site [here](https://savor-pages.herokuapp.com/).
# Validation 
## HTML Validation
| **Feature**| **Expected Outcome** | **Result** | **Pass/Fails**
| :--- | :--- | :--- | :--- |
| HOME             | - | -                         | -          |
| RECIPES         | - | -                                                                                   | -           |
| ADD RECIPE         | - | -                                                                                 | -           |
| EDIT RECIPE        | - | -                                                                                 | -           |
| CATEGORY         | - | --                                                                                                | -            |
| ADD CATEGORY        | = | -                                                                        | -           |
| EDIT CATEGORY       | -s | -                                                                       | -          |
| PROFILE          | - | -                                                                           | -           |
| REGISTER         | -- |                  -                                                        |  -           |
| LOGIN | -| -                                                                                       |-           |
| ERROR             |- | -                                                                             | -      |

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
