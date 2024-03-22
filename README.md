# Frequency
Group 8 Text Analytics Project 
## Overview
The goal of the project is to arrive at a more precise formulation of frequency and evaluate current stopword removal methods in regards to their applicability and efficiency with everyday texts on social media.  

## TODO:
- [x] Implement basic crawling
- [x] Improve to include custom timeframes, search string criteria
- [x] Expand on the search to include more posts
- [x] Create the initial preprocessing procedure
- [ ] Add comments (optional)

## Installation

### Prerequisites
- Python 3.9.6  

### Setup
1. Clone the repo  
```git clone https://github.com/illmet/Frequency```  
2. Set up a virtual environment  
```python3 -m venv freq```  
```source freq/bin/activate```  
3. Install packages  
   ```pip install -r requirements.txt```  
4. Set up enviroment variables for crawling reddit (Updated soon)

### Usage (READ THIS FIRST)
The current procedure is starting with crawling the raw data from reddit, that is done here:  
```python3 crawl.py```  
This will save the required posts and comments corpora in respective folders.  
The preprocessing.py file turns the text into a readable version.   
