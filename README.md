# **[EaRRRth](#)**
EaRRRth is an environmentaly focused, community based responsive web application where users can contribute their green objectives under the applications "Reuse, Reduce, Recycle" philosiphy. Through this philosiphy and the function of the site, users are able to select a contribution that they've made through the UI and add a comment to describe it. The users contribution is stored in a database and shown throughout the site. The community contributions are then counted and used as statistics throughout the site to promote more users to get involved.

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

## **UX**

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

### **Contributions Page**


## **References**
Our privacy policy was generated using freeprivacypolicy.com with the following link: https://app.freeprivacypolicy.com/download/5e14f11c-1d94-47f0-aa11-5e6394210b25