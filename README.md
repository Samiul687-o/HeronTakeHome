# HeronTakeHome
Take Home Test for Heron Data

Approach:

1. Standardise transaction descriptions using a regex pattern which targets abbreviated months and optional years. These are stripped out.
2. Group transactions by their standardised descriptions.
3. For each group identify whether these occur on a monthly basis.
4. Transactions must be repeated at least 3 times to establish that they are recurring


How would you measure the accuracy of your approach?

Firstly, I would calculate the precision and recall of correctly identified transactions. Precision is transactions labelled as recurring that are actually recurring and recall is proportion of actual recurring transactions that were identified. Secondly, test cases to evaluate the function's accuracy. Lastly, manually verify.

How would you know whether solving this problem made a material impact on customers?

Customer feedback through surveys could be useful tool. Additionally, Usage metrics would show over time if more users begin to rely on the automated recurring transaction finder. Finally, less customer support requests would be indicative of a working system.

How would you deploy your solution?

The service could be wrapped in an API allowing applications to send transaction data for real time recurring transaction detection.

What other approaches would you investigate if you had more time?

Machine Learning or NLP. Instead of fixed rules and regex, I would use them to classify recurring transactions based on patterns in historical data.

What are the limitations of your approach?

1. The regex pattern may will not capture all possible date formats. Additionally, it is it only capable of capturing recurring transactions in a set format (With abbreviated months and optional years).
2. Due to time constraints, I opted to focus on monthly recurring transactions as these are the most common. However, this could be expanded to include weekly, bi-weekly, etc.
3. The is_monthly_pattern function assumes that recurring transactions will be between a 27–33 day range. This is not always the case.
4. The function is not capable of identifying transactions that are recurring but do not have a standardised description. For example, a recurring transaction with a random description.

Given more time, these limitations could be addressed.