from happytransformer import HappyTextToText

happy_tt = HappyTextToText("T5", "t5-base")

from datasets import load_dataset

train_dataset = load_dataset("jfleg", split='validation[:]')

eval_dataset = load_dataset("jfleg", split='test[:]')

import csv

def generate_csv(csv_path, dataset):
    with open(csv_path, 'w', newline='') as csvfile:
        writter = csv.writer(csvfile)
        writter.writerow(["input", "target"])
        for case in dataset:
     	    # Adding the task's prefix to input
            input_text = "grammar: " + case["sentence"]
            for correction in case["corrections"]:
                # a few of the cases contain blank strings.
                if input_text and correction:
                    writter.writerow([input_text, correction])



generate_csv("train.csv", train_dataset)
generate_csv("eval.csv", eval_dataset)

before_result = happy_tt.eval("./eval.csv")
print("Before loss:", before_result.loss)


from happytransformer import TTTrainArgs

args = TTTrainArgs(batch_size=8)
happy_tt.train("train.csv", args=args)

before_loss = happy_tt.eval("eval.csv")

print("After loss: ", before_loss.loss)

from happytransformer import TTSettings

beam_settings =  TTSettings(num_beams=5, min_length=1, max_length=20)

example_1 = "grammar: This sentences, has bads grammar and spelling!"
result_1 = happy_tt.generate_text(example_1, args=beam_settings)
print(result_1.text)

example_2 = "grammar: I am enjoys, writtings articles ons AI."

result_2 = happy_tt.generate_text(example_2, args=beam_settings)
print(result_2.text)

