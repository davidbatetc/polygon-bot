# Polygon Bot
This document describes the [Polygon Bot](https://github.com/jordi-petit/lp-polimomis-2020) project, a Python and ANTLR programming project of the course *Programming Languages* (Fall semester, 2020), which is part of the course offer of the *Facultat d'Informàtica de Barcelona* (FIB - UPC). This project consists of a [Telegram](https://telegram.org/) bot that replies with text messages and images to operations related to convex polygons.

## Table of contents
*(to be automatically written)*


## Installation
### Installing Python and the Python libraries
The following instructions have been tested on Ubuntu and as a consequence they might differ slightly in other operating systems. The first thing that we need to do is make sure that we have Python3 installed on your computer. We can do so by running

```bash
$ python3 --version
```

This command gives us the Python3 version that we have on our computer if it is installed. Otherwise, we can install it with

```bash
$ sudo apt-get install python3
```

After installing Python3, we need to install the libraries that the program uses and are not included by default with the Python3 installation. In order to do so, we can use the `requirements.txt` file of the project. However, we first need to download the project files in a folder that we can later access. When we have done so, we can access this folder and run

```bash
$ python3 -m pip install -r requirements.txt
```

This command will download the Python3 libraries that are needed for this project and not included in the Python3 installation by default.

### Installing ANTLR
The installation guide for ANTLR is available on the [official repository](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) of the project. Once ANTLR is installed, it might be a good idea to access the `./cl` folder and run

```bash
$ antlr4 -Dlanguage=Python3 -no-listener -visitor Poly.g
```

This command will create again ANTLR's automatically generated files for the grammar defined in `./cl/Poly.g`, making sure that all the changes that have been made to ANTLR or the grammar are properly applied.

## Getting started
### Setting up the Telegram bot
In order to run a Telegram bot, we first have to create it. To do so, we have to [install Telegram](https://telegram.org/) and send the message `/newbot` to the Telegram user [`@BotFather`](https://t.me/BotFather), which is the official Telegram bot for managing and creating new Telegram bots. By following the instructions given by the bot, we can easily create a new bot. When creating our bot, the [`@BotFather`](https://t.me/BotFather) will give us a private token that we will use to access the Telegram API.

After creating our bot, we need to create a new file inside the `./bot` folder with the name `token.txt` and save the token inside this file. This will be used by the project files in order to run the bot. Note that this token should be kept private, since any person with this token would be able to take control of our bot.

### Running the Telegram bot
Running our Telegram bot is as easy as accessing the `./bot` folder and running the command

```bash
$ python3 bot.py
```

This command will bring our bot to life and we will now be able to interact with it. Once our bot is running, we can send messages to the bot by accessing the link [https://t.me/NameOfOurBot]().


## Project files
The files of this project can be split into three kinds of files:
- The file the contains the `ConvexPolygon` class and all of its associated definitions.
- The files of the compiler, which make the execution of a program in our programming language possible.
- The files used to interact with Telegram and run the Telegram bot.



## References
- [[num]](https://github.com/jordi-petit/lp-polimomis-2020) [Programming Languages](https://www.fib.upc.edu/en/studies/bachelors-degrees/bachelor-degree-informatics-engineering/curriculum/syllabus/LP) (Fall 2020). [*Decision Trees*](https://github.com/jordi-petit/lp-polimomis-2020). [FIB - UPC](https://www.fib.upc.edu/). [Accessed: December 27, 2020]
- [[num]](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) [ANTLR](https://www.antlr.org/). [*Getting started with ANTLR v4*](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md). [Accessed: December 27, 2020]
- [[num]](https://telegram.org/) [Telegram](https://desktop.telegram.org/). [*Telegram Messenger*](https://desktop.telegram.org/). [Accessed: December 27, 2020]
