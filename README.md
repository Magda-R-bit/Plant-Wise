# **Plant-Wise**

[Project live link](https://plant-wise-97799c6a3824.herokuapp.com/)


![Screenshot of Main Page](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/home.png)

 **Plant Wise** is an eCommerce web application built for plant lovers who want a smooth and intuitive online shopping experience. Whether you're a seasoned gardener or just starting your indoor jungle, Plant Wise makes discovering, purchasing, and managing plant products simple and enjoyable.
  
 This website is designed for organic vegetables and herbs enthusiasts. Whether you're growing basil on a windowsill or planning a full backyard garden, this site supports your passion for fresh, healthy food.
 Especially those interested in natural pest control, companion planting, and sustainable growing methods using flowers and herbs to protect crops.

 The platform features dynamic product listings, seasonal deals (including Buy One Get One Free and discounts), secure checkout, and user account management – all designed with both user experience and business functionality in mind.



## Contents

* [UI/UX](#uiux) 
* [Features](#features)
* [Design](#design)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## UI/UX

### User Interface (UI) and Experience (UX)

 ### Agile

  Plant Wise was built using **Agile** approach, allowing me to stay flexible and deliver features in incremental steps. I followed Agile principles to manage tasks and ensure continuous improvement throughout development.

  To keep track of tasks and progress, I used a **Kanban board** to visually organize work, monitor the flow of tasks, and ensure that each feature was delivered efficiently.

  I created [GitHub Project](https://github.com/users/Magda-R-bit/projects/6) to help me manage tasks by moving them trough various stages from To Do, to In Progress, and finally to Done. 
  
  The **Kanban board** was split into two distinct views to improve clarity and collaboration:

   1. User Stories View
   * Focused on high level features and functionality from the end user perspective.

  ![Kanban Board User Story](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/UserStory.png)

   2. Developer Tasks View
   * Broke down each user story into smaller, actionable development tasks. This helped in maintaining a clear separation between business objectives and technical implementation, while supporting better planning and prioritization.

  ![Kanban Board Developer](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Developer.png)

  #### Issues

  ![Issue](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Issues.png)


### Wireframes

- [Figma](https://www.figma.com/) (Used to create Wireframes)

![Screenshot of Wireframes Shop](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Wireframe.png)

### ERD Diagram

- [Graphviz](https://graphviz.gitlab.io/download/) (ERD Generated using django-extensions and Graphviz to visualize the relationships between the models and improve the understanding of the database structure)

[ERD Diagram](erd.png)

### Design

#### Colour:

The primary colours chosen for this website are green: #198754 and #2d6a4f, for its association with nature, healthy green vegetables.

Green is often associated with relaxation and harmony, which aligns perfectly with the theme of wellness and healthy organic food.


![Buttons](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/198754.png)
![Buttons](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/2d6a4f.png)

The navbar and Footer uses Bootstrap's `bg-light` class, which applies a soft light-gray background (`#f8f9fa`) for a clean and minimalistic look.

![Navbar](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Navbar.png)


##  SEO & Marketing

For SEO & Marketing research please refer to [SEO and Marketing](MARKETING.md)

## Features


### Existing Features

- User authentication with Django Allauth (signup, login, logout).
- Responsive UI with Bootstrap 5.
- **CRUD** Functionality:
  - Tips and Guides – Users can create, view, update their tips. Admin can add or delete the guides.
  - Shop – Admins can manage products in the shop.
  - Wish List – Users can add, edit, and delete items from the Wish List.
  - Cart - adding, removing products, and updating cart. 


#### **Navigation**
- Responsive Navbar with burger dropdown manu
- Navigation options depend on user authentication

![Navbar](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FNavbar.png)
![Burger](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FBurger.png)

#### **Footer**

- Responsive Footer with social media links and address

![Footer Full](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FFooter.png)
![Footer](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FFmob.png)



####  **Home Page**

User can go to the shop by scrolling on the image and clicking the arrow. This feature was designed to improve usability and guide users directly into the shopping expirience with minimal effort.

 ![Home Page](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FHome.png)



#### **Shop**

The Shop offers a nice selection of products, categorized into 3 categories: Vegetables, Herbs and Flowers.
Users can browse all products or filter by category via the dropdown in the navigation bar.

![Shop](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FShop.png)


### Product Detail

Each product has a dedicated detail page featuring a product image, description, price and add to cart functionality.

![Product](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FProduct.png)

#### **Vegetables**


![Vegetables](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FVege.png)


#### **Herbs**


![Herbs](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FHerbs.png)



#### **Flowers**


![Flowers](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FFlowers.png)


### Deals

A separate Deals section showcases discounted or promotional products. This gives users quick access to special offers and encourages return visits.

![Deals](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FDeals.png)


#### **Tips & Guides**

The Tips & Guides section is split into two areas:

* Guides – Curated articles providing advice on gardening, planting, and sustainability.
* User Tips – Community contributed tips to share knowledge and experience.

Authenticated users can submit their own tips, creating a collaborative and helpful space.

##### Tips

![Tips](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FTips.png)
![Tips Form](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FSubmit.png)

##### Guides

![Guides](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FGuides.png)


### About Page

![About](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FAbout.png)

####  **Contact Form**


![Form](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FContact.png)


### Search


![Search](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FSearch.png)
![Results](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FSResult.png)

### Cart
The cart icon in the navbar shows a live item count badge, improving visibility.
On the Cart page, users can adjust product quantities, remove items, view total pricing with all deals applied  and how much saved on this deal.
Automatically calculated subtotal and total.
The cart includes clear information about delivery charges. Users are shown how much more they need to spend to qualify for free delivery, encouraging upselling and larger orders.

![Cart](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Cart.png)


### Checkout

Checkout is simple and secure, collecting necessary shipping details.
Feedback is provided on order completion to confirm successful purchase.

![Checkout](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FCheckout.png)

#### **Wish List**

##### Wish List
Logged-in users can add items to a personal wishlist.
This allows users to save favorite products for later, encouraging return visits and improving engagement.

Wishlist access is always available from the navbar.

![wish List](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FWishlist.png)



#### **Register Form**

![Register](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FRegister.png)


#### **Log in Form**

![Log in](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FLogin.png)


### Profile

![Profile](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FProfile.png)


#### **Log Out**

![Logout Form](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FLogout.png)

#### **404 Error Page**

![404 Error](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/404.png)

#### **500 Error Page**

![500 Error](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/500.png)


### Future Features:

- Add more Categories.
- Create Order Update.



## Technologies

### Language

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Framework

- [Django](https://www.djangoproject.com/)

### Database

- [PostgreSQL](https://www.postgresql.org/)

### Frontend
- [HTML](https://en.wikipedia.org/wiki/HTML) (Used to structure the content and pages of the application. HTML templates are used to display dynamic data in the frontend)
- [CSS](https://en.wikipedia.org/wiki/HTML) (Used for styling the application)
   - [Bootstrap 5](https://getbootstrap.com/) (Used for styling, layout, and modals)

### Backend and Server Tools

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)


### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control the rendering behaviour of Django forms)
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) (Support for crispy forms)
- [django-resized](https://pypi.org/project/django-resized/) (Optimizes image resizing)
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) (Provides additional management commands, including graph_models for generating Entity Relationship Diagrams (ERD))


### Development & Code Formatting

- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)
- [Flake8](https://flake8.pycqa.org/en/latest/) (Python linter used for python code validation)


### Deployment & Hosting

- [GitHub](https://github.com/Magda-R-bit) ( Repository hosting service used for version control)
- [Heroku](https://help.heroku.com/) (Cloud platform where project was deployed)
- [AWS](https://aws.amazon.com/) (Amazon Cloud storage for images and static files)


### Development Environment

- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) (Main code editor used for writing and testing this project)
- [Gitpod](https://www.gitpod.io/) (Online development environment for coding and testing)



## Testing
  
### Manual Tests and Results

* Testing for layout and functionality completed on the below browser:
  - Chrome ✅
  - Edge ✅
  - FireFox ✅
  - DuckDuckGo ✅

* For more manual tests please refer to [Manual Testing](TESTING.md)


### Validation

- [HTML Validator](https://validator.w3.org/)


Home Page

![Home Page](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/ValHome.png)

Shop

![Shop](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/ValSchop.png)

About

![About](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/ValAbout.png)

Cart

![Cart](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/ValCart.png)

Checkout

![Checkout](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/ValCheckout.png)

404.html

![Error Page](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Val404.png)



- [CSS Validator](https://validator.w3.org/#validate_by_input)

![Base CSS](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/ValCSS.png)


#### Python 

To maintain clean, readable, and PEP8 compliant code throughout the project:

   - [Flake8](https://flake8.pycqa.org/en/latest/) was used as a Python linter to check for potencial errors and enforce coding standards.

Special attention was given to views.py files for shop, cart and checkout apps to ensure high quality code, so double checked these files with 
[CI Python Linter](https://pep8ci.herokuapp.com/)

![Shop](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/LinterS.png)

![Cart](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/LinterCV.png)

![Checkout](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/LinterCHV.png)


#### Lighthouse Testing

Mobile

![Lighthouse Mobile](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/LightMob.png)

Due to external libraries and technologies like Bootstrap, JQuery and Stripe, performance gets only yellow score. 

Desktop

![Lighthouse Desktop](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/LightD.png)


## Bugs

### Fixed Bugs

1. OrderLineItem() got an unexpected keyword argument: 'lineitem_price'

   * Issue: The model had a field lineitem_total, but the view was passing lineitem_price.
   * Fix: Renamed the keyword argument in the view to match the model field:
   lineitem_total=item["line_price"]

2. All Deals Displaying as a Buy One Get One Free

   * Issue:The variable free_items was referenced before assignment if no deal was applied.
   * Fix: Ensured free_items = 0 was always defined at the start of the loop to avoid conditional initialization errors.

3. Deals Not Displaying in Checkout Summary

   * Issue: Cart items with deals (discounts or BOGO) weren't showing correct deal information during checkout.
   * Fix: Refactored cart_context.py to attach deal info to each item. Adjusted the checkout view and checkout_success.html to properly render item.deal, item.discount, and item.free_items.

4. Static Files did not upload to the S3 Bucket

   * Issue: Static Files did not upload to the S3 Bucket due to use of latest version of Django, which requires adjustment to the AWS setup in settings.py.
   * Fix: Configured "USE_AWS" in settings.py for STORAGES section.



### Unfixed Bugs

* No unfixed bugs.

## Deployment

### Version Control

* The project was developed using the Visual Studio Code, the Gitpod editor, and was pushed to GitHub in the remote repository Plant-Wise.
* Git commands were used to push the code to the repository.

### Deployment to Heroku

* The project was deployed to Heroku with the following steps:
  - Create an account and log in to Heroku
  - Go to the dashboard, click *New*, then *Create new app*
  - Navigate to *Settings*
  - Go to *Config Vars*, click *Reveal Config Vars*, and add the KEY, and the VALUE for Database, Cloudinary and Secret Key. Click *add*
  - Go to VS Code project settings and allow Heroku as a host (ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost'])
  - Navigate to the *Deploy* tab at the top
  - Click *GitHub*, then *Connect to GitHub*
  - Search for the repository you want to deploy and click *connect*
  - Select *Enable Automatic Deploys* or *Deploy Branch*

[Link to deployed project](https://plant-wise-97799c6a3824.herokuapp.com/)

### How to clone the repository

- Go to the https://github.com/Magda-R-bit/Plant-Wise reposotory on GitHub
- Click on the Code button located above the project files
- Select HTTPS and copy the repository link
- Open your work environment, type *git clone* and paste the copied Git URL and press Enter
- The project is now created as a local clone

### How to Fork the repository

- Log into GitHub and click on repository to download ([Plant-Wise](https://github.com/Magda-R-bit/Plant-Wise))
- Click the **Fork** button in the top right-hand corner
- Click **Create Fork**
- The repository is now in your chosen account and can be cloned or changed

## Credits

 - **Special Thanks**:
   - **Spencer Barriball**- For your mentorship. Your insights and advices were crucial to the success of this project
 - *ChatGPT-4* - For creating Tips description and debugging
 -  Slack Community - For helping me solving issues with settings

### Inspiration

- [w3schools](https://www.w3schools.com/howto/howto_css_modals.asp)
- [stackoverflow](https://stackoverflow.com/)
- [Boutique Ado Walkthrough Project](https://github.com/Magda-R-bit/boutique_ado_v1)
- [Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1)
- [Very Academy](https://www.youtube.com/watch?v=OgA0TTKAtqQ) - Wish List
- [codepiep](https://www.youtube.com/watch?v=H8uvpvpas_U&t=913s) - Deals
- Antonio Melé: ["Django 5 By Example"](https://books.google.ie/books/about/Django_5_By_Example.html?id=P-AEEQAAQBAJ&redir_esc=y)

### Media

- [Unsplash](https://unsplash.com/s/photos/wild-nature) Used for all images.
- [Freepik](https://www.freepik.com/) Used for images for error pages.
- [Canva](https://www.canva.com/logos/) Used for creating Logo
- [Favicon](https://favicon.io/) Used for generating favicon
