Opening the black box

Note: **means manim stuff 


How do you evaluate a model’s performance?
- What if I told you that I’ve made a model that doesn’t actually need to see any training observations to 

At its core, what does a ML model do?
- **Take an example of an observation and transform it into a “dictionary” of features
- **Line up the little latex arrays and send them through a input/output machine 
    - **Gear churning animation
    - Spit out: a “I’m 80% sure” that’s a cat, or I’m only 20% sure thats a cat, so let’s call it a dog
    - Let’s label each of our predictions for a cat as a positive case, and the dog as the negative case
    - Notice that the model may be getting it wrong sometimes, but we’re labelling each case by our prediction
    - If our prediction is wrong, we call it false, and if we get it right, we call it true
    - In sum, we can sort out all the observations we’re testing the model on as TP, TN, FP, or FN
    - **Move camera to right and focus on the pile of predicted observations
        - **Observations itself should be little images of a cat or a dog, a latex label underneath, with a light X over it if false   
- **Sort the pile of observations into 4 categories and attach bracket labels to each group
    - Create a VGroup of all of these little observations 

Introduce Confusion Matrix 
- **Move each VGroup of FP, TP, etc into a corresponding matrix, fade them out in exchange of a bg rectangle that’s shaded to scale w/  # of observations in that box
- **Show a light from the left side 
    - This shows that what’s positive and negative is only from the perspective of the model, not reality
    - This is b/c we don’t oftentimes know what the reality or ground truth is until some time after we’ve conducted the test or made the prediction
- We can calculate out little metrics from this:
        - Accuracy is probably the easiest to start with: How many did we get right out of how many we predicted from?
            - **Draw a surrounding highlight box around TP, TN, then another with a darker color on the entire matrix
            - **Transform those boxes (colored for the numerator vs denominator) into a color coded latex formula on the right
        - Sensitivity: Think of this as how sensitive, or how jumpy our model is when it sees some little indication that this could be a positive case. 
            - We’ll define it as the proportion of actual positive cases that our model picked up on and labelled as true. 
            - **Draw a darker orange box around FP + TP, and then light yellow around TP
            - **Transform the boxes (colored for the numerator vs denominator) into a color coded latex formula on the right
        - etc. 
- What do we want in a model?
    - Minimizes error– what about if the relative cost of type I error is much higher than type II? 

~Next Steps~ 
- Show predicted probabilities of each observation as a scatter plot 
- Plot those on a number line (P(x) from 0 to 1), and color those by the ground truth state
- Draw cts beta distributions around them
- Draw threshold at 0.5 and show that as the decision line => Which region is FP and which region is FP

- A better model is one that splits apart the two curves and minimizes the overlap => better distinguishing ability
- Dummy classifier is one that is unable to separate the two curves

- What happens when we move threshold up and down => show fluctuations in confusion matrix => trace out points on ROC curve

- What happens if underlying data has hella class imbalance => Show effects on confusion matrix, probability distributions, ROC curve, etc.
- 
