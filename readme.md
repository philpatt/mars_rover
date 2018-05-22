# Mars Rover Tech Challenge -- Python
## Prompt:
[Mars Rover Tech Challenge Prompt](https://code.google.com/archive/p/marsrovertechchallenge/)  
### *Input*:
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
 --------------
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

 