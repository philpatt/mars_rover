# Mars Rover Tech Challenge -- Python
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
   #### *Test Input*
  * 5 5 (Landing Area)
  * 1 2 N (First Rover initial position)
  * LMLMLMLMM (Command sequence to land First Rover)
  * 3 3 E (Second Rover initial position)
  * MMRMMRMRRM (Command sequence to land second Rover)

### *Output*:
  * The output for each rover should be its final co-ordinates and heading.
 #### *Expected Output*
  * 1 3 N (First Rover final position coordinates and direction)
  * 5 1 E (Second Rover final position coordinates and direction)

## How to Run program
 * If python is not installed, run `brew install python3` in your console
 * To begin Run `python3 main.py` in console
 * Next, you will be prompted to enter Landing Area dimensions:
 ```
 ** Please enter two numbers, separated by a space, to determine the`
 dimensions for the Mars landing Area:
--------------
 =>
 ```
   * Try entering `5 5`
 * After determining the Landing Area dimensions, you will be prompted to create a Rover starting position. You may also enter `report` to get a *Rover Report* or `end` to terminate the program:
 ```
 --------------
 ** Enter a Rover's starting position and direction.
* Or enter 'report' to get Rover Report.
* Or enter: 'end' to terminate:
--------------
=>
 ```
   * Try entering `1 2 N`
* Once a Rover's initial coordinates have been created, you will be asked to send a sequence of landing commands to for the Rover. The Rover will compute these commands to attempt to land:
```
--------------
Please enter a sequence of commands:
Only use 'L','R','M' or 'end' to terminate
--------------
=>
```
   * Try entering `LMLMLMLMM`
* If the landing is successful, you will be alerted with a `Rover Landing Successful!` message and `** Rover Report **`

```
-----------------------
 ** Rover Report **
-----------------------
Mars landing area:
5 x 5

1 3 N
-----------------------
```
Then prompted to land another Rover, end the program, or get another Rover Report Status.

```
--------------
** Enter a Rover's starting position and direction.
* Or enter 'report' to get Rover Report.
* Or enter: 'end' to terminate:
--------------
=> end

========================
### End Program ###
========================
```

 