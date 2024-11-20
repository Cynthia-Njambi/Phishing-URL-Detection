# **CREATING A URL PHISHING DETECTOR**
This project aims to develop a machine learning model that can detect phishing URLs and deploy it as a web application, allowing users to input a URL and receive an immediate classification as either phishing or legitimate. By providing this accessible tool, we aim to help users avoid phishing scams and protect sensitive information.


<!-- Setting dimensions -->
<img src="https://github.com/user-attachments/assets/c34659ab-1573-4f29-b1d3-6ec3cc4726ac" alt="Image Description" width="1280" height="640">


## BUSINESS AND DATA UNDERSTANDING
Imagine you're a small business owner who relies on a website to manage customer relationships, handle transactions, and communicate with clients. Like many users, you’re constantly online—navigating links from emails, social media, and suppliers. But as your business grows, so does the threat landscape around you. Cybercriminals are getting smarter, and phishing attacks are more sophisticated than ever, often hiding behind seemingly legitimate URLs. One wrong click, and you could be handing over sensitive data, from financial details to client information, putting your business and customers at serious risk. According to a recent report by the Anti-Phishing Working Group (2023), phishing attacks have increased by over 50% in the past year, with small businesses being one of the primary targets due to their perceived lack of robust cybersecurity measures.
### DATA
The dataset we have is from Mendeley which is stored in a folder on Google Drive known as the Phishing Website Detection Dataset, The data contained the URLs and their respective labels and from the URL other features were extracted
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


## Correlation Analysis
![image](https://github.com/user-attachments/assets/3f487e22-55c0-4d89-be1f-0dc2912500c8)

Domain Length and Number of Subdomains: 

These features show a strong positive correlation, indicating that URLs with longer domain names are likely to have a higher number of subdomains.

URL Length, Path Length, and Number of Slashes: 

URL length demonstrates a strong positive correlation with both path length and the number of slashes, suggesting that longer URLs are often more intricate, containing multiple directory levels.

URL Similarity Score and Common Phishing Words: 

A slight negative correlation exists between these two factors, implying that URLs containing more common phishing-related words tend to have lower similarity scores, as they may focus more on including keywords than on replicating trusted URLs.

Domain Age and Phishing URLs: 

Negative correlations with domain age suggest that phishing URLs often use newly registered domains, potentially to imitate legitimate websites and evade detection.

## Pair Plots
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

## F1 score for the different models
![image](https://github.com/user-attachments/assets/43ea327e-1075-4da4-a1ab-ecd58b1fab00)


The models demonstrate consistently high F1 scores across training, testing, and cross-validation datasets, indicating strong generalization and robustness.
There is minimal variance between the train, test, and cross-validation F1 scores, suggesting that the models are neither overfitting nor underfitting.
The overall performance shows that the models are reliable and effective for phishing URL detection tasks.

## Combined ROC curve for all models
![image](https://github.com/user-attachments/assets/0e3b6295-b556-442f-a6a0-40dd80e0a8f3)

Strong Model Performance: Models like Random Forest, Gradient Boosting, Support Vector Machine (SVM), and XGBoost achieve high Area Under the Curve (AUC) scores (0.97), indicating excellent ability to distinguish between phishing and legitimate URLs.

Logistic Regression Competence: Logistic Regression also performs well with an AUC of 0.96, showing it is a reliable, albeit slightly less effective, alternative to the top-performing models.

Baseline Comparison: The Dummy Classifier has an AUC of 0.51, barely above random guessing, highlighting the significant improvement achieved by the other models.

Conclusion on Model Suitability: The top models (Random Forest, Gradient Boosting, SVM, and XGBoost) are robust choices for phishing detection due to their consistent and superior performance.


## CONCLUSION

### 1. High-Accuracy Phishing Detection
The selected models excel in phishing detection, achieving high F1 scores on the test set, with all exceeding 92%—significantly surpassing the target of 90% accuracy. Among these models, the Support Vector Machine (SVM) stands out with an impressive F1 score of 93.55%. This indicates its exceptional capability to accurately differentiate between phishing and legitimate URLs. Such performance ensures that the model minimizes both false positives and false negatives, delivering reliable results for real-world applications.

### 2. Balanced F1-Score
The chosen models maintain a robust and balanced F1 score, showcasing their effectiveness in addressing both precision and recall. High precision ensures that the model correctly identifies phishing URLs with minimal false positives, while high recall ensures the model effectively minimizes false negatives, reducing the likelihood of phishing threats being overlooked. This balance is essential for achieving a comprehensive detection system that users can trust for accurate and reliable results.

### 3. User-Friendly Web Deployment
The SVM model will be deployed using Streamlit, a platform known for its simplicity and ease of use. This deployment strategy ensures that even non-technical users can effortlessly access the phishing detection tool through a clean, intuitive web interface. Users will be able to enter URLs and instantly receive a classification result, making the solution highly practical and accessible to a broader audience.

### 4. Real-Time Classification
Streamlit-based deployment enables real-time classification, allowing users to receive immediate feedback on whether a URL is phishing or legitimate. This feature is particularly crucial for scenarios where users need instant validation to make timely decisions, such as avoiding potential phishing scams during online activities.

### 5. Identify Important Features
The Random Forest model goes beyond classification by providing valuable insights into feature importance. By identifying the characteristics that contribute most to phishing detection, the model helps explain its decision-making process. For example, features such as URL length, domain age, and the presence of suspicious keywords might be highlighted. This transparency not only improves the model's interpretability but also builds trust with users by demonstrating the rationale behind its predictions.


## RECOMMENDATION

### 1. Train the Model Using More URLs
Expanding the dataset by incorporating more URLs can significantly enhance the model's ability to generalize across different scenarios. A more diverse dataset increases robustness, enabling the model to detect new and more sophisticated phishing techniques more effectively.

### 2. Consider Deployment as a Browser Extension
While deploying the model with Streamlit is effective, creating a browser extension would elevate the user experience by offering real-time URL verification directly within the browser. This seamless integration allows users to identify phishing attempts without navigating to a separate application, enhancing both convenience and protection.

### 3. Implement Continuous Model Retraining
Given the constantly evolving nature of phishing attacks, establishing a mechanism for continuous model retraining using newly collected data is critical. Regular updates ensure the model stays relevant and effective in identifying emerging phishing tactics, maintaining its reliability over time.

### 4. User Feedback Integration
Gathering user feedback through the web application provides valuable insights into areas of improvement, such as common false positives or negatives. This feedback loop enhances the model's performance and improves the overall user experience by addressing pain points and ensuring the solution remains user-centric.

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
