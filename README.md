# Discord Bot

A powerful and easy-to-use Discord bot that plays music from YouTube. This bot is built using Python and discord.py, and it includes several useful features such as playing, leaving, and showing bot latency. Additionally, using this bot can help you earn the Active Developer Badge on Discord!

## Features

- **Play Music:** Search and play music from YouTube.
- **Leave Voice Channel:** Make the bot leave the voice channel.
- **Show Latency:** Check the bot's latency.
- **Member Join/Leave Notifications:** Greet new members and say goodbye when they leave.

## Requirements

- Python 3.8+
- [discord.py](https://github.com/Rapptz/discord.py)
- [youtube_dl](https://github.com/ytdl-org/youtube-dl)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/RautuA/Discord-Bot.git
    cd Discord-Bot
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Add your bot token and other configurations:**
    - Create a file named `apikeys.py` in the root directory.
    - Add your bot token and application ID:
      ```python
      BOTTOKEN = 'your_bot_token'
      ```

## Usage

1. **Run the bot:**
    ```sh
    python bot.py
    ```

2. **Commands:**
    - **`/ping`**: Show bot latency.
    - **`/leave`**: Leave the voice channel.
    - **`/play [music_name]`**: Play music from YouTube.

3. Replace placeholder text such as your_bot_token, insert_your_application_id, and insert your channel id with the appropriate values for your bot.

Earn the Active Developer Badge:
By using and developing this bot, you can apply for the Active Developer Badge on Discord.

To qualify:

Make sure your bot is active and used by users.
Visit the Discord Developer Portal for more information on the criteria and application process.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

