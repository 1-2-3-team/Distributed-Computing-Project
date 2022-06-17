<h1 align="center" style="color:red;"> How people are reacting to </h1>

Final project of the Distributed Computing 2022-2 class, taught by [Dr. Victor de la Luz](https://github.com/itztli) (<vdelaluz@enesmorelia.unam.mx>) and Dr. Héctor Guzmán (<guzman@enesmorelia.unam.mx>) at *[Universidad Nacional Autónoma de México](https://www.unam.mx/)* (National Autonomous University of Mexico | UNAM) [http://www.gicc.unam.mx/](http://www.gicc.unam.mx/), in its *[Escuela Nacional de Estudios Superiores, Unidad Morelia](https://www.enesmorelia.unam.mx/)* (National School of Superior-Level Studies, *Morelia* Campus | ENES).


# Equipo 1,2,3

# Team Members:
- [Sofia De La Rosa](https://github.com/SofiaDeLaRosa) (<chapatulita@gmail.com>)
- [Ana Paola Carreón Hernández](https://github.com/Mordran) (<anapcahe@gmail.com>)
- [Luis Yovanny Bedolla Galvan](https://github.com/GalvanLuis) (<gruisu93@gmail.com>)

> 1-2-3-team/Distributed-Computing-Project is licensed under the MIT License





# Introduction
The first idea of this project was to analyze the "cancel culture" because there is a great debate about whether it infringes on freedom of expression or benefits the communication between people, but to tell the truth any word, phrase or #hashtag, could be analyzed to know the positions of people on the tweets that contain it.

Based on that idea we could think of a text string that normally makes people give their opinion about it.

As we read in the first paragraph we will use tweets, because twitter is one of the most popular and "free" platforms, and has lent itself to its users to give their opinion on different topics. 


# Objectives
The aim of our project is to obtain with a distributed system structure the opinion polarity of a sample taken from Twitter of tweets with a common word, phrase or hashtag every certain time in order to visualize its changes in real time.



# General system architecture
![Infrastructure](https://raw.githubusercontent.com/1-2-3-team/Distributed-Computing-Project/main/estructura.png)

![DatabaseStructure](https://raw.githubusercontent.com/1-2-3-team/Distributed-Computing-Project/main/db%20structure.jpeg)



# Toolset
* [Python 3.8.13](https://www.python.org/)
* [Tweepy 3.9.0](https://www.tweepy.org/) for data collection of tweets. 
* [Psycopg2](https://pypi.org/project/psycopg2/) For conection between python and the postgress database
* [NumPy](https://numpy.org/)
* [TextBlop](https://textblob.readthedocs.io/en/dev/)

# Methodology

To develop the project based on a word, phrase or hashtag we have taken a sample of 1000 tweets through the Twitter V2 API, this sample is analyzed by TextBlop which returns the polarity of the text in the following ranges [-3, -2, -1, 1, 2, 3] where a negative value is a negative polarity or opinion, while a positive value is a positive polarity or opinion.

# Usage

For usage please place the files to the next locations:

* Files inside 00_spider > Data server
* Files inside 02_processing > Processing server
* Files inside public_html > Web server

-Create crontab -e write inside Data server:
>*/30 * * * * /usr/bin/python3 ./path/to/00_spider/webcrawler.py
>*/31 * * * * /usr/bin/python3 ./path/to/00_spider/get_image.py

-Create crontab -e write inside Processing server:
>*/31 * * * * /usr/bin/python3 ./path/to/02_processig/processing.py

# Results

Every 30 minutes we get an image which gives us the percentages of polarity in the sample of tweets with a date and time when the script was executed.

![Results](https://raw.githubusercontent.com/1-2-3-team/Distributed-Computing-Project/main/02_processing/chart.png)

# Conclusions
People can have different kinds of opinions on many subjects and freedom of expression in all aspects of life is underpinned by the morality of the human being in the case of Twitter, freedom of expression is driven by the majority of people having an opinion on the same subject and the terms and conditios of Twitter.

With this little piece of software we can get a brief visualization of the polarity of the people's opinion about a topic.

# Reference
>Twitter API Documentation. (n.d.). Docs | Twitter Developer Platform. Retrieved June 15, 2022, from https://developer.twitter.com/en/docs/twitter-api
>Tweepy Documentation — tweepy 3.9.0 documentation. (n.d.). Tweepy. Retrieved June 15, 2022, from https://docs.tweepy.org/en/v3.9.0/
>TextBlob: Simplified Text Processing — TextBlob 0.16.0 documentation. (n.d.). TextBlop. Retrieved June 15, 2022, from https://textblob.readthedocs.io/en/dev/
>Nott, L. N. (n.d.). PERSPECTIVE: UNPACKING CANCEL CULTURE: IS IT CENSORSHIP, CIVIL RIGHT OR SOMETHING ELSE? Freedomforum.Org. Retrieved June 15, 2022, from https://www.freedomforum.org/2022/02/09/perspective-unpacking-cancel-culture-is-it-censorship-civil-right-or-something-else/
>3.8.13 Documentation. (n.d.). Python. Retrieved June 15, 2022, from https://docs.python.org/3.8/

Copyright
All licenses in this repository are copyrighted by their respective authors. Everything else is released under The MIT License. See LICENSE for details.
