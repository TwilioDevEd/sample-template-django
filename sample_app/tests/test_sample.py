import json

from unittest.mock import Mock, patch

from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
from twilio.base.exceptions import TwilioException


class SampleViewsTest(SimpleTestCase):
    def test_index(self):
        # Arrange & Act
        response = self.client.get(reverse('sample_app:index'))

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_example(self):
        # Arrange & Act
        response = self.client.get(reverse('sample_app:example'))

        # Assert
        self.assertEqual(response.content, b'{"example": true}')

    @patch('sample_app.views.Client')
    def test_send_sms_fail(self, fake_twilio):
        # Arrange
        client = Mock()
        client.messages.create.side_effect = TwilioException('Boom!')
        fake_twilio.return_value = client

        # Act
        response = self.client.post(
            reverse('sample_app:send_sms'),
            json.dumps({'body': 'Test Message', 'to': '11111'}),
            content_type='application/json',
        )

        # Assert
        self.assertEqual(response.status_code, 500)
        self.assertIn(b'Failed to send SMS', response.content)

    @patch('sample_app.views.Client')
    def test_send_sms_success(self, fake_twilio):
        # Arrange
        client = Mock()
        client.messages.create.return_value = Mock(sid='asdf123')
        fake_twilio.return_value = client

        # Act
        response = self.client.post(
            reverse('sample_app:send_sms'),
            json.dumps({'body': 'Test Message', 'to': '11111'}),
            content_type='application/json',
        )

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b'SMS sent to 11111.')
        self.assertContains(response, b'SID: asdf123')
