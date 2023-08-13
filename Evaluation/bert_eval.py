import pandas as pd
df = pd.read_csv('train-balanced-sarcasm.csv')

df.dropna(inplace = True)
df.isna().sum()
df.drop(columns = ['author', 'subreddit', 'score', 'ups', 'downs', 'date', 'created_utc'], inplace = True)
df.head()

df['label'] = df['label'].astype(float) # prevents “mse_cpu” / “mse_cuda” not implemented for ‘Long’ error
df.head()

df_sample = df.sample(frac = .01)

len(df_sample)

import numpy as np
df_sample['input'] = 'TEXT1: ' + df_sample.parent_comment + '; TEXT2: ' + df_sample.comment + '; LABEL1: ' + str(df_sample.label)

test_df = df_sample[['input', 'label']]

import torch
import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import string
def preprocess_data(text: str) -> str:
    return text.lower().translate(str.maketrans("", "", string.punctuation)).strip()

import torch
import pandas as pd
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import string

def preprocess_data(text: str) -> str:
    return text.lower().translate(str.maketrans("", "", string.punctuation)).strip()

# Load the pre-trained model and tokenizer
MODEL_PATH = "helinivan/english-sarcasm-detector"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# Prepare test data
test_text = test_df['input'].tolist()
preprocessed_test_text = [preprocess_data(text) for text in test_text]

# Tokenize test data
tokenized_test_text = tokenizer(preprocessed_test_text, padding=True, truncation=True, max_length=256, return_tensors="pt")

with torch.no_grad():
  output = model(**tokenized_test_text)
# Get predicted labels
predicted_labels = output.logits.argmax(dim=-1).tolist()

# Get true labels
true_labels = test_df['label'].tolist()

# Calculate accuracy
correct_predictions = sum(pred == true for pred, true in zip(predicted_labels, true_labels))
total_samples = len(test_df)
accuracy = correct_predictions / total_samples

print(f"Accuracy: {accuracy * 100:.2f}%")

from tqdm import tqdm  # Import tqdm for progress bar

# Initialize accuracy counters
total_samples = len(test_df)
correct_predictions = 0

# Load the pre-trained model and tokenizer
MODEL_PATH = "helinivan/english-sarcasm-detector"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# Process the DataFrame row by row with tqdm
for index, row in tqdm(test_df.iterrows(), total=total_samples):
    text = row['input']
    true_label = row['label']

    # Preprocess the text
    preprocessed_text = preprocess_data(text)

    # Tokenize the preprocessed text
    tokenized_text = tokenizer(preprocessed_text, padding=True, truncation=True, max_length=256, return_tensors="pt")

    # Make prediction
    with torch.no_grad():
        output = model(**tokenized_text)

    predicted_label = output.logits.argmax(dim=-1).item()

    # Compare prediction with true label
    if predicted_label == true_label:
        correct_predictions += 1

accuracy = correct_predictions / total_samples
print()
print(f"Accuracy: {accuracy * 100:.2f}%")

