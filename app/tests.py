import json
from django.test import TestCase
from django.urls import reverse

from app.factories import (
    UserFactory,
    AlertNotificationFactory,
)

test_user = {"username": "testuser", "password": "testpassword"}


class NotificationMessageCreateAPIViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory(username=test_user["username"], password=test_user["password"])
        self.url = reverse('alert_create')
        self.alert_msg = "account spend is too high"

    def get_token(self):
        res = self.client.post(
            '/api/token/',
            data=json.dumps({
                'username': test_user["username"],
                'password': test_user["password"],
            }),
            content_type='application/json',
        )
        result = json.loads(res.content)
        self.assertTrue("access" in result)

        return result["access"]

    def test_create_message_forbidden(self):
        data = {
            'user': self.user,
            'alert_status': 'info',
            'alert_msg': self.alert_msg,
        }
        response = self.client.post(self.url, params=data)
        self.assertEquals(response.status_code, 401)

    def test_create_message_invalid(self):
        token = self.get_token()
        data = json.dumps({
            'user': self.user.id,
            'alert_status': 'info',
        })
        response = self.client.post(
            self.url, 
            data=data, 
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEquals(response.status_code, 400)

    def test_create_message_ok(self):
        token = self.get_token()
        data = json.dumps({
            'user': self.user.id,
            'alert_status': 'info',
            'alert_msg': self.alert_msg,
        })
        response = self.client.post(
            self.url, 
            data=data, 
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        self.assertEquals(response.status_code, 201)
        result = json.loads(response.content)["data"]
        self.assertEquals(result["alert_status"], 'info')
        self.assertEquals(result["alert_msg"], self.alert_msg)


class NotificationMessageListAPIViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory(username=test_user["username"], password=test_user["password"])
        self.alert_msg = "no products in the merchant center"
        self.url = reverse('alert_list')

    def get_token(self):
        res = self.client.post(
            '/api/token/',
            data=json.dumps({
                'username': test_user["username"],
                'password': test_user["password"],
            }),
            content_type='application/json',
        )
        result = json.loads(res.content)
        self.assertTrue("access" in result)

        return result["access"]

    def test_get_alert_messages(self):
        token = self.get_token()
        AlertNotificationFactory(
            user = self.user,
            alert_msg = self.alert_msg,
        )
        res = self.client.get(
            self.url,
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}',
        )

        self.assertEquals(res.status_code, 200)
        result = json.loads(res.content)["data"]
        self.assertEquals(len(result), 1)  # 1 records
        self.assertTrue(result[0]["alert_msg"] == self.alert_msg)

    def test_get_empty_alert_messages(self):
        token = self.get_token()
        res = self.client.get(
            self.url,
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {token}',
        )

        self.assertEquals(res.status_code, 200)
        result = json.loads(res.content)["data"]
        self.assertEquals(len(result), 0)  # no records



    