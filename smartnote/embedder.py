from typing import Optional, List
from loguru import logger
from tqdm.auto import tqdm
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

from .config import settings

class SentenceDataset(Dataset):
    def __init__(self, sentences, tokenizer, max_length):
        self.sentences = sentences
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, idx):
        sentence = self.sentences[idx]
        inputs = self.tokenizer(sentence, return_tensors="pt", max_length=self.max_length, 
                                padding="max_length", truncation=True)
        return inputs


class SentenceEmbedder:
    def __init__(
            self,
            model_name: Optional[str] = None,
            # dtype: Optional[torch.dtype] = None,
            batch_size: int = 32,
            max_length: int = 128,
            l2_normalize: bool = True
    ):
        """
        Initialize SentenceEmbedder object.

        :param model_name: huggingface model name, required if not set in settings
        # :param dtype: convert model to this dtype, e.g. torch.bfloat16, to save memory
        :param batch_size: batch size for inference
        :param max_length: max length of input sentence
        :param l2_normalize: whether to normalize embeddings to unit length
        """
        assert hasattr(settings, "TORCH_DEVICE"), "run init_env() first"
        if model_name is None:
            model_name = settings.embed.model_name
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name, trust_remote_code=True)
        if settings.TORCH_DEVICE.type != 'cpu':
            model = model.to(settings.TORCH_DEVICE)
        if torch.cuda.is_available() and torch.cuda.is_bf16_supported():
            logger.info("Device supports BF16, using BF16 to save VRAM")
            model = model.to(dtype=torch.bfloat16)
        model.eval()

        self.model = model
        self.tokenizer = tokenizer
        self.batch_size = batch_size
        self.max_length = max_length
        self.l2_normalize = l2_normalize

    def encode(self, sentences: List[str]) -> pd.DataFrame:
        """
        Encode list of sentences into embeddings.

        :param sentences: list of sentences to encode
        :return: DataFrame of embeddings
        """
        dataset = SentenceDataset(sentences, self.tokenizer, self.max_length)
        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False)

        embeddings = []
        with torch.no_grad():
            for batch in tqdm(dataloader, desc="Generating embeddings"):
                try:
                    input_ids = batch['input_ids'].to(settings.TORCH_DEVICE).squeeze(1)
                    attention_mask = batch['attention_mask'].to(settings.TORCH_DEVICE).squeeze(1)
                    outputs = self.model(input_ids, attention_mask=attention_mask)
                    _emb = outputs.last_hidden_state[:, 0]
                    # l2 normalization
                    if self.l2_normalize:
                        _emb = F.normalize(_emb, p=2, dim=1)
                    # numpy doesn't support bfloat16
                    embeddings.append(_emb.cpu().detach().float().numpy())
                except Exception as e:
                    logger.error('Error in encoding')
                    logger.error('batch: {}'.format(batch))
                    logger.error(e)
                    raise e

        df_embs = pd.DataFrame(
            np.vstack(embeddings), 
            columns=[f'emb{i}' for i in range(embeddings[0].shape[1])]
        )
        return df_embs
    

if __name__ == '__main__':
    from .config import init_env
    init_env('repo')

    emb = SentenceEmbedder()
    df = emb.encode([
        "This is a test sentence.",
    ])
    df = emb.encode([
        "This is a test sentence.",
        "This is another test sentence.",
    ])
    print(df)