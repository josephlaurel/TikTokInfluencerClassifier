# Import the TikTok API
from TikTokApi import TikTokApi

# Instantiate the API
api = TikTokApi.get_instance(use_selenium=True, use_test_endpoints=True)

# Import Python libraries
import pandas as pd # This is needed to save the metadata to a pandas dataframe
import random

# Set parameters for scraping
did = random.randint(1111111,9999999) # This will ensure that unique videos are scraped
results = 2000 # The daily scraping limit of the API is 2000 rows. Based on my experience, the API generates a new batch of
        # trending videos every two weeks. Using the API over consecutive days may cause duplicate videos to be scraped.

# Instantiate the trending videos scraper (seems to automatically access videos which are trending within your current location)
trendingPH = api.trending(count=results,
                            custom_did=str(did),
                            custom_verifyFp="verify_kj9gr1uo_SJtTbYl5_OlCF_4ReJ_9aDz_nq0mHvK5bx9a"
                            )
                            # Change the value of custom_verifyFp (this is different for every browser on your computer).
                            # This value can be obtained by accessing TikTok.com in Firefox,
                            # right-clicking on the page, clicking "Inspect Element" on the menu that appears, selecting "Storage",
                            # and copying the value of s_v_web_id.

# Save the scraped metadata to a pandas dataframe
dfPH = pd.DataFrame.from_dict(trendingPH)

# Copy the data from the dataframe to an exported CSV file
dfPH.to_csv(r'/Users/josephlaurel/Desktop/Analytiks/Capstone_Project/12-29-20.csv', index=False)

## custom_verifyFp values for my browsers:
# Firefox s_v_web_id: verify_kh49gewh_CYyCTj1W_5VxN_4SCG_A4CE_sHDqQOdUM7Yk
# Chrome 12-29-20: verify_kj9gr1uo_SJtTbYl5_OlCF_4ReJ_9aDz_nq0mHvK5bx9a
# Chrome 12-15-20: verify_kipi1xv3_NhlJcjJX_aic2_46qQ_8xtE_P4ekk2G39uig
