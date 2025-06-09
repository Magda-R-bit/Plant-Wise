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

  1. Sprint Planning:

  - I planned my tasks in sprints, typically lasting 1-2 weeks, to stay focused on specific goals. I focused first on functionality of my project. Each sprint would target the development of core features, like user authentication, adding and deleting products to the shop, adding tips and guides, updating and deleting. Adding products to the cart and testing checkout flow.

  

  2. Kanban Board:

  -  I created [GitHub Project](https://github.com/users/Magda-R-bit/projects/6) to help me manage tasks by moving them trough various stages from To Do, to In Progress, and finally to Done.


  ![Kanban Board User Story](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/UserStory.png)
  ![Kanban Board Developer](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Developer.png)
  ![Issue](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Issues.png)


### Wireframes

- [Figma](https://www.figma.com/) (Used to create Wireframes)

![Screenshot of Wireframes Shop](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Wireframe.png)


### Design

#### Colour:

The primary colours chosen for this website are green: #198754 and #2d6a4f, for its association with nature, healthy green vegetables.

Green is often associated with relaxation and harmony, which aligns perfectly with the theme of wellness and healthy organic food.


![Buttons](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/198754.png)
![Buttons](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/2d6a4f.png)

The navbar and Footer uses Bootstrap's `bg-light` class, which applies a soft light-gray background (`#f8f9fa`) for a clean and minimalistic look.

![Navbar](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/Navbar.png)

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
- Navigation options depend of user authentication

![Navbar](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FNavbar.png)
![Burger](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FBurger.png)

#### **Footer**

- Responsive Footer with social media links and address

![Footer Full](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FFooter.png)
![Footer](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FFmob.png)



####  **Home Page**

##### User can start photo slider by clicking on the image

 ![Home Page](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FHome.png)



####  **Shop**


![Shop](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FShop.png)


### Product Detail

![Product](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FProduct.png)

#### **Vegetables**


![Vegetables](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FVege.png)


#### **Herbs**


![Herbs](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FHerbs.png)



#### **Flowers**


![Flowers](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FFlowers.png)


### Deals

![Deals](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FDeals.png)


#### **Tips & Guides**

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

![Cart](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FCart.png)


### Checkout

![Checkout](https://plant-wise.s3.eu-north-1.amazonaws.com/media/images/readMe/FCheckout.png)

#### **Wish List**

##### Wish List 

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

![404 Error]()

#### **500 Error Page**

![500 Error]()


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
- [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) (Serves static files efficiently in production)


### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control the rendering behaviour of Django forms)
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) (Support for crispy forms)
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) (Manages media and static files)
- [django-resized](https://pypi.org/project/django-resized/) (Optimizes image resizing)
- [django-richtextfield](https://pypi.org/project/django-richtextfield/) (Provides rich text editing, used in the admin for creating cabin descriptions)
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) (Provides additional management commands, including graph_models for generating Entity Relationship Diagrams (ERD))


### Development & Code Formatting

- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)
- [Black](https://pypi.org/project/black/) (Python code formatter)
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


### Automated Tests

* Automated test created for booking app to test app functionality. All tests ok, no errors found.

![Model Test]()


* Tests Results

![Tests Results]()

### Validation

- [HTML Validator](https://validator.w3.org/)

base.html

![Base HTML]()

index.html

![Home Page]()

header.html

![Navbar HTML]()

footer.html

![Footer  HTML]()

404.html

![Error Page]()

500.html

![Error Page]()


- [CSS Validator](https://validator.w3.org/#validate_by_input)

![Base CSS]()

#### Python 

To maintain clean, readable, and PEP8 compliant code throughout the project:
   - [Black](https://pypi.org/project/black/) was used as an automatic code formatter. Since the project contains multiple Python files, Black ensured consistency and adherence to PEP8 standards across all files.
   - [Flake8](https://flake8.pycqa.org/en/latest/) was used as a Python linter to check for potencial errors and enforce coding standards.

Special attention was given to views.py files for shop and checkout apps to ensure high quality code, so double checked these files with 
[CI Python Linter](https://pep8ci.herokuapp.com/)

![]()

![]()


#### Lighthouse Testing

Mobile

![Lighthouse Mobile]()

Desktop

![Lighthouse Desktop]()


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
- Antonio Melé: ["Django 5 By Example"](https://books.google.ie/books/about/Django_5_By_Example.html?id=P-AEEQAAQBAJ&redir_esc=y)

### Media

- [Leonardo AI](https://leonardo.ai/) Used for creating Cabins images
- [Unsplash](https://unsplash.com/s/photos/wild-nature) Used for all images.
- [Freepik](https://www.freepik.com/) Used for images for error pages.
- [Canva](https://www.canva.com/logos/) Used for creating Logo
- [Favicon](https://favicon.io/) Used for generating favicon
