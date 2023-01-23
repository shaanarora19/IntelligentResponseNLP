# smart-review-model
TLDR: Model that uses NLP/sentiment analysis to generate intelligent replies to customer reviews.

Over the past few years, the popularity of online retailers has risen exponentially. This increase has made shopping online commonplace, leading to a dramatic shift in consumer leverage. Customers now have access to many product offerings online relative to older brick-and-mortar stores. All these items have their page with more information than we have ever had access to before. 

This page usually has photos, product features, and perhaps most importantly— ratings and reviews from previous customers. It is clear from this that customers place great importance on reviews. According to Dixa, "93% of customers will read online reviews before making a purchase." Furthermore, rankings of products on the marketplace depend increasingly on the quality and quantity of reviews. This dependence on reviews incentivizes businesses to solicit reviews to increase the review count. A product may be superior to its competitors, but if it has no reviews, it is unlikely that a consumer would choose it if better-reviewed products were available.

Furthermore, businesses have had to deal with the impact that both good and bad reviews have had on their business— using good reviews to boost their loyal following and demonstrate to new customers that their product is substantial. While also mitigating negative reviews by dealing with customers’ frustrations and poor experiences to ensure it does not leave a long-term mark on the business. According to Google, businesses that respond to reviews are 1.7 times more trustworthy than companies that don’t. Additionally, according to Brighlocal’s Local Consumer Review Survey, 57% say they would be 'not very' or 'not at all likely to use a business that doesn't respond to reviews. Although the importance of review response is significant, 63% say that at least one company they reviewed never even responded. To make it even more challenging for businesses to deal with online reviews, according to ReviewTracker data, 53% of customers expect companies to respond to negative reviews within a week.

In comparison, 33% have a shorter time frame of 3 days or less. Therefore, to make businesses' lives easier, they need a way to respond to reviews efficiently without throwing more people at the problem. As such, our group has set out to solve this problem using natural language processing and various machine learning techniques to identify review sentiments and respond to them effectively. In doing so, businesses will have an automated solution to one of the most salient factors that impact the success of their business.

When thinking about the motivation for our topic, we wanted to create a project that we could work on as a group after this class and be able to work with companies to iterate and strengthen our idea. So, when thinking about what we can work on after this class, we thought we would like to use a dataset and provide valuable data to businesses and also provide curated responses to their customers. So, we created this idea to sell as B2B software, allowing companies to understand customer reviews better and digest them in an accessible format. We hope to be able to work with companies, aggregate their reviews through web scraping, run NLP to understand sentiment analysis, and then provide individually-catered responses to these companies.

We aim to create a model that can efficiently, effectively, and meaningfully generate individually-catered responses to customer reviews. Our model will have two major components:



A natural language processing component that identifies sentiment, keywords, and actionable items in a customer review, and
A response-generating model that uses the above information to create a meaningful customer response.

We will need to isolate (or manually gather) a robust dataset of customer reviews that we can train/test our model on. Then, we will need to either build from scratch or borrow from other open-source models to create our proprietary review response model.
