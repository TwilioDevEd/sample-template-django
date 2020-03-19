import json

from unittest.mock import Mock, patch

from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class SampleViewsTest(SimpleTestCase):
    def test_index(self):
        response = self.client.get(reverse('sample_app:index'))
        self.assertEqual(response.status_code, 200)

    def test_example(self):
        response = self.client.get(reverse('sample_app:example'))
        self.assertEqual(response.content, b'{"example": true}')

    @patch('sample_app.views.Client')
    def test_send_sms_fail(self, fake_twilio):
        client = Mock()
        client.messages.create.side_effect = Exception('Boom!')
        fake_twilio.return_value = client
        response = self.client.post(
            reverse('sample_app:send_sms'),
            json.dumps({'body': 'Test Message', 'to': '11111'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 500)
        assert 'Failed to send SMS' in str(response.content)

    @patch('sample_app.views.Client')
    def test_send_sms_success(self, fake_twilio):
        class MessageFake:
            sid = 'asdf123'

        client = Mock()
        client.messages.create.return_value = MessageFake()
        fake_twilio.return_value = client
        response = self.client.post(
            reverse('sample_app:send_sms'),
            json.dumps({'body': 'Test Message', 'to': '11111'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)
        assert 'SMS sent to 11111.' in str(response.content)
