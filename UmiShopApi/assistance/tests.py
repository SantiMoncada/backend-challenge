import json
from rest_framework import status
from rest_framework.test import APITestCase
from assistance.serializer import AssistanceSerializer


class AssistanceTestCase(APITestCase):
    issueData = {
        "email": "person@example.com",
        "topic": "Sales",
        "address": "Madrid, Madrid",
    }

    def test_create_issue(self):
        # creates an issue
        response = self.client.post(
            "/api/assistance", self.issueData, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # retrives the issue just created
        responseData = json.loads(response.content.decode('utf8'))
        issue_id = responseData["id"]
        response = self.client.get(
            f'/api/assistance/{issue_id}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checks if the issue has the correct shape
        responseData = json.loads(response.content.decode('utf8'))
        serializer = AssistanceSerializer(data=responseData)
        self.assertTrue(serializer.is_valid())

        # validates if the data is the same
        self.assertEqual(responseData["email"], self.issueData["email"])
        self.assertEqual(responseData["topic"], self.issueData["topic"])
        self.assertEqual(responseData["address"], self.issueData["address"])

    def test_get_issues_list(self):
        # gets the list of issues
        response = self.client.get(
            "/api/assistance")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_and_delete_issue(self):
        # creates a new issue
        response = self.client.post(
            "/api/assistance", self.issueData, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # gets the issue just created
        responseData = json.loads(response.content.decode('utf8'))
        issue_id = responseData["id"]
        response = self.client.get(
            f'/api/assistance/{issue_id}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deletes the issue
        response = self.client.delete(f'/api/assistance/{issue_id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Tries to get it again but fails because it has been deleted
        response = self.client.get(f'/api/assistance/{issue_id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
