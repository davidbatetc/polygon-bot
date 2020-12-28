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

### First interaction with the bot
The first message that we should send to the bot is `/start`. When the bot receives this command, it will present itself and it will guide us and help us understanding how it works. The commands `/help` and `/help program` will be especially useful to see what we can do with the bot. For now, we can see the execution of some sample programs using `/sample n`, where `n` is the number of the sample program. For example, running `/sample 4` will give us the corresponding program and the output of the program, which in this case is.


## Project files
The files of this project can be split into three kind of files:
- The file the contains the `ConvexPolygon` class and all of its associated definitions.
- The files of the compiler, which make the execution of a program in our programming language possible.
- The files used to interact with Telegram and run the Telegram bot.

### Class for convex polygons
The `polygons.py` file gathers all the definitions related to the `ConvexPolygon`. Among other things, this file defines `Point`, `Vector`, `Edge` and `Color` classes and includes methods such as a method that computes the convex hull of a set of points, a method that finds the intersection of two convex polygons or a method that returns whether a point is inside a convex polygon. This file is duly documented using docstrings. Hence, its documentation can be read accessing the root folder of the project and running

```python
>>> import polygons
>>> help(polygons)
```

inside Python's interactive environment, which can be accessed running

```bash
$ python3
```

### Compiler files
The files of the compiler are the ones inside the `./cl` folder. The file `./cl/Poly.g` defines the grammar of our programming language using ANTLR, while the file `./cl/PolyEval.py` defines a class that is used to evaluate the parse trees that ANTLR generates given a program in our language. All the other files are automatically generated by ANTLR using the grammar file. If any change is made to the grammar of the language, it is necessary to update this files. To do so, access the `./cl` folder and run

```bash
$ antlr4 -Dlanguage=Python3 -no-listener -visitor Poly.g
```

### Telegram bot files
The files corresponding to the Telegram bot itself are the ones included in the folder `./bot`. In particular, `bot.py` is the file that runs the bot and handles all the interactions with the Telegram API for bots. Note that, as mentioned before, we should have a file named `token.txt` with the token of our bot. The files with the names `sample-program-n.poly` are the sample programs that the bot showcases when the command `/sample n` is sent to the bot.


## Programming in the convex polygon language
When interacting with our Telegram bot, in order for the bot to understand the instructions related to operations with convex polygons, we will need to use the language that this project uses. While most of the available instructions are already explained with detail in [[1]](https://github.com/jordi-petit/lp-polimomis-2020), this project extends the list of commands by adding the following commands:
- `copy p` returns a copy of the polygon stored in the variable `p`. Note that in this case `p` has to be a variable.
- `regular n, r, cx cy, alpha` returns a regular polygon of radius `r` with `n` vertices and centered on the point `(cx, cy)`. `alpha` is the angle of rotation of the polygon, in radians. If the angle is zero, then the right-most vertex of the polygon lies on the line {y = `c.y`}.
- `translate p, vx vy` translates the polygon `p` by the vector `v = (vx, vy)`. Note that in this case `p` has to be a variable.
- `rotate p, alpha` rotates `p` an angle `alpha` around its centroid. Note that in this case `p` has to be a variable.
- `scale p, k` scales the polygon `p` with respect to its centroid by a factor `k`. Note that in this case `p` has to be a variable.

The full list of commands is duly documented and can be accessed by sending a message with `/help program` to our bot.


## Further comments
### Comparing floating point values
When implementing algorithms related to convex polygons, it has been detected that for some of the steps it is required that the comparisons are made with a certain numerical tolerance in mind. Otherwise, the algorithms fail due to numerical errors. Note that we have

```python
>>> 0 == 0.0000000001
False
```

whereas

```python
>>> abs(0 - 0.0000000001) <= 1e-9
True
```

For this reason, when testing for equality in the program, `abs(x - y) <= ε` is preferred over `x == y`, where `ε` is a given tolerance (for example `ε = 1e-9`). Analogously, `x - y < ε` is preferred over `x <= y`, and so on. The functions `eq`, `ge`, `le`, `gt` and `lt` are defined in `polygons.py` for this purpose.


### Error handling
Blablabla


## References
- [[1]](https://github.com/jordi-petit/lp-polimomis-2020) [Programming Languages](https://www.fib.upc.edu/en/studies/bachelors-degrees/bachelor-degree-informatics-engineering/curriculum/syllabus/LP) (Fall 2020). [*PolyBot*](https://github.com/jordi-petit/lp-polimomis-2020). [FIB - UPC](https://www.fib.upc.edu/). [Accessed: December 27, 2020]
- [[2]](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) [ANTLR](https://www.antlr.org/). [*Getting started with ANTLR v4*](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md). [Accessed: December 27, 2020]
- [[3]](https://telegram.org/) [Telegram](https://desktop.telegram.org/). [*Telegram Messenger*](https://desktop.telegram.org/). [Accessed: December 27, 2020]
