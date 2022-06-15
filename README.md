<h1 align="center" style="color:red;"> How people are reacting to </h1>

Final project of the Distributed Computing 2022-2 class, taught by [Dr. Victor de la Luz](https://github.com/itztli) (<vdelaluz@enesmorelia.unam.mx>) and Dr. Héctor Guzmán (<guzman@enesmorelia.unam.mx>) at *[Universidad Nacional Autónoma de México](https://www.unam.mx/)* (National Autonomous University of Mexico | UNAM) [http://www.gicc.unam.mx/](http://www.gicc.unam.mx/), in its *[Escuela Nacional de Estudios Superiores, Unidad Morelia](https://www.enesmorelia.unam.mx/)* (National School of Superior-Level Studies, *Morelia* Campus | ENES).

> 1-2-3-team/Distributed-Computing-Project is licensed under the MIT License

# Equipo 1,2,3

# Team Members:
- [Sofia De La Rosa](https://github.com/SofiaDeLaRosa) (<chapatulita@gmail.com>)
- [Ana Paola Carreón Hernández](https://github.com/Mordran) (<anapcahe@gmail.com>)
- [Luis Yovanny Bedolla Galvan](https://github.com/GalvanLuis) (<gruisu93@gmail.com>)


## Introduction
[Twitter](https://es.wikipedia.org/wiki/Twitter) is a social networking service where there are no limits or censorship at the time of sharing and posting in exchange for that liberty Twitter can be used as a tool that shows collective behaviors and significant social functions that have been studied in the fields of semiotic communication, the social construction of information and knowledge and other collective phenomena.

In this case, the main subject is to investigate the position that people have regarding "x" topic on twitter, in this way we can observe what kind of majority dominates and if such topic can even be controversial or quite talked about. 

## Objectives
The aim of this project is to analyze the slant of tweets to determine where people stand on an issue. 


## Libraries

- [NumPy](https://numpy.org/)

- [Tweepy](https://github.com/tweepy/tweepy)

- [TextBlop](https://textblob.readthedocs.io/en/dev/)

## Methodology

We create a program that calcultates the sentiment of a tweet through [TextBlop](https://medium.com/red-buffer/sentiment-analysis-let-textblob-do-all-the-work-9927d803d137) and returns the percentages of whether a tweet is strongly postitive, weakly positive, positive, neutral, weakly negative, negative or strongly negative. <br>

TextBlop provides us numeric values for polarity and subjectivity. Polarity describes how much a text is positive or negative, whereas subjectivity describes how much a text is objective or subjective. For this, TextBlob uses a process defined in [_text.py](https://github.com/sloria/TextBlob/blob/eb08c120d364e908646731d60b4e4c6c1712ff63/textblob/_text.py) and each word in the lexicon is scored as follows: <br>

1. polarity: negative vs. positive (-1.0 → +1.0)
2. subjectivity: objective vs. subjective (+0.0 → +1.0)
3. intensity: modifies next word? (x0.5 → x0.2) <br>

These lexicons are referred to in [en-sentiment.xml](https://github.com/sloria/TextBlob/blob/eb08c120d364e908646731d60b4e4c6c1712ff63/textblob/en/en-sentiment.xml). 

## Running



## Results

We graph if the percentages of whether a tweet was strongly postitive, weakly positive, positive, neutral, weakly negative, negative or strongly negative given a word. <br>

 ![alt text](https://github.com/1-2-3-team/Distributed-Computing-Project/blob/main/02_processing/chart.png)
 
## References:

> Lin, C., 2022. How to Build a Real-Time Twitter Analysis Using Big Data Tools. [online] Medium. Available at: <https://towardsdatascience.com/how-to-build-a-real-time-twitter-analysis-using-big-data-tools-dd2240946e64> [Accessed 18 April 2022].
> https://medium.com/red-buffer/sentiment-analysis-let-textblob-do-all-the-work-9927d803d137
> https://github.com/sloria/TextBlob/tree/eb08c120d364e908646731d60b4e4c6c1712ff63




