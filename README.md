# **CREATING A URL PHISHING DETECTOR**
This project aims to develop a machine learning model that can detect phishing URLs and deploy it as a web application, allowing users to input a URL and receive an immediate classification as either phishing or legitimate. By providing this accessible tool, we aim to help users avoid phishing scams and protect sensitive information.

![image](https://github.com/user-attachments/assets/c34659ab-1573-4f29-b1d3-6ec3cc4726ac)
<!-- Setting dimensions -->
<img src="https://github.com/user-attachments/assets/c34659ab-1573-4f29-b1d3-6ec3cc4726ac" alt="Image Description" width="1280" height="640">


## BUSINESS AND DATA UNDERSTANDING
Imagine you're a small business owner who relies on a website to manage customer relationships, handle transactions, and communicate with clients. Like many users, you’re constantly online—navigating links from emails, social media, and suppliers. But as your business grows, so does the threat landscape around you. Cybercriminals are getting smarter, and phishing attacks are more sophisticated than ever, often hiding behind seemingly legitimate URLs. One wrong click, and you could be handing over sensitive data, from financial details to client information, putting your business and customers at serious risk. According to a recent report by the Anti-Phishing Working Group (2023), phishing attacks have increased by over 50% in the past year, with small businesses being one of the primary targets due to their perceived lack of robust cybersecurity measures.
### DATA
The dataset we have is from Mendely which is stored in a folder on Google Drive known as Phishing Website Detection Dataset
### PROJECT GOAL
The goal of this project is to come up with detector that is able to separate phishing and non phishing URLs.

## DEVELOPMENT TOOLS
- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- scikit-Learn
- Whois
- Urlib


Correlation Analysis
![image](https://github.com/user-attachments/assets/3f487e22-55c0-4d89-be1f-0dc2912500c8)

Domain Length and Number of Subdomains: These features show a strong positive correlation, indicating that URLs with longer domain names are likely to have a higher number of subdomains.
URL Length, Path Length, and Number of Slashes: URL length demonstrates a strong positive correlation with both path length and the number of slashes, suggesting that longer URLs are often more intricate, containing multiple directory levels.
URL Similarity Score and Common Phishing Words: A slight negative correlation exists between these two factors, implying that URLs containing more common phishing-related words tend to have lower similarity scores, as they may focus more on including keywords than on replicating trusted URLs.
Domain Age and Phishing URLs: Negative correlations with domain age suggest that phishing URLs often use newly registered domains, potentially to imitate legitimate websites and evade detection.

Pair Plots
![image](https://github.com/user-attachments/assets/39d218a1-b07c-4c85-a762-70a2e37b250e)

Strong Correlations Between Features:
Features like domain_length and domain_entropy, as well as domain_length and typosquatting_distance, show positive correlations, indicating that longer domain names often have higher entropy and greater similarity to typosquatting patterns.
Distinct Clustering Between Labels:
Benign and malignant URLs exhibit distinguishable patterns in certain feature pairs (e.g., domain_length vs. domain_entropy), suggesting that these features are effective for differentiating between the two classes.
Distribution Differences:
The distributions for features such as char_repetition and typosquatting_distance show noticeable differences between benign and malignant URLs, implying their relevance for classification. Malignant URLs tend to have higher values for char_repetition, which could reflect obfuscation tactics.


## MODELLING
The models used in this project are:

- Dummy Classifier
- Logistic Regression
- Random Forest
- XGBoost
- Simple Perception
- Support Vector Machine

![image](https://github.com/user-attachments/assets/02b76d44-a646-48b1-b810-193fb142762c)

XGBoost and Gradient Boosting models exhibit the highest performance across all metrics, demonstrating their strong predictive capabilities.
Random Forest and Support Vector Machine also perform well, while Logistic Regression and Simple Perceptron show good but slightly lower performance.
Dummy Classifier displays the lowest scores, indicating its ineffectiveness as a benchmark.


## CONCLUSION
### High-Accuracy Detection
The solution achieves high-accuracy detection, making it a reliable tool for identifying potential threats. This ensures that the system can consistently differentiate between legitimate and malicious activities, significantly reducing the likelihood of false positives or negatives. By meeting rigorous performance standards, the model not only enhances trust in its predictions but also minimizes the manual intervention needed for verification.
### Real-Time Classification
The implementation of real-time classification empowers users with immediate insights into potential threats. This capability is crucial in dynamic environments where rapid decision-making can prevent significant damage. For instance, in the context of phishing attacks, detecting and flagging malicious URLs in real time enables users to avoid accessing harmful sites. Additionally, the swift feedback loop provided by real-time classification improves the overall user experience, ensuring that the tool integrates seamlessly into fast-paced workflows without causing delays.
### URL Phishing Detector
A URL phishing detector is a powerful and proactive tool designed to safeguard individuals and organizations from phishing attacks. By analyzing URLs for patterns or features indicative of phishing attempts, the detector helps prevent users from falling victim to scams that could compromise sensitive information. Its application is especially critical in today's digital age, where phishing attacks are increasingly sophisticated and prevalent. Organizations benefit from this tool as part of a broader cybersecurity strategy, reducing the risk of data breaches, financial losses, and reputational damage.


## RECOMMENDATION
### Continuous Learning
To maintain the model's effectiveness against evolving threats, it is crucial to implement a strategy for regularly updating the system with new phishing data. This involves creating a robust pipeline to collect fresh datasets, including real-world phishing attempts and newly identified tactics. Additionally, periodic retraining of the model using these datasets will ensure that it stays adaptive and resilient to emerging attack patterns.
### User Feedback
Integrating user feedback as part of an iterative improvement process is essential for enhancing the application's usability and effectiveness. Users can provide insights into false positives, overlooked phishing attempts, and usability challenges. Establishing a streamlined feedback mechanism—such as in-app reporting tools or periodic user surveys—will allow the development team to prioritize updates and adjustments that directly address user concerns.
### Expansion
Beyond detecting phishing attempts, the tool should be expanded to cover other forms of online threats, such as ransomware, malicious URLs, and social engineering tactics. This requires a modular approach to development, allowing new features to integrate seamlessly into the existing framework. Collaboration with cybersecurity experts and staying informed on emerging threat landscapes will help guide the prioritization and implementation of these additional functionalities.


## REPOSITORY NAVIGATION
the respiratory contains:
- a ipynb notebook
- powerpoint presentation
- deployment_pipeline.py
- url_processor.py
- streamlit_demo.py
- richard.ipynb
- cynthia.ipynb

[Phishing URL Detection Repository](https://github.com/Cynthia-Njambi/Phishing-URL-Detection/blob/main)
