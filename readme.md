# **Background Remover Bot**

A Telegram bot that uses AI image processing to remove the background from images.

## **Getting Started**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### **Prerequisites**

- Python 3.6 or later
- **[pyrogram](https://github.com/pyrogram/pyrogram)**
- **[rembg](https://pypi.org/project/rembg/)**

### **Installing**

1. Clone the repository

```
git clone https://github.com/habitual69/cutimagebg_bot.git
```

1. Install the requirements

```
pip install -r requirements.txt
```

1. create .env file and put API_ID, API_HASH,BOT_TOKEN varible with values

2. Run the bot

```
python bot.py
```

## **Deploying the Telegram Bot using Docker**

This guide will show you how to deploy the Telegram bot using Docker.

### **Prerequisites**

- **[Docker](https://www.docker.com/)** installed on your machine
- Telegram API credentials (API ID ,API hash, BOT TOKEN)
- **`.env`** file containing Telegram API credentials

### **Building the Image**

To build the Docker image, run the following command in the root directory of the project:

```
docker build -t my_bot .
```

This command will create an image with the name 'my_bot' using the current directory as the build context.

### **Running the Container**

To run the Telegram bot in a Docker container, use the following command:

```
docker run -it --env-file .env my_bot
```



## **How to use**

- Start a conversation with the bot.
- Send an image to the bot.
- The bot will use AI image processing to remove the background from the image and send the new image back to you.

## **Deployment**

The bot can be deployed on a server or a hosting platform, such as Heroku.

## **Built With**

- **[pyrogram](https://github.com/pyrogram/pyrogram)** - MTProto library for Telegram
- **[rembg](https://pypi.org/project/rembg/)** - A python library for removing the background from images.

## **Contributing**

Please read **[CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426)** for details on our code of conduct, and the process for submitting pull requests to us.

## **Authors**

- **Your Name** - *Initial work* - **[Your GitHub](https://github.com/habitual69)**

## **License**

This project is licensed under the MIT License - see the **[LICENSE.md](https://raw.githubusercontent.com/git/git-scm.com/main/MIT-LICENSE.txt)** file for details

## **Acknowledgments**

- Hat tip to anyone whose code was used
- Inspiration
- Thanks to **[Daniel Gatis](https://github.com/danielgatis)** for rembg

## **Demo Bot**
**[Background Remover](https://t.me/cutimagebg_bot)**