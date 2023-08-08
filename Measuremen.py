def calculate_influence(followers, retweets, favorites):
    influence_score = (0.4 * followers) + (0.3 * retweets) + (0.3 * favorites)
    return influence_score
