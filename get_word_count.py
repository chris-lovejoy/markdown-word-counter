import os
import config
import datetime

# (1) Functions for getting the word count across all the files of interest

def count_words_in_directory(directory):
    word_count = 0
    for root, _, files in os.walk(directory):
        # TODO: add option to not look in subfolders (based on config file)
        for file in files:
            if file.endswith('.md'):
                filename = os.path.join(root, file)
                count = count_words(filename)
                word_count += count
    return word_count

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # TODO: consider removing YAML elements at start of files
        words = file.read().split()
        return len(words)

# (2) Function for outputting the result into a log file, with the desired format

def log_word_count(word_count):
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    log_filename = config.LOG_FILE_PATH
    with open(log_filename, 'a+', encoding='utf-8') as log_file:
       # Load the previous day's log
        log_file.seek(0)  # Move the file pointer to the beginning of the file
        previous_day_count = 0 # Initialise variable for count on the previous day 
        previous_day_str = "- " + (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        for line in log_file:
            if line.startswith(previous_day_str):
                previous_day_count = int(line.split()[2]) # Index into second element of the line
                break

        # Calculate the difference in the word count
        diff = word_count - previous_day_count

        # Write the log message
        log_file.write(f'- {date_str}: {word_count} words ({diff:+} from {previous_day_count})\n')
    

# Call the script

if __name__ == '__main__':
    word_count = count_words_in_directory(config.WORD_COUNT_DIRECTORY)
    log_word_count(word_count)
