# Internet Speed Twitter Bot

A Python script that uses Selenium to check your internet speed and tweet about it on Twitter if the speed doesn't meet the promised internet speed.

## Features

- Checks your internet speed using [Speedtest](https://www.speedtest.net/).
- Tweets a message on Twitter about your internet speed if it's below the promised speed.
- Automatically logs in to Twitter using your credentials.

## Prerequisites

- Python 3.x
- Chrome WebDriver (make sure the version matches your Chrome version)
- Internet connection
- Twitter account credentials

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ulquiorraexe/twitter-bot.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your operating system and place it in your project directory.

## Usage

1. Set up your email and password in the `main.py` file:
   
   ```python
   MAIL = "your_email@example.com"
   PASSWORD = "your_password"
   ```

2. Run the bot:

   ```bash
   python main.py
   ```

   The bot will:
   - Check your internet speed on [Speedtest](https://www.speedtest.net/).
   - If the speed is below the promised values, it will tweet the following message on Twitter:
     ```
     Hey Internet Provider, why is my internet speed {down} down/{up} up?
     ```
   - The bot will also log in to your Twitter account using the credentials provided.

## How It Works

- The bot first navigates to [Speedtest](https://www.speedtest.net/) to get the current internet speed.
- It then compares the speed with the promised download and upload speeds.
- If the speed is below the promised speeds, the bot automatically logs into Twitter, writes a tweet with the speed information, and posts it.

## Customization

You can change the promised download and upload speeds in the following lines of the `main.py` file:

```python
PROMISED_DOWN = 20  # Change this value to your expected download speed
PROMISED_UP = 10    # Change this value to your expected upload speed
```

## Notes

- Make sure your internet speed is available and stable while running the script.
- You may need to adjust the XPaths in the script if the website layout changes.

## License

This project does not have a license.
