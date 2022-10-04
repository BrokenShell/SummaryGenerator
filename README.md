# Summary Generator Component

A simple example of an NLP summary generator component.

This example employs a selective strategy to maintain a high level of data integrity. Each sentence in the output appeared somewhere in the source document. Other solutions employ a generative strategy where the output is constructed and does not necessarily appear in the source. The selective strategy is more accurate but less precise, the generative strategy can be more precise but is often less accurate. We have chosen the selective strategy to reduce the likelihood of producing an incorrect summary.

Today's objective: Take a json file of descriptions and create a new json file of summaries.
- The output should have the same format as the input.
- We will not be using the pandas.
- Summary size should be 1-2 sentences.
