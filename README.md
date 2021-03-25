# DevOps Core Fundamental Project
- I created a Shopping List App.

# Requirements
- A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project.

- A relational database used to store data persistently for the project, this database needs to have at least 2 tables in it, to demonstrate your understanding, you are also required to model a relationship.

- Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment.

- A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board.

- Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach.

- A functioning front-end website and integrated API's, using Flask.

- Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

# Trello Board
![alt text](https://github.com/WeePickMeUp/DevOps-Core-Fundamental-Project/blob/main/images/trello%20board.PNG)
- You can find my updated Trello Board here https://trello.com/b/7HEuH9vk/simple-project-board

# Database Layout
![alt text](https://github.com/WeePickMeUp/DevOps-Core-Fundamental-Project/blob/main/images/Shopping%20List%20Database.jpg)

# My Design Process
To begin my creation of my app I used GCP to host a Virtual Linux Machine. Using a startup script from my peer, I  was able to install VS Code directly on the the VM and bypass having to ssh into the VS Code terminal using Remote Desktop Connection. I was able to use my VMs GUI and input my code directly onto the VS Code installed on the VM. Using a folder template from QA Community I created all my folders and all my files and made a basic app which responds "Hi". I then began planning my app and put in research into strengthening certain areas of my fundamentals as well as using everything I managed to learn. I then decided that I would make a Shopping List app. So using MySQL to create a database, I created my first table and some basic routes to create a single html that would store some information and have the ability to remove it. I then began writing tests for these routes and my app and it did not go well. So I put it on hold  
  

This is a diagram showing you the flow of my pipeline and how I have integrated all that we have been taught. MySQL database is hosted on GCP along with my Virtual Machine (VM). All my code is then written in VsCode, which is installed on my VM, and this is linked to my GitHub repository. All my changes are pushed to my develop branch to make sure that there are no conflicts between branches. Then my testing is again written in VsCode and is tested using pytest, this is to make sure that there are no errors in my code and that the pass rate returns at 80% or above. If successful and the pass rate is above 80%, the code is then pushed to my develop branch before merging with the master branch. If unsuccessful, or the pass rate is lower than 80% then I return to the previous step and check the errors in my code and fix any issues. Once the code has been pushed to my master branch, Jenkins can run and host the live application.

# Risk Assessment
![alt text](https://github.com/WeePickMeUp/DevOps-Core-Fundamental-Project/blob/main/images/risk%20assessment.PNG)

# Test Results
![alt text](https://github.com/WeePickMeUp/DevOps-Core-Fundamental-Project/blob/main/images/test.PNG)
![alt text](https://github.com/WeePickMeUp/DevOps-Core-Fundamental-Project/blob/main/images/test2.PNG)

# Jenkins
![alt text](https://github.com/WeePickMeUp/DevOps-Core-Fundamental-Project/blob/main/images/jenkins.PNG)
I deployed my app under the name Hello World. 

# References
- My images can be found im my Public Repository "WeePickMeUp-DevOps-Core-Fundamental-Project-Images": https://github.com/WeePickMeUp/WeePickMeUp-DevOps-Core-Fundamental-Project-Images
- I used a startup script in my Linux VM to pre-install VS Code and worked directly on my instance through Remote Desktop connection. This was given to me by a peer. Unfortunately I don't have a direct link to the repository he stored the script in but the script is located in startup.bash

- I used everything I've learnt from Dara Oladapo and QA Community to contribue to my code: https://www.youtube.com/user/DaraOladapo | https://qa-community.co.uk/~/_/learning

- I used Stack Overflow for general error queries through my coding: https://stackoverflow.com/

- For Pytest help I used these YouTube videos: https://youtu.be/7BJ_BKeeJyM | https://youtu.be/bbp_849-RZ4

- For Python help I also needed some support from:
https://www.w3schools.com/python/default.asp

- For HTML help I also needed some support from:
https://www.w3schools.com/html/default.asp

- To get a better understanding of project structure and CRUD fundamentals I used: https://www.digitalocean.com/community/tutorials/build-a-crud-web-app-with-python-and-flask-part-one | https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

- I also used a Live Tutorial on YouTube to understand the design process of a CRUD app and what you can do in HTML:
https://youtu.be/XTpLbBJTOM4

- To build a base for my app and understand what each line of code does I used a Todo app tutorial:
-https://youtu.be/yKHJsLUENl0
