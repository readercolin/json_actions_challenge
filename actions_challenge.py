import json
from threading import Lock


class actionChallenge(object):
    def __init__(self):
        """Initializer"""
        # actionDict contains all the actions that have been recorded
        # actions are recorded as the action name as the keyword, and then
        # an internal dictionary with "totalTime" and "numActions" as its
        # elements.  To access the dictionary, use
        # self.actionDict["actionName"], and then
        # self.actionDict["actionName"]["totalTime"] or
        # self.actionDict["actionName"]["numActions"] to access the internal
        # dictionary
        self.actionDict = {}
        self.actionMutex = Lock()

    def addAction(self, jsonInput):
        """Take JSON input of actions and time and add to list.

        This function takes the input as a JSON message.  The expected format
        is {"action":"actionName", "time":integerValue}.
        After receiving the message, it records the action name in a class list
        and records the time in a form that it can get the average time
        provided.
        """
        try:
            jsonDict = json.loads(jsonInput)
        except Exception:
            # error in getting json value
            return "error: invalid JSON"
        # check for action and time in incoming JSON data
        if "action" not in jsonDict:
            return "error: action not found"
        if "time" not in jsonDict:
            return "error: time not found"
        # JSON contains data, get mutex and add to dictionary
        self.actionMutex.acquire()
        try:
            if jsonDict["action"] in self.actionDict:
                self.actionDict[jsonDict["action"]]["totalTime"] += (
                    jsonDict["time"])
                self.actionDict[jsonDict["action"]]["numActions"] += 1
            else:
                self.actionDict[jsonDict["action"]] = {
                    "totalTime": jsonDict["time"], "numActions": 1}
        finally:
            self.actionMutex.release()
        return "success"

    def getStats(self):
        returnDict = []
        self.actionMutex.acquire()
        try:
            for key in self.actionDict:
                returnDict.append(
                    {"action": key,
                     "avg": int(self.actionDict[key]["totalTime"] /
                                self.actionDict[key]["numActions"])
                     }
                )
        finally:
            self.actionMutex.release()
        return json.dumps(returnDict)
