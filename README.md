# Markdown Word Counter

The purpose of this script is to count all of the words within a specified directory.

At present, it only looks at .md files. It is well-suited for use with a tool like [Obsidian](https://obsidian.md).

I created it to automatically log the amount of words that I write each day. I run this script as a daily cron job.

## Usage
To run the script:
1. Add the desired word count directory in config.py (variable WORD_COUNT_DIRECTORY).
2. Add the desired log file path in config.py (variable LOG_FILE_PATH). This works best as a plaintext file (such as .md).
3. Run the script as follows:

```
python get_word_count.py
```


## Potential future improvements:
- Counting the number of *new* words since last time function was called, rather than just the total number of words.
- Incorporating the *changes* in word. Sometimes I'll do editing of existing words, which is important but doesn't lead to *new* words being written
