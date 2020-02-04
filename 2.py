{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Prerequisites"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "pi\n",
    "nltk==3.4.5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data loading"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load data from this link:\n",
    "    \n",
    "    https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "import nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"train.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>comment_text</th>\n",
       "      <th>toxic</th>\n",
       "      <th>severe_toxic</th>\n",
       "      <th>obscene</th>\n",
       "      <th>threat</th>\n",
       "      <th>insult</th>\n",
       "      <th>identity_hate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0000997932d777bf</td>\n",
       "      <td>Explanation\\nWhy the edits made under my usern...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>000103f0d9cfb60f</td>\n",
       "      <td>D'aww! He matches this background colour I'm s...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000113f07ec002fd</td>\n",
       "      <td>Hey man, I'm really not trying to edit war. It...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0001b41b1c6bb37e</td>\n",
       "      <td>\"\\nMore\\nI can't make any real suggestions on ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0001d958c54c6e35</td>\n",
       "      <td>You, sir, are my hero. Any chance you remember...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>00025465d4725e87</td>\n",
       "      <td>\"\\n\\nCongratulations from me as well, use the ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0002bcb3da6cb337</td>\n",
       "      <td>COCKSUCKER BEFORE YOU PISS AROUND ON MY WORK</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>00031b1e95af7921</td>\n",
       "      <td>Your vandalism to the Matt Shirvington article...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>00037261f536c51d</td>\n",
       "      <td>Sorry if the word 'nonsense' was offensive to ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>00040093b2687caa</td>\n",
       "      <td>alignment on this subject and which are contra...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 id                                       comment_text  toxic  \\\n",
       "0  0000997932d777bf  Explanation\\nWhy the edits made under my usern...      0   \n",
       "1  000103f0d9cfb60f  D'aww! He matches this background colour I'm s...      0   \n",
       "2  000113f07ec002fd  Hey man, I'm really not trying to edit war. It...      0   \n",
       "3  0001b41b1c6bb37e  \"\\nMore\\nI can't make any real suggestions on ...      0   \n",
       "4  0001d958c54c6e35  You, sir, are my hero. Any chance you remember...      0   \n",
       "5  00025465d4725e87  \"\\n\\nCongratulations from me as well, use the ...      0   \n",
       "6  0002bcb3da6cb337       COCKSUCKER BEFORE YOU PISS AROUND ON MY WORK      1   \n",
       "7  00031b1e95af7921  Your vandalism to the Matt Shirvington article...      0   \n",
       "8  00037261f536c51d  Sorry if the word 'nonsense' was offensive to ...      0   \n",
       "9  00040093b2687caa  alignment on this subject and which are contra...      0   \n",
       "\n",
       "   severe_toxic  obscene  threat  insult  identity_hate  \n",
       "0             0        0       0       0              0  \n",
       "1             0        0       0       0              0  \n",
       "2             0        0       0       0              0  \n",
       "3             0        0       0       0              0  \n",
       "4             0        0       0       0              0  \n",
       "5             0        0       0       0              0  \n",
       "6             1        1       0       1              0  \n",
       "7             0        0       0       0              0  \n",
       "8             0        0       0       0              0  \n",
       "9             0        0       0       0              0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(159571, 8)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the previous day we worked with already preprocessed data for us.  \n",
    "This day try to make this preprocessing by ourselves."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Text lowercasing: "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Create a column 'comment_text_lower' in a dataframe, and make all of the text from the column 'comment_text' copied to the 'comment_text_lower' column, but lowercased."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['comment_text_lower'] = df['comment_text'].str.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>comment_text</th>\n",
       "      <th>toxic</th>\n",
       "      <th>severe_toxic</th>\n",
       "      <th>obscene</th>\n",
       "      <th>threat</th>\n",
       "      <th>insult</th>\n",
       "      <th>identity_hate</th>\n",
       "      <th>comment_text_lower</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0000997932d777bf</td>\n",
       "      <td>Explanation\\nWhy the edits made under my usern...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>explanation\\nwhy the edits made under my usern...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>000103f0d9cfb60f</td>\n",
       "      <td>D'aww! He matches this background colour I'm s...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>d'aww! he matches this background colour i'm s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000113f07ec002fd</td>\n",
       "      <td>Hey man, I'm really not trying to edit war. It...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>hey man, i'm really not trying to edit war. it...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0001b41b1c6bb37e</td>\n",
       "      <td>\"\\nMore\\nI can't make any real suggestions on ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>\"\\nmore\\ni can't make any real suggestions on ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0001d958c54c6e35</td>\n",
       "      <td>You, sir, are my hero. Any chance you remember...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>you, sir, are my hero. any chance you remember...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 id                                       comment_text  toxic  \\\n",
       "0  0000997932d777bf  Explanation\\nWhy the edits made under my usern...      0   \n",
       "1  000103f0d9cfb60f  D'aww! He matches this background colour I'm s...      0   \n",
       "2  000113f07ec002fd  Hey man, I'm really not trying to edit war. It...      0   \n",
       "3  0001b41b1c6bb37e  \"\\nMore\\nI can't make any real suggestions on ...      0   \n",
       "4  0001d958c54c6e35  You, sir, are my hero. Any chance you remember...      0   \n",
       "\n",
       "   severe_toxic  obscene  threat  insult  identity_hate  \\\n",
       "0             0        0       0       0              0   \n",
       "1             0        0       0       0              0   \n",
       "2             0        0       0       0              0   \n",
       "3             0        0       0       0              0   \n",
       "4             0        0       0       0              0   \n",
       "\n",
       "                                  comment_text_lower  \n",
       "0  explanation\\nwhy the edits made under my usern...  \n",
       "1  d'aww! he matches this background colour i'm s...  \n",
       "2  hey man, i'm really not trying to edit war. it...  \n",
       "3  \"\\nmore\\ni can't make any real suggestions on ...  \n",
       "4  you, sir, are my hero. any chance you remember...  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Text tokenization "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Create a column 'comment_text_tokenized_space' in a dataframe, and make all of the text from the column 'comment_text' copied to the 'comment_text_tokenized_space' column, but lowercased tokenized by space."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['comment_text_tokenized_space'] = df['comment_text_lower'].str.split() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>comment_text</th>\n",
       "      <th>toxic</th>\n",
       "      <th>severe_toxic</th>\n",
       "      <th>obscene</th>\n",
       "      <th>threat</th>\n",
       "      <th>insult</th>\n",
       "      <th>identity_hate</th>\n",
       "      <th>comment_text_lower</th>\n",
       "      <th>comment_text_tokenized_space</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0000997932d777bf</td>\n",
       "      <td>Explanation\\nWhy the edits made under my usern...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>explanation\\nwhy the edits made under my usern...</td>\n",
       "      <td>[explanation, why, the, edits, made, under, my...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>000103f0d9cfb60f</td>\n",
       "      <td>D'aww! He matches this background colour I'm s...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>d'aww! he matches this background colour i'm s...</td>\n",
       "      <td>[d'aww!, he, matches, this, background, colour...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000113f07ec002fd</td>\n",
       "      <td>Hey man, I'm really not trying to edit war. It...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>hey man, i'm really not trying to edit war. it...</td>\n",
       "      <td>[hey, man,, i'm, really, not, trying, to, edit...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0001b41b1c6bb37e</td>\n",
       "      <td>\"\\nMore\\nI can't make any real suggestions on ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>\"\\nmore\\ni can't make any real suggestions on ...</td>\n",
       "      <td>[\", more, i, can't, make, any, real, suggestio...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0001d958c54c6e35</td>\n",
       "      <td>You, sir, are my hero. Any chance you remember...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>you, sir, are my hero. any chance you remember...</td>\n",
       "      <td>[you,, sir,, are, my, hero., any, chance, you,...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 id                                       comment_text  toxic  \\\n",
       "0  0000997932d777bf  Explanation\\nWhy the edits made under my usern...      0   \n",
       "1  000103f0d9cfb60f  D'aww! He matches this background colour I'm s...      0   \n",
       "2  000113f07ec002fd  Hey man, I'm really not trying to edit war. It...      0   \n",
       "3  0001b41b1c6bb37e  \"\\nMore\\nI can't make any real suggestions on ...      0   \n",
       "4  0001d958c54c6e35  You, sir, are my hero. Any chance you remember...      0   \n",
       "\n",
       "   severe_toxic  obscene  threat  insult  identity_hate  \\\n",
       "0             0        0       0       0              0   \n",
       "1             0        0       0       0              0   \n",
       "2             0        0       0       0              0   \n",
       "3             0        0       0       0              0   \n",
       "4             0        0       0       0              0   \n",
       "\n",
       "                                  comment_text_lower  \\\n",
       "0  explanation\\nwhy the edits made under my usern...   \n",
       "1  d'aww! he matches this background colour i'm s...   \n",
       "2  hey man, i'm really not trying to edit war. it...   \n",
       "3  \"\\nmore\\ni can't make any real suggestions on ...   \n",
       "4  you, sir, are my hero. any chance you remember...   \n",
       "\n",
       "                        comment_text_tokenized_space  \n",
       "0  [explanation, why, the, edits, made, under, my...  \n",
       "1  [d'aww!, he, matches, this, background, colour...  \n",
       "2  [hey, man,, i'm, really, not, trying, to, edit...  \n",
       "3  [\", more, i, can't, make, any, real, suggestio...  \n",
       "4  [you,, sir,, are, my, hero., any, chance, you,...  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### There a lot of words tokenized by space, but they contains additional punctuation characters. Let's try to delete them. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load punctuation \n",
    "from string import punctuation\n",
    "\n",
    "punctuation = punctuation + ''\n",
    "\n",
    "def clean_token(token): \n",
    "    '''\n",
    "    Args: token: str \n",
    "    Returns: token: str \n",
    "    \n",
    "    This function deletes all of the punctuation characters \n",
    "    in the token and returns the cleaned one \n",
    "    '''\n",
    "    chars_cleaned = token.strip(punctuation) \n",
    "    return \"\".join(chars_cleaned)\n",
    "\n",
    "# Use method apply - read about it more if needed (pandas, df.apply, lambda functions, list of comprehension)\n",
    "df['comment_text_tokenized_space_cleaned'] = df.comment_text_tokenized_space.apply(\n",
    "    lambda x:  [clean_token(i) for i in x] )\n",
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>comment_text</th>\n",
       "      <th>toxic</th>\n",
       "      <th>severe_toxic</th>\n",
       "      <th>obscene</th>\n",
       "      <th>threat</th>\n",
       "      <th>insult</th>\n",
       "      <th>identity_hate</th>\n",
       "      <th>comment_text_lower</th>\n",
       "      <th>comment_text_tokenized_space</th>\n",
       "      <th>comment_text_tokenized_space_cleaned</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0000997932d777bf</td>\n",
       "      <td>Explanation\\nWhy the edits made under my usern...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>explanation\\nwhy the edits made under my usern...</td>\n",
       "      <td>[explanation, why, the, edits, made, under, my...</td>\n",
       "      <td>[explanation, why, the, edits, made, under, my...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>000103f0d9cfb60f</td>\n",
       "      <td>D'aww! He matches this background colour I'm s...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>d'aww! he matches this background colour i'm s...</td>\n",
       "      <td>[d'aww!, he, matches, this, background, colour...</td>\n",
       "      <td>[daww, he, matches, this, background, colour, ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000113f07ec002fd</td>\n",
       "      <td>Hey man, I'm really not trying to edit war. It...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>hey man, i'm really not trying to edit war. it...</td>\n",
       "      <td>[hey, man,, i'm, really, not, trying, to, edit...</td>\n",
       "      <td>[hey, man, im, really, not, trying, to, edit, ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0001b41b1c6bb37e</td>\n",
       "      <td>\"\\nMore\\nI can't make any real suggestions on ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>\"\\nmore\\ni can't make any real suggestions on ...</td>\n",
       "      <td>[\", more, i, can't, make, any, real, suggestio...</td>\n",
       "      <td>[, more, i, cant, make, any, real, suggestions...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0001d958c54c6e35</td>\n",
       "      <td>You, sir, are my hero. Any chance you remember...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>you, sir, are my hero. any chance you remember...</td>\n",
       "      <td>[you,, sir,, are, my, hero., any, chance, you,...</td>\n",
       "      <td>[you, sir, are, my, hero, any, chance, you, re...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 id                                       comment_text  toxic  \\\n",
       "0  0000997932d777bf  Explanation\\nWhy the edits made under my usern...      0   \n",
       "1  000103f0d9cfb60f  D'aww! He matches this background colour I'm s...      0   \n",
       "2  000113f07ec002fd  Hey man, I'm really not trying to edit war. It...      0   \n",
       "3  0001b41b1c6bb37e  \"\\nMore\\nI can't make any real suggestions on ...      0   \n",
       "4  0001d958c54c6e35  You, sir, are my hero. Any chance you remember...      0   \n",
       "\n",
       "   severe_toxic  obscene  threat  insult  identity_hate  \\\n",
       "0             0        0       0       0              0   \n",
       "1             0        0       0       0              0   \n",
       "2             0        0       0       0              0   \n",
       "3             0        0       0       0              0   \n",
       "4             0        0       0       0              0   \n",
       "\n",
       "                                  comment_text_lower  \\\n",
       "0  explanation\\nwhy the edits made under my usern...   \n",
       "1  d'aww! he matches this background colour i'm s...   \n",
       "2  hey man, i'm really not trying to edit war. it...   \n",
       "3  \"\\nmore\\ni can't make any real suggestions on ...   \n",
       "4  you, sir, are my hero. any chance you remember...   \n",
       "\n",
       "                        comment_text_tokenized_space  \\\n",
       "0  [explanation, why, the, edits, made, under, my...   \n",
       "1  [d'aww!, he, matches, this, background, colour...   \n",
       "2  [hey, man,, i'm, really, not, trying, to, edit...   \n",
       "3  [\", more, i, can't, make, any, real, suggestio...   \n",
       "4  [you,, sir,, are, my, hero., any, chance, you,...   \n",
       "\n",
       "                comment_text_tokenized_space_cleaned  \n",
       "0  [explanation, why, the, edits, made, under, my...  \n",
       "1  [daww, he, matches, this, background, colour, ...  \n",
       "2  [hey, man, im, really, not, trying, to, edit, ...  \n",
       "3  [, more, i, cant, make, any, real, suggestions...  \n",
       "4  [you, sir, are, my, hero, any, chance, you, re...  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Quite a lot of work, yes?   \n",
    "Let's try to use already implemented methods for performing a tokenization:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## NLTK"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
   {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#  sent_tokenize - if you need to separate sentences one from another \n",
    "#  word_tokenize - if you need to tokenize a sentence\n",
    "from nltk.tokenize import sent_tokenize, word_tokenize\n",
    "\n",
    "nltk.download('punkt') # if needed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['nltk_tokenized'] = df.comment_text.apply(### Your code here)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>comment_text</th>\n",
       "      <th>toxic</th>\n",
       "      <th>severe_toxic</th>\n",
       "      <th>obscene</th>\n",
       "      <th>threat</th>\n",
       "      <th>insult</th>\n",
       "      <th>identity_hate</th>\n",
       "      <th>comment_text_lower</th>\n",
       "      <th>comment_text_tokenized_space</th>\n",
       "      <th>comment_text_tokenized_space_cleaned</th>\n",
       "      <th>nltk_tokenized</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0000997932d777bf</td>\n",
       "      <td>Explanation\\nWhy the edits made under my usern...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>explanation\\nwhy the edits made under my usern...</td>\n",
       "      <td>[explanation, why, the, edits, made, under, my...</td>\n",
       "      <td>[explanation, why, the, edits, made, under, my...</td>\n",
       "      <td>[Explanation, Why, the, edits, made, under, my...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>000103f0d9cfb60f</td>\n",
       "      <td>D'aww! He matches this background colour I'm s...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>d'aww! he matches this background colour i'm s...</td>\n",
       "      <td>[d'aww!, he, matches, this, background, colour...</td>\n",
       "      <td>[daww, he, matches, this, background, colour, ...</td>\n",
       "      <td>[D'aww, !, He, matches, this, background, colo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>000113f07ec002fd</td>\n",
       "      <td>Hey man, I'm really not trying to edit war. It...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>hey man, i'm really not trying to edit war. it...</td>\n",
       "      <td>[hey, man,, i'm, really, not, trying, to, edit...</td>\n",
       "      <td>[hey, man, im, really, not, trying, to, edit, ...</td>\n",
       "      <td>[Hey, man, ,, I, 'm, really, not, trying, to, ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0001b41b1c6bb37e</td>\n",
       "      <td>\"\\nMore\\nI can't make any real suggestions on ...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>\"\\nmore\\ni can't make any real suggestions on ...</td>\n",
       "      <td>[\", more, i, can't, make, any, real, suggestio...</td>\n",
       "      <td>[, more, i, cant, make, any, real, suggestions...</td>\n",
       "      <td>[``, More, I, ca, n't, make, any, real, sugges...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0001d958c54c6e35</td>\n",
       "      <td>You, sir, are my hero. Any chance you remember...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>you, sir, are my hero. any chance you remember...</td>\n",
       "      <td>[you,, sir,, are, my, hero., any, chance, you,...</td>\n",
       "      <td>[you, sir, are, my, hero, any, chance, you, re...</td>\n",
       "      <td>[You, ,, sir, ,, are, my, hero, ., Any, chance...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 id                                       comment_text  toxic  \\\n",
       "0  0000997932d777bf  Explanation\\nWhy the edits made under my usern...      0   \n",
       "1  000103f0d9cfb60f  D'aww! He matches this background colour I'm s...      0   \n",
       "2  000113f07ec002fd  Hey man, I'm really not trying to edit war. It...      0   \n",
       "3  0001b41b1c6bb37e  \"\\nMore\\nI can't make any real suggestions on ...      0   \n",
       "4  0001d958c54c6e35  You, sir, are my hero. Any chance you remember...      0   \n",
       "\n",
       "   severe_toxic  obscene  threat  insult  identity_hate  \\\n",
       "0             0        0       0       0              0   \n",
       "1             0        0       0       0              0   \n",
       "2             0        0       0       0              0   \n",
       "3             0        0       0       0              0   \n",
       "4             0        0       0       0              0   \n",
       "\n",
       "                                  comment_text_lower  \\\n",
       "0  explanation\\nwhy the edits made under my usern...   \n",
       "1  d'aww! he matches this background colour i'm s...   \n",
       "2  hey man, i'm really not trying to edit war. it...   \n",
       "3  \"\\nmore\\ni can't make any real suggestions on ...   \n",
       "4  you, sir, are my hero. any chance you remember...   \n",
       "\n",
       "                        comment_text_tokenized_space  \\\n",
       "0  [explanation, why, the, edits, made, under, my...   \n",
       "1  [d'aww!, he, matches, this, background, colour...   \n",
       "2  [hey, man,, i'm, really, not, trying, to, edit...   \n",
       "3  [\", more, i, can't, make, any, real, suggestio...   \n",
       "4  [you,, sir,, are, my, hero., any, chance, you,...   \n",
       "\n",
       "                comment_text_tokenized_space_cleaned  \\\n",
       "0  [explanation, why, the, edits, made, under, my...   \n",
       "1  [daww, he, matches, this, background, colour, ...   \n",
       "2  [hey, man, im, really, not, trying, to, edit, ...   \n",
       "3  [, more, i, cant, make, any, real, suggestions...   \n",
       "4  [you, sir, are, my, hero, any, chance, you, re...   \n",
       "\n",
       "                                      nltk_tokenized  \n",
       "0  [Explanation, Why, the, edits, made, under, my...  \n",
       "1  [D'aww, !, He, matches, this, background, colo...  \n",
       "2  [Hey, man, ,, I, 'm, really, not, trying, to, ...  \n",
       "3  [``, More, I, ca, n't, make, any, real, sugges...  \n",
       "4  [You, ,, sir, ,, are, my, hero, ., Any, chance...  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Please, see that word_tokenize not only separated the punctuation from the text corretly, but saved the punctuation inside the token (' or -)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### ! Modify your function defined previously to save a pucntuation inside the token and delete it only if it glued to the token in the end or in the beginning. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_token_modified(token):\n",
    "    return token.strip(list(punctuation))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def flat_nested(nested):\n",
    "    '''\n",
    "    Args: nested list: list ([[a], [b]])\n",
    "    Returns: flatten list: list ([a, b])\n",
    "    '''\n",
    "    flatten = []\n",
    "    for i in nested:\n",
    "        if type(i) == list:\n",
    "            flatten = flatten + flat_nested(i)\n",
    "        else:\n",
    "            flatten.append(i)\n",
    "    return flatten"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.probability import FreqDist\n",
    "\n",
    "# Frequency dict will accept only list of tokens, not list of lists of tokens, etc \n",
    "# Flat your list previously if needed \n",
    "fdist = FreqDist(flat_nested(df.comment_text_tokenized_space_cleaned.tolist()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('the', 495141),\n",
       " ('to', 296821),\n",
       " ('of', 224004),\n",
       " ('and', 222325),\n",
       " ('a', 214120),\n",
       " ('you', 204456),\n",
       " ('i', 200423),\n",
       " ('is', 175926),\n",
       " ('', 161939),\n",
       " ('that', 154258),\n",
       " ('in', 144128),\n",
       " ('it', 129540),\n",
       " ('for', 102430),\n",
       " ('this', 97011),\n",
       " ('not', 93318),\n",
       " ('on', 89425),\n",
       " ('be', 83313),\n",
       " ('as', 77216),\n",
       " ('have', 72167),\n",
       " ('are', 71852)]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fdist.most_common(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Analyse the results. What are these words? Have you seen it previously in the 1 task?  \n",
    "Does these words contains a lot of meaningful information? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "Мы не можем ничего понять с этих слов и отнести их к какой то конретной категории, так как они являются вспомогающими словами в предложениях и не имеют значения"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Distribution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZcAAAEcCAYAAAALEfkWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjAsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+17YcXAAAgAElEQVR4nO3dd3xc1Zn/8c+jXm1ZrnLBNsZUYwOysSGwgdAMSxY2SwoJNQR2E1J2SbKQTfJLI1mym06ybAgQIIQQ0gB7aaaYamPLGFcwLrjbuEoukmxLfn5/3CN5PB5JI3lGI0vf9+t1X5o5c+acc6XRPPeUe6+5OyIiIqmUlekGiIhI96PgIiIiKafgIiIiKafgIiIiKafgIiIiKafgIiIiKZeT6QZ0Ff369fMRI0Z06L11dXUUFhamNK/KzEyZ3W1/VKbKTGWZicyZM2eLu/c/5AV31+ZOZWWld1RVVVXK86rMzJTZ3fZHZarMVJaZCFDlCb5TNSwmIiIpp+AiIiIpl9bgYmYrzWyBmb1lZlUhrdzMppnZ0vCzT0g3M/uFmS0zs/lmdlpMOdeG/EvN7NqY9MpQ/rLwXmutDhER6Ryd0XM5191Pcffx4fltwPPuPhp4PjwHuBgYHbabgLsgChTAt4CJwOnAt2KCxV3AjTHvm9xGHSIi0gkyMSx2GfBAePwAcHlM+oNhjmgmUGZmFcBFwDR33+bu24FpwOTwWi93nxkmlR6MKytRHSIi0gnSHVwceNbM5pjZTSFtoLtvCI83AgPD4yHAmpj3rg1praWvTZDeWh0iItIJzNN4yX0zG+Lu68xsAFGP4wvAE+5eFpNnu7v3MbOpwB3u/mpIfx64FTgHKHD320P6N4E6YHrIf35IPxu41d0vNbPqRHUkaN9NRENwVFRUVE6ZMqVd+9fozsrqBjZW1/KBkb2Tek9tbS1FRUUpy6cyU1tmd9sflakyU1lmIuPHj58TM+1xQKL1yenYgG8DXwGWABUhrQJYEh7/GrgyJv+S8PqVwK9j0n8d0iqAd2LSm/O1VEdrW0fOc9nX0OhHf+3/fPitU71ub0NS7zlS1rP31DK72/6oTJWZyjITobPPczGzYjMrbXoMXAgsBJ4AmlZ8XQs8Hh4/AVwTVo1NAmo8Gtp6BrjQzPqEifwLgWfCazvMbFJYJXZNXFmJ6kipnOwsBvUqAGBDTX06qhAROSKl8/IvA4G/hdXBOcDD7v60mc0GHjWzG4BVwMdC/ieBS4BlQC1wPYC7bzOz7wGzQ77vuvu28PhzwP1AIfBU2ADuaKGOlBtSVsi66jrWV9cxsl9xuqoRETmipC24uPsKYFyC9K3AeQnSHbi5hbLuA+5LkF4FjEm2jnQY0qcQVsK67XWdUZ2IyBFBZ+gfpiFl0QXf1lYruIiINFFwOUxD+kTBRT0XEZEDFFwOU1PPZV11bYZbIiLSdSi4HKbmnouGxUREmim4HKamnsuG6noa96fvhFQRkSOJgsthKsjNpnd+Fg37nU07da6LiAgouKREv6Lo16hJfRGRiIJLCvQvygY07yIi0kTBJQX6Fyu4iIjEUnBJgeaei4bFREQABZeU0LCYiMjBFFxSoHlYTD0XERFAwSUlYnsunsabr4mIHCkUXFKgONcoyc+hdm8j1bX7Mt0cEZGMU3BJATOLucaYhsZERBRcUqTpGmNrNe8iIqLgkiqDy6LbHa9Xz0VERMElVYaUFQEaFhMRAQWXlNFNw0REDlBwSRFN6IuIHKDgkiJDddMwEZFmCi4p0r8kn7zsLLbt3kvt3oZMN0dEJKMUXFIkK8uo0IoxERFAwSWlmuZddK6LiPR0Ci4p1BRc1lfrdsci0rMpuKTQ4OYVY7UZbomISGYpuKSQznUREYkouKTQUJ3rIiICKLiklHouIiIRBZcUquhdiBls3FHPvsb9mW6OiEjGKLikUF5OFgNK89nvsLFGK8ZEpOdScEkxXWNMRETBJeWG9AmX3te8i4j0YAouKXbgREoFFxHpuRRcUmyIro4sIpL+4GJm2WY218ymhucjzewNM1tmZn80s7yQnh+eLwuvj4gp42shfYmZXRSTPjmkLTOz22LSE9bRGYaEi1cquIhIT9YZPZcvAW/HPP8h8FN3PwbYDtwQ0m8Atof0n4Z8mNmJwCeAk4DJwP+EgJUN/Aq4GDgRuDLkba2OtGu+3bHmXESkB0trcDGzocDfA/eE5wZ8CPhzyPIAcHl4fFl4Tnj9vJD/MuARd9/j7u8By4DTw7bM3Ve4+17gEeCyNupIu9hhMXfvrGpFRLoUS+cXoJn9GfhPoBT4CnAdMDP0KDCzYcBT7j7GzBYCk919bXhtOTAR+HZ4z0Mh/V7gqVDFZHf/TEi/Oi7/IXUkaN9NwE0AFRUVlVOmTOnQftbW1lJUVNT8/NrH3mfXPufeD/enrCC71bzJlpmKvCqza9etMlVmVy8zkfHjx89x9/GHvODuadmAS4H/CY/PAaYC/Yh6G015hgELw+OFwNCY15aH/L8EropJvxe4Imz3xKRfHfK2WEdrW2VlpXdUVVXVQc8v/tnLPvzWqT539fY28yZbZiryqsyuXbfKVJldvcxEgCpP8J2azmGxDwD/YGYriYasPgT8HCgzs5yQZyiwLjxeFwIB4fXewNbY9Lj3tJS+tZU6OoWuMSYiPV3agou7f83dh7r7CKIJ+Rfc/VPAi0S9DoBrgcfD4yfCc8LrL4So+ATwibCabCQwGpgFzAZGh5VheaGOJ8J7WqqjUwzRfV1EpIfLxHkutwK3mNkyoC/RMBfhZ9+QfgtwG4C7LwIeBRYDTwM3u3ujuzcAnweeIVqN9mjI21odnWJoH92RUkR6tpy2sxw+d58OTA+PVxCt9IrPUw98tIX3fx/4foL0J4EnE6QnrKOzNPVc1mpYTER6KJ2hnwaDdfFKEenhFFzS4MCEvuZcRKRnUnBJg77FeRTkZrGjvoGd9fsy3RwRkU6n4JIGZqahMRHp0RRc0qR5ObIm9UWkB1JwSZOhuvS+iPRgCi5pop6LiPRkCi5popuGiUhPpuCSJs33dVFwEZEeSMElTXTxShHpyRRc0mRgaT7ZWcamnXvY09CY6eaIiHQqBZc0ycnOYlCvAgA26AKWItLDKLik0RCdSCkiPZSCSxpp3kVEeioFlzRqvvS+ei4i0sMouKTRkOabhim4iEjPouCSRjpLX0R6KgWXNNJZ+iLSUym4pFFTz2VDTR3793uGWyMi0nkUXNKoIDebfiV57Gt0Nu3ck+nmiIh0GgWXNDtw0zDd8lhEeg4FlzRrXo6sSX0R6UEUXNJMZ+mLSE+k4JJmOktfRHoiBZc0a+q56ERKEelJFFzSTOe6iEhPpOCSZkOb7ki5vQ53nesiIj2Dgkua9SrMoSQ/h917G6mp25fp5oiIdAoFlzQzMy1HFpEeR8GlEwwui+5IqXkXEekpFFw6gZYji0hPo+DSCYY0Teqr5yIiPYSCSydQz0VEehoFl07QfCJljYKLiPQMCi6dYKh6LiLSw6QtuJhZgZnNMrN5ZrbIzL4T0kea2RtmtszM/mhmeSE9PzxfFl4fEVPW10L6EjO7KCZ9ckhbZma3xaQnrCNT+pfkk5edxdbde9nToBMpRaT7a3dwMbM+ZjY2iax7gA+5+zjgFGCymU0Cfgj81N2PAbYDN4T8NwDbQ/pPQz7M7ETgE8BJwGTgf8ws28yygV8BFwMnAleGvLRSR0ZkZRkVYTny5trGTDZFRKRTJBVczGy6mfUys3LgTeA3ZvaT1t7jkV3haW7YHPgQ8OeQ/gBweXh8WXhOeP08M7OQ/oi773H394BlwOlhW+buK9x9L/AIcFl4T0t1ZEzTvIuCi4j0BJbM9a7MbK67n2pmnwGGufu3zGy+u7fagwm9iznAMUS9jP8GZoYeBWY2DHjK3ceY2UJgsruvDa8tByYC3w7veSik3ws8FaqY7O6fCelXx+U/pI4E7bsJuAmgoqKicsqUKW3+LhKpra2lqKio1Ty/ml3DCyvruP7kAi49viwlZbY3r8rs2nWrTJXZ1ctMZPz48XPcffwhL7h7mxuwAKgAngUmhLT5ybw35C0DXgTOIuptNKUPAxaGxwuBoTGvLQf6Ab8EropJvxe4Imz3xKRfHfL2a6mO1rbKykrvqKqqqjbz/HTaEh9+61T/wr0vpKzM9uZVmV27bpWpMrt6mYkAVZ7gOzXZOZfvAM+EL+3ZZnY0sDTJ9+Lu1SG4nAGUmVlOeGkosC48XhcCAeH13sDW2PS497SUvrWVOjLm9BHlAFSt36OrI4tIt5dscNng7mPd/XMA7r4CaHXOxcz6m1lZeFwIXAC8TRRkrgjZrgUeD4+fCM8Jr78QouITwCfCarKRwGhgFjAbGB1WhuURTfo/Ed7TUh0Zc/rIcsqL81i/q5F339/V9htERI5gyQaXO5NMi1UBvGhm84kCwTR3nwrcCtxiZsuAvkTDXISffUP6LcBtAO6+CHgUWAw8Ddzs7o3u3gB8nqhH9TbwaMhLK3VkTE52FhedNBCAJxdsyHBrRETSK6e1F83sDOBMoL+Z3RLzUi8gu7X3uvt84NQE6SuIVnrFp9cDH22hrO8D30+Q/iTwZLJ1ZNrFYyr4w6w1PLVwA/92wbGZbo6ISNq01XPJA0qIglBpzLaDA8NOkqQzRvWlJNd49/1dLNu0M9PNERFJm1Z7Lu7+EvCSmd3v7qs6qU3dVm52FqcPKeCFlXU8uWAjXzyvNNNNEhFJi2TnXPLN7G4ze9bMXmja0tqybmrS0OhMfc27iEh31mrPJcafgP8F7gF0ivlhGDsgj9KCHN7ZuJMVm3dxdP+STDdJRCTlku25NLj7Xe4+y93nNG1pbVk3lZttXHBCtGrsqYUbM9waEZH0SDa4TDGzz5lZhZmVN21pbVk3dvHJFQA8tVBDYyLSPSU7LNZ0cuNXY9IcODq1zekZzh7dj5L8HBau28HqrbUc1bfj1/UREemKkuq5uPvIBJsCSwcV5GZz3gkDAPVeRKR7SqrnYmbXJEp39wdT25ye4+IxFTz+1nqeXLCBf/7gqEw3R0QkpZIdFpsQ87gAOI/ovi4KLh10znH9KcrLZt7aGtZur2VoHw2NiUj3keyw2BdithuB04jO3JcOKsjN5tzjo6Gxp7VqTES6mXbf5jjYDYxMZUN6okvGRKvGdEKliHQ3yc65TCFaHQbRBStPILpSsRyGc47rT0FuFm+urmZDTR0VvQsz3SQRkZRIds7lRzGPG4BVHm5HLB1XnJ/DOccO4OlFG3l64Uau/4A6gyLSPSQ75/IS8A7RFZH7AHvT2aie5OKTBwHw1ALNu4hI95FUcDGzjxHd/fGjwMeAN8xMl9xPgfNOGEheThazV21j0476TDdHRCQlkp3Q/zowwd2vdfdriG7E9c30NavnKMnP4YPH9scdnl6k3ouIdA/JBpcsd98U83xrO94rbbgkDI1p1ZiIdBfJTug/bWbPAH8Izz9OgtsLS8ecd8JAcrONWe9tY/POPfQvzc90k0REDkurvQ8zO8bMPuDuXwV+DYwN2wzg7k5oX4/QqyCXs0f3Z7/Ds4s1NCYiR762hrZ+BuwAcPe/uvst7n4L8LfwmqTIxWO0akxEuo+2gstAd18QnxjSRqSlRT3UBScOJCfLmLFiK9t2a6W3iBzZ2gouZa28ptPJU6isKI8zj+lH435nmobGROQI11ZwqTKzG+MTzewzgG5znGKXjGlaNabgIiJHtraCy78C15vZdDP7cdheAm4AvpT+5vUsF540iOws47VlW9i5d3+mmyMi0mGtBhd3f9/dzwS+A6wM23fc/Qx31+F1ipUX5zHp6HIa9juz1+tsfRE5ciV1nou7vwi8mOa2CHDJyRW8tmwrL75Xx9+t2EpZUR5lRbn0LsylIDc7080TEUlKsidRSie58MRBfPOxhSzeso+P3z3zoNcKcrMoKzwQbMqKcikvzmdIdj0njW1U8BGRLkPBpYvpX5rP9y4fw99mLoW8Iqrr9lFdu4+aur3U79vPxn31bExwgcu75kzjghMH8uFxgzl7dH/ycnR1HhHJHAWXLuhTE4dzfM4WKisrm9Pcndq9jSHY7KWmdh/VdftYva2Wv7yxnKXb9vHYW+t57K319CrIYfKYQXx43GDOOLovOdkKNCLSuRRcjhBmRnF+DsX5OQwpO/gUowkl1fQfcQJT5q9nyrz1vLNxJ49WreXRqrX0Lc7j4pMH8eGxg8lyb6F0EZHUUnDpJo7qW8TN5x7Dzecew7JNO5kybwNT5q1nxZbdPDRzNQ/NXE2/wiyuqVnKxycMY2Cvgkw3WUS6MQWXbuiYAaX82wWl/Ov5o1m8YQdT5m1g6vz1rN1ex0+mvcvPn1/K+ScM4JMTh3P2Mf3IyrJMN1lEuhkFl27MzDhpcG9OGtybf7/oOO5/egZV2/N5dtH7PBO2YeWFXHn6UXy0cpgu9S8iKaPg0kNkZRnjBubz6Usq2bSznj9VreXhN1azZlsd//X0En467V0uPHEQn5p4FGeM6pvp5orIES5ty4jMbJiZvWhmi81skZl9KaSXm9k0M1safvYJ6WZmvzCzZWY238xOiynr2pB/qZldG5NeaWYLwnt+YWbWWh0SGVBawM3nHsPL/34uv71+AhecOJDG/c7/LdjAJ+95g3N/NJ1fza7hNy+vYPqSTayvrsO1GEBE2iGdPZcG4Mvu/qaZlQJzzGwacB3wvLvfYWa3AbcBtwIXA6PDNhG4C5hoZuXAt4DxgIdynnD37SHPjcAbRHfGnAw8FcpMVIfEyM4yzj1uAOceN4ANNXX8cfYa/jh7DSu31rJyK7yw8u3mvKX5ORwzsIRjB5Ry7KBSjh1YwrEDSxV0RCShtAUXd98AbAiPd5rZ28AQ4DLgnJDtAWA60Rf/ZcCDHn1bzTSzMjOrCHmnufs2gBCgJpvZdKCXu88M6Q8ClxMFl5bqkBZU9C7kX88/ls+fewxz11Tz7KxF1Of14d33d7J00y627d7L3NXVzF1dfdD7RvXJ4Y/H76FfieZrROQA64wjTzMbAbwMjAFWu3tZSDdgu7uXmdlU4A53fzW89jxRQDgHKHD320P6N4E6ooBxh7ufH9LPBm5190vNrDpRHQnadRNwE0BFRUXllClTOrR/tbW1FBUVpTRvVyuzpr6R1TsaWLOjgTU10c9V1Q3UNjhH9c7hOx8sp1d+66OsR8K+d7Xfu8pUmV2pzETGjx8/x93HH/KCu6d1A0qI7v3ykfC8Ou717eHnVOCsmPTniYbCvgJ8Iyb9myFtPPBcTPrZwNTW6mhtq6ys9I6qqqpKed4joczNO+v9A7c/5cNvneoX/+xl3757T0rqz+S+Hwm/d5WpMjNVZiJAlSf4Tk3rdUHMLBf4C/B7d/9rSH4/DHcRfm4K6euAYTFvHxrSWksfmiC9tTokhfqV5PPtD5Yzsl8xizfs4Op7Z1FTty/TzRKRLiCdq8UMuBd4291/EvPSE0DTiq9rgcdj0q8Jq8YmATUezds8A1xoZn3Cqq8LgWfCazvMbFKo65q4shLVISnWpzCbh2+cyFHlRSxYV8N1v53FznoFGJGeLp09lw8AVwMfMrO3wnYJcAdwgZktBc4PzyFa7bUCWAb8BvgcgEcT+d8DZoftuyGNkOee8J7lRJP5tFKHpEFF70IevnEiQ8oKmbu6mk/fP5vdexoy3SwRyaB0rhZ7FWjpuiLnJcjvwM0tlHUfcF+C9CqiRQLx6VsT1SHpM7RPEY/cNImP/XoGs1du54YHZvPb606nME/3mBHpiXQtdkmZYeVF/OHGSQwozWfmim3c+GAV9fsaM90sEckABRdJqRH9inn4xkn0K8nn1WVb+JeH5rCnQQFGpKdRcJGUO2ZACQ/fOJHy4jymL9nMzb9/k70N+zPdLBHpRAoukhbHDizloRsmUlaUy3Nvb+KLf5hLw35dKkakp1BwkbQ5cXAvHrphIr0Kcnh60Ua++txWZizfmulmiUgnUHCRtBozpDe/u2EiQ/sUsrqmgSt/M5Obf/8ma7fXZrppIpJGCi6SduOGlfHcLR/kypNKKMjN4v8WbOD8n7zEz59bqtVkIt2Ugot0ioLcbK44sYQXvnwOHx43mPp9+/npc+9y3o9f4qkFG3TpfpFuRsFFOtXgskLuvPJU/njTJE6o6MW66jo++/s3+dQ9b7Bk485MN09EUkTBRTJi4tF9mfqFs7j98jGUFeXy+vKtXPKLV/j2E4vYuVfLlkWOdAoukjHZWcZVk4Yz/SvncM0Zw3F37n99JTdN2cSND1bxlzlrqanVRTBFjkTpvM2xSFLKivL47mVjuPL0o/jBk2/zytItTFv8PtMWv09OlnHGqL5cdNIgLjxpIANKCzLdXBFJgoKLdBknVPTidzdMZNqrs9iYPYCnF21k5optvLJ0C68s3cI3H19I5VF9mDxmEBedNIhh5R2/e56IpJeCi3Q55YXZXFA5gqvPGMH23Xt57u33eWbRRl5euoWqVdupWrWd2//vbU4a3IszBjrHjWmgJF8fZZGuRP+R0qX1Kc7jo+OH8dHxw9i1p4HpSzbx9MKNvPjOJhat38Gi9fDI4ue5onIoV58xnFH9SzLdZBFBwUWOICX5OVw6djCXjh1M/b5Gnnv7fX717ELe3rKP+19fyf2vr+Ts0f247swRnHPcALKzWrqdkIikm4KLHJEKcrO5dOxgKvZtoLBiNA/OWMljb61rnp8ZVl7I1ZOG87Hxwygryst0c0V6HC1FliPeiYN7ccc/jWXm187jPy45nmHlhazZVscPnnyHSf/5PLf9ZT6ra7SkWaQzqeci3UZZUR43/d0objjraKYv2cT9r6/klaVbeGT2Gh4F5u9exC0XHEtpQW6mmyrS7annIt1OdpZx3gkD+d0NE3n+yx/kUxOPAuC3r63kvB+/xBPz1utaZiJppuAi3dqo/iV8/x9P5r8u6MupR5WxaecevviHuVx17xss37wr080T6bYUXKRHGFmWy1/+5Uzu+MjJlBXl8tqyrUz+2cv86Jkl1O3VZf9FUk3BRXqMrCzjE6cfxQtfPoePjx/Gvkbnly8u44KfvsQL77yf6eaJdCsKLtLjlBfn8cMrxvKXz57B8YNKWbu9jk/fX8VND1axuVa9GJFUUHCRHqtyeDlTv3AW37z0RIrzsnl28ft86ektPLtoY6abJnLEU3CRHi0nO4sbzhrJ818+h78/uYI9jc4X/jCXOau2Z7ppIkc0BRcRYFDvAn75yVM5f2Qhexr285kHZrNCq8lEOkzBRSQwM246rRfnHtef7bX7uPa3s9i8c0+mmyVyRFJwEYmRnWX88pOnMXZob9Zsq+OGB2ZTu7ch080SOeIouIjEKc7P4d5rJzCsvJD5a2v4/MNzaWjcn+lmiRxRFFxEEuhfms8D159On6JcXnhnE998fKEuGSPSDgouIi04un8J91w7nvycLP4waw2/enFZppskcsRQcBFpReXwcn7+iVMxgx89+y5/nrM2000SOSIouIi0YfKYQXz7wycBcNtf5vPK0s0ZbpFI15e24GJm95nZJjNbGJNWbmbTzGxp+NknpJuZ/cLMlpnZfDM7LeY914b8S83s2pj0SjNbEN7zCzOz1uoQORzXnjmCf/67o2nY73z2oTdZtL4m000S6dLS2XO5H5gcl3Yb8Ly7jwaeD88BLgZGh+0m4C6IAgXwLWAicDrwrZhgcRdwY8z7JrdRh8hhuXXy8Xx43GB27Wng+t/O1nXIRFqRtuDi7i8D2+KSLwMeCI8fAC6PSX/QIzOBMjOrAC4Cprn7NnffDkwDJofXern7TI+W8DwYV1aiOkQOS1aW8aOPjmXiyHI27dzDLc9u4dP3z+ZXLy5jxvKtOh9GJEZn3+Z4oLtvCI83AgPD4yHAmph8a0Naa+lrE6S3VofIYcvPyebua8Zz3W9nMXd1NS+8s4kX3tkERCdgnljRi8rhfThteB8qh/dhcO+CDLdYJDMsnWv3zWwEMNXdx4Tn1e5eFvP6dnfvY2ZTgTvc/dWQ/jxwK3AOUODut4f0bwJ1wPSQ//yQfjZwq7tf2lIdLbTvJqJhOCoqKiqnTJnSof2sra2lqKgopXlVZmbKTDafu7Nm625W1WazZOs+lmzZy8qaBvbH/TuVF2YxqncWI8vzGVKaw+DSHAaXZlOQk3jQ4Ej4HanMnltmIuPHj5/j7uMPecHd07YBI4CFMc+XABXhcQWwJDz+NXBlfD7gSuDXMem/DmkVwDsx6c35Wqqjra2ystI7qqqqKuV5VWZmyjycunfV7/PXlm32O59/16+77w0f++1nfPitUxNuZ/zgOb/qnpn+rccX+gOvv+evLt3s66trffbs2Wlvp8pUmR0tMxGgyhN8p3b2sNgTwLXAHeHn4zHpnzezR4gm72vcfYOZPQP8IGYS/0Lga+6+zcx2mNkk4A3gGuDONuoQSavi/BzOHNWPM0f1A2D/fmfFlt08/spbNBb3Y/nmXazYvJuVW3ezvqae9TX1vLJ0y0FlFOQYx818lWMGlDJ6YAnH9C9h9MAShvYpIjvLMrFbIh2StuBiZn8gGtbqZ2ZriVZ93QE8amY3AKuAj4XsTwKXAMuAWuB6gBBEvgfMDvm+6+5NiwQ+R7QirRB4Kmy0UodIp8rKMo4ZUMI5IwqprDy+Ob2hcT9rt9exfPOu5oATPd7Ntt17mbe2hnlrD17qnJ+TxdH9Sxg9oIRjBpSQvaueo47dQ//S/M7eLZGkpC24uPuVLbx0XoK8DtzcQjn3AfclSK8CxiRI35qoDpGuIic7ixH9ihnRr5jzTjh4vcmLr8+muGIUyzbtYummnSzbtItlm3axoaaetzfs4O0NO5rz/veM5xg9oIQzRvXlzFF9mTiyL32K8zp7d0QS6uxhMRFpRa/8LCpHlnP6yPKD0nfW72P55t0sfT8KODOXrOXdbY0s3bSLpZt28eCMVZjBCYN6NQebCSPL6VWQm6E9kZ5OwUXkCFBakMspw8o4ZVi0EHLOwFpOHncq89ZWM2P5Vl5fvoU3V1ezeMMOFm/Ywb2vvkeWwclDejOyuIFdpZuZMKIPRXn6l5fOoU+ayBEqLyeLCSPKmTCinC+eN5r6fSdKEjEAABnGSURBVI28uXo7M5ZvZcbyrby1pjqavwEeWzKLnCxj3LAyzhzVlzOO7stpw/tQkJud6d2QbkrBRaSbKMjNPmi12u49DcxeuY3HXl/Me7tzWLCuhjmrtjNn1XbufGEZeTlZnDqsLAyj9WN/o+5XI6mj4CLSTRXn53DOcQMo3bWGyspKdtTvY/Z723g99Gze3riDN97bxhvvbeNnzy0lLwvGznmdccPKGDesjFOGljGsvJBwTViRdlFwEekhehXkct4JA5tXqFXX7mXmim3MWL6FGSu28u77u6hatZ2qVdub31NenMe4ob2bA864oWWUa0WaJEHBRaSHKivKY/KYQUweMwiA6a/Phr7Dmbemhnlrq5m3ppqtu/fy4pLNvLjkwD1sjiovondOA2VvvUGWGTlZRlaWkW1Gdnb0syltV/UOaorf5+zR/cnN1u2jehIFFxEBoDQ/i8rjBnDOcQOA6NJQa7fXNQeaeWtqWLCuhtXbaqM3bNrSSmkHPL28ivLiPD48toLLTx3CKcPKNNTWAyi4iEhCZsaw8iKGlRdx6djBQHR1gaWbdjFz7kJGHTOaRncaGz36uT/a9rvTENLefHsFVZth2aZdPDBjFQ/MWMWIvkVcfuoQLj9lCCP6FWd4LyVdFFxEJGk52VmcUNGL2vX5VB7bv838o2wT/3naaSxav4PH5q7j8XnrWbm1lp89t5SfPbeUU48q4x9PHdIcvKT7UHARkbQyM8YM6c2YIb352iUn8PryLfxt7jqeXriRuaurmbu6mu9OWcwxfXI4ddV8RvUvad6G9CnUBTuPUAouItJpsrOMs0f35+zR/bn98gamLX6fx+au4+WlW3hn6z7e2brmoPz5OVmM7FfMqAFNAaeYPdv30X9rLSUFORTnZ5OfoxNBuyIFFxHJiKK8HC47ZQiXnTKEbbv38thLVWSXDW6+WvTyTbvZuKOedzbu5J2NOw9+83MvNj/My86iOD+bkoIcSvJzKcnPpiQ/h+L8HPbX7mDO7uUMLitkcFkhQ8sK6VeST5Z6Q2mn4CIiGVdenMe4gflUVo44KH1n/b6YWxJEAeedtVtoyMpl954Gdu1pYG/jfvbW7md77T6iG9Ue7Mll7xz0PDfbqOhdyOCyAoaUFTGkrIA91bWszV5HQW42hbnZFOZlU5CTTWFe1iFpkhwFFxHpskoLcptP4GwyZ84cKisrgWi59J6G/c2BZteeBnbVN7B7bwM76xuY+/Zyskr6sa66lvXV9ayvrmPr7r2s3lYbllRvO1DZm28l1aaiXGPQ9On0L8mnf+mBbUBpQfQ4pDem8RbyRwIFFxE5YpkZBbnZFORm07fk0BunDW3cSGXliQel1e1tZH1NHeuro23d9joWvbeOol59qNvbyJ6GRur2NlK3L9rq9zZS37C/Oa12n7Ni825WbN7detuA0qnP0Kswl14FufQqzKFXQS6lMY+j13Ko27KX4/c0UJzffb6Su8+eiIgkoTAvu3k1WpM5c3ZRWXlqm+/dv995+Y0qhhx9PJt37mHzrj1s3rmHTTujn83brj1s272XHfUN7KhvINFwXbxvv/QMxw4sbb61wilHlTF6QOkRu1pOwUVEJElZWUZpXhajB5YyemBpq3lnza7i2JPGsqOugR31+9hRty8Em5jHdfuoqdvHvPfeZ/WOxubFC4/MjlbNFedlc/LQ3pwyrA+nDCvDdzewaWc9hpFlUc/NADMwDCx6nGXGvv2ZHZZTcBERSYPsLKOsKI+yorYv9DlnzhxOGnsKC9fV8Naaauauqeat1dWsq65j5optzFwRMzf05PNJtyHnb09SmJdNUV42xXk5zY+L8nIoyosWKeyuqeHTfbYy8ei+HdnNlutOaWkiItIhBbnZjB9RzvgRB25xvXnnHuatqeatsC1eu42snBzcwYH97tFjdxwgJn3PvkYa9js766PFDbCnxbrPPnmXgouISE/RvzSf808cyPknRrdJiF0p15Y5c+Zw8rhTqdvbyO69DdTubWx+XLe3kdrweMny95gQE9BSRcFFRKSbysvJIi8ni95FuS3mmWObOG5Q6/NHHaEbLIiISMopuIiISMopuIiISMopuIiISMopuIiISMopuIiISMopuIiISMqZ9/DLQjcxs83Aqg6+vR+wJcV5VWZmyuxu+6MyVWYqy0xkuLv3PyTV3bUd5gZUpTqvysxMmd1tf1Smykxlme3ZNCwmIiIpp+AiIiIpp+CSGnenIa/KzEyZ3W1/VKbKTGWZSdOEvoiIpJx6LiIiknIKLiIiknIKLiIiknIKLl2Amf0u/PxSmsrvY2anm9nfNW3pqKczmFl+MmntLPOQ33t8mpllm9nvD6eeVupP+T51dWaWZWYfS3GZPww/P5rKcttRv5nZsHbk/0Ayae1sQ2rvVXw40nHyTHffgIHAvcBT4fmJwA1t5L80bAMSvL4YGAzMA/oA5bHbYbb1M8ACYDvwIlAHvJAg3zWJthT8rj4AFIfHVwE/ITqjt6PlvZlMWsxrZwKfbG2fWihzboK0V4G8JNv5JaAXYOGz8iZw4eHsE5Af9uU/gP/XtB3OZ7Sd7TwWeB5YGJ6PBb5xGHW36+S9tv6W4XNurX0eOrg//xV+R7kh/2bgqhbKXJCOzzIwHDg/PC4ESlvItxT4E3AJYcFWC/n6h8/R3cB9TVt7/h5tbbrNccfcD/wW+Hp4/i7wR6J/qIOEo7P/BqYTffDvNLOvuvufY7L9L9GH9mhgTuzbAQ/pmNnO8Dwhd++VIPlLwARgprufa2bHAz9IkG9CzOMC4DyiL5oHY/blVXc/K0E7LKo+Yf13AePMbBzwZeCeUOYHW9qPRMxsEDAEKDSzU0OdEP3TF7Xwnt8Bo4C3gMaQ7E37ZGZXEn1ZjTSzJ2LeWgpsS1DkCuC1kHd3U6K7/yRB3k+7+8/N7CKiA4argd8Bzx7GPj0O1BB9RvYk2ucY95PcZ7TNdsb4DfBV4NcA7j7fzB4Gbu9g3c+Z2VfCa7G/z0N+9239LYOniQ6iSsxsR+zbSfz5THZ/LnT3fzezfwRWAh8BXgYeim8n8KaZTXD32Qlea9qXM4gCZX8zuyXmpV5AdoL8NwI3ER1sjgKGEn1nnJeg+GOB84FPA78ws0eB+9393bh8jwOvAM9x4PeZUgouHdPP3R81s68BuHuDmbX0B/o6MMHdNwGYWX+iP2hzcHH3XxB9EO4i+tA0DVu97O7zYvKVhjK+B2wg+hIw4FNARQv117t7vZlhZvnu/o6ZHRefyd2/EPvczMqAR+LynBXbjiQ1uLub2WXAL939XjO7oR3vb3IRcB3RP1bsl/lOoiOwRMYDJ3o4VEvgdaLfYz/gx3Flzk+Qf3nYsogCUGuaAsUlwO/cfZGZWVye9u7TUHef3Ea9TZL9jCbTziZF7j4r7uWGw6j74+HnzTFpzQdTcdr6W+LuXwW+amaPu/tlLeWLkez+NH1P/j3wJ3evaflXxETgKjNbSRQwmwLb2Jg8eUBJKDf2c7QDuCJBmTcDpwNvEBW21MwGJKo8/H6mAdPM7FyiAPg5M5sH3ObuM0LWIne/taWdSAUFl47ZHcY2HcDMJhEdUSaS1RRYgq20PNf1DtGH4a9EH8rfmdlv3P3OuHz/4O7jYp7fFT48/y9BmWtDoHiM6AO3neQu0LkbGJlEvrbsDF8yVwF/Z2ZZRMML7eLuDwAPmNk/uftfknzbQmAQUQBJVOYqot/FGUm24TsAZlYSnu9qJfscM3uW6Hf4NTMrBfbHldfefXrdzE529wVJ5E32M9pmO2NsMbNRMWVeQeLfbVJ1u3t7Pl+t/i3jyk0msEDy+zPVzN4hGlL+bDhArG+hzKYe4Nnh+ctAdVz7XgJeMrP7w2ewLXvcfW9TQDOznKY2xwu/96uIhg03Al8AngBOIRoua/qdTzWzS9z9ySTq7xCdRNkBZnYacCcwhuhD3x+4wt0POdo1s/8CxgF/CEkfB+YnOmows/nAGe6+OzwvBmbEHfVgZq8DvyLqWThwJXCzu5/ZRrs/CPQGnnb3vXGvTeHABzYbOAF41N1va63MtoShn08Cs939FTM7CjjH3R9s462tlfn3wElEw3cAuPt3E+R7keifahYxw0ju/g/h9XYN85nZGKLeYnlI2kI07r8oQd1Zoe4V7l4d/umHtPAZKSM6MGjqsb4EfNfda+LyLQZGEw3P7SHxUXFT3qbP6EnAIlr4jMa0M5doTqdfaGf8AQ1mdjTRGP2ZRMNP7wGfiv+CTPb/w8yuia+DaIdih2KbPpeltPK3DHnj/54W+zPB3zPR/lzl7isT7Hs5UOPujWZWBPRy940J8n2JaJ6z6QDxciDRAWLT5/OQL2B3/1Bcvv8iClDXEAWLzwGL3f3r8e81s3eJPqP3ufu6uNdudfemRQ87gWKi3+W+ln5Hh0PBpYPC0cNxRH+UJe6+r4V8PyTqzp4Vkl4BJrUQXBYQDaHVh+cFRF/KJ8flGwH8nGiy3IHXgH9N9E/Rjv2JnQNpAFa5+9qOlpcuZva/RPMR5xLN31wBzHL3Q4ba4vapWThy7EjdrwNfd/cXw/NzgB/EBnUzOz4MPZ7WQt1vJij3L0Rfwg+EpKuBce7+kbh8w0lwVJzo6Dd8dj5PdCS9E5gB3Nn02YrJ9xmiebmhRPMZk4gOaD5EHDPLDl+uxUQ98p0J8mSFMmbRxv+HmcV+4TbP87n7FTF5Wp2b6+jfMq4dLe5PTJ4xRAsTYg9oDjlASvYAMbxWGfO0APgnomHkf4/LlwXcAFxI9Pt8Brgn0RChmU0gGlIdTszIVAv1lxMdrMTu02H/PpvLV3DpGDM7ExjBwX/ARB+2N939tLi0+S38sW8BrgX+FpIuJ5qM+1kKm94iMxvIgYn9WXHDee0tqyOT/8mUO9/dx8b8LCFalXR2m28+TGY2L2448pA0M7vb3W8KR6XxvIUv7bfc/ZQk0tpzVPwo0Rh+0/LpTwJl7v7RuHwLOLDg4xQLCz7iA1vIu5po0vyPRCsOWxqamevupyZ6rTWhB/eIJ5hXMrMfxh+QJUpLsp5bWnvd4xZomNm3gHOIgsuTwMXAq7FBMCZvUgeIrbRtlrufnkzeFt6/BPgK0cFK8/Bmgt5looOK19090SKBDtGcSwdYEitXzOyzRN3Xo8PRTJNSop7GIdz9J2Y2nQO9nOvdfW6C+vsDN3JocPt0x/aIZFe1Jc07NvmfjLrws9bMBhPNYR20mCFdgQ1YYWbfJBp2gGhse0VsBne/Kfw8tx3l1pnZWe7+amj/Bziwn7FuIOr1Nh0V/5DQI0mQd4y7nxjz/MUwrBYvqQUfwfFEy+lvBu41s6lEweDVuHzPm9k/AX9tKQC1oLV5vguA+EBycYK0ZLT3M3kF0dD2XHe/PhyEJVopBtEquTfMLPYA8ZBVpNDcc2iSRbRooXeCfAs4dPisBqgCbnf3rTHpm919Shv7A8mvIu0wBZeOaXPlCvAw8BTwn0DsvMVOT7DUskkYNjlk6CROOpYRtrmqrYuYGo5w/5vo9+REw2PNUh3YzOx37n410e98BFHPAaJhqRYDerK9W+CzRBP7TV8s24l6sIcUycF/70YOrPaK96aZTXL3maEtE4m+jOIlveDD3WuBR4FHzawP0dDsSxy6fPafgVuABjOrp+U5j4TzfHF52n2Q1hYPCzPaod7d95tZg5n1AjYBCU+WTPYAMZjDgf1vIFrmnGgl5VNEf+uHw/NPEA0NbyRa9v3hmLzfMrN7iE5tiJ2b+isHa89BRYcouHRMmytXPJqMrSGabE+1dCwjbM+qtoxx9++Fh38JR84FHjfxnQaVoZd0LdFcT9NEMbTw5Z5M7zbG20Qn6o0Cyog+N5dz6HLoNo+KY45yc4lWl60Oz4cTrUY8iLv/Y3j47TCU15to6CuhMAfycWAyUbA65Cx7dy9NNJ6fwI9iHrc0z9ehg7RkmNkDwJfcvTo87wP8OMEIwOwQgH9DFBB2EfUYE0ryABGiYbbPEQUiJzp4SXQAcH7c0PqCpuF2M7sqLu/1RD3MXA4MizkHDoiadHQVadI059IO1o6VK2lux+1E46MpW0Zo7VjVlmnt6BGkqr4vEvUujgZiV+A0HZEfcl6Gmb1N273bprxPE60GepOYnom7/zhB3tOIWRwSf1QcJv1blGjyP1kWnbsxl6h38UTT8FyCfEmP57c1z2dmvdx9R9wQUrPDCTCJ5oZaSHuIqIf2CtES5F6eYNVfB+pPdl5sHnCju88KzycQTeiPi2+vmS1x93b1QKyVVaSHQ8GlHcIfwYAfArErOgz4obtP7KR2pHwZYfgCXcOBlUivuPvfWnlLRrTUI3D3L3ZC3Xe5+2eTzPsn4Ivu3uZ5GWa20N3HHHYD06zpiz6JfEktEkgwz3c2cNA8n5lNdfdLzew9DiwrbpIwsLdjf+YRLYvfHp6XAy/FT75bdDLi2WEbRRRgX3b3n3e07lDu4rh5sZbSJhBdnqWEaP93EC3sWAT8vbs/GpP3t8B/u3ui+bVOpWGxdvCwTM/Mcj1uyZ6ZFXZiO5IddmiPAcAXiY6e7yNa7tgVJTPflRbJBJa43u1iM0umd9uekyMzaa+Z3cyh5xjFDyMlO56fzNUrLg0PXyP0Htz9kOG9DvoxMCMcCBjRxP334zO5+4tm9jJRwDwX+Bei38FhBReSnBfz6FIyJzfNycUNAz8al30S8FYIxq2eC5VuCi7tkI7JxQ62I+GwA4mvNZQUd/9GWAl1IdG47S9Dt/1ed19++K1OmaTP1M6QH3Ggd3t5THpTWiJnAdd1hS+ENvyOaN7mIuC7RJcdejtBvmTH89szz3cvUc/hTovOqn+TKNB0+Ave3R80syqgaXn4RxId8ZvZ80QjBTOIhsYm+OEt02/XvFh4T/OJwxbO1PcEJw4TzYV1CRoWa4dw5NCHNEwutrMdSZ+b0IGyxxEFl8lEV1GeBEzzuBO7OltXme9KlrXv/KaE8ySHMz+SDk3j+3bgHKNcoi/4Sa28p7WrQrRrns/Msjm491Dn7sd3YD/aNY9jZj8FKok+b68RrRKc4e6JlosnU3+75sWsHScOdyXqubRDmleAtUfKlxFadILeNUSXNLmHaOx7n0VnBy/l4DmmTOhIj6DTdaR329WCSCuazrKvtuiM9Y1Ew6ktih8+jrOWqDfQNM93d0vzfCnuPTxMdL5O7FJgOLAK8KB5HHf/t9CGUqILjf6WqPfcoXvudODvfaYfOHH4O2b2Y6IVdF2agsuRKR3LCMuJhgUOKsej9f2XtvCeTtNV5ruSkLals13A3WG57jeILoZYAnzzMMprzzzffKLewxiiA7xqM+tQ76FpHseTvHCmmX2eKABWEp2Lch9RgOssbZ443BVpWOwIl65lhF1NbI+A6LL3TUqB19w9fr2/pJhFd8f8J6Jl4E1XtvYWxv6TLdM4MM83nmiCusV5vpjew1eAQe7e4Tt2mtnz8cujW0j7ClEwmePuiS7Jn1ZhLvROormhX4Xke9z9cAJ72qnncoRrY9ihO+nOPYIjRXtuVpYUd3cz20g0xNZANKf5ZzM7aJ4vlb0Hi673VQT0Cz2x2Ju0DUnQxh/Fp3WyHxGdZ3U2B4YF78poi5KgnouIJCXV5+MkmOd7LHaez91HxeRNWe8h1PuvRLcWX8eB4LKD6EKgvzyc8lMtrNrcyYHrmX0S6O3uh1wdoStRcBGRpJjZ3USX7U/J+Thm9h2i+44kumXACe6eaJlzSoSVZ//hBy4n1GUle7JlV6PgIiKtijkvI4ckb1Z2JIi/dEpXZdHlZ34Zd7Llze6e8GZrXYWCi4i0qr3nZRwpzOxHRHMY7b01QKey6Dp1xwGrQ9JRwBKiOaouG9wVXESkR4q5Rl8D0QUpU36r31Q4UoO7VouJSI+Upmv0pVxXDR5tUXARkR4pHdfokwO63M2gREQ6SdOtfld5dFvqU4nO45EUUHARkZ6q3t3rgeZr9BFNnEsKaFhMRHqqtN/qtyfTajER6fF6yjX6OpOCi4iIpJzmXEREJOUUXEREJOUUXETSwMy+bmaLzGy+mb0VrgeVrrqmm9n4dJUv0hFaLSaSYmZ2BtFtdE9z9z1m1g/Iy3CzRDqVei4iqVcBbHH3PQDuvsXd15vZ/zOz2Wa20MzuDndhbOp5/NTMqszsbTObYGZ/NbOlZnZ7yDPCzN4xs9+HPH82s6L4is3sQjObYWZvmtmfzKwkpN9hZotDTyrTN7+SHkDBRST1ngWGmdm7ZvY/YZkrRJdNnxBuuFVI1LtpstfdxwP/S3THx5uJ7hd/nZn1DXmOA/7H3U8gurHV52IrDT2kbwDnu/tpQBVwS3j/PwInhSvo3p6GfRY5iIKLSIq5+y6i2/HeBGwG/mhm1wHnmtkb4f4oHwJOinnbE+HnAmCRu28IPZ8VwLDw2hp3fy08fgg4K67qScCJwGtm9hZwLTCc6JIm9cC9ZvYRoDZlOyvSAs25iKSBuzcC04HpIZj8MzAWGO/ua8zs2xx8Jd6me9Lv5+D70+/nwP9p/Elp8c8NmObuV8a3x8xOJ7og4xXA54mCm0jaqOcikmJmdpyZjY5JOoXo5k4AW8I8yBUdKPqosFgAovuovxr3+kzgA2Z2TGhHsZkdG+rr7e5PAv8GjOtA3SLtop6LSOqVAHeG61Y1AMuIhsiqgYXARmB2B8pdAtxsZvcBi4G7Yl90981h+O0PZpYfkr8B7AQeN7MCot7NLR2oW6RddPkXkSOAmY0ApobFACJdnobFREQk5dRzERGRlFPPRUREUk7BRUREUk7BRUREUk7BRUREUk7BRUREUk7BRUREUu7/Az5dt15PjqaoAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline \n",
    "\n",
    "fdist.plot(30, cumulative=False)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Stop words "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'with', 'the', 'y', 'can', \"won't\", 'his', 'ma', 'about', 'do', \"you're\", 'did', \"wasn't\", 'he', 'myself', \"weren't\", 'an', 'again', 'will', \"aren't\", 'our', 'having', \"that'll\", 'o', 'aren', 'because', 'where', 'under', 's', 'couldn', 'was', 'have', 'weren', 'some', 'wasn', 'whom', 'nor', 'its', 'ourselves', \"couldn't\", \"doesn't\", 'needn', 'hasn', \"haven't\", 'then', 'am', \"needn't\", 'each', 'didn', 'further', 'own', 'wouldn', 'is', 'very', 'such', 'being', 're', 'll', 'over', 'through', 'him', 'it', 'shan', 'are', 'but', 'not', 'her', \"shan't\", 'in', 'those', 'when', 'doesn', 'yourselves', 've', 'as', 'you', 'me', 'same', 'after', 'out', 'haven', 'all', 'theirs', 'below', 'we', 'at', 'a', 'or', 'were', 'this', 'once', 'just', 'these', 'here', 'itself', \"don't\", 'into', \"should've\", 'both', 'that', 'down', 'mustn', 'had', 'now', 'hers', \"you'll\", 'she', 'more', \"shouldn't\", 'their', 'be', 'how', 'your', \"it's\", 'should', \"didn't\", 'd', 'before', 'than', 'yourself', 'what', 'why', 'hadn', 'mightn', \"hasn't\", 'shouldn', 'until', 'most', 'any', \"mustn't\", 'which', \"isn't\", 'yours', 'for', 'ain', 'too', 'been', \"mightn't\", 'to', 't', 'isn', \"she's\", 'against', 'from', 'who', 'while', 'i', 'ours', 'on', 'themselves', 'few', 'only', 'by', 'm', 'them', 'up', 'herself', 'himself', 'they', 'has', 'my', \"hadn't\", 'during', \"you'd\", 'so', \"you've\", 'of', 'doing', 'won', 'other', 'between', 'off', 'there', \"wouldn't\", 'and', 'above', 'does', 'no', 'don', 'if'}\n"
     ]
    }
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "from nltk.corpus import stopwords\n",
    "nltk.download('stopwords')\n",
    "stop_words=set(stopwords.words(\"english\"))\n",
    "print(stop_words)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Delete all of the stop words from the list of tokens created by nltk word_tokenize function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "cleaned_tokens = []\n",
    "for w in stop_words:\n",
    "    del cleaned_tokens[w]\n",
    "cleaned_tokens.most_common(13)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are probably a lot of words such as 'apple'/'apples', etc whose presence extends our vocabulary a lot. \n",
    "Please, calculate the size of your vocabulary here. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
   {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "248573\n"
     ]
    }
   ],
   "source": [
    "### Define the size of your vocab - number of uniq words from all of the texts \n",
    "\n",
    "vocab_size_init = len(cleaned_tokens)\n",
    "print(vocab_size_init)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package wordnet to /root/nltk_data...\n",
      "[nltk_data]   Package wordnet is already up-to-date!\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lemmatized Word: fly\n",
      "Stemmed Word: fli\n"
     ]
    }
   ],
   "source": [
    "# Stemming will help us to reduce the numbed of uniq words in our vocabulary by deleting different forms of the same word\n",
    "from nltk.stem import PorterStemmer \n",
    "from nltk.stem.wordnet import WordNetLemmatizer\n",
    "nltk.download('wordnet')\n",
    "\n",
    "stem = PorterStemmer()\n",
    "lem = WordNetLemmatizer()\n",
    "\n",
    "word = \"flying\"\n",
    "print(\"Lemmatized Word:\",lem.lemmatize(word,\"v\"))\n",
    "print(\"Stemmed Word:\",stem.stem(word))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Please, apply stemming  and lemmatization to the tokenized words.  \n",
    "##### 1. Apply stemming first - calculate the number of the uniq words after it \n",
    "##### 2. Apply lemmatization and calculate the same\n",
    "##### 3. Compare, analyse "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
   {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "248731, 261893\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "sys.setrecursionlimit(5000)\n",
    "stemmed = []\n",
    "lemmatized = []\n",
    "stemmed = [stem.stem(i) for i in cleaned_tokens]\n",
    "lemmatized = [lem.lemmatize(i) for i in cleaned_tokens]\n",
    "vocab_size_stemmed = len(stemmed)\n",
    "vocab_size_lemmatized = len(lemmatized)\n",
    "print(vocab_size_stemmed, ',' ,vocab_size_lemmatized)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Spacy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_text = \"\"\"What is impeachment?\n",
    "Put simply, it's a process that allows senior figures in government to hold other officials (like judges, the president and cabinet members) to account if they're suspected of committing offences while in office.\n",
    "Those offences can include \"treason, bribery or other high crimes and misdemeanours\".\n",
    "After someone is impeached, they then go on trial in the Senate, the upper house of Congress, the members of which will decide whether they are guilty or not. It's a political trial, not a criminal one.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_text = sample_text.replace(\"\\n\", \" \").replace(\"\\t\", \" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "# You need to load the model firstly, once loaded, you can comment the line \n",
    "\n",
    "# ! python -m spacy download en"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tokenized words: ['What', 'is', 'impeachment', '?', 'Put', 'simply', ',', 'it', \"'s\", 'a', 'process', 'that', 'allows', 'senior', 'figures', 'in', 'government', 'to', 'hold', 'other', 'officials', '(', 'like', 'judges', ',', 'the', 'president', 'and', 'cabinet', 'members', ')', 'to', 'account', 'if', 'they', \"'re\", 'suspected', 'of', 'committing', 'offences', 'while', 'in', 'office', '.', 'Those', 'offences', 'can', 'include', '\"', 'treason', ',', 'bribery', 'or', 'other', 'high', 'crimes', 'and', 'misdemeanours', '\"', '.', 'After', 'someone', 'is', 'impeached', ',', 'they', 'then', 'go', 'on', 'trial', 'in', 'the', 'Senate', ',', 'the', 'upper', 'house', 'of', 'Congress', ',', 'the', 'members', 'of', 'which', 'will', 'decide', 'whether', 'they', 'are', 'guilty', 'or', 'not', '.', 'It', \"'s\", 'a', 'political', 'trial', ',', 'not', 'a', 'criminal', 'one', '.']\n"
     ]
    }
   ],
   "source": [
    "import spacy\n",
    "nlp = spacy.load(\"en\", disable=[\"tagger\", \"parser\", \"ner\"])\n",
    "\n",
    "doc = nlp(sample_text)\n",
    "spacy_words = [token.text for token in doc]\n",
    "\n",
    "print(f\"Tokenized words: {spacy_words}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Attributes which spacy token has: \n",
      " ['_', '__bytes__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__pyx_vtable__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', 'ancestors', 'check_flag', 'children', 'cluster', 'conjuncts', 'dep', 'dep_', 'doc', 'ent_id', 'ent_id_', 'ent_iob', 'ent_iob_', 'ent_type', 'ent_type_', 'get_extension', 'has_extension', 'has_vector', 'head', 'i', 'idx', 'is_alpha', 'is_ancestor', 'is_ascii', 'is_bracket', 'is_currency', 'is_digit', 'is_left_punct', 'is_lower', 'is_oov', 'is_punct', 'is_quote', 'is_right_punct', 'is_sent_start', 'is_space', 'is_stop', 'is_title', 'is_upper', 'lang', 'lang_', 'left_edge', 'lefts', 'lemma', 'lemma_', 'lex_id', 'like_email', 'like_num', 'like_url', 'lower', 'lower_', 'n_lefts', 'n_rights', 'nbor', 'norm', 'norm_', 'orth', 'orth_', 'pos', 'pos_', 'prefix', 'prefix_', 'prob', 'rank', 'remove_extension', 'right_edge', 'rights', 'sent', 'sent_start', 'sentiment', 'set_extension', 'shape', 'shape_', 'similarity', 'string', 'subtree', 'suffix', 'suffix_', 'tag', 'tag_', 'text', 'text_with_ws', 'vector', 'vector_norm', 'vocab', 'whitespace_']\n"
     ]
    }
   ],
   "source": [
    "print(\"Attributes which spacy token has: \\n {}\".format([dir(tok) for tok in doc][0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lemmatized words: ['What', 'be', 'impeachment', '?', 'Put', 'simply', ',', '-PRON-', 'have', 'a', 'process', 'that', 'allow', 'senior', 'figure', 'in', 'government', 'to', 'hold', 'other', 'official', '(', 'like', 'judge', ',', 'the', 'president', 'and', 'cabinet', 'member', ')', 'to', 'account', 'if', '-PRON-', 'be', 'suspect', 'of', 'commit', 'offence', 'while', 'in', 'office', '.', 'Those', 'offence', 'can', 'include', '\"', 'treason', ',', 'bribery', 'or', 'other', 'high', 'crime', 'and', 'misdemeanour', '\"', '.', 'After', 'someone', 'be', 'impeach', ',', 'they', 'then', 'go', 'on', 'trial', 'in', 'the', 'Senate', ',', 'the', 'upper', 'house', 'of', 'Congress', ',', 'the', 'member', 'of', 'which', 'will', 'decide', 'whether', 'they', 'be', 'guilty', 'or', 'not', '.', '-PRON-', 'have', 'a', 'political', 'trial', ',', 'not', 'a', 'criminal', 'one', '.']\n"
     ]
    }
   ],
   "source": [
    "# We can access lemmas: \n",
    "\n",
    "lemmas = [token.lemma_ for token in doc]\n",
    "print(f\"Lemmatized words: {lemmas}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cleaned words: ['impeachment', '?', 'simply', ',', 'process', 'allow', 'senior', 'figure', 'government', 'hold', 'official', '(', 'like', 'judge', ',', 'president', 'cabinet', 'member', ')', 'account', 'suspect', 'commit', 'offence', 'office', '.', 'offence', 'include', '\"', 'treason', ',', 'bribery', 'high', 'crime', 'misdemeanour', '\"', '.', 'impeach', ',', 'trial', 'Senate', ',', 'upper', 'house', 'Congress', ',', 'member', 'decide', 'guilty', '.', 'political', 'trial', ',', 'criminal', '.']\n"
     ]
    }
   ],
   "source": [
    "# We can filter stop words: \n",
    "\n",
    "cleaned_words = [token.lemma_ for token in doc if not token.is_stop]\n",
    "print(f\"Cleaned words: {cleaned_words}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cleaned words: ['What', 'be', 'impeachment', 'Put', 'simply', '-PRON-', 'have', 'a', 'process', 'that', 'allow', 'senior', 'figure', 'in', 'government', 'to', 'hold', 'other', 'official', 'like', 'judge', 'the', 'president', 'and', 'cabinet', 'member', 'to', 'account', 'if', '-PRON-', 'be', 'suspect', 'of', 'commit', 'offence', 'while', 'in', 'office', 'Those', 'offence', 'can', 'include', 'treason', 'bribery', 'or', 'other', 'high', 'crime', 'and', 'misdemeanour', 'After', 'someone', 'be', 'impeach', 'they', 'then', 'go', 'on', 'trial', 'in', 'the', 'Senate', 'the', 'upper', 'house', 'of', 'Congress', 'the', 'member', 'of', 'which', 'will', 'decide', 'whether', 'they', 'be', 'guilty', 'or', 'not', '-PRON-', 'have', 'a', 'political', 'trial', 'not', 'a', 'criminal', 'one']\n"
     ]
    }
   ],
   "source": [
    "# We can filter punctuation tokens: \n",
    "\n",
    "cleaned_words = [token.lemma_ for token in doc if not token.is_punct]\n",
    "print(f\"Cleaned words: {cleaned_words}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_sample = df.sample(100, random_state=13) # fix random_state to make your experiments reproducible "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Create columns [spacy_lemmas], [spacy_tokens], [spacy_filtered_stop_words], [spacy_filtered_punct], [spacy_filtered_stop_punct]  \n",
    "In spacy_filtered_stop_punct filter stop words AND punctuation \n",
    "\n",
    "TIP: Use lambda functions "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_sample['spacy_tokens'] = df_sample['comment_text'].apply(lambda x: nlp(x.replace("\n", " ").\n",
    "replace("\r", " ")))\n",
    "df_sample['spacy_lemmas'] = df_sample['spacy_tokens'].apply(lambda x: [token.lemma_ for token in x])\n",
    "df_sample['spacy_filtered_stop_words'] = df_sample['spacy_tokens'].apply(lambda x: [token.lemma_ for\n",
    "token in x if not token.is_stop])\n",
    "df_sample['spacy_filtered_punct'] = df_sample['spacy_tokens'].apply(lambda x: [token.lemma_ for token\n",
    "in x if not token.is_punct])\n",
    "df_sample['spacy_filtered_stop_punct'] = df_sample['spacy_tokens'].apply(lambda x: [token.lemma_ for\n",
    "token in x if not (token.is_stop or token.is_punct)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>comment_text</th>\n",
       "      <th>toxic</th>\n",
       "      <th>severe_toxic</th>\n",
       "      <th>obscene</th>\n",
       "      <th>threat</th>\n",
       "      <th>insult</th>\n",
       "      <th>identity_hate</th>\n",
       "      <th>comment_text_lower</th>\n",
       "      <th>comment_text_tokenized_space</th>\n",
       "      <th>comment_text_tokenized_space_cleaned</th>\n",
       "      <th>nltk_tokenized</th>\n",
       "      <th>spacy_lemmas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>25680</th>\n",
       "      <td>43fb0a70fae5057f</td>\n",
       "      <td>(incorrect, moronic allegations of)</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>(incorrect, moronic allegations of)</td>\n",
       "      <td>[(incorrect,, moronic, allegations, of)]</td>\n",
       "      <td>[incorrect, moronic, allegations, of]</td>\n",
       "      <td>[(, incorrect, ,, moronic, allegations, of, )]</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>74202</th>\n",
       "      <td>c688777f515b665a</td>\n",
       "      <td>As the previous article lead already used, dig...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>as the previous article lead already used, dig...</td>\n",
       "      <td>[as, the, previous, article, lead, already, us...</td>\n",
       "      <td>[as, the, previous, article, lead, already, us...</td>\n",
       "      <td>[As, the, previous, article, lead, already, us...</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>87912</th>\n",
       "      <td>eb233cfbf51fd72f</td>\n",
       "      <td>^ to ? \\n\\n...character encoding issues. Oops....</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>^ to ? \\n\\n...character encoding issues. oops....</td>\n",
       "      <td>[^, to, ?, ...character, encoding, issues., oo...</td>\n",
       "      <td>[^, to, , character, encoding, issues, oops, f...</td>\n",
       "      <td>[^, to, ?, ..., character, encoding, issues, ....</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>130308</th>\n",
       "      <td>b920ddbf9499a110</td>\n",
       "      <td>Yes. I know that was what Mikka did. And you k...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>yes. i know that was what mikka did. and you k...</td>\n",
       "      <td>[yes., i, know, that, was, what, mikka, did., ...</td>\n",
       "      <td>[yes, i, know, that, was, what, mikka, did, an...</td>\n",
       "      <td>[Yes, ., I, know, that, was, what, Mikka, did,...</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147189</th>\n",
       "      <td>386b62dc67bcb66c</td>\n",
       "      <td>Son of a bitchSon of a bitch</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>son of a bitchson of a bitch</td>\n",
       "      <td>[son, of, a, bitchson, of, a, bitch]</td>\n",
       "      <td>[son, of, a, bitchson, of, a, bitch]</td>\n",
       "      <td>[Son, of, a, bitchSon, of, a, bitch]</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      id                                       comment_text  \\\n",
       "25680   43fb0a70fae5057f                (incorrect, moronic allegations of)   \n",
       "74202   c688777f515b665a  As the previous article lead already used, dig...   \n",
       "87912   eb233cfbf51fd72f  ^ to ? \\n\\n...character encoding issues. Oops....   \n",
       "130308  b920ddbf9499a110  Yes. I know that was what Mikka did. And you k...   \n",
       "147189  386b62dc67bcb66c                       Son of a bitchSon of a bitch   \n",
       "\n",
       "        toxic  severe_toxic  obscene  threat  insult  identity_hate  \\\n",
       "25680       1             0        0       0       0              0   \n",
       "74202       0             0        0       0       0              0   \n",
       "87912       0             0        0       0       0              0   \n",
       "130308      0             0        0       0       0              0   \n",
       "147189      1             0        1       0       1              0   \n",
       "\n",
       "                                       comment_text_lower  \\\n",
       "25680                 (incorrect, moronic allegations of)   \n",
       "74202   as the previous article lead already used, dig...   \n",
       "87912   ^ to ? \\n\\n...character encoding issues. oops....   \n",
       "130308  yes. i know that was what mikka did. and you k...   \n",
       "147189                       son of a bitchson of a bitch   \n",
       "\n",
       "                             comment_text_tokenized_space  \\\n",
       "25680            [(incorrect,, moronic, allegations, of)]   \n",
       "74202   [as, the, previous, article, lead, already, us...   \n",
       "87912   [^, to, ?, ...character, encoding, issues., oo...   \n",
       "130308  [yes., i, know, that, was, what, mikka, did., ...   \n",
       "147189               [son, of, a, bitchson, of, a, bitch]   \n",
       "\n",
       "                     comment_text_tokenized_space_cleaned  \\\n",
       "25680               [incorrect, moronic, allegations, of]   \n",
       "74202   [as, the, previous, article, lead, already, us...   \n",
       "87912   [^, to, , character, encoding, issues, oops, f...   \n",
       "130308  [yes, i, know, that, was, what, mikka, did, an...   \n",
       "147189               [son, of, a, bitchson, of, a, bitch]   \n",
       "\n",
       "                                           nltk_tokenized spacy_lemmas  \n",
       "25680      [(, incorrect, ,, moronic, allegations, of, )]               \n",
       "74202   [As, the, previous, article, lead, already, us...               \n",
       "87912   [^, to, ?, ..., character, encoding, issues, ....               \n",
       "130308  [Yes, ., I, know, that, was, what, Mikka, did,...               \n",
       "147189               [Son, of, a, bitchSon, of, a, bitch]               "
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_sample.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####  Save the results (df and df_sample) in csv file using df.to_csv function. Share your csv files using google drive or email. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### WordCloud visualizations \n",
    "\n",
    "Create wordclouds for words cleaned from stop words and punctuation using NLTK library - as in previous task. \n",
    "(with spacy it would work slow, so do not apply it to the whole dataset, use only df_sample part) "
   ]
  },
{
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
   {
     "data": {
      "text/plain": [
       "<Figure size 1440x1080 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from os import path\n",
    "from PIL import Image\n",
    "from wordcloud import WordCloud, STOPWORDS\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "text = \"\".join(df.comment_text)\n",
    "wordcloud = WordCloud(width=2000, height=1000, contour_color=\"black\", max_words=500, \n",
    "                      relative_scaling = 0, background_color = \"white\").generate(text)\n",
    "plt.figure(figsize=[20,15])\n",
    "plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation=\"bilinear\")\n",
    "plt.axis(\"off\")\n",
    "_=plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Histograms visualizations\n",
    "\n",
    "Create histograms of words frequency or counts for tokens cleaned from stop words and punctuation as in previous day task.  \n",
    "Compare the newly created visualizations to the visualisations from the previous day. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
   {
     "data": {
      "text/plain": [
       "<Figure size 1080x1440 with 6 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Рисуем гистограммы, выбирая самые популярные слова с каждой категории\n",
    "import re\n",
    "import nltk\n",
    "import seaborn as sns\n",
    "from collections import Counter\n",
    "from nltk.tokenize import sent_tokenize, word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "\n",
    "category = ['identity_hate', 'insult', 'obscene', 'severe_toxic', 'threat', 'toxic', 'toxicity']\n",
    "for i in category:\n",
        "text = ""\n",
        "for j in range(len(df[i])):\n",
            "if df[i][j] != 0:\n",
                "text = text + " " + (df.comment_text[j])\n",
    "cnt = Counter(re.split(r'\s+', text)).most_common(13)\n",
    "data = {'words', 'frequency'}\n",
    "df_i = pd.DataFrame(cnt,columns = data)\n",
    "plt.figure(figsize = (8, 4))\n",
    "sns.barplot(y = 'words', x = 'frequency', data = df_i)\n",
    "plt.title('Frequency', fontsize = 10)\n",
    "plt.ylabel('Occurrences', fontsize = 10)\n",
    "plt.xlabel(i, fontsize = 10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Word counts plot \n",
    "\n",
    "Complete the plot as we did previously using FreqDict, but make plot larger (see how to set the plots size) and show 50 most common tokens withing the label and 50 most unfrequent. "
   ]
  }
 {
  "cell_type": "code",
  "execution_count": 38,
  "metadata": {},
  "outputs": [],
  "source": [
  "Code"
  ]
 }
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
