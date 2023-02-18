import os


# (1) Get the word count across all the files of interest

def count_words_in_directory(directory):
    word_count = 0
    for root, _, files in os.walk(directory):
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


directory = '/Users/chrislovejoy/Documents/My Drive/everything/10-19 Public Creation/13 Personal website/02-personal-website/_notes'
word_count = count_words_in_directory(directory)


# (2) Output the result into a log file, with the desired format

print(word_count)

# TODO: Write logging functionL
    # Open log file
    # Append date and total word count
