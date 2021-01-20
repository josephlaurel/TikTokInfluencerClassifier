# **TikTok Influencer Classification using Trending Videos in the Philippines**
by [Joseph Laurel](http://linkedin.com/in/josephlaurel)
<br> assisted by [Francisco Aguirre](https://www.linkedin.com/in/franciscoeaguirre/)

## <b> Background </b>
<p align='justify'>
According to the website iPrice, <b>TikTok</b> was the most downloaded entertainment app in the Philippines’ iOS App Store as of 2020. Besides delighting users with addictive short-form videos, the app has significantly grown online search interest in products which have been featured in viral clips. For instance, Google Trends reported a 1329% surge in interest for Ocean Spray’s cran-raspberry juice after being featured in an American TikTok user’s unsponsored video <i><a href="https://www.onenews.ph/tiktok-still-the-most-downloaded-entertainment-app-in-phl-retains-global-popularity-despite-controversies">(Mateo, 2020)</a></i>. Hence, both local and foreign brands have increasingly turned to the platform as a content marketing tool.
<br><br>
However, several limitations prevent local marketers from fully benefiting from the influence of TikTokers.
<br> 

1.   There are <b>limited platforms</b> which track the performance of TikTok influencers in the Philippines. To the knowledge of our team, the only websites which provide data on local TikTokers are Influence Grid and Hypetrace. <br>
2.   The aforementioned websites merely classify influencers based on metrics such as followers, likes, views, and average engagement. They do not provide insight into <b>other characteristics of trending videos</b>, such as the optimal publishing schedule, music, text, and visual elements used by influencers. <br>
3.   By relying on the influencer rankings published by existing platforms, which are largely based on past engagement rates, marketers may be <b>late in identifying up-and-coming influencers</b> who may have greater growth potential than top influencers who may have already reached the peaks of their careers.

So, how can local marketers better leverage TikTokers’ huge online influence to drive the growth of their brands?

</p>

## <b> Objectives </b>

To address the needs of local marketers, our project is patterned after the work of [Şimşek and Kabakus (2018)](https://www.researchgate.net/publication/329896342_Finding_Influencers_on_Twitter_with_Using_Machine_Learning_Classification_Algorithms) and has the following objectives:

1.   To develop a holistic <b>influencer classification algorithm</b> that considers the audio, visual and text characteristics of a trending video, the engagement on a single video, and the overall engagement on the creator's account. The model was trained and tested using 6,882 trending videos scraped between November and December 2020 using the unofficial TikTok application programming interface wrapper created by [David Teather](https://davidteather.github.io/TikTok-Api/).<br>
2.   To perform a feature importance analysis to identify <b>key features</b> that are most greatly associated with influencer-generated videos. 

## <b> Summary of Results </b>
![Best Model Results](Images/Screen%20Shot%202021-01-20%20at%208.00.25%20PM.png)

<p align='justify'>
Listed above are best performing versions of each algorithm sorted in ascending order of accuracy. Hyperparameter optimization using 10-fold cross validation was used to generate the optimal classifiers. Using the original dataset was found to improve the performance of the Naive Bayes and K-nearest neighbors models, while synthetic minority oversampling improved the performance of the Random Forest and XGBoost classifiers. The XGBoost classifier generated the highest accuracy at 96%.

Given the imbalance between of non-influencer and influencer generated videos in the dataset, it is also important to evaluate the performance of the models using the f1-score, which considers the impact of both false negative and false positive predictions. False negative predictions would mean leaving influencers with good engagement rates undetected, while false positive predictions would incorrectly classify non-influencers as influencers. Hence, we can minimize opportunity costs associated with both scenarios by comparing the models’ scores.

As shown in the last row, the XGBoost model’s f1-score for non-influencers is 97% while its f1-score for influencers is 93%. Although the model is slightly better at classifying non-influencers, the classification of influencers may be improved in the future as more natural observations of influencer-generated videos are added to the training data. Moreover, the overall performance is positive with both f1-scores above 90%, as well as false negative and false positive rates below 10%. Hence, we should be able to use the XGBoost model to holistically identify influencers and non-influencers with minimal error, which would allow brands to select the right endorsers for their campaigns.
</p>

![Feature Importance Analysis](Images/Screen%20Shot%202021-01-20%20at%208.07.52%20PM.png)

<p align='justify'>
The feature importance comparison for the best-performing XGBoost classifier is shown above. Out of the top 15 features, those most highly correlated with influencer-generated videos were video play count, video heart count and whether the video was a reply, each having importance ratings of over 6%. Moreover, 6 out of the 19 engineered features (marked above with asterisks) were among the most important features. These include whether the video is a duet, effect sticker count, challenge count, video height, video width, and whether the video is a reply.

Intuitively, engagement metrics such play count, heart count, authorDiggCount (meaning number of videos liked by the user), countTaggedUsers, follower count, and author verified status are among the the top features correlated with a user’s influencer classifications. 

Platform-specific features such as author video count, isDuet, isReply, effectStickerCount, challengeCount, and video height and width are also top indicators of an influencer generated video. Additional features may be engineered to more deeply assess the impact of these factors on influencer classification. Some examples of these are the number of duet and reply videos made by the users, as well as the aggregate number of the user’s videos that contain effect stickers.
</p>
