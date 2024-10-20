# Positive, Negative, and Neutral reviews lists
positive_reviews = [ 
    "The wireless earbuds are amazing! The sound quality is crystal clear."
"I love these earbuds. They fit perfectly and have great bass."
"The battery lasts forever! I can go days without charging."
"Comfortable and stylish. Perfect for daily use."
"Exceeded my expectations! The noise-cancellation is superb."
"Perfect for workouts. They stay in place and are sweat-resistant."
"Amazing sound quality. Worth every penny!"
"These earbuds are a steal for the price. Highly recommend."
"Long battery life and quick charging. Can't ask for more."
"The best wireless earbuds I’ve owned."
"Very lightweight and comfortable to wear for hours."
"Superb connection stability. No dropouts at all."
"Great value for money. Fantastic product!"
"The touch controls work flawlessly. Easy to use."
"They pair instantly with my phone. Seamless experience."
"Excellent sound clarity and deep bass."
"Battery life is impressive. Easily lasts a full day."
"The earbuds fit snugly in my ears. Very comfortable."
"The charging case is sleek and portable."
"The wireless range is fantastic. Works from far distances."
"Really happy with these! Worth every dollar."
"Crystal-clear audio, especially during calls."

    ]  # Add 50 positive reviews here
negative_reviews = [
    "Terrible sound quality. Very disappointing."
"The battery drains too quickly. Not reliable."
"The left earbud stopped working after just a week."
"Very uncomfortable to wear for long periods."
"The Bluetooth connection keeps cutting out."
"Not worth the money. I expected better quality."
"They don’t stay in my ears while I’m walking."
"The charging case is flimsy and feels cheap."
"These earbuds are overpriced for what they offer."
"They feel heavy in the ears. Very uncomfortable."
"The bass is weak, and the sound is tinny."
"After a few weeks, one earbud stopped working."
"The fit is terrible. They fall out constantly."
"Noise cancellation doesn’t work at all."
"Very poor microphone quality for calls."
"The earbuds disconnect randomly during use."
"The controls are not intuitive and hard to use."
"The sound lags when watching videos."
"The battery life is far too short."
"They don’t block out any outside noise."
"Poor build quality. They broke after a month."
"The sound is muffled and lacks clarity."

    ]  # Add 50 negative reviews here
neutral_reviews = [
    "The earbuds are okay, but not exceptional."
"Decent sound, but I expected more for the price."
"They work fine, but the fit isn’t great for my ears."
"The battery life is average, nothing special."
"Sound quality is fine, but not the best I’ve heard."
"They do the job, but they’re not super impressive."
"The noise cancellation is decent, but could be better."
"The earbuds are fine, but the case feels a bit cheap."

    ]  # Add 50 neutral reviews here

# Save to .txt files
with open('positive_reviews.txt', 'w') as pos_file:
    for review in positive_reviews:
        pos_file.write(review + "\n")

with open('negative_reviews.txt', 'w') as neg_file:
    for review in negative_reviews:
        neg_file.write(review + "\n")

with open('neutral_reviews.txt', 'w') as neu_file:
    for review in neutral_reviews:
        neu_file.write(review + "\n")

print("Reviews have been saved to text files!")
