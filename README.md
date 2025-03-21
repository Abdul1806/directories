## Directories INFO: 
### You have 2 ways of interacting with this python script: 
  - Command line interface and writing a command (CREATE, DELETE, MOVE, LIST) one at a time
    ### or
  - Using the 'TEST' command to run the given prepopulated commands. You would need to adjust the value of command1 or command2, whichever variable you pass into process.

## To run the code
1. Pull in this github repo to your local
2. Navigate to directories folder
3. run the script with:  ``` python3 directories.py ```
4. Have fun testing!


## Some thoughts
- I added additional behavior (TEST) that allowed me to test the code in a more efficient manner instead of constantly going through each command one at a time
- I made the user experience for moving files not result in error if destination path doesn't exist. Instead we actually create it and then move it there.


## The problem

A common method of organizing files on a computer is to store them in hierarchical directories. For instance:

 

```

photos/

  birthdays/

    joe/

    mary/

  vacations/

  weddings/

```

 

In this challenge, you will implement commands that allow a user to create, move and delete directories.

 

A successful solution will take the following input:

 

```

CREATE fruits

CREATE vegetables

CREATE grains

CREATE fruits/apples

CREATE fruits/apples/fuji

LIST

CREATE grains/squash

MOVE grains/squash vegetables

CREATE foods

MOVE grains foods

MOVE fruits foods

MOVE vegetables foods

LIST

DELETE fruits/apples

DELETE foods/fruits/apples

LIST

```

 

and produce the following output

 

```

CREATE fruits

CREATE vegetables

CREATE grains

CREATE fruits/apples

CREATE fruits/apples/fuji

LIST

fruits

  apples

    fuji

grains

vegetables

CREATE grains/squash

MOVE grains/squash vegetables

CREATE foods

MOVE grains foods

MOVE fruits foods

MOVE vegetables foods

LIST

foods

  fruits

    apples

      fuji

  grains

  vegetables

    squash

DELETE fruits/apples

Cannot delete fruits/apples - fruits does not exist

DELETE foods/fruits/apples

LIST

foods

  fruits

  grains

  vegetables

    squash

```
