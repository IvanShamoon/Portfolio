# Ivan Shamoon's Portfolio

## About
This is a repository of all largescale personal projects and course work I have completed over my time learning and developing my toolset in Data Science. This repository will continually be updated will all the work I am proud to present to the public. It hopes to reflect the vast learning curve of data science of which I hope to cultivate and grow over time

## Table of contents

- [Country Social Factor Clustering](#country-social-factor-clustering)
- [Anime or  Adult Anime?](#anime-or-adult-anime)
- [Risk Calculator for Kidney Transplantation](#risk-calculator-for-kidney-transplantation)
- [LinkedIn Australian Data Job Scrape](#linkedin-australian-data-job-scrape)
- [Titanic Analysis](#titanic-dataset-analysis)


# [Country Social Factor Clustering](https://nbviewer.org/github/IvanShamoon/Portfolio/blob/main/social_cluster.ipynb)
This is a personal project made to examine the social factors of all countries and to deploy unsupervised machine learning techniques to create clusters. Through these techniques I managed to optimize models and create insightful clusters. The data is sourced through webscraping using the automated tool in Selenium and the other library in BeautifulSoup. The final project deployed onto PowerBi.

## [Dashboard ](https://github.com/IvanShamoon/Portfolio/blob/main/Social_factors_clustering/Country_clustering_dashboard.pdf)
This dashboard provides a clear visualisation for the data. The first page explores initial observations and the second pages explores the clustering analysis, and finally the final verdict reguarding the project's hypothesis. A PDF is provided because I lack the Microsoft's license.


## Project Objective
This project aims to determine if the social factors of each of the seven continents is distinctive enough to create their own clusters within the unsupervised learning process. In addition, I hope to optimize clustering through PCA and K-means using metrics such as inertia and variance explained. This project also hopes to provide visual aids and all around a descriptions of the final clusters and to perhaps piece them to their respective continent. 


## Methods Used
* Machine learning (k-means)
* PCA
* Ploty
* [Web Scraping (BeautifulSoup and Selenium)](https://github.com/IvanShamoon/Portfolio/blob/main/Social_factors_clustering/social_factors_scrap.ipynb)
* Data Cleaning
* Text processing


# [Anime or Adult Anime?](https://github.com/IvanShamoon/Portfolio/blob/main/Anime_scarpe/anime_or_adult_anime.ipynb)
This is a personal project inspired by course work to use text processing and machine learning. It is influenced by the binary comparison of spam and ham, and engages with an area many are interested in, anime. It examines the textual differences of anime and adult anime from summaries as listed from the cite [MyAnimeList](https://myanimelist.net/).

## Project Objective

This project deploys a variety of text processing and machine learning tools to investigate whether there's any differences between the summaries of Anime and Adult Anime. The main intention was of personal development in terms of data. However, there is no doubt an interest of the differences between these two bodies of work. Do certain genres engages more with wordplay than the other genre? Do certain words populate a genre more than the others? These questions are the main tenents of this project.

## Methods Used
* Web Scraping (BeautifulSoup)
* Data Cleaning
* Text processing
* Machine learning classifiers 

# [LinkedIn Australian Data Job Scrape](https://github.com/IvanShamoon/Portfolio/blob/main/Job_scrape/job_scrap.ipynb)
This is a personal project made to gain insight on the state of data science/analysis job listing in Australia. My main intention was to develop my web scarping abilities by learning how to use the automated tool Selenium. The data is deploy onto PowerBi for better visualisation and interactivity.

## [Dashboard](https://github.com/IvanShamoon/Portfolio/blob/main/Job_scrape/LinkedIn_jobscrap_dashboard.pdf)
This dashboard provides a hoslitics representation of the data. It is interactive allowing users to choose Australia states/industry to view initial observations in terms of common words/language/tools. A PDF is provided because I lack the Microsoft's license.

## Project Objective
This projects uses a variables of methods using Selenium to scrape off LinkedIn job listing. The chanllenge of this task was selecting item within the cite that is not immediately avaliable when clicking. It makes use of wait time and xpath to extract important information and to finally gather infromation for our the project's aim.


## Methods Used
* Web Scraping (Selenium)
* Data Cleaning
* Power Bi

# [Risk Calculator for Kidney Transplantation](https://kidneya6data3888.shinyapps.io/Data3888/)
This is a course project where we  were assigned the task to create a useful tool using gene expression data from patients. The team decided on a risk calulator deployed through Shiny R which takes in gene expression from a user's input to predict whether a certian collection of gene expression calulators a stable/rejection or kidney transplatation.


## Project Objective
This projects uses a variety of libraries and tools within R to analyse gene expression data to predict an outcome. The final app hoped to be used my medical researchers who would have stake in analysing a certain basket of genes for kidney research. Furthermore, it hoped to create a user friendly tool that is useful and intuitive.


## Methods Used
* Machine Learning Classifiers 
* Protein Pathway Analysis
* R Shiny App
* Linking symbol and gene name
* PCA

# [Titanic Dataset Analysis](https://github.com/IvanShamoon/Portfolio/blob/main/Titanic/titanic.ipynb)
This project is a personal project analysing the famous Titantic dataset, and was one of the first elementary datasets used to develop my data knowledge and tools deployment. 

## Project Objective
Reveal insighful information through data about the passengers of the Titanic tragedy and to use machine learning classifiers to predict whether a passenger survived or not.

## Methods Used
* Machine Learning Classifiers 
* Data Cleaning
* Chi-squared test
* Adjusted p-value
