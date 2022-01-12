<a  href="https://www.twilio.com">
<img  src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg"  alt="Twilio"  width="250"  />
</a>
 
# Twilio Sample App Template

[![Actions Status](https://github.com/TwilioDevEd/sample-template-django/workflows/Django%20CI/badge.svg)](https://github.com/TwilioDevEd/sample-template-django/actions)

## About

This is a GitHub template for creating other [Twilio] sample/template apps. It contains a variety of features that should ideally be included in every Twilio sample app. You can use [GitHub's repository template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) functionality to create a copy of this.

Implementations in other languages:

| .NET | Java | Ruby | PHP | NodeJS                                                        |
| :--- | :--- | :--- | :-- | :------------------------------------------------------------ |
| TBD  | TBD  | TBD  | TBD | [Done](https://github.com/twilio-labs/sample-template-nodejs) |

### How it works

This is only a barebones python/Django application. Whenever, possible we should be using this. However, if you are using another framework like Flask that comes with their own standardized application structure, you should try to merge these by using the same `README` structure and test coverage, configuration etc. as this project.

<!--
**TODO: UML Diagram**

We can render UML diagrams using [Mermaid](https://mermaidjs.github.io/).


**TODO: Describe how it works**
-->

## Features

- [Django](https://www.djangoproject.com/) framework version 3
- User interface to send SMS with bootstrap.
- End to End UI testing using [Selenium](https://www.selenium.dev/)
- [Automated CI testing using GitHub Actions](/.github/workflows/django.yml). Windows workflow is not included as there is an issue with the chrome driver and the selenium tests.
- Linting using [flake8](https://flake8.pycqa.org/en/latest/)
- Formatting using [Black](https://github.com/psf/black)
- Project specific environment variables using `.env` files.
- One click deploy buttons for Heroku, Glitch and now.sh
- Pre-commit hooks using [pre-commit](https://pre-commit.com/) to ensure standardized code style and formatting.

## How to use it

1. Create a copy using [GitHub's repository template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) functionality
2. Update the [`README.md`](README.md) with the respective values.
3. Build your app as necessary while making sure the tests pass.
4. Publish your app to GitHub

## Set up

### Requirements

- [Python](https://www.python.org/downloads) version >= **3.6.x**.
- [ChromeDriver](https://chromedriver.chromium.org/) for the `Selenium` tests. Ensure the `chromedriver` executable is on the OS `path`. For Linux/Mac the easiest way to do this is to install it through the OS package manager:
  - Mac:
    ```bash
    brew install --cask chromedriver
    ```
  - Ubuntu:
    ```bash
    sudo apt-get install chromium-chromedriver
    sudo ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
    ```
- A Twilio account - [sign up](https://www.twilio.com/try-twilio)

### Twilio Account Settings

This application should give you a ready-made starting point for writing your
own appointment reminder application. Before we begin, we need to collect
all the config values we need to run the application:

| Config&nbsp;Value | Description                                                                                                                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account&nbsp;Sid  | Your primary Twilio account identifier - find this [in the Console](https://www.twilio.com/console).                                                         |
| Auth&nbsp;Token   | Used to authenticate - [just like the above, you'll find this here](https://www.twilio.com/console).                                                         |
| Phone&nbsp;number | A Twilio phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) - you can [get one here](https://www.twilio.com/console/phone-numbers/incoming) |

### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it

   ```bash
   git clone git@github.com:twilio-labs/sample-template-django.git
   cd sample-template-django
   ```

1. Create a virtual environment and activate it

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. Set your environment variables

   ```bash
   cp .env.example .env
   ```

   See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

1. Configure pre-commit hooks

   ```bash
   pre-commit install
   ```

1. Run the application

   ```bash
   python manage.py runserver
   ```

   This will start a development server. It will reload whenever you change any files.

1. Navigate to [http://localhost:8000](http://localhost:8000)

That's it!

### Tests

**NOTE:** Be sure you have Google Chrome installed with the same version as the `chromedriver` installed earlier. Usually it's the latest version. 

You can run the tests locally by typing:

```bash
python manage.py test
```

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. Here is a small selection of them.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

| Service                           |                                                                                                                                                                |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Heroku](https://www.heroku.com/) | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/sample-template-django/tree/master) |

**Some notes:**

- For Heroku, please [check this](https://devcenter.heroku.com/articles/django-app-configuration) to properly configure the project for deployment.
- [Glitch](https://glitch.com/) is not included because it only supports NodeJS officially. Instead, you can try [PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/) which is a similar alternative por Python projects.
- [Zeit Now](https://zeit.co) is also not included because it uses a serverless architecture which doesn't work with frameworks such as Django.

## Resources

- [GitHub's repository template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) functionality

## Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).

[Visit the project on GitHub](https://github.com/twilio-labs/sample-template-django)

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com
