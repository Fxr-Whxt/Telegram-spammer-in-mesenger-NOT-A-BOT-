# Telegram Spammer in Messenger (NOT A BOT)

**Disclaimer: This is a test program designed for educational purposes to understand the libraries used for Telegram!**

## Description

This script allows you to spam messages to people on Telegram. All you need is your Telegram ID, hash, and phone number.

## Prerequisites

To get your Telegram ID and hash:
1. Visit [telegram.org](https://telegram.org)
2. Register a developer account to get your ID and hash
3. You will also need your phone number associated with your Telegram account

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Fxr-Whxt/Telegram-spammer-in-messenger-NOT-A-BOT-.git
    cd Telegram-spammer-in-messenger-NOT-A-BOT-
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your Telegram ID, hash, and phone number in the script.

## Usage

Run the script and follow the prompts:

1. **Account to send messages to**: Enter the username or ID of the recipient.
2. **Message to repeat**: Enter the message you want to spam.

By default, the script will send 100 messages. You can change this parameter in the code.

### Example of changing parameters in the code:
```python
# Change the number of messages to be sent
number_of_messages = 100  # Default is 100