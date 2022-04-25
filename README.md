# **[EaRRRth](#)**
EaRRRth is an environmentaly focused, community based responsive web application where users can contribute their green objectives under the applications "Reuse, Reduce, Recycle" philosophy. Through this philosophy and the function of the site, users are able to select a contribution that they've made through the UI and add a comment to describe it. The users contribution is stored in a database and shown throughout the site. The community contributions are then counted and used as statistics throughout the site to promote more users to get involved.

## Table of contents
* ### [Deployed Site](#deployed-website)
* ### [Demo](#site-demonstration)
* ### [User Stories](#site-demonstration)
* ### [UX](#user-experience)
* ### [Design](#design-features)
* ### [Features](#functional-features)
* ### [Technologies](#technologies-used)
* ### [Testing](#application-testing) - IS THIS NEEDED?
* ### [Deployment](#deploying-the-site) - IS THIS NEEDED?
* ### [Further Development](#further-development-scope)
* ### [Team](#team-credits)

## [**Deployed Website**](#)  
By clicking the hyperlinked header above, you can access the final deployed site hosted on Heroku.

## <a id="site-demonstration"> **Site Demonstration**</a>  
![An image of the site on different viewports](#) - WE NEED AN AM I RESPONSIVE IMAGE HERE, I'VE PRETTY GOOD A DOCTORING THESE SEEING AS IT DOESNT WORK FOR FULL STACK PROJECTS

## **User Stories**
Below are the user stories that needed to be fulfilled for the project to be successful from the perspective of the user and the store owner. There are 10 user stories in total broken down into three different epics:

| EaRRRth User Stories           |                           |                                                                   |                                                                        |                                               |
|--------------------------------|---------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------|-----------------------------------------------|
| ID                             | As a….                    | I want to be able to….                                            | So that I can                                                          | Must have, should have, could have, wont have |
| Registering, log in & logout   |                           |                                                                   |                                                                        |                                               |
| 1                              | User                      | register easily for an account                                    | enter information into the site that will associate with my account.   | must have                                     |
| 2                              | User                      | login to my account                                               | enter a contribution  into the site.                                   | must have                                     |
| 3                              | User                      | logout of my account                                              | so that I can keep my account safe when I am not using the app.        | must have                                     |
| User profile and entry history |                           |                                                                   |                                                                        |                                               |
| 4                              | Registered User           | view my profile                                                   | so that I can see what I have done on the site in the past.            | must have                                     |
| 5                              | Registered User           | view my previous entries                                          | so that I can see what personal impact I have had on the environment.  | must have                                     |
| 6                              | Registered User           | add a profile avatar                                              | personalise my profile                                                 | should have                                   |
| User entries                   |                           |                                                                   |                                                                        |                                               |
| 7                              | Anonymous/Registered User | submit my eco contributions                                       | contribute to the site community and track how I help the environment. | must have                                     |
| 8                              | Anonymous/Registered User | choose the category of my contribution (reuse, recycle & reduce). | accuratley submit my contribution.                                     | must have                                     |
| 9                              | Registered User           | leave a message with my contribution                              | add a personal touch and include my contribution details.              | must have                                     |
| 10                             | Registered User           | add a photo with my contribution                                  | show the site community what I have done                               | could have                                    |

## **UX / Design**

The UX design for our site was initially conceptualied using balsamiq wireframes. You can find these wireframes [here](docs/wireframes).

### **Positioning**
All of our site elements were first postitioned using Bootstrap 5. This allows us to work responsively up from mobile first design. We then fine tuned element positioning and responsivenes using custom CSS.
### **Color Palette**

We used [Coolers](https://coolors.co/) to create this neat palette for our site. Detail on the use of each color below.
![Cooler Palette](docs/color-palette/EaRRRth-Cooler-Palette.png)

**#498E61 Middle Green:** This color is used as our primary green shade, used in the navigation, matched with the hero image, the Reduce tab and column and for submit form buttons.

**#6E8E49AD Maximum Green:** This color is used for our Reuse tabs and column. It contrasts nicely with our primary green to divide our RRR columns in a visully appealing way. It is made slightly transparent to lighten its shade.

**#FDE081AD Jasmine:** This color is used for our Recycle tab, again contrasting nicely with our other shades, giving its section some individuality. It is made slightly transparent for a lighter shade. It is also used for the Sign In, Register and Contribute buttons.

**#8A7618 Spanish Bistre:** This color is used for our hero image messages. It is a nice olive shade allowing the text and items in the container to pop. It is also used for Cancel buttons.

**#EEEEEE Cultured:** This color is used as a lower contrast background color in combination with a white backgroud to give a nice highlight to certain containers and add a touch more dynamism to the site.

### **Home**
The home page contains a hero image, chosen for its clean, minimalist visual appeal and its color scheme which meshes nicely with our sites color palette. The hero image contains our welcome message to new users, acting as an invitation and briefly explaining the purpose of the site and its intended use. The message terminates with a "Contribute" button.

Beneath the hero image, there is a dynamicly designed grid of site user statistics, showing off the contributions of active users to the EaRRRth community. The grid is intended to be eye catching, utilising different cell shapes, colors and icons used draw attention and denote the particular data on display. The stats in these cells are updated, using a Django context processor, every time a user makes a contribution to the specified category.

### **Contributions**
Our contributions page starts with a hero image and message box. The message box contains data specific to the individual RRR categories, specifically their total contributions. They are also complemented with corresponding icons for easy identification.

Next are the tabs for the three RRRs, nicely contrasting each other. Clicking a tab updates the R actions available to the user in the dropdown menu beneath. The user, if they are a signed in member, can also leave a comment describing the specifics of their fulfillment of the R action they took. They can then click the "Submit" button to save to the sites database. This will update the site data for that R action and display on the home page infographic grid and the contributions page hero image message container. Alternatively, the user can clear the form using "Reset".

Signed up users who added comments to their contributions have them categoried and displayed at the bottom of the page. These are available for all users to view.

### **Sign In / Register**
These pages present similarly, with a fun hero image filling the full background. In the top right is a message box containing the user forms, asking for either registration information or sign in membership information. The user has an option to switch to the alternative form via a message link, as an alternative to using the navigation elements.


## **Features**

### - Responsive Design
### - Responsive Navigation Bar
### - Reactive User Interface
### - Anonymous Contribution Functionality
### - Membership Create and Read Functionality
### - Data Context Controls for Data Infographics
### - Membership Profile Options
### - Contribution History

## **Technologies**

### Languages Used

-   [HTML](https://en.wikipedia.org/wiki/HTML5)
-   [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Bootstrap:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
3. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome Icons was used throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
    - jQuery is used for various elements to reduce use of raw javascript code.
5. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](docs/wireframes) during the design process.
8. [Django:](https://docs.djangoproject.com/en/4.0/)
    - Django is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern. It allows a user to quickly put together full stack applications with responsive frontend design and intuative backend controls.
9. [Heroku:](https://en.wikipedia.org/wiki/Heroku)
    - Heroku is a cloud platform as a service (PaaS) supporting several programming languages. It serves as the host platform for our website.

## **References**
Our privacy policy was generated with this [link](https://app.freeprivacypolicy.com/download/5e14f11c-1d94-47f0-aa11-5e6394210b25) on [freeprivacypolicy.com](https://app.freeprivacypolicy.com/).