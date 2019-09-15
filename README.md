# news-word-association

This repo contains several plots comparing the words used by different TV news stations on 2019-09-13, the day following the third debate of Democratic presidential candidates. These exploratory graphs show the words most associated with some TV stations, and the words that most distinguishes a station, based on term frequencies. 

The plots are created using [Scattertext](https://github.com/JasonKessler/scattertext) in python, with data from [GDELT Project's Television News Ngram Datasets](https://blog.gdeltproject.org/announcing-the-television-news-ngram-datasets-tv-ngram/).

Static preview of plot comparing words associated with CNN and Fox News captured on 2019-09-13. 

![](https://raw.githubusercontent.com/fanghuiz/news-word-association/master/cnn-fox.png)

Some words are not labeled to make the plot more readable, but in the interactive version linked below, you can see all the words by mouse-over the dots, or by typing a word in the search box on the page. Try typing in some candidates' names! (Only 1000 most frequenly used words are included in the my visualizations here, for computation reasons, because my computer is old :turtle:)

So how to read the plot? Each dot corresponds to a word used by CNN or Fox News on 2019-09-13. In this plot, CNN is on the y-axis, and Fox news is on the x-axis.

* Dots closer to the top of the plot are words more frequently used by CNN.
* Dots further to the right hand side are words used more frequently by Fox News. 
* Words more associated with CNN are blue, and words more associated with Fox News are red.
* **Upper right corner**: High frequency words used by both stations, e.g. "donald", "sanders" (not labeled on static image)
* **Upper left cornder**: Words frequently used by CNN, but rarely used by Fox News, e.g. "bahamas", "dorian" (not labeled)
* **Bottom right corner**: Words frequenly used by Fox News, but not by CNN, e.g. "fbi", "maccabe" (probably Andrew McCabe, which CNN mentioned exactly 0 times).
* **Bottom left corner**: Low frequency words for both stations.

Interactive versions comparing different TV stations (takes a few moments to load). 

* [ABC - Fox News](https://fanghuiz.github.io/news-word-association/plot/abc_fox_20190913.html)
* [CBS - Fox News](https://fanghuiz.github.io/news-word-association/plot/cbs_fox_20190913.html)
* [CNN - Fox News](https://fanghuiz.github.io/news-word-association/plot/cnn_fox_20190913.html)
* [MSNBC - Fox News](https://fanghuiz.github.io/news-word-association/plot/msnbc_fox_20190913.html)
* [NBC - Fox News](https://fanghuiz.github.io/news-word-association/plot/nbc_fox_20190913.html)
* [PBS - Fox News](https://fanghuiz.github.io/news-word-association/plot/pbs_fox_20190913.html)
