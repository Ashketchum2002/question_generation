# experiment ID
exp = "qg-2"

# data directories
newsqa_data_dir = "/Users/ashketchum/Downloads"
squad_data_dir = "/Users/ashketchum/Downloads/"
out_dir = "/Users/ashketchum/Downloads/"
train_dir = squad_data_dir + "train/"
dev_dir = squad_data_dir + "dev/"

# model paths
# spacy_en = "/Users/ashish/Downloads/spacy/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0"
glove = "/Users/ashketchum/question_generation/glove/"
squad_models = "/ashketchum/ashish/Downloads/"

# preprocessing values
paragraph = False
min_len_context = 5
max_len_context = 100 if not paragraph else 1000
min_len_question = 5
max_len_question = 20
word_embedding_size = 300
answer_embedding_size = 2
in_vocab_size = 45000
out_vocab_size = 28000

# training hyper-parameters
num_epochs = 1
batch_size = 64
learning_rate = 1.0
hidden_size = 600
n_layers = 2
drop_prob = 0.3
start_decay_epoch = 8
decay_rate = 0.5
use_answer = True
cuda = False
pretrained = False

# eval hyper-parameters
eval_batch_size = 1
min_len_sentence = 5
top_k = 0.
top_p = 0.9
temperature = 0.7
decode_type = "topk"


with open("/Users/ashketchum/Downloads/train/train.sentence") as file:
    lines = file.readlines()
    print(lines[99])