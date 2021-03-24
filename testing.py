from actions_challenge import actionChallenge
import json
import unittest


class actionChallengeTest(unittest.TestCase):

    def setUp(self):
        """The set up function, runs before every test."""
        self.ac = actionChallenge()

    def tearDown(self):
        """The tear down function, runs after every test."""
        print("--------------\n")

    def testAddNonJson(self):
        """Test addAction with non-JSON message."""
        print("--------------")
        print("Test add non-JSON message")
        result = self.ac.addAction("Hello")
        print(result)
        self.assertEqual(result, "error: invalid JSON")
        print("test success")

    def testAddNonAction(self):
        """Test addAction with a json message with no provided "action"."""
        print("--------------")
        print("Test add non-Action message")
        testDict = {"hello": "errors"}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        self.assertEqual(result, "error: action not found")
        print("test success")

    def testAddNonTime(self):
        """Test addAction with a json message with no provided "time"."""
        print("--------------")
        print("Test add non-Time message")
        testDict = {"action": "testError", "value": 10}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        self.assertEqual(result, "error: time not found")
        print("test success")

    def testAddAction(self):
        """Test addAction with a json message with valid input."""
        print("--------------")
        print("Test add correct action message")
        testDict = {"action": "testInput", "time": 10}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        self.assertEqual(result, "success")
        print("test success")

    def testGetEmptyStats(self):
        """Test getStats with no provided elements."""
        print("--------------")
        print("Test getStats with no elements")
        expected = (
            "[]"
        )
        print(expected)
        result = self.ac.getStats()
        print(result)
        self.assertEqual(result, expected)
        print("test success")

    def testGetSingleStats(self):
        """Test getStats with a single element added one time."""
        print("--------------")
        print("Test getStats with a single element")
        testDict = {"action": "testInput", "time": 10}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        expectedResult = [{"action": "testInput", "avg": 10}]
        expectedJson = json.dumps(expectedResult)
        result = self.ac.getStats()
        print(expectedResult)
        print(expectedJson)
        print(result)
        print("\n")
        self.assertEqual(result, expectedJson)
        print("test success")

    def testGetMultipleStats(self):
        """Test getStats with multiple elements added one time."""
        print("--------------")
        print("Test getStats with multiple elements")
        testDict = {"action": "testInput", "time": 10}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        testDict = {"action": "testFunction", "time": 25}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        expectedResult = [
            {"action": "testInput", "avg": 10},
            {"action": "testFunction", "avg": 25}
        ]
        expectedJson = json.dumps(expectedResult)
        result = self.ac.getStats()
        print(expectedResult)
        print(expectedJson)
        print(result)
        print("\n")
        self.assertEqual(result, expectedJson)
        print("test success")

    def testGetSingleRepeatedStats(self):
        """Test getStats with a single element with multiple inputs."""
        print("--------------")
        print("Test getStats with a single element added multiple times")
        testDict = {"action": "testInput", "time": 10}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        testDict = {"action": "testInput", "time": 20}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        expectedResult = [
            {"action": "testInput", "avg": 15}
        ]
        expectedJson = json.dumps(expectedResult)
        result = self.ac.getStats()
        print(expectedResult)
        print(expectedJson)
        print(result)
        print("\n")
        self.assertEqual(result, expectedJson)
        print("test success")

    def testGetMultipleRepeatedStats(self):
        """Test getStats with multiple elements and multiple inputs."""
        print("--------------")
        print("Test getStats with multiple elements added multiple times")
        testDict = {"action": "testInput", "time": 10}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        testDict = {"action": "testInput", "time": 20}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        testDict = {"action": "testFunction", "time": 20}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        testDict = {"action": "testFunction", "time": 40}
        testInput = json.dumps(testDict)
        result = self.ac.addAction(testInput)
        print(testInput)
        print(result)
        print("\n")
        self.assertEqual(result, "success")
        expectedResult = [
            {"action": "testInput", "avg": 15},
            {"action": "testFunction", "avg": 30}
        ]
        expectedJson = json.dumps(expectedResult)
        result = self.ac.getStats()
        print(expectedResult)
        print(expectedJson)
        print(result)
        print("\n")
        self.assertEqual(result, expectedJson)
        print("test success")


if __name__ == "__main__":
    unittest.main()
