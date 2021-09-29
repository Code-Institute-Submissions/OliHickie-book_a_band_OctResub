# BOOK A BAND


[&#127926;  &nbsp; **View Live Website**  &nbsp; &#127926;](https://bookaband.herokuapp.com/)

[&#127928;  &nbsp; **View GitHub Repository** &nbsp; &#127928;](https://github.com/OliHickie/book_a_band)

![Image of website](media/responsive.png)

Book a Band is an e-commerce website designed to help users plan and book musical entertainment for their wedding day. The site offers users an easy booking system which allows them to book a variety of acts, as well as view all bookings in one easy place. 

The website is built using the Django framework alongside Bootstrap and jQuery, with the checkout process provided by Stripe. Static files are hosted by Amazon Web Services and the site is deployed on Heroku. This website was created as part of my Full Stack Web Developer Diploma with Code Institute.

# Contents

1) [User Experience](#user-experience)
2) [Features](#features)
3) [Technologies](#technologies)
4) [Testing](#testing)
5) [Deployment](#deployment)
6) [Credits](#credits)

<br>

# User Experience

The layout of the site is clear, clean and relatively simple. The idea behind this is for users to understand the functionality of the site and navigate to their desired destination quickly. The site will offer a number of different acts and to make the searching easier, there are a number of different categories that the user may reduce the amount of search results and, in turn, find an appropriate band or act. 
The checkout process is quick and clear, made easy by the use of Stripe. Once all bands or acts have been paid for, the booking is marked as confirmed. 
Many of the site actions are supported by notifications at the top of the screen to confirm the users actions and keep a clean feel to the sight. 

## User Stories

| # | User | Would want to |
| :----- | :------- | --------- |
| US01 | New User | Quickly understand the purpose of the  website |
| US02 | New User | Navigate to a list of bands |
| US03 | New User | Navigate to a list of blogs |
| US04 | New User | Search for bands depending on category or keyword |
| US05 | New User | View bands depending on location or price |
| US06 | New User | View a band's details, cost, ratings and location |
| US07 | New User | View user reviews for the band |
| US08 | New User | View suggestions for similar bands |
| US09 | New User | Read blogs about wedding music |
| US10 | New User | Share blogs on social media |
| US11 | New User | Visit website's socials |
| US12 | New User | View website's contact information |
| US13 | New User | Register for an account |
| US14 | Registered User | Create a booking for a band |
| US15 | Registered User | View all bookings in one place |
| US16 | Registered User | Confirm bookings through making a payment |
| US17 | Registered User | View confirmation of bookings and payments made |
| US18 | Registered User | Leave a review on bands that I have booked |
| US19 | Registered User | Delete any bookings that aren't confirmed |
| US20 | Registered User | Update and recover account information |
| US21 | Site Owner | Add and Update new bands to the site |
| US22 | Site Owner | Add, update and delete blogs from the site |

## Design

The site is aimed at those planning on getting married, although a future step would be to open the site up to attract people planning events in general. With the focus, for now, being on weddings, the color scheme, imagery and design reflects this.  

### Color Scheme

![Image of color scheme](media/babcolor1.png)

I used a lot of pinks in the site as a soft color and that often associated with weddings. THe two contrasting shades of pink are used as both backdrops as well as for the logo, text and buttons. Blue offered a nice contrast to this so if often used for headings and bold text. 
I wanted to keep the color scheme relatively simple as there is a lot of color introduced to pages through busy imagery. 

### Typography

Throughout the site I used two types of font, both downloaded from Google Fonts. For titles and large text, including the logo, I used Abril Fatface and for the rest of the site I used Playfair Display, a very easy to read font, which has a smart and fun look about it. 

### Wireframes

INSERT WIREFRAMES HERE!

### Database Schema
![Image of schema](media/schema.png)

Schema created on [dbdiagram.io](https://dbdiagram.io/)

# Features

## Nav Bar

![Image of nav bar](media/navbar.png)

- The nav bar is full responsive and navigation menu items collapse into a Bootstrap hamburger icon. 

![Image of nav bar in mobile view](media/navbar-collapse.png)

- The nav bar is visible across the whole site, including checkout and error pages. 
- Users will find a search bar in the top right corner of the nav bar in desktop view. This searches for keywords in the bands' names and biographies and filters the search results accordingly. The search bar moves inside the collapsable menu for smaller screens. 
- The menu items include links for the index page, musicians page, blogs menu and account options. 
    - **Musicians** This option opens a Bootstrap dropdown menu for larger screens or an accordian for smaller screens for a better user experience. The options available navigate the user to the bands page, returning either all the bands, or bands by category. 
    ![Image of nav bar and musicians tab](media/navbar-musicians.png)

    - **My Account** This option is set up in a similar way to the musicians link. The options available depend on whether the user or superuser is logged in or not.
        
        |User status|Options|Results|
        |:-----|:------|:------|
        |No User|Log In|Takes user to a log in page which takes an email address and password|
        ||Create Account|Take user to account setup page, after which a confirmation email is sent to users account to allow user to log in |
        User Logged in| My Bookings | Shows user if they have any bookings, whether they are confirmed or not, and displays outstanding balance plus a link to the checkout|
        ||Log Out| Logs the user out after confirmation|
        |Superuser logged in|Add Band |Allows superuser to add a band to database|
        ||Add Blog|Allows superuser to add a blog to the database|
        ||My Bookings|Displays any bookings made by the superuser|
        ||Log Out| Logs the superuser out after confirmation|

    ![Image of my account tab in mobile view](media/navbar-myaccount.png)

- After any user actions such as making a booking or payment, these are confirmed by Bootstrap toasts, which appear over the nav bar. The stay open until the user closes them. 

## Footer 

- The Footer is situated at the bottom of each page including the error pages and is fully responsive
![Image of page footer](media/footer.png)

- The footer contains the site logo, which links the user to the index page. THe user can also find similar links to that which are found in the nav bar, under the menu title. 
- The footer also contains a search box, similar to that found in the nav bar. 
- There are 4 social media links which navigate the user to social media sites in a separate tab, as well as contact details including an email address (which opens the users email sender), a phone number (which is also clickable) and an address which navigates to a google maps site. 

## Index Page

- When the index page loads, the user is greated by a heading, a tag line and a cta button leading the user directly to the page of musicians. This section also contains two images for an appealing welcome and to help the user visually understand what the sites main aims are. 
- Below this section are six images which are backed up by titles. These six clickable images, which expand when hovered over, direct the user to bands in a category of their choosing. 

![Image of style section of index page](media/index-style.png)

- The final section of the index page is a quick introduction (and links) to the basic actions a user can take. These are to sign up for an account, to find a band, make a booking and to complete payments. 

## Musicians Page

- The musicians page is where the user can search for and find bands of different styles, price and from different geographical areas. 
- The bands are displayed on cards which give the user some basic information, including the band's name, an image, the price and their location. It also contains a button which navigates to the bands profile page. 
- Quick links are visible at the top or to the side of the cards, depending on screen size. These are quick links, which allow the user to reduce the number of search results and just return bands depending on category, location or price. A user can also sort all the bands either alphabetically or by price. 
- The page is paginated to avoid having too many bands on one page and improve the user experience. 

## Band Profile

- A band profile page is made up of three sections. The chosen band's profile details, any reviews made and alternative suggestions. 
![Image of Band Profile page](media/bandprofile.png)

- The page displays the band's images (up to a maximum of four). One image is much larger than the others. If a smaller image is clicked, it trades places with the larger image in order for the user to view all the images clearly. 
- The information section displays the band name, the price, a rating (which is an average from the reviews - alternatively, 'no ratings'), the band's location and biography.
- If the superuser is logged in, a button is visible which allows the superuser to edit this bands information. 
- Two buttons, situated below the biography, allow the user to either book the band, or, head back to view all bands. 

![Image of band reviews and suggestions](media/bandprofile-reviews.png)

- The second half of the page contains user reviews which displays who the review was written by, their star rating (out of five), the review itself, plus the date it was written. These reviews are in date order with the newest first.
- The final section is alternative suggestions for the user of up to four different bands, based on the current bands category. 

## New Bookings Page

- The bookings page takes all of the information from the user, required to create a booking, minus payment. 
- The input fields are split into three sections; 'About You', 'About the Venue' and 'On the Day'. 
- All fields are compulsory, except for the address2 and additional information. 
- The Wedding date field uses a jQuery date picker which only allows users to pick a date in the future. This field is also read-only to prevent any alternative date formats being added for validation reasons. 
- The time picker is a jQuery plugin from [https://timepicker.co/#](https://timepicker.co/#) which automatically changes any integer into a time format. 
- The user can choose to either create the booking or head back to the 'all bands' page.

## My Bookings Page

- Once the user has created a booking, they can be viewed on the My Bookings page. If no bookings have been made, a message reads 'You currently have no bookings' and a button is available to take the user back to the bands page. 

![Image of My Bookings page](media/mybookings.png)

- On the page, users can view all bookings made and whether the bookings are conformed or not. This page acts as both a 'cart' and a 'order history' page in order to keep all users bookings in one place.
- From here, users can delete unconfirmed bookings, with confirmation made via a modal. They can also leave a review on bands they have confirmed, meaning only users who have booked and confirmed bands may leave a review for them. 
- The total outstanding balance is calculated as a total for all unconfirmed bookings. When this balance has been paid, the booking becomes confirmed. 
- As, in a real life situation, bands are booked for weddings and can't be cancelled, any changes to be made for bookings must be done via direct contact with the site owner. 

## Payment Page

- From here, the user can view what band payments are still outstanding and pay for the bookings. The outstanding payments are itemised for the user to see and a total is calculated. 
- The payment is then taken using Stripe. 
- This site is currently just for education use only, so Stripe is in test mode. 

![Image of payments page](media/payments.png)

- Once payment is made, all bookings are confirmed and the user receives a message of confirmation and directed back to their bookings page. 

## Blogs Page

- From the blogs page, users may view all blogs available to read on the site. 
- If the superuser is logged in, they can delete, edit or add a new blog from this page. 
- The blogs are displayed with an image, the date they were last updated and the title of the blog. 

## Read blog

- Here is where the user may read the blog and also view the author and a link to the source of the content. 
- The user also has social media links which create a link for the user to post on their social media pages. 

<hr>

## Future Features

- I would like to offer a more complicated searching system on the musicians page. This will allow the user to add queries on to one another and reduce the search results to a more specific criteria. 
- The user's wedding day information is stored and is automatically present when create a booking. This can be done either when signing up for an account or once they have made a booking. 

<br>

# Technologies

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python3](https://www.python.org/) 
- [Javascript](https://www.javascript.com/) / [JQuery](https://jquery.com/)
- [Django](https://www.djangoproject.com/) - the framework used for the site.
- [Amazon Web Services](https://aws.amazon.com/) - used to store static and media files. 
- [Git](https://git-scm.com/) - used for version control.
- [Bootstrap5](https://getbootstrap.com/) - Features and componants were used across the site, such as the collapsible nav bar, toasts, modals, dropdowns and accordians. 
- [SQLite](https://www.sqlite.org/index.html) - used as the database whilst in development.
- [PostgreSQL](https://www.postgresql.org/) - used as the database when the site is deployed. 
- [Stripe](https://stripe.com/gb) - used to handle payment feature on the site. 
- [GitPod](https://gitpod.io/) - IDE used.
- [GitHub](https://github.com/) - used to house the repository.
- [Heroku](https://id.heroku.com/) - used for deploying the website.
- [FontAwesome](https://fontawesome.com/) - used to import icons.
- [Google Fonts](https://fonts.google.com/) - used to import fonts.
- [Balsamiq](https://balsamiq.com/) - used to build wireframes.
- [Tiny JPG](https://tinyjpg.com/) - used to compress images.


# Testing

### Functionality Testing

-  Manual testing was carried out on:
    - Desktop: Apple and Dell
    - Tablets and mobile: Apple and Samsung
    - Browsers: Chrome, Safari, Edge and Internet Explorer

    Live tests were also carried out on [https://comparium.app/](https://comparium.app/)

During testing the following tests were carried out on large and small screens

- Nav Bar/Footer
    - All nav bar links worked and directed user to correct page. 
    - Collapse navbar worked on smaller screens across all browsers and was accessible through a hamburger icon.
    - Accordians and dropdowns worked on all browsers.
    - My account menu displayed correct options depending on user/superuser status.
    - The search bar worked across the site both from the nav bar and the footer.
    - The nav bar search element appears in collapsable menu for screens. 
    - All social links are opened in separate tabs. 
    - Toasts appear and are clear to the user when actions have been successful. 

- Index Page
    - CTA button directs user to the 'all bands' page. 
    - Category tiles expand when mouse moves over them. They all link to the 'all bands' page and display correct bands by category. 
    - Icons at bottom of page rotate when mouse moves over them. 
    - The links all direct the user to the correct page. 
    - 'My bokings' page only accessible if user logged in.
    - All sections are responsive and are formatted accordingly.

- Musicians Page
    - All page quick links work and filter the results due to what link is chosen. 
    - All buttons take the user to the diesired page. 
    - 'Location' has overflow added to avoid being too long a list. 
    - 'Location' venues also display the correct number of bands in that location. 
    - The cards are fully resposive showing from anywhere between four cards to one card per row depending on screen size. 
    - The search results at the top of the screen tells the user how many bands have been returned by the query. There is also a link to clear the query and display all bands again. 
    - If no image is present for a band, then a generic image appears in it's place.
    - The band cards are paginated to 12 cards per page. This also takes any arguments or queries added by the user and paginates the results successfully across the pages. 

- Band Profile
    - All buttons take the user to desired page.
    - Large image is replaced by smaller image if and when one is selected.
    - Ratings are calculated as an average of from the reviews. If no ratings or reviews, then that is communicated to the user. 
    - Suggested band cards are responsive to the screen size. 
    - If superuser is logged in, they can choose to edit the band information. This takes the superuser to a form which is automatically filled in with the current information in the database. 

- New Bookings Page
    - If the user creates a new booking, the form displayed is clear and responsive. 
    - Form validation is present, allowing the user to only leave address2 and additional information blank. 
    - The wedding date field is only editable via the jQuery datepicker. This also allows the field to be formatted correctly. 
    - The start time field automatically updates any integer in 24hr clock format. 
    - The 'clear form' button clears all fields. 
    - The 'create booking' button saves the form information and adds the information to the booking model. 
    - The image displayed on the page correlates to the band currently being booked. 

- My Bookings Page/Payment
    - Bookings that have been paid for appear as confirmed and likewise, those not paid for appeear as unconfirmed. 
    - Tooltips appear when delete or review icons are hovered over. 
    - The delete icon opens a modal to confirm whether the user wishes to delete this booking. 
    - The review icon leads the user to a review page. 
    - The checkout button takes the user to a checkout page incorporating Stripe functionality. 
    - The payment page also itemises unpaid bookings and displays total which is currently being paid for. 
    - The Stripe payment function (which is in test mode) was tested with both a successful payment card number as well as various card errors which are avaiable in the Stripe docs. 
    - On successful payment, the user is directed back to the booking page where all bookings are now confirmed.

- Blogs 
    - Blogs cards are responsive depending on screen size. 
    - They grow as the user moves their mouse over each card. 
    - The card displays date where the blog was last updated. 
    - All links to social media and the blog source open in new tabs. 
    - Blogs are rendered with line breaks. 

- Add/Edit forms
    - All forms are rendered correctly and are responsive. 
    - All form validation is present and correct.
    - Editing forms display content already present on database. 
    - Ratings form prevents user from going above 5 or below 1 for the rating. 

- Delete functions
    - All delete functions remove objects from database. 

- Security
    - Using the @login_required decorator enforces all users to be logged in to view member pages. If user is not logged in, they are directed to the sign in page. 
    - Similarly, this is the case for all pages that are only available to the superuser. 
    - If users try and direct to a band profile page or blog page that doesn't exist they are directed to the error page. From here, the user may use the navigation bar or the home button to direct back to a safe place. 

### Validation

HTML, CSS and Python code was all tested using online validators. 

#### HTML Validator

The following pages passed validation successfully:
Index, band profile, blog page, read blog, login, my bookings, add review, add band, add blog, edit band, edit blog. 
 
The following error appeared when testing the bands page:
![Image of html error](media/html-error1.png)

This is due to the variable having a space in it. This has been corrected using javascript and replacing all spaces in links to '%20'

#### CSS Validator

All CSS passed without error

#### Flake8

The following errors appear when running <code>python3 -m flake8</code> in the terminal. 

![Image of Flake8 errors](media/flake8.png)

The errors displayed are all either in automativcally generated files, or deal with <code>null=True</code> being used on string based fields. 

No errors were found when running python code through [PEP8 Online Check](http://pep8online.com/checkresult)


### Testing User Stories

|#|Results|
|---|---|
|US01|The purpose of the website is clear from the index page. The header and subtitle make it clear the site's purpose. The four stages of making a booking at the end of the index page explains the steps clearly. The imagery on the index page further backs the site's function.|
|US02|Across the site, there are many ways the user may navigate to the bands page. Most commonly, this will be done through the nav bar menu. A link is also available in the footer and via various buttons across the pages. |
|US03|The blogs are easy to navigate to via the nav bar menu|
|US04|Users can search for bands using the search bar in the nav bar or the footer. These are visible across all pages|
|US05|Location and price can be filtered using the quick links on the 'all bands' page|
|US06|Viewing a bands profile page will display details, cost, ratings and location to the user|
|US07|Reviews are available to read on the band's profile page|
|US08|Suggestions for similar bands appear on the band's profile page. These are filtered through bands in the similar category and are chosen at random|
|US09|Blogs are available through the blogs page.|
|US10|Blogs can be shared directly to social media via the icons at the end of the blog. The post is made automatically meaning the user just needs to share.|
|US11|Social media links are displayed in the footer across all pages on the site.|
|US12|Contact information is displayed in the footer across all pages on the site.|
|US13|Account registration is accessible through the My Accounts tab in the nav bar as well as as a link on the home page. Users are also navigated directly to sign in and registration if they try and access a page or make a booking without logging in.|
|US14|Bookings can be made via each band's profile page. They can input all necessary information needed to create a booking for the band.|
|US15|All bookings made by the user are available to view on the my bookings page.|
|US16|Once payment has been received, all bookings are automatically confirmed.|
|US17|All confirmed bookings are available on the my bookings page. |
|US18|From the 'my bookings' page, users who have confirmed and paid for a band may then leave a review for that particular band. |
|US19|Bookings that aren't yet paid for or confirmed may be deleted. Before deletion is successful, the user must confirm this via the modal. |
|US20|Account information can be updated and recovered on the log in pages.|
|US21|Bands can be added from the Add Bands tab under My Account. Band information can be updated from their band profile page. |
|US22|Blogs can be added from the Add Blog tab under My Account, alternatively, from the Blogs page. From the Blogs page, the superuser is able to delete and edit the blogs too. |



    


# Deployment


# Credits






