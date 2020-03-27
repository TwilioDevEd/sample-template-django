from unittest.mock import Mock, patch

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from twilio.base.exceptions import TwilioException


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.headless = True
        cls.selenium = WebDriver(chrome_options=opts)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def _send_sms(self):
        phone_number = self.selenium.find_element_by_name('to')
        phone_number.send_keys('11111')
        message_body = self.selenium.find_element_by_name('body')
        message_body.send_keys('Test message')
        self.selenium.find_element_by_css_selector('button[type="submit"]').click()

    @patch('sample_app.views.Client')
    def test_send_sms_invalid_number(self, fake_twilio):
        # Arrange
        client = Mock()
        client.messages.create.side_effect = TwilioException('Boom!')
        fake_twilio.return_value = client
        timeout = 2

        # Act
        self.selenium.get(self.live_server_url)
        self._send_sms()

        WebDriverWait(self.selenium, timeout).until(
            lambda driver: 'alert-danger'
            in driver.find_element_by_id('dialog').get_attribute('class')
        )

        # Assert
        self.assertEqual(client.messages.create.call_count, 1)
        dialog = self.selenium.find_element_by_id('dialog')
        dialog_title = self.selenium.find_element_by_id('dialogTitle')
        dialog_content = self.selenium.find_element_by_id('dialogContent')
        self.assertNotIn('d-none', dialog.get_attribute('class'))
        self.assertIn('Error', dialog_title.text)
        self.assertIn('Failed to send SMS', dialog_content.text)

    @patch('sample_app.views.Client')
    def test_send_sms_valid_number(self, fake_twilio):
        # Arrange
        client = Mock()
        client.messages.create.return_value = Mock(sid='asdf123')
        fake_twilio.return_value = client
        timeout = 2

        # Act
        self.selenium.get(self.live_server_url)
        self._send_sms()
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: 'alert-success'
            in driver.find_element_by_id('dialog').get_attribute('class')
        )

        # Assert
        self.assertEqual(client.messages.create.call_count, 1)
        dialog = self.selenium.find_element_by_id('dialog')
        dialog_title = self.selenium.find_element_by_id('dialogTitle')
        dialog_content = self.selenium.find_element_by_id('dialogContent')
        self.assertNotIn('d-none', dialog.get_attribute('class'))
        self.assertIn('SMS Sent!', dialog_title.text)
        self.assertIn('SMS sent to 11111.', dialog_content.text)
