# Meal-Share

** Welcome to the MealShare**
---

Image here
link to Live site

MealShare is an online platform created to help get ideas for their weekly meal planning.It allows users to create an account and add recipe, view, edit and delete recipes.

# Index
- [UX/User Stories](#uxuser-stories)
- [Features](#features)
- [Design](#design)
- [Testing](#testing)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Credits](#credits)


## User Stories

<table>

  <tr>
    <th>User Story</th>
    <th>Features</th>
    <th>Bugs / Issues</th>
  </tr>

  <tr>
    <td>As a User, I can view a list of recipes and click on the recipe I want to view. </td>
    <td>All the recipes are desplayed on the recipe page.</td>
    <td>None detected</td>
    </tr>

  <tr>
    <td>As a User, I can click on the recipe so that I can read the full description.</td>
    <td>When recipe image/title is clicked, a detailed view of the recipe is displayed.</td>
    <td>None detected</td>
  </tr>

  <tr>
    <td>As a User I can view comments on the individual recipe.</td>
    <td>Give one or more comments the user can view.</td>
    <td>None detected</td>
  </tr>

  <tr>
    <td>As a User I can leave comments on the recipe.</td>
    <td>Comments need to be approved by an admin. When approved they are displayed under the recipe.</td>
    <td>None detected</td>
  </tr>

  <tr>
    <td>As a User, I can register/sign up an accout so that I can add recipe and comment on the individual recipe.</td>
    <td>Given username and password a user can sigup to accout and log in.When logged in they can comment. </td>
    <td>None detected</td>
  </tr>
  
  <tr>
    <td>As a user/admin, I can login so that I can access all the available content.</td>
    <td>User/admin can logout successfully.</td>
    <td></td>
  </tr>

  <tr>
    <td>As a Admin, I can create draft recipe so that I can finish later, prior to publishing</td>
    <td>I can save draft and finish the content at a later time.</td>
    <td></td>
  </tr>

  <tr>
    <td>As a Admin I can approve/disapprove comments in order to filter out objectionable comments.</td>
    <td>I can approve or un-approve a comment.</td>
    <td></td>
  </tr>

  <tr>
    <td>As a User I can create a meal plan for a week so that I can organize my meals ahead of time.</td>
    <td>I can access a form to fill in, that includes fields:meal names and days of the week </td>
    <td>Feature for future iteration.</td>
  </tr>

  <tr>
    <td>As a User I can generate a shopping list based on my meal plan so that I can purchese all the necessary ingredients.</td>
    <td>I can access shopping with all ingredients for the whole weeks meals.</td>
    <td>Feature for future iteration.</td>
  </tr>

  <tr>
    <td></td>
    <td></td>
    <td>Feature for future iterations</td>
  </tr>

  </table>

<br>

<br>
 
## Features

- Home Page
The home page displays the carousel with images and highlights of what is the page about.
In the future, it will display the latest recipes and a link(view) to the weekly meal planner.
![home page](static/images/image%20(1).png)

- Navigation Bar
Template from Bootstrap 
(Fully responsive)

- Footer
Simple footer with social links

- Sign Up
The site has a user sign-up facility to add, edit, and delete recipes.
![alt text](image.jpg)

- Sign In
After creating accound user can sign in to be able to make changes to their recipes.
![alt text](image.jpg)

- Sign Out
The site allows user to sign out of their account
![alt text](image.jpg)

- Admin
This site has standard Django admin interface
![alt text](image.jpg)

- ERD
The following Entity Relationship Diagram data structure was created:
![alt text](image.jpg)


# Design

## Design Choices
 **Colors**: Soft green for a fresh, healthy feel.
-Background:
-Text color
-Buttons
-Nav bar links
-Additional background:

![Color pallet](static/images/color%20palet.png)

 **Typography**: 
Google Fonts:
-Oxygen(body text)
-Karla(headings)


- **Layout**: Mobile-first design for a responsive experience.
## Wireframes
- Homepage wireframe showing recipe cards and a search bar.
- Recipe detail page with ingredients, preparation steps, and images.

###Home Page Wireframe Design
![Home page](static/images/home_page.png)

###Recipe List/Detail Page Wireframe Design
![Home page](static/images/list_recipes.png)
![Home page](static/images/recipe.png)

###Login Page Wireframe Design
![Home page](static/images/log_in.png)

# Testing

## Manual Testing

<table>

  <tr>
    <th>Test</th>
    <th>PASS/FAIL</th>
  </tr>

  <tr>
    <td>Click Home page</td>
    <td></td>
  </tr>

  <tr>
    <td>Click Recipe page</td>
    <td></td>
  </tr>

  <tr>
    <td>Click Add(recipe) page</td>
    <td></td>
  </tr>

  <tr>
    <td>Click Login page</td>
    <td></td>
  </tr>

  <tr>
    <td>Click Logout page</td>
    <td></td>
  </tr>

  <tr>
    <td>Create profile</td>
    <td></td>
  </tr>

  <tr>
    <td>Leave a comment</td>
    <td></td>
  </tr>

  <tr>
    <td>See recipe details</td>
    <td></td>
  </tr>

  <tr>
    <td>Add new recipe</td>
    <td></td>
  </tr>

  <tr>
    <td>Edit recipe</td>
    <td></td>
  </tr>

  <tr>
    <td>Delete recipe</td>
    <td></td>
  </tr>

  <tr>
    <td>Searching recipes</td>
    <td>Fail</td>
  </tr>

  <tr>
    <td>Manage recipes(Admin)</td>
    <td></td>
  </tr>

  <tr>
    <td>Approve comments(Admin)</td>
    <td></td>
  </tr>

  <tr>
    <td>Generate a shopping list</td>
    <td>Fail</td>
  </tr>

  <tr>
    <td>Add recipes to meal plan</td>
    <td>Fail</td>
  </tr>

  <tr>
    <td>Create meal plan</td>
    <td>Fail</td>
  </tr>

  <tr>
    <td>Rate recipes</td>
    <td>Fail</td>
  </tr>

</table>



## AI Tools Usage

### DALL-E
Describe how DALL-E was used for image generation, including examples of successes and challenges.  
**Guidance:** Specifically mention how you used DALL-E for image generation and the impact this had on your design process.

# Features
- **Recipe Details**: Each recipe has a detailed page with ingredients and instructions
- **User Authentication**: Users can sign up, log in, and save their favorite recipes.
- **Rating System**: Users can rate recipes and leave reviews.


### Core Features (Must-Haves)
- **Feature 1:** Description of the implemented feature.
- **Feature 2:** Description of the implemented feature.

(Include all must-have features)  
**Guidance:** Use this section as you complete Phase 2: Must User Stories Implementation & Testing. Document all the must-have features you implemented, explaining how they align with the user stories and acceptance criteria.

### Advanced Features (Should-Haves)
- **Feature 1:** Description of the implemented feature.
- **Feature 2:** Description of the implemented feature.

(Include all should-have features)  
**Guidance:** Include any advanced features you implemented during Phase 3: Should User Stories Implementation & Any Advanced Features. Explain how these features enhance user experience and their alignment with the acceptance criteria.

### Optional Features (Could-Haves)
- **Feature 1:** Description of the implemented feature (if any).
- **Feature 2:** Description of the implemented feature (if any).

(Include any could-have features that were implemented or considered)  
**Guidance:** If any could-have features were implemented, describe them here. This is an opportunity to showcase extra work done beyond the initial scope. But remember - keep it simple! Focus on the Must stories first. Could user story features are commonly earmarked for future project iterations.

## AI Tools Usage

### GitHub Copilot
Describe how GitHub Copilot assisted in coding, including any challenges or adjustments needed.  
**Guidance:** Reflect on how GitHub Copilot assisted in coding, particularly any challenges or adjustments that were needed to align with project goals.

# Testing
## Unit Testing
- All major functions, such as search, authentication, and rating, were unit tested.

## User Testing
- Conducted with a small group of users to identify pain points in navigation and search functionality.

## Bug Fixes
- Fixed an issue where the recipe image wouldn’t load if it wasn’t set.




# Deployment
## Steps to Deploy

### Deployment Process
Briefly describe the deployment process to GitHub Pages or another cloud platform.  
Mention any specific challenges encountered during deployment.  
**Guidance:** Describe the steps you took to deploy your website during Phase 4: Final Testing, Debugging & Deployment, including any challenges encountered.

## AI Tools Usage

### Reflection
Describe the role AI tools played in the deployment process, including any benefits or challenges.  
**Guidance:** Reflect on how AI tools assisted with the deployment process, particularly how they streamlined any tasks or presented challenges.

## Reflection on Development Process

### Successes
Effective use of AI tools, including GitHub Copilot and DALL-E, and how they contributed to the development process.

### Challenges
Describe any challenges faced when integrating AI-generated content and how they were addressed.

### Final Thoughts
Provide any additional insights gained during the project and thoughts on the overall process.  
**Guidance:** Begin drafting reflections during Phase 1 and update throughout the project. Finalize this section after Phase 4. Highlight successes and challenges, particularly regarding the use of AI tools, and provide overall insights into the project.

## Code Attribution
Properly attribute any external code sources used in the project (excluding GitHub Copilot-generated code).  
**Guidance:** Document any external code sources used throughout the entire project, especially during Phase 2 and Phase 3. Exclude GitHub Copilot-generated code from attribution.

# Credits
- **Developers**:
- **Icons**: favicon
- **Resources**: Recipe API from [Spoonacular](https://spoonacular.com).

## Future Improvements
Briefly discuss potential future improvements or features that could be added to the project.  
**Guidance:** Reflect on potential enhancements that could be made to the project after Phase 4: Final Testing, Debugging & Deployment. These could be Could user story features you didn’t have time to implement or improvements based on testing feedback.