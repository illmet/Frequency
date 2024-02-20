# Frequency
Group 8 Text Analytics Project 
## Overview
The goal of the project is to arrive at a more precise formulation of frequency and evaluate current stopword removal methods in regards to their applicability and efficiency with everyday texts on social media.  

## TODO:
- [x] Implement basic crawling funcionality
- [ ] Improve to include custom timeframes
- [ ] Preprocess textual data 

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

### Usage
Run the script like so:  
```python3 crawl.py```  
The output is saved in the data folder, in .json files for each subreddit.  
