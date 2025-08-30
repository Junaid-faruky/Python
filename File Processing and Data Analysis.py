# Analyze text file and count word frequencies
def analyze_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        
        # Remove punctuation and split into words
        import string
        words = text.translate(str.maketrans('', '', string.punctuation)).split()
        
        # Count word frequencies
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # Get top 10 most common words
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
        
        print(f"Total words: {len(words)}")
        print(f"Unique words: {len(word_count)}")
        print("\nTop 10 most frequent words:")
        for word, count in sorted_words:
            print(f"{word}: {count}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

# Example usage
analyze_text_file('sample.txt')
