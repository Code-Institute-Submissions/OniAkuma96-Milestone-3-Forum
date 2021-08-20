# R3view

R3view is a forum for discussion on anything, the emphasis is on free discussion by its users. Here registered users are free to make posts and reply to posts. 
Posts will have a title, body, and linked image while replies will just have a body and image (optional). 
Posts will also have some additional info such as who made the post, at what time, and on what day. Posts and replies are displayed newest first.
Registered users will be able to navigate to their profile page to see all the posts they have made.
This site is for registered users who want free and open discussion by making posts and replying to other posts and also for non-registered users who wish to read the posts.

[Live link to finished site](https://r3view.herokuapp.com/)

## User Stories

- As a non-registered user I want to register. From the homepage I can click on rigister in the navbar and register once I provide a valid username and password.

- As a registered user I want to make a post. I log in by clicking on log in in the navigation bar, then click on the new post button on the homepage.

- As a registered user I want to edit a post I made. I navigate to the profile page in the navbar and find the post I would like to edit. I click the edit button and make the changes before submitting.

- As a non-registered user I want to read replies to a post. I can click on the view replies button of the post I want to see.

- As a registered user I want to log out. I can click on logout in the navbar.

- As a registered user I want to delete a reply I made. I find the post in question and click on the view replies button, I find my reply and click delete.

## Wireframes

These are the wireframes that I made for this project. Can be found in /static/wireframes folder.

![Homepage Web](/static/wireframes/homepage-web.png)

![Profile Page Web](/static/wireframes/profile-web.png)

![Register/Login Web](/static/wireframes/register-login-web.png)

![View Post and Replies Web](/static/wireframes/view-post-replies-web.png)

![Homepage Tablet](/static/wireframes/homepage-tablet.png)

![Profile Page Tablet](/static/wireframes/profile-tablet.png)

![Register/Login Tablet](/static/wireframes/register-login-tablet.png)

![View Post and Replies Tablet](/static/wireframes/view-post-replies-tablet.png)

![Homepage Mobile](/static/wireframes/homepage-phone.png)

![Profile Page Mobile](/static/wireframes/profile-phone.png)

![Register/Login Mobile](/static/wireframes/register-login-phone.png)

![View Post and Replies Mobile](/static/wireframes/view-post-replies-phone.png)

## Features

### Existing Features

- __Navigation Bar__

    - The site will contain a few pages and users will be able to navigate through them at the top of the page.
    - Some navigation links will only be available to registered users.
    - Registered users can navigate to the profile page which has all their posts displayed.
    - Registered users also have the option to sign out.
    - Users that are not logged in will have the option to register or sign in if already registered.

- __Register and Login__

    - Users are free to register with a username and password. Registered users can login by providing their username and password.

- __Profile Page__

    - Registered users can navigate to the profile page to see all the posts they have made.

- __New Post Button__

    - Registered users are free to make new posts from the homepage.

- __View Replies Button__

    - Both registered and non-registered users are free to view replies to a certain post.
    - Clicking this button will go to a page with the post in question and all replies to said post indented below.

- __Reply Button__

    - Only registered users are allowed to make replies, which are then displayed.

- __Delete Post/Reply__

    - Users can delete posts/replies they have made.

- __Edit Post/Reply__

    - Users can edit a post/reply they have made.

### Features Left to Implement

- Like system

    - A system where registered users can 'like' a post or a reply, wont change how much the post or reply is seen as that is dictated by submission date/time.

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](https://www.python.org/doc/)

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Micro web framework written in Python to build application

- [Heroku](https://dashboard.heroku.com/login)
    - For deployment of Python application

- [MongoDB](https://www.mongodb.com/)
    - As a database for storing infomation

- [jQuery](https://jquery.com/)

- [Materialize](https://materializecss.com/)
    - For a webpage framework

- [Font Awsome](https://fontawesome.com/)
    - For icons

## Testing

To validate my code I used [W3 HTML validator](https://validator.w3.org/), [Jigsaw validator](https://jigsaw.w3.org/css-validator/), and [Python syntax checker](https://extendsclass.com/python-tester.html)

I used Google Chrome on my windows 10 PC throughout the process of making this site so I know everthing works well on that side of things. I can make, edit, view, and delete posts and replies and all the features work as intended. I have tested the game and all other features using the inspect feature offered by Chrome too to test different screen sizes. I have also tested my site with Edge and Firefox browsers to ensure everything works on them aswell.
I have also tested on an iPad mini, a Macbook Air, a Samsung Galaxy J3. Here was my testing procedure for these devices.

- Testing registration and login functionality
    - From homepage navigate to register.
    - Tried submitting form with invalid data, which does not work.
    - Submitted form with valid data.
    - Navigate to login and provide username and password recently created.
    - Successful login redirects user to their profile, as intended.
    - Click logout and successfully log out.

- Testing CRUD
    - Login if not already logged in.
    - Navigate to homepage and click on new post button.
    - Try submitting post with invalid data, which does not work.
    - Submit post with valid data.
    - Post is submitted and displayed on the homepage and user's profile.
    - Click view replies and click reply button.
    - Submit valid reply which is then displayed under the post, indented to differentiate between posts and replies.
    - Click edit on the post and change the title and description before submitting, edit is successful and the timestamp on the post successfully shows it has been edited and the time it was edited at.
    - Click edit reply on the reply I made just now. Change reply descriptiona and submit, everything works as intended.
    - Click delete on reply then post, both are successfully deleted.

### Unfixed Bugs

## Deployment

- I deployed my app to Heroku after getting Flask running by doing the following:

1 Created requirements.txt file so Heroku knows what it needs to run app using pip3 freeze --local > requirements.txt command in terminal.

2 Created Procfile needed for Heroku to run app using echo web: python app.py > Procfile command in terminal.

3 Logged in to Heroku and clicked on 'create new app', set app name to r3view, and region to Europe.

4 On deploy tab clicked on Connect to GitHub button to setup automatic deployment. Searched for repo name and clicked connect.

5 Navigate to settings tab and reveal Config Vars and added keys and values.

6 Back in GitPod pushed requirements.txt and Procfile, enabled automatic deployment on Heroku, and clicked deploy branch. Heroku confirmed app was successfully deployed.

## Credits

### Content

### Media

### Code