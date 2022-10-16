import json
from urllib import response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from users.serializers import UserSerializer


class UserTestCase(APITestCase):
    userData = {
        "name": "Michael",
        "phone": "4545454545454545",
        "email": "example@email.com",
        "address": "Madrid,Madrid"
    }

    def test_create_user(self):
        # creates the user
        response = self.client.post(
            "/api/user", self.userData, format='json')

        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)

        # retrives the user just created
        responseData = json.loads(response.content.decode('utf8'))
        user_id = responseData["id"]

        response = self.client.get(
            f'/api/user/{user_id}'
        )

        # validates if the data is the same
        responseData = json.loads(response.content.decode('utf8'))

        self.assertEqual(responseData["email"], self.userData["email"])
        self.assertEqual(responseData["phone"], self.userData["phone"])
        self.assertEqual(responseData["name"], self.userData["name"])
        self.assertEqual(responseData["address"], self.userData["address"])

    def test_get_list_of_users(self):
        # get the list of users
        response = self.client.get(
            "/api/user")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_and_delete_user(self):
        # creates a new user
        response = self.client.post(
            "/api/user", self.userData, format='json')
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)

        # gets the user jsut created
        responseData = json.loads(response.content.decode('utf8'))
        user_id = responseData["id"]

        response = self.client.get(
            f'/api/user/{user_id}'
        )

        # Deletes the issue
        response = self.client.delete(f'/api/user/{user_id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Tries to get it again but fails because it has been deleted
        response = self.client.get(f'/api/assistance/{user_id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_and_updates_user(self):
        newUserData = {
            "name": "veronica",
            "phone": "565656565656",
            "email": "vero@email.com",
            "address": "Cuenca"
        }

        # creates a new user
        response = self.client.post(
            "/api/user", self.userData, format='json')
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)

        # updates the user jsut created
        responseData = json.loads(response.content.decode('utf8'))
        user_id = responseData["id"]

        response = self.client.put(
            f'/api/user/{user_id}', newUserData, format='json')

        # retrives the user just updated
        responseData = json.loads(response.content.decode('utf8'))
        user_id = responseData["id"]

        response = self.client.get(
            f'/api/user/{user_id}'
        )

        # check if it was updated
        responseData = json.loads(response.content.decode('utf8'))

        self.assertEqual(responseData["email"], newUserData["email"])
        self.assertEqual(responseData["phone"], newUserData["phone"])
        self.assertEqual(responseData["name"], newUserData["name"])
        self.assertEqual(responseData["address"], newUserData["address"])

    def test_registered_fucntionU(self):
        # checks if user if registered
        response = self.client.get(
            f'/api/user/registered/{self.userData["email"]}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # creates the user
        response = self.client.post(
            "/api/user", self.userData, format='json')

        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)

        # checks if user if registered
        response = self.client.get(
            f'/api/user/registered/{self.userData["email"]}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
