Requirements are for 2 functions:

addAction(string) returning error
  Take JSON serialized input string with the form:
    {"action":"actionName", "time":integer input}
  Save the action names, and give the average time that is recorded

getStats() returning string
  returns a serialized JSON array of the average time for each action that has been added via addAction

Lastly, assume that the end user will be making concurrent calls into all functions

The submission needs to be documented, tested, and organized

-------------------------------

To solve this, I have the actions_challenge.py function, which has the class and the 2 functions that we want.  Then, I have testing.py, which contains all the unit tests for this code.

addAction needs to be able to see if the new action already exists
  if it exists, it needs to record the average time provided.  To do this, we need to record either the sum of all the times provided, or the average time provided.  We also need to record the number of times a time has been provided.
    If we record the sum, then we can run into the risk of integer overflow if too many numbers are added.  If we record the average, then we risk losing some fidelity if we record the average as integers.
    Because the loss of fidelity is going to cause more minor errors than the sum, I will be recording the sum and getting the average by dividing it by the number of instances before it is returned.
    Note, we could probably get around this by storing data as a double, and only presenting the results as an integer later.
  If the action doesn't already exist, a new element needs to be added to the list with one element recorded.

getStats needs to have access to the list of actions, and list out the action and the average time
  This is fairly simple, and just iterates through the list and prints out everything inside

For testing, the following tests are used:
  addAction - input non-json message - return an error
  addAction - input json message, no "action" provided - return an error
  addAction - input json message, no "time" provided - return an error
  addAction - input json message, add action to list and return no error

  getStats - request with no elements added, return string of empty array
  getStats - request with 1 element added
  getStats - request with 2 different elements added
  getStats - request with 1 element added multiple times
  getStats - request with 2 different elements added multiple times
