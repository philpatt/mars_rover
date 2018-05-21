# Mars Rover Tech Challenge
## Instructions:  

  * A squad of robotic rovers are to be landed by NASA on a plateau on Mars.
  * This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.
  * A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
  * In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.
  * 'M' means move forward one grid point, and maintain the same heading.
  * Assume that the square directly North from (x, y) is (x, y+1).

## User Stories
The target user group for this app is those who are planning to do a trip to see any of the US National Park, and those who might have already travelled to see these parks and want to keep track of what they have seen. 

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