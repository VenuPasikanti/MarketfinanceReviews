1.This script "Main_Market_finance_rev‪iews.py" is used to extract all reviews from https://www.trustpilot.com/review/marketfinance.com by webscraping using python libraries beautifulsoup and requests and then written to a Json file data.json.
2. Using pandas read the data.json file and produced visualization of reviews (Number of reviews by review type) in jupyter notebook.
Note : Please change the file path in the jupyter notebook from where you are reading.

Things I could have done better Provided there was bit more time.
1.Modularize the data extraction code.
2.Test case - Scraping the total reviews on website and comparing with number of records extracted (in my case extracted only 282 against 327 - could not debug) .
3.Better visuals - Given the data there is not much scope.
4.With more volumes of data could contribute to much more in depth analysis into some of the words in the reviews like "excellent","highly recommend","helpful" using  bag of words/Data bricks ML/spark ML/Azure ML and do some exploration in collaboration with data scientists to produce some regression model which can be trained and plugged in as API on the website for repeat customers by recommending new products etc.