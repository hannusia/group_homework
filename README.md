## Project name: sentimental_analysis_project

## Description: 
This project aims to build a web-application that can:
* do sentimental analysis for English and Ukrainian texts
* determine if text is acceptable for immature audiences
* work with instagram, twitter and facebook posts

## Table of Contents:

### screens:
contains screnshoots from Wiki-pages examples

### docs:
contains project documentation

### examples:
contains examples of results of every stage of homework

### modules:
contains all program modules
* <i>adt.py, twitter_api.py</i> - module to extract text from tweet
* <i>analyze.py</i> - module that analyzes text and returns final data to build diagram and worldcloud
* <i>cusswords.txt, мати.txt</i> - contains dirty words and cusswords for english and ukrainian
* <i>diagram_builder.py</i> - module that uses data from <i>analyze.py</i> and returns image of diagram and worldcloud
* <i>divide.py</i> - module with ADT and other classes to process text and perform sentimental analysis
* <i>url_check.py</i> - check if input on website is a raw text or a link
* <i>read_file.py</i> - contains all functions to read information from different files(txt and tsv)
* <i>web.py</i> - module that creates website
* <i>templates</i> - folder with html-files that are used in web

### tests:
contains modules for program testing
* <i>test.py</i> - contains unittests for testing <i>divide.py</i> and <i>analyze.py</i>

### Wiki pages:
* [Homework №1 results](https://github.com/hannusia/group_homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%961)
* [Homework №2 results](https://github.com/hannusia/group_homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%962)
* [Homework №3 results](https://github.com/hannusia/group_homework/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)

## Installation:
```bash
$ git https://github.com/hannusia/group_homework.git
$ cd group_homework
$ pip install -r requirements.txt
```

## Usage:
1) You can follow instructions from instalation and run Flask app at [modules/web.py](https://github.com/hannusia/group_homework/blob/main/modules/web.py)
or open the [website](https://task-16.herokuapp.com/)
2) After this you have to enter some text in english or in ukrainian(or link to a twitter post) and press submit-button then you will see sentimental analysis of your text



## Contributing:
If you want to contribute in one way or another, open an issue or clone and install the project using the abovementioned installation instructions, opening up the pull request once you are finished

## Credits: 
Hanna Yershova, Yana Holoborodko, Oleksandra Tkachenko, Maksym Tsapiv, Mykhailo Kuzmyn,
UCU, 2021

## License:
MIT License
