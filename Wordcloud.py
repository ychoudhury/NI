###### 8/10/21
###### Y. Choudhury, supervisor C. Malaby
###### This program generates word clouds from exported salesforce case
###### descriptions.
###### Find the README in OneDrive -> Yasir Choudhury -> Case Analysis
###### Project


# python program to generate wordcloud

# import all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# read csv file
df = pd.read_csv(r"test.csv", encoding ="latin-1")

comment_words = ''
stopwords = set(STOPWORDS)

# list of words to exclude from wordcloud
stopwords.update(["customer", "error", "issue", "labview", "need", "ni", "please", "software", "support", "system", "thank","use", "using", "vi"])


# iterate through the csv file
for val in df.Description:
	
	# typecast each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# convert each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "

# generates .csv containing all words in dataframe, and their frequency. 
# frequencyList = df.Description.str.split(expand=True).stack().value_counts()
# frequencyList.to_csv('frequencyList.csv')

wordcloud = WordCloud(width = 1000, height = 800,
				background_color ='white', collocations=False,
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)

# plot the wordcloud image					
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()

