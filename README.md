 <h1 align="center">Milestone Project 4 - Revaamp</h1>

# Revaamp - Buy refurbished laptops online!

[View the live project here.](https://revaamp.herokuapp.com/)

![WebApp Store](https://github.com/IainMcHugh/milestone-project-4/blob/main/readme_media/mockup.png?raw=true)

Welcome to Revaamp! Revaamp is an ecommerce website that sells refurbished laptops and computers, as well as other tech periferals. As someone who uses a computer everyday and has built my own computer, I love to browse different PC parts websites and PC refurbished shops online. I would love at some point to create a fully fledged web application for an electronics shop and so this is where the inspiration for this project came from. Revaamp offers an end to end ecommerce experience for tech customers wishing to browse and purchase laptops and PCs.

## User Experience (UX)

- ### User stories

  - #### Site Visitor Goals

    1. As a site visitor, I want to a clear way to navigate the site to find what I'm looking for
    2. As a site visitor, I want to be able to re-order my searches to suit my needs.
    3. As a site visitor, I want to add products to a shopping cart and be notified when I have done so
    4. As a site visitor, I want to a clear breakdown of the items I am buying at the checkout.
    5. As a site visitor, I want a smooth checkout experience, where I feel confident my order has been recorded.
    6. As a returning user, I want to be able to see my save products so I can review them.
    7. As a returning user, I want to be able to save my shipping details to improve my checkout experience.
    8. As a returning user, I want to be able to see my order history against my profile.
    9. As a returning user, I want to receive confirmation emails when my order has successfully been processed.
    10. As a returning user, I want to be able to leave feedback against a product that I have purchased.
    11. As a site owner, I want the ability to edit and delete products directly from the product page.

- ### Design
  - #### Colour Scheme
    - For Revaamp colour scheme I decided to use a great themeing resource for generating a consistent colour palette (Coolors.co). I used this to generate css variables that I stuck to using when adding colours throughout the site. The colours I used were:
      - ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff - WHITE`
      - ![#f2f2f2](https://via.placeholder.com/15/f2f2f2/000000?text=+) `#f2f2f2 - OFFWHITE`
      - ![#531cb3](https://via.placeholder.com/15/531cb3/000000?text=+) `#531cb3 - PURPLE`
      - ![#944bbb](https://via.placeholder.com/15/944bbb/000000?text=+) `#944bbb - PURPLE PLUM`
      - ![#aa7bc3](https://via.placeholder.com/15/aa7bc3/000000?text=+) `#aa7bc3 - AFRICAN VIOLET`
      - ![#cc92c2](https://via.placeholder.com/15/cc92c2/000000?text=+) `#cc92c2 - ORCHID CRAYOLA`
      - ![#dba8ac](https://via.placeholder.com/15/dba8ac/000000?text=+) `#dba8ac - PASTEL PINK`
      - ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000 - BLACK`
      - ![#0d0d0d](https://via.placeholder.com/15/0d0d0d/000000?text=+) `#0d0d0d - OFFBLACK`

- #### Typography
    - I used PT Mono as the single font for this project, with monospace as the fallback font. I used this font as I feel it fits with the tech nature of the website, having slightly sharper features with a retro typewriter feel.
      <a href="https://fonts.google.com/specimen/PT+Mono">PT Mono</a> - Google Fonts
  - #### Imagery
    - Being an ecommerce site, there are two main focuses for imagery throughout the site. The first being the hero image which dominates the viewport above the fold on the homepage. This is a high resolution image that displays immediate site purpose, while also being clean enough to not draw the users attention away from interactions available to them. I added a transparent overlay to darken the hero image to further focus the hero text and shop now button. The second source of imagery is in the product images. Product imagery definitely adds to the user experience and gives greater clarity to the user on the products they're browsing.

* ### Wireframes

  - Figma Wireframe - [View](https://www.figma.com/file/lMTjTxxHjyL1UzxZzGcWme/Revaamp?node-id=0%3A1)

## Features

- Responsive layout for all screen sizes.

- Fully featured user authentication.

- Comprehensive searching and product categorisation.

- Adding products to wishlist.

- Shopping cart.

- User profile with saved details

- Full CRUD functionality for siteowner

- Integrated stripe payment process

- Fallback stripe webhook to guarantee order tracking

- AWS static hosting

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python)

### Frameworks, Libraries & Programs Used

1. [jQuery:](https://jquery.com/)
   - jQuery was used to control all of the modal functionality on the website.
2. [Django:](https://www.djangoproject.com/)
   - Django was the fullstack python framework used for the entire web application
3. [Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/)
   - Crispy Forms is a django plugin used to optimise form usage throughout the site.
3. [Allauth:](https://django-allauth.readthedocs.io/en/latest/installation.html)
   - All auth is a django plugin that handles user auth flows and provides templates for each auth page.
4. [Black:](https://pypi.org/project/black/)
   - Python code formatter to keep consistent code.
5. [AWS Hosting Service](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fs3.console.aws.amazon.com%2Fs3%2Fbuckets%2Frevaamp%3Fregion%3Deu-west-1%26state%3DhashArgs%2523%26tab%3Dpermissions%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fs3&forceMobileApp=0&code_challenge=AZTkrRJi3AhPQhXLciQhTdapQ5JWI_4aOMsjpSQp0C8&code_challenge_method=SHA-256)
   - AWS was used to host all static files associated with the site.
6. [Heroku](https://dashboard.heroku.com/apps)
   - Heroku was used to deploy the site live on the internet.
7. [GitHub:](https://github.com/)
   - GitHub is used to store the projects code after being pushed from Git.
8. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
   - Photoshop was used to edit the logo, resizing images and editing photos for the website.
9. [Figma:](https://figma.com/)
   - Figma was used to create the [wireframes](https://www.figma.com/file/lMTjTxxHjyL1UzxZzGcWme/Revaamp?node-id=0%3A1) during the design process.
10. [Visual Studio Code:](https://visualstudio.com/)
   - VSCode was the IDE I used to create, update, and maintain this project.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/) - PASS (NOTE: I had to test each HTML section manually as the validator can not handle Django templating)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - PASS
  (Note:
  - I had to manually test both the base.css and reset.css files.
  - I was getting an error with invalid use of linear-gradient but it is being used correctly)

### Testing User Stories from User Experience (UX) Section

- #### Site Visitor Goals

  1. As a site visitor, I want to a clear way to navigate the site to find what I'm looking for

      - The header provides product breakdowns by category so the user can search a specific section of products. There is also a search bar that will return results that match either the product title or product description, giving users a fast and convenient way to find the product they're looking for.

  2. As a site visitor, I want to be able to re-order my searches to suit my needs.

      - Within the header navigation there is also the 'All Products' sections, that allow users to organise products by price, rating, and categories alphabetically. Also when a user selects a product category they will see both tags and a drop down filter available on the products search page to further categorise their search.

  3. As a site visitor, I want to add products to a shopping cart and be notified when I have done so

      - When a user finds the product they are searching for, it is a one click process to add this item to their shopping cart. They also have the ability to set a quantity before adding to cart. When the item is added, they will receive a toast notification to let them know the item has been added successfully.

  4. As a site visitor, I want to a clear breakdown of the items I am buying at the checkout.

      - Navigating to the checkout, the user will see a clear list breakdown of all the products they have added. It gives them a thumbnail image of the product, the product price, quantity selected, and total cost for that item. After the product breakdown there is clear feedback given for the order total, any shipping costs, and a grand total.

  5. As a site visitor, I want a smooth checkout experience, where I feel confident my order has been recorded.

      - The Revaamp checkout experience features Stripe payment. The order process is as simple as entering the users card number and details on the checkout screen, and completing the order. While the user is then presented with a loading spinner, in the background a few things are happening to secure the users order and payment. Firstly, a payment intent is being sent to Stripe before then registering the order in the Revaamp database. Simultaneously we utilise Stripe web hooks that fire on the payment intent being registered. This will listen for a small window of time for the order being created, and if at the end the order can not be found the order will be created via the webhook call. This ensures that whenever a user completes an order and stripe payment intent is received they are guarenteed to have the order processed by Revaamp.

  6. As a returning user, I want to be able to see my save products so I can review them.

      - Along with shopping cart functionality, Revaamp also provides a wishlist page that allows users to save products. In essence this allows them to create their own section of products they're particularly interested in. To ensure a good UX flow from the wishlist page, the user can both access the products details page from a specific product, as well as add any saved product directly to their shopping cart. They can also delete products out of their saved products.

  7. As a returning user, I want to be able to save my shipping details to improve my checkout experience.

      - For returning users it is a straightforward process to add and save shipping details. If the user simply navigates to their account page they can fill in their details here, which will automatically update their details on the checkout page. Similarly if they fill out their details on the checkout page and select to save their details, it will update their account details and use the same information for future checkout sessions.

  8. As a returning user, I want to be able to see my order history against my profile.

      - On a user's account page, they can access a full breakdown of all of their previous orders. It will provide them the order number, order date, order items, and order total. Clicking through to the order will give a full breakdown that they would have received when first successfully submitting the order.

  9. As a returning user, I want to receive confirmation emails when my order has successfully been processed.

      - After a user's order has been successfully submitted, the user is brought to a checkout success page where they will see a full breakdown of their order. Simultaneously they will receive an email with the same order information, which gives them further peace of mind that their order has successfully been processed.

  10. As a returning user, I want to be able to leave feedback against a product that I have purchased.

      - Entering a product detail page, the user can select reviews to be brought to the comments section for a given product. Here they can read previous reviews left by other users, as well as leave their own review against the product. Along with a written review they need to give a star rating, and their review will be timestamped for others to see.

  11. As a site owner, I want the ability to edit and delete products directly from the product page.

      - Logging in with an admin account, when viewing a product details page the admin will see two extra options to edit and delete that product. Selecting edit will open a form where they can change fields specific to that product and save their changes, while selecting delete will soft delete the item from the site, making it inaccessible for users.

### Further Testing

- The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
- A large amount of testing was done to ensure that all pages were linking correctly.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
- All site routes have been tested for authentication also and should correctly handle unauthenticated users.

### Known Bugs

- I ran into a unique issue where the superuser deletes a product that is is being referenced in other models/contexts around the site. For example if another user has an item in their wishlist or shopping cart, it will throw an error when the superuser deletes that item. I got around this problem by adding a `soft_delete` field to the Product model which defaults to False. When the superuser now deletes a product, instead of hard deleting the product, the soft_delete flag is set to True. I then updated the views that retrieve instances of the Product model and first filter them by the `soft_delete` field. I have comprehensively tested this update for all user flows on the site as of making this change and this fix seems to have solved the problem. I will give special credit to this [Stackoverflow post](https://stackoverflow.com/a/50905650) where I learned how to correctly use `prefetch_related` in order to filter on an attribute of a model that acts as a foreign key (essentially prefetching all instances of that Model from the database once instead of requerying every time).

## Future Features

- As it is a refurbished laptop site, the intention is that the site owner gives a static rating to his own products. However after adding a reviews section, it would be great to add a user's rating data point that gets the average user rating from that products reviews.

- Currently on the wishlist page, a user can easily add a single item to their shopping cart. However I would like to extend this to allow them to multiselect items to add to cart. Also currently after adding to cart they must manually delete that product out of their wishlist. It could provide a better user experience to automatically remove this item from their wishlist, although I have seen both flows being utilised.

- I think for any successful ecommerce site, it is important to keep your brand in the mind of your customers, and so a future plan for me would be to setup a mailing list against users with profiles, letting them know of promotional offers on a monthly basis.

## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/IainMcHugh/milestone-project-4)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/IainMcHugh/milestone-project-4/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone git@github.com:IainMcHugh/milestone-project-4.git
```

7. Press Enter. Your local clone will be created.

```
$ git clone git@github.com:IainMcHugh/milestone-project-4.git
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Requirements

You will need the following installed in order to run this project locally:

- [pip](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)

## Creating a Virtual environment and installing dependencies

1. In order to keep track of the python libraries you need for this project, it is easiest to create a virtual environment in the root directory where package version control can be easily tracked. In the root directory of the project run:

```
python3 -m venv revaampvenv
source revaamp/bin/activate
```

This will install a venv and then activate it. From here we need to install all of the required packages utilised in the project:

```
pip install -r requirements.txt
```

Finally to run the project, simply run:

```
cd revaamp/ && python3 manage.py runserver
```

Note: In order to run this application locally you will most likely need to open `settings.py` and make two changes:
   -  comment current DEBUG setting, and set `DEBUG = True`
   -  comment current SECRET_KEY setting, and set `SECRET_KEY = "some_key"`

In the terminal if all is successful you should see the website is ready on localhost at port 8000.

## Running migrations

To check if there are any migrations not yet run, you can run in the terminal:

```
python3 manage.py showmigrations
```

To run migrations:

```
python3 manage.py migrate
```

Note: The `--plan` flag will give a breakdown of what migrations will be run and is good practice to check before running migrate command

## Creating a Superuser

In order to create a superuser that can access the admin panel, in the terminal run:

```
python3 manage.py createsuperuser
```

From here you will need to set a username, email, and password.


## Deploying to Heroku

The three packages that are required for this process (and should be installed now as part of requirements.txt) are:

- psycopg2-binary
- dj-database-url
- gunicorn

### Steps

1. Navigate to the [heroku](https://www.heroku.com) website and login or signup with a new account.
2. Add a new heroku App, giving it a name and appropriate region.
3. Navigate to the `Resources` tab and add the Heroku Postgres addon.
4. You will need to update the allowed hosts array in `settings.py` to include your live domain. It will be of the format:

```
ALLOWED_HOSTS = ['<YOUR HEROKU APP NAME>.herokuapp.com']
```

5. From the terminal you will then need to run `heroku login` and initialise the git remote with:

```
heroku git:remote -a <YOUR HEROKU APP NAME>
```

6. You should now be able to deploy to heroku by running `git push heroku main`
7. Optionally you can now setup automatic deployments from heroku by connecting your revaamp repo in the `Deploy` tab.

The following config variables will need to be setup in the `Settings` tab:

![Reveal Config Vars](https://github.com/IainMcHugh/milestone-project-4/blob/main/readme_media/config_vars.png?raw=true)

## Setting up AWS static file hosting

The two packages that are required for this process (and should be installed now as part of requirements.txt) are:

- boto3
- django-storages

### Steps

1. Navigate to [AWS](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fs3.console.aws.amazon.com%2Fs3%2Fbuckets%2Frevaamp%3Fregion%3Deu-west-1%26state%3DhashArgs%2523%26tab%3Dpermissions%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fs3&forceMobileApp=0&code_challenge=AZTkrRJi3AhPQhXLciQhTdapQ5JWI_4aOMsjpSQp0C8&code_challenge_method=SHA-256) and create an account if you have not already done so.
2. In the AWS console search for S3, choosing the option to Create a bucket.
3. You will need to enable Static Website Hosting for the bucket, specifying the `Index document` as `index.html`
4. In the permissions tab, paste the following CORS configuration:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Navigate to the bucket policy tab, and generate a security policy associated with the S3 bucket.

## Creating AWS Groups, Policies and Users

### Steps

1. In the AWS console search for and open IAM
2. In the `Groups` tab, select `Create New Group` option, giving it an appropriate name.
3. After creating a group, navigate to the `Policies` tab and select `Create Policy`
4. With the JSON tab open, import the S3 prebuilt full access policy.
5. The `Resource` value is currently set to allow all, this needs to be modified to only allow resources from the previously created bucket.
6. In order to do this, get the bucket ARN and update the Resources with this.
7. From here you can create the policy, filling out all required fields with appropriate values.
8. You will need to navigate back the the `Groups` tab and select `Attach Policy`, and applying the policy just created.
9. Finally you will need to create a user, by first navigationg to the `Users` tab and clicking `Add User`.
10. Make sure to add this user to our newly created group.
11. It is important here to download the `.csv` file that is generated when adding the new user.
12. Create two new heroku config variables:

```
AWS_ACCESS_KEY_ID: This will be in the .csv file generated from AWS
AWS_SECRET_ACCESS_KEY: This will be in the .csv file generated from AWS
USE_AWS: True (As we always want production app to use AWS)
```

13. Any future pushes to the heroku remote repository should cause the web applications static files to be collected and added to the S3 bucket.

## Stripe Integration

### Steps

1. Navigate to [Stripe](https://www.stripe.com) and sign in or create an account.
2. Obtain the `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`, adding them to Heroku config variables.
3. In the Developers section, open the `Webhooks` tab and select __Add endpoint__
4. For the __Endpoint URL__, add the following:

```
https://<YOUR DEPLOYED APPLICATION>/checkout/wh
```

5. Make sure to select receive all events.
6. Add the webhooks secret key to the Heroku config vars, referring to it as `STRIPE_WH_SECRET`

(Note: In order to test Stripe webhooks on your local machine you must use the Stripe CLI, for more information on how to set this up follow: [Stripe-CLI/webhooks](https://stripe.com/docs/stripe-cli/webhooks). You must also export the stripe environment variables from the root directory of the project.)

## Credits

### Code

- [Django documentation](https://docs.djangoproject.com/en/3.2/): Definitely an extremely useful resource that I basically had open for the duration of my development. It was really important to me to be able to look up new resources in the course content here so I could get a detailed understanding.

- [Allauth documentation](https://django-allauth.readthedocs.io/en/latest/overview.html): I was amazed at how a package could abstract away so much of the authentication process for a web application while providing a high quality, all encompassing result. Again I used this documentation to teach myself as well as fixing any small issues I encountered with authentication flows.

- [Crispy Forms documentation](https://django-crispy-forms.readthedocs.io/en/latest/): I loved using crispy forms and realised the more I used it the more customisation that was available to me. I used their documentation in particular to help me construct the commenting flow.

### Content

## Credits


- All content was written by Iain McHugh.

- [Multi-mockup](https://techsini.com/multi-mockup/): A great resource for generating mockup displays for the site on various different screens and devices. Used for the cover photo of this readme file.

- [Colour Scheme](https://coolors.co/531cb3-944bbb-aa7bc3-cc92c2-dba8ac): I can't recommend this site enough for getting quick and amazing colour templates for your website.

- [Reset CSS](https://meyerweb.com/eric/tools/css/reset/): A tool I often use on projects to remove most of the default styling that the browser

### Media

- All images were created/edited by the developer or sourced from image websites where Creative Commons license is active.

- [Site for icons](https://fontawesome.com/)

- [Favicon](https://www.pngfind.com/mpng/TiiRoJo_geometry-dash-icon-ball-png-download-geometry-dash/)

- [Hero Image](https://www.google.com/search?q=laptop%20website%20background&tbm=isch&tbs=il:cl&hl=en-GB&sa=X&ved=0CAAQ1vwEahcKEwjwz4yn8qPxAhUAAAAAHQAAAAAQAg&biw=2559&bih=1225#imgrc=P5UTcfS4dj6vYM)

### Acknowledgements

- Most importantly I would like to thank my mentor Oluwafemi. He has been the primary source of guidance on this project for me, really helping me to set down a direction and flow for the site. It was extremely useful for me to have someone to bounce ideas and problems off and just having a second pair of eyes intermittently checking the progress of the site to make sure it delivers on it's core concepts. Thanks for all of your help on these 4 projects.

- I also want to thank Code Institute in providing me with information and guides on how to structure my project. I really felt with this milestone project the video content Code Institute provided was essential for allowing me to lay the foundations of this project and get it up and running. While I feel the complexity has increased with each project, I feel very clear on how everything is working in this application.

- Again I would like to thank the Slack community associated with Code Institute. It is a great way to find inspiration and feel as part of a community who share a similar mindset and goal.
