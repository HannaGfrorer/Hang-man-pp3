## Hangman game 

#### This game is a word game where the goal is to guess the word by selecting different letters until the word is complete. The user is presented with a number of blank spaces representing the missing letters that they will need to find. This game was created to complete the third portfolioprodject for Code Insitute's Full Stack Software Developer course.

#### Live Site [Here]()

![alt text]()

#### How to play


## Features


## Future features


## Technologies used

### Languages
. Python

## Frameworks, Deployement & Libraries

* [Github](https://github.com/)

* [Gitpod](https://gitpod.io)

## Testing

* Testing was done throughout the project mainly by running the program in the terminal as well as python debugger. I committed the codes to github after writing every new list or code.

* I used the deployed site to manually type correct and incorrect data to validate and see how the program responded.

## Accessibility

* The whole project was built using python, therefore no other langueges were used.

## Issues and bugs


## Fixed bugs



## Validator Testing
I ran through my file in [](https://pep8ci.herokuapp.com/)


## Deployment

I followed the below steps when deploying my project to Heroku, based on the Code Institute instructions:

* Add to requirements.txt file:-
pip3 freeze > requirements.txt
Commit changes to Github:
git commit -m "Add requirements for deployment”

In HEROKU after creating the account:

1. "Create new App"

2. Give the App a unique name and enter region

3. Click on "Create App"

4. Click on "Settings" on your new App Dashboard

5. Scroll down to Config Vars where in my instance I only inserted KEY: PORT and VALUE: 8000 since I have no creds.json files to add.

6. Press Add-button

7. Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon for Nodejs and save changes. These Buildpacks need to be in below order:

Python NodeJS

8. Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter search for my Github Repository "Parents Allowance Calculator" and then click connect.

9. Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to github automatically updates in Heroku.

10. Then in the Manual Deploy section, press Deploy Branch.

11. After project has been deployed successfully I clicked the View-button to see the program run in the terminal.

## Credits

[Kite] https://www.youtube.com/watch?v=m4nEnsavl6w
My whole project is based on his youtube tutorial. however, I have tried to change a bit but have largely coded with him in his video.

[Meyaal] https://github.com/Meyaal/Hangman-game/blob/main/run.py
I used this for some code

Pages I used to solve errors and other problems and some code: https://stackoverflow.com/ 
https://www.programiz.com/python-programming/docstrings
https://www.edureka.co/blog/indentation-error-in-python/
https://medium.com/@gdsc.cu/python-project-for-beginners-part-2-6f9f372e58da
https://realpython.com/invalid-syntax-python/
https://www.w3schools.com/python/python_conditions.asp
https://www.geeksforgeeks.org/python-docstrings/

## Special Thanks

A big thank you to tutor suport who helped me through this project with a lot of patience and always nice treatment.

A big thank you to Liz_5P who was there with her incredible knowledge and supported me when it was most difficult. She's the best.

A special thanks my mentor Martina Terlević which always makes me feel like I can pull this off. She always cheers me on and is there to support me all the way. She is a star.
