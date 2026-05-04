import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
        
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        self.word_to_id.clear()
        self.id_to_word.clear()
        special_tokens = [
        self.pad_token,
        self.unk_token,
        self.bos_token,
        self.eos_token
        ]
        for idx, token in enumerate(special_tokens):
            self.word_to_id[token] = idx
            self.id_to_word[idx] = token
        unique_words = set()
        for sentence in texts:
            unique_words.update(sentence.lower().split())
        start_idx = len(self.word_to_id)
        for idx, word in enumerate(sorted(unique_words), start=start_idx):
            self.word_to_id[word] = idx
            self.id_to_word[idx] = word
        self.vocab_size = len(self.word_to_id)
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        str_list = []
        words = text.lower().split()
        for sentence in words:
            str_list.extend(sentence.lower().split())
        int_list = []
        for i in str_list:
            if i in self.word_to_id:
                int_list.append(self.word_to_id[i])
            else:
                int_list.append(self.word_to_id[self.unk_token])
        return int_list
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        str_list = []
        for i in ids:
            if i in self.id_to_word:
                str_list.append(self.id_to_word[i])
            else:
                str_list.append("<UNK>")
        return " ".join(str_list)
