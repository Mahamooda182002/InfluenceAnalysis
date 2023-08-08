import matplotlib.pyplot as plt

# Visualization of sentiment distribution
sentiments = [result['sentiment'] for result in influence_results]
sentiment_counts = Counter(sentiments)

plt.bar(sentiment_counts.keys(), sentiment_counts.values())
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Distribution')
plt.show()
