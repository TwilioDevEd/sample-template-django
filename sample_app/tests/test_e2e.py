from unittest.mock import Mock, patch

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUp(cls):
        super().setUp(cls)
        opts = Options()
        opts.headless = True
        cls.selenium = WebDriver(chrome_options=opts)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDown(cls):
        cls.selenium.quit()
        super().tearDown(cls)

    @patch('sample_app.views.Client')
    def test_send_sms_invalid_number(self, fake_twilio):
        client = Mock()
        client.messages.create.side_effect = Exception('Boom!')
        fake_twilio.return_value = client
        timeout = 2
        self.selenium.get('%s%s' % (self.live_server_url, '/sample-app/'))
        send_sms(self.selenium)
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: 'alert-danger'
            in driver.find_element_by_id('dialog').get_attribute('class')
        )
        self.assertEqual(client.messages.create.call_count, 1)
        dialog = self.selenium.find_element_by_id('dialog')
        dialog_title = self.selenium.find_element_by_id('dialogTitle')
        dialog_content = self.selenium.find_element_by_id('dialogContent')
        assert 'd-none' not in dialog.get_attribute('class')
        assert 'Error' in dialog_title.text
        assert 'Failed to send SMS' in dialog_content.text

    @patch('sample_app.views.Client')
    def test_send_sms_valid_number(self, fake_twilio):
        class MessageFake:
            sid = 'asdf123'

        client = Mock()
        client.messages.create.return_value = MessageFake()
        fake_twilio.return_value = client
        timeout = 2
        self.selenium.get('%s%s' % (self.live_server_url, '/sample-app/'))
        send_sms(self.selenium)
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: 'alert-success'
            in driver.find_element_by_id('dialog').get_attribute('class')
        )
        self.assertEqual(client.messages.create.call_count, 1)
        dialog = self.selenium.find_element_by_id('dialog')
        dialog_title = self.selenium.find_element_by_id('dialogTitle')
        dialog_content = self.selenium.find_element_by_id('dialogContent')
        assert 'd-none' not in dialog.get_attribute('class')
        assert 'SMS Sent!' in dialog_title.text
        assert 'SMS sent to 11111.' in dialog_content.text


def send_sms(selenium):
    phone_number = selenium.find_element_by_name('to')
    phone_number.send_keys('11111')
    message_body = selenium.find_element_by_name('body')
    message_body.send_keys('Test message')
    selenium.find_element_by_css_selector('button[type="submit"]').click()
