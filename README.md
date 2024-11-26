# Sentiment analysis: Customer Feedback Analysis for Improved Service Delivery.

****

![alt text](sentiments.png)


## Overview
In the competitive and customer-oriented markets of today, feedback is an important commodity needed in formulating business strategies as well as improving service delivery. Customer reviews, ratings, and comments highlight the trend of preference, pain points, and sentiment, thus helping the
business to frame its offerings to meet the expectations of the customers.
Efficiently analyzing large volumes of unstructured customer feedback is a challenge. The current manual ways of doing these things are extremely cumbersome and prone to errors, while most existing tools are lacking in comprehensive thematic analysis and tracking sentiment trends. 
This project will help bridge this gap through the provision of an automated system for sentiment analysis, identificationof trends, and thematic discovery and present actionable insights in real-time.

**Target Audience**
The project serves:

- **Business Owners:** Benefit from increased sales, customer retention, and improved product offerings.
- **Customers:** Receive tailored product recommendations and an improved shopping experience.
- **Product Managers:** Gain insights into product performance and areas for improvement.
- **Marketing Teams:** Leverage customer sentiment insights to refine campaigns and messaging.
- **Development Teams:** Build and maintain the API-driven, scalable system for seamless integration.
- **Data Analysts:** Source raw feedback into actionable insights.

## Problem Statement
Businesses struggle to meet diverse customer expectations due to challenges in analyzing vast data from interactions and reviews. This hampers their ability to deliver personalized recommendations and understand customer sentiment, leading to missed opportunities for engagement, satisfaction, and loyalty in a competitive market.
Impact
The proposed system shall contribute by:
- Enhancing Customer Satisfaction: This will help address negative sentiments.
- Improve Decision Making: showing key themes and trends for strategy.
- Enhance Competitive Advantage: Improve customer loyalty and reduce churn.

## Objectives
**Main Objective:**

To design and implement a Sentiment Analysis System that classifies customer feedback into positive, neutral, and negative sentiments using advanced Natural Language Processing (NLP) techniques, ensuring an accurate understanding of customer sentiment.

**Specific Objectives**
1. **Provide Tailored Recommendations:** Utilize collaborative and content-based filtering techniques to suggest products that align with user preferences.
2. **Analyze Customer Sentiment:** Classify customer feedback into positive, neutral, or negative sentiments to identify satisfaction levels and areas of concern.
3. **Generate Actionable Insights:** Assist businesses in refining product offerings and improving services through sentiment-driven analysis.
4. **Enable Scalability:** Build a system capable of handling increasing data and user volumes while maintaining consistent performance.

## Data understanding

The dataset combines internal and public repositories to analyze customer feedback.
- **Internal Sources:** Company databases with post-purchase reviews, customer service feedback, and survey responses.
- **Public Sources:** Datasets from Yelp, Amazon reviews, and Kaggle, offering diverse customer insights.
  
**Data Features:**
>1. Review Text: Unstructured feedback for sentiment and topic analysis.
>2. Ratings: Quantifies satisfaction, validates sentiment classification, and offers a quick satisfaction overview.
>3. Product/Service Category: Labels for segmentation, enabling targeted analysis of sentiment and themes specific to offerings.


## Data Preparation

To prepare the data for modelling, these are the steps we took: 
- Handling missing values: Identify and address gaps in the data by imputing missing values and removing incomplete records to ensure consistency 
- Feature selection and engineering: Select the most relevant variables and created new ones to improve model performance and highlight underlying patterns. 


## EDA

**Univariate Data analysis:**
1. I visualized the top and bottom  20 subcategories that have the highest sentiment count. This highlighted the subcateegories that has the most positive sentiments and the least positive sentiments.
2. The second visualization was on distribution of sentiments. The observation was that some categories had only positive sentiments .
   
**Bivariate Data analysis:**
1. The first visualization was a heat map on the value for money by sub categories.When analyzing the heatmap, you can gain insights into which subcategories offer the best value for money based on both sentiment and price. This information can be valuable for various purposes, such as product recommendations, marketing strategies, and business decision-making.
2. A bar graph on average sentimental score against prices.By analyzing the price range vs sentiment score chart alongside the heatmap from the previous step, you can gain a more comprehensive understanding of how sentiment scores vary across subcategories, price ranges, and value for money. This can be helpful for making informed decisions about product pricing, marketing strategies, and overall business planning.


## Modelling
After training the dataset, SVM, TFIDF, Naive Bayes, and LTSM were tested. Naive Bayes  performed best,compared to SVM, TFIDF. we deployed a sentiment analysis app that classifies sentiments according to Negative positive and neutral sentiments. 

## Conclusions
This project aimed to design and implement a Sentiment Analysis System that classifies customer feedback into positive, neutral, and negative sentiments , ensuring an accurate understanding of customer sentiment.. Through the analysis of reviews and sentiments using Naive Bayes, I was able to classify sentiments into Positive,Neutral and Negative.

**The results indicate that:**
- some categories like Educational books category offers the highest value for money while some like baby disposable dipers offer the least value for money. This information can be valuable for various purposes, such as product recommendations, marketing strategies, and business decision-making.
- Overall The sentiment count shows that the positive sentiments have a higher count showing that customers are generally  sattisfied with the products.
- By analysing the sentiment count against price of goods we discovered that goods with medium prices get more positive sentiments compared to those with low or high prices. This shows that prices of products affect the reviews and sentiments they get.

 These insights can be valuable for:Business Owners, Customers, Product Managers, Marketing Teams, Development Teams and Data Analysts.


## Recommendations

1. Data Quality: Invest in improving data quality and consistency to enhance model performance.
2. Model Selection: Consider exploring other machine learning algorithms or ensemble methods to potentially improve accuracy and robustness.
3. Hyperparameter Tuning: Conduct rigorous hyperparameter tuning to optimize model performance.
4. Feature Engineering: Experiment with different feature engineering techniques to extract more informative features from the data.
5. Domain Expertise: Collaborate with domain experts to gain deeper insights and refine the analysis.
6. Ethical Considerations: Ensure that the model is fair, unbiased, and adheres to ethical guidelines.

## Presentation slides


[Presentation (1).pdf](Presentation (1).pdf)
