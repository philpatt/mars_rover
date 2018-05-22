# Mars Rover Tech Challenge -- Python
  ###Prompt: 
  [Mars Rover Tech Challenge Prompt](https://code.google.com/archive/p/marsrovertechchallenge/)  

  ### *Test Input*
  * 5 5 (Landing Area)
  * 1 2 N (First Rover initial position)
  * LMLMLMLMM (Command sequence to land First Rover)
  * 3 3 E (Second Rover initial position)
  * MMRMMRMRRM (Command sequence to land second Rover)
  ### *Expected Output*
  * 1 3 N (First Rover final position coordinates and direction)
  * 5 1 E (Second Rover final position coordinates and direction)

  ## Install Python
  * run `brew install python3` in your console

  ## Run Tests
  * For Main.py tests run `python3 maintests.py` in console
  * For Mars.py tests run `python3 marstests.py` in console

  ## Run Program
  * To begin Run `python3 main.py` in console
  * Next, you will be prompted to enter Landing Area dimensions: (Example Input: `5 5`)
```
===============================
~~ MARS ROVER TECH CHALLENGE ~~
===============================

--------------
** Please enter two numbers, separated by a space, to determine the dimensions for the Mars landing Area:
--------------
 =>
 ```
  * After determining the Landing Area dimensions, you will be prompted to create a Rover starting position. You may also enter `report` to get a *Rover Report* or `end` to terminate the program:(Example Input: `1 2 N`) 
 ```
 --------------
 ** Enter a Rover's starting position and direction.
* Or enter 'report' to get Rover Report.
* Or enter: 'end' to terminate:
--------------
=>
 ```
* Once a Rover's initial coordinates have been created, you will be asked to send a sequence of landing commands to for the Rover. The Rover will compute these commands to attempt to land:(Example input `LMLMLMLMM`)
```
--------------
Please enter a sequence of commands:
Only use 'L','R','M' or 'end' to terminate
--------------
=>
```
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


  