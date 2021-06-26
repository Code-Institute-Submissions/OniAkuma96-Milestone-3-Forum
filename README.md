# R3view

R3view, pronounced review, is a forum for discussion of a wide range of topics.
Here registered users are free to post and reply to posts made by other users on anything their heart desires.
Posts will have a title, image and description, all compulsory to make a post, and users are free to read and post replies to posts or other replies inside a post, no title and optional image.
This site is for registered users who want free and open discussion and also for non-registered users who wish to read the posts.
The site will display posts and replies in order of date submitted and will uses a like system visible on a user's profile.

## Features

### Existing Features

- __Navigation Bar__

    - The site will contain x pages and users will be able to navigate through them at the top of the page.
    - Some navigation links will only be available to registered users.

### Features Left to Implement

## Technologies Used

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Micro web framework written in Python to build application

- [Heroku](https://dashboard.heroku.com/login)
    - For deployment of Python application

- [MongoDB]()
    - As a database for storing infomation

- [jQuery]()

- [Materialize]()

- [Font Awsome]()

## Testing

### Validator Testing

### Unfixed Bugs

- On submit new post form the label text of 'title' doesn't go up as it should and blocks the title as it is written.

- When subbmitting post the description sometimes displays as none.

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