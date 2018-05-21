# Mars Rover Tech Challenge
## Instructions:  

  * A squad of robotic rovers are to be landed by NASA on a plateau on Mars.
  * This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.
  * A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
  * In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.
  * 'M' means move forward one grid point, and maintain the same heading.
  * Assume that the square directly North from (x, y) is (x, y+1).
### *Input*:
  * The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
  * The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.
  * The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.
  * Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.
### *Output*:
  * The output for each rover should be its final co-ordinates and heading.

 #### *Test Input*
  * 5 5 (Landing Area)
  * 1 2 N (First Rover initial position)
  * LMLMLMLMM (Command sequence to land First Rover)
  * 3 3 E (Second Rover initial position)
  * MMRMMRMRRM (Command sequence to land second Rover)
 #### *Expected Output*
  * 1 3 N (First Rover final position coordinates and direction)
  * 5 1 E (Second Rover final position coordinates and direction)
  
## User Stories

As a user, I want to be able to:
  * Search through all of the national parks
  * View more details about each park
  * Save the park to my profile if it is one that interests me
  * Also, delete anyone 

## Aproach 

### *Sprint 1*
* Wireframe application using draw.io
![trello-1](/public/img/readme-img/wireframe-1.png)  

* Setup Trello Board
![trello-1](/public/img/readme-img/trello-1.png)

* Add and populate gitignore file
* Decide on technologies
* Create database - models/associations
* Basic folder structure
* HTML for index.js filled out
* Stub out routes
* Empty ReadMe  

### *Sprint 2* 

* Add Basic styling
* Reach MVP functionality
  * Save api information to db
* Deploy to heroku

* Debug 
![trello-1](/public/img/readme-img/trello-3.png)  

### *Sprint 3*

* Finishing Touches
* Advanced Styling
* Fill out ReadMe
* Begin strech goals
![trello-4](/public/img/readme-img/trello-4.png)

## Steps to Setting Up
* 

## Backlog
* Give users ability to comment on the different parks
* Allow users to have a more customized profile page (add profile picture)
* Images to search results (web scrape wikipedia)
* Like/dislike column -- star system