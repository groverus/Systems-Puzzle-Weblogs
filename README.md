# Insight DevOps Engineering Systems Puzzle: Weblogs

## Table of Contents
1. [Understanding the puzzle](README.md#understanding-the-puzzle)
2. [Introduction](README.md#introduction)
3. [Puzzle details](README.md#puzzle-details)
4. [Assignments](README.md#assignments)
5. [Instructions to submit your solution](README.md#instructions-to-submit-your-solution)
6. [FAQ](README.md#faq)

# Understanding the puzzle

We highly recommend that you take a few dedicated minutes to read this README in its entirety before starting to think about potential solutions. You'll probably find it useful to review the codebase and understand the system at a high-level before attempting to find specific bugs.

# Introduction

Imagine you work for a company that has a webserver running. It is highly important to the companies success that the webserver is highly available. Unfortunately, the company currently has not data about the availability of the webserver. To fix this, they have tasked an engineer to build a pipeline that processes the logs and stores the results in a database. Data scientists can then query the database to analyze the availability of the system. The engineer came up with the following solution:
- The logs are ingested into a RabbitMQ queue (for the purpose of this challenge, this done via reading a given log file with a Python script - in reality, the logs would be sent straight from the webserver)
- A python script reads the messages from the RabbitMQ queue, processes it and stores the results in a PostgreSQL database
- An application server built in Flask queries the database to calculate the percentage of GET requests that have failed
- The application server can be accessed via an nginx webserver
All of this is developed with the Docker Engine, and put together with Docker Compose.


Unfortunately, the developer is new to many of these tools, and is having a number of issues. The developer needs your help debugging the system and getting it to work properly.

# Puzzle details

The codebase included in this repo is nearly functional, but has a few bugs that are preventing it from working properly. The first goal of this puzzle is to find these bugs and fix them. To do this, you'll have to familiarize yourself with the various technologies (Docker, RabbitMQ, nginx, Flask, and Postgres). You definitely don't have to be an expert on these, but you should know them well enough to understand what the problem is.

Assuming you have the Docker Engine and Docker Compose already installed, the developer said that the steps for running the system is to open a terminal, `cd` into this repo, and then enter these two commands:

    docker-compose up -d db
    docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"

This "bootstraps" the PostgreSQL database with the correct tables. After that you can run the whole system with:

    docker-compose up -d

At that point, the web application should be visible by going to `localhost:8080` in a web browser. 

## Weblogs

In this challenge, we simulate incoming weblogs by having a Python script reading weblogs from  weblogs.log. The data in this file is real data from a real webserver. It is a great idea to look at the file to familiarize yourself with the format of the log data.
A typical log entry looks like

    local - - [24/Oct/1994:13:43:13 -0600] "GET index.html HTTP/1.0" 200 3185

More details about the weblog can be found [here.](http://ita.ee.lbl.gov/html/contrib/Calgary-HTTP.html)

When processing these logs, we extract wether it was a GET request and we use the HTTP staus code to determine whether the request was succesful. Look at the [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for an overview over all status codes.
For the purpose of this challenge, a request is considered succesful if it returns a status code of the form 2XX.
# Assignments

The challenge consists of the following parts:

- **Correct the bugs to have the basic features working** - The weblogs should get processed, the results should be stored in the database and the webapp should display the rate of failed GET requests
- **Extend the functionality:** The data scientists suspect that local GET requests behave differently than remote GET requests. To help them investigate their suspicion, modify the platform so that it determines and displayes the rate of failed GET requests for local and remote requests separately


Once you've corrected the bugs and have the basic features working, commit the functional codebase to a new repo following the instructions below. As you debug the system, you should keep track of your thought process and what steps you took to solve the puzzle.

## Instructions to submit your solution
* Don't schedule your interview until you've worked on the puzzle 
* To submit your entry please use the link you received in your systems puzzle invitation
* You will only be able to submit through the link one time
* For security, we will not open solutions submitted via files
* Use the submission box to enter the link to your GitHub repo or Bitbucket ONLY
* Link to the specific repo for this project, not your general profile
* Put any comments in the README inside your project repo

# FAQ

Here are some common questions we've received. If you have additional questions, please email us at `devops@insightdata.com` and we'll answer your questions as quickly as we can (during PST business hours), and update this FAQ. Again, only contact us after you have read through the Readme and FAQ one more time and cannot find the answer to your question.

### Which Github link should I submit?
You should submit the URL for the top-level root of your repository. For example, this repo would be submitted by copying the URL `https://github.com/InsightDataScience/Systems-Puzzle-Weblog` into the appropriate field on the application. **Do NOT try to submit your coding puzzle using a pull request**, which would make your source code publicly available.

### Do I need a private Github repo?
No, you may use a public repo, there is no need to purchase a private repo. You may also submit a link to a Bitbucket repo if you prefer.

### What sort of system should I use to run my program (Windows, Linux, Mac)?
You should use Docker to run and test your solution, which should work on any operating system. If you're unfamiliar with Docker, we recommend attending one of our Online Tech Talks on Docker, which you should've received information about in your invitation. Alternatively, there are ample free resources available on docker.com.

### How will my solution be evaluated?
While we will review your submission briefly before your interview, the main point of this puzzle is to serve as content for discussion during the interview. In the interview, we'll evaluate your problem solving and debugging skills based off how you solved this puzzle, so be sure to document your thought process.

### The website is ugly...should I improve the design?  
No, you should focus on the functionality. Your engineering team will bring on a designer and front-end developer later in the process, so don't worry about that aspect in this puzzle. If you have extra time, it would be far better to focus on aspects that make the code cleaner and easier to use, like tests and refactoring.

### Should I use orchestration tools like Kubernetes?
While technologies like Kubernetes are quite powerful, they're likely overkill for the simple application in this puzzle. We recommend that you stick to Docker Compose for this puzzle.