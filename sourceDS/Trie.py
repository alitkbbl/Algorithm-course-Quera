class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store children nodes
        self.is_end_of_word = False  # Marks the end of a word
        self.word_count = 0  # How many times this word was inserted
        self.meaning = None  # Optional: store meaning/definition

    def __repr__(self):
        return f"TrieNode(children={list(self.children.keys())}, is_end={self.is_end_of_word})"


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0
        self.total_nodes = 1  # Count the root node

    def insert(self, word, meaning=None):
        """Insert a word into the trie"""
        print(f"\n{'=' * 60}")
        print(f"INSERTING WORD: '{word}'")
        print(f"{'=' * 60}")

        current = self.root
        path = []

        for i, char in enumerate(word):
            print(f"  Processing character '{char}' (position {i + 1})")

            if char not in current.children:
                print(f"    Character '{char}' not found, creating new node")
                current.children[char] = TrieNode()
                self.total_nodes += 1
            else:
                print(f"    Character '{char}' found in children")

            current = current.children[char]
            path.append(char)
            print(f"    Current path: {''.join(path)}")

        # Mark the end of the word
        if not current.is_end_of_word:
            print(f"  ✓ Marking '{word}' as complete word")
            current.is_end_of_word = True
            self.total_words += 1
        else:
            print(f"  Word '{word}' already exists, incrementing count")

        current.word_count += 1
        if meaning:
            current.meaning = meaning
            print(f"  Added meaning: {meaning}")

        print(f"  Total words in trie: {self.total_words}")
        print(f"  Total nodes in trie: {self.total_nodes}")

    def search(self, word, return_node=False):
        """Search for a word in the trie"""
        print(f"\n{'=' * 60}")
        print(f"SEARCHING FOR WORD: '{word}'")
        print(f"{'=' * 60}")

        current = self.root
        path = []

        for i, char in enumerate(word):
            print(f"  Looking for character '{char}' (position {i + 1})")

            if char not in current.children:
                print(f"    ✗ Character '{char}' not found!")
                print(f"    Word '{word}' does NOT exist in trie")
                return (False, None) if return_node else False

            current = current.children[char]
            path.append(char)
            print(f"    ✓ Found '{char}', moving to node")
            print(f"    Current path: {''.join(path)}")

        if current.is_end_of_word:
            print(f"  ✓ Word '{word}' FOUND in trie")
            print(f"    Word count: {current.word_count}")
            if current.meaning:
                print(f"    Meaning: {current.meaning}")
        else:
            print(f"  ✗ '{word}' is a PREFIX but not a complete word")

        return (current.is_end_of_word, current) if return_node else current.is_end_of_word

    def starts_with(self, prefix):
        """Check if any word starts with the given prefix"""
        print(f"\n{'=' * 60}")
        print(f"CHECKING PREFIX: '{prefix}'")
        print(f"{'=' * 60}")

        current = self.root

        for char in prefix:
            if char not in current.children:
                print(f"  ✗ Prefix '{prefix}' NOT found")
                return False
            current = current.children[char]

        # If we reach here, prefix exists
        print(f"  ✓ Prefix '{prefix}' exists in trie")

        # Find all words with this prefix
        words = self._get_words_from_node(current, prefix)
        print(f"  Words with prefix '{prefix}': {words}")

        return True

    def delete(self, word):
        """Delete a word from the trie"""
        print(f"\n{'=' * 60}")
        print(f"DELETING WORD: '{word}'")
        print(f"{'=' * 60}")

        # First, find the node
        found, node = self.search(word, return_node=True)

        if not found:
            print(f"  ✗ Word '{word}' not found, cannot delete")
            return False

        if node.word_count > 1:
            # Word was inserted multiple times, just decrement count
            node.word_count -= 1
            print(f"  Word '{word}' count decremented to {node.word_count}")
            return True

        # Word exists only once, mark as not end of word
        node.is_end_of_word = False
        node.word_count = 0
        node.meaning = None
        self.total_words -= 1

        print(f"  ✓ Word '{word}' marked as deleted")
        print(f"  Total words in trie: {self.total_words}")

        # Optional: prune unused nodes (advanced implementation)
        # self._prune_unused_nodes(word)

        return True

    def autocomplete(self, prefix, max_suggestions=5):
        """Get autocomplete suggestions for a prefix"""
        print(f"\n{'=' * 60}")
        print(f"AUTOCOMPLETE FOR: '{prefix}'")
        print(f"{'=' * 60}")

        current = self.root

        # Navigate to the prefix node
        for char in prefix:
            if char not in current.children:
                print(f"  ✗ No words found with prefix '{prefix}'")
                return []
            current = current.children[char]

        # Get all words from this node
        suggestions = self._get_words_from_node(current, prefix, max_suggestions)

        print(f"  Found {len(suggestions)} suggestions:")
        for i, word in enumerate(suggestions, 1):
            print(f"    {i}. {word}")

        return suggestions

    def _get_words_from_node(self, node, prefix, limit=None):
        """Get all words starting from a given node"""
        words = []
        self._collect_words(node, prefix, words, limit)
        return words

    def _collect_words(self, node, current_word, result, limit):
        """Recursively collect words from a node"""
        if limit is not None and len(result) >= limit:
            return

        if node.is_end_of_word:
            result.append((current_word, node.word_count, node.meaning))

        for char, child_node in sorted(node.children.items()):
            self._collect_words(child_node, current_word + char, result, limit)

    def get_all_words(self):
        """Get all words in the trie"""
        all_words = self._get_words_from_node(self.root, "")
        return all_words

    def word_count_stats(self):
        """Get statistics about word counts"""
        words = self.get_all_words()

        unique_words = len(words)
        total_occurrences = sum(count for _, count, _ in words)
        most_common = max(words, key=lambda x: x[1]) if words else None

        return {
            'unique_words': unique_words,
            'total_occurrences': total_occurrences,
            'most_common_word': most_common
        }

    def longest_common_prefix(self):
        """Find the longest common prefix of all words"""
        prefix = ""
        current = self.root

        while len(current.children) == 1 and not current.is_end_of_word:
            char = next(iter(current.children))
            prefix += char
            current = current.children[char]

        return prefix

    def print_trie(self, node=None, prefix="", last=True):
        """Print the trie structure visually"""
        if node is None:
            print("\nTRIE STRUCTURE:")
            print("-" * 40)
            node = self.root

        # Print current node
        if prefix == "":
            print("🌳 ROOT")
        else:
            marker = "└── " if last else "├── "
            end_marker = " ✓" if node.is_end_of_word else ""
            print(f"{prefix}{marker}{prefix[-1] if prefix else ''}{end_marker}")

        # Print children
        child_prefix = prefix + ("    " if last else "│   ")
        children = sorted(node.children.items())

        for i, (char, child_node) in enumerate(children):
            is_last = (i == len(children) - 1)
            self.print_trie(child_node, child_prefix, is_last)

    def print_statistics(self):
        """Print trie statistics"""
        print("\n" + "=" * 60)
        print("TRIE STATISTICS")
        print("=" * 60)

        stats = self.word_count_stats()

        print(f"Total unique words: {self.total_words}")
        print(f"Total nodes: {self.total_nodes}")
        print(f"Unique words (from scan): {stats['unique_words']}")
        print(f"Total word occurrences: {stats['total_occurrences']}")

        if stats['most_common_word']:
            word, count, meaning = stats['most_common_word']
            print(f"Most common word: '{word}' (appeared {count} times)")
            if meaning:
                print(f"  Meaning: {meaning}")

        lcp = self.longest_common_prefix()
        if lcp:
            print(f"Longest common prefix: '{lcp}'")
        else:
            print("No common prefix (or trie is empty)")

        # Compression ratio
        if self.total_words > 0:
            chars_in_words = sum(len(word) for word, _, _ in self.get_all_words())
            compression_ratio = (1 - (self.total_nodes / chars_in_words)) * 100
            print(f"Compression ratio: {compression_ratio:.1f}% space saved")


# Test Trie Implementation
if __name__ == "__main__":
    # Create a trie
    trie = Trie()

    print("TRIE DATA STRUCTURE DEMONSTRATION")
    print("=" * 60)

    # Insert words
    print("\nPHASE 1: INSERTING WORDS")
    print("-" * 60)

    words_with_meaning = [
        ("apple", "a sweet red fruit"),
        ("app", "short for application"),
        ("application", "a program or piece of software"),
        ("apply", "to make a formal request"),
        ("banana", "a long curved fruit"),
        ("band", "a group of musicians"),
        ("bandana", "a piece of cloth worn on head"),
        ("bat", "a flying mammal or sports equipment"),
        ("batch", "a quantity of goods produced at one time"),
        ("bath", "a container for washing"),
        ("cat", "a small domesticated carnivore"),
        ("category", "a class or division"),
        ("cater", "to provide food and drink"),
        ("dog", "a domesticated carnivorous mammal"),
        ("document", "a piece of written work"),
        ("domain", "an area of territory"),
    ]

    for i, (word, meaning) in enumerate(words_with_meaning):
        trie.insert(word, meaning)
        print(f"\nInserted {i + 1}/{len(words_with_meaning)} words")
        print("-" * 40)

    # Insert some duplicates
    print("\nInserting duplicate words to test counting:")
    duplicate_words = ["apple", "apple", "bat", "cat", "cat", "cat"]
    for word in duplicate_words:
        trie.insert(word)

    # Search for words
    print("\n\nPHASE 2: SEARCHING WORDS")
    print("-" * 60)

    search_words = ["apple", "app", "application", "xyz", "bat", "bathroom"]
    for word in search_words:
        trie.search(word)

    # Prefix search
    print("\n\nPHASE 3: PREFIX SEARCH")
    print("-" * 60)

    prefixes = ["app", "ba", "cat", "do", "xyz"]
    for prefix in prefixes:
        trie.starts_with(prefix)

    # Autocomplete
    print("\n\nPHASE 4: AUTOCOMPLETE")
    print("-" * 60)

    autocomplete_prefixes = ["ap", "ba", "c", "do"]
    for prefix in autocomplete_prefixes:
        trie.autocomplete(prefix, max_suggestions=3)

    # Delete words
    print("\n\nPHASE 5: DELETING WORDS")
    print("-" * 60)

    delete_words = ["app", "xyz", "bat"]
    for word in delete_words:
        trie.delete(word)

    # Get all words
    print("\n\nPHASE 6: GET ALL WORDS")
    print("-" * 60)

    all_words = trie.get_all_words()
    print(f"All words in trie ({len(all_words)} unique):")
    for i, (word, count, meaning) in enumerate(sorted(all_words), 1):
        print(f"  {i:2d}. {word:<15} (count: {count})", end="")
        if meaning:
            print(f" - {meaning}")
        else:
            print()

    # Print trie structure
    print("\n\nPHASE 7: TRIE VISUALIZATION")
    print("-" * 60)

    trie.print_trie()

    # Print statistics
    trie.print_statistics()

    # Advanced operations
    print("\n\nPHASE 8: ADVANCED OPERATIONS")
    print("-" * 60)

    # Longest common prefix
    lcp = trie.longest_common_prefix()
    print(f"Longest common prefix among all words: '{lcp}'")

    # Word with specific prefix
    print("\nAll words starting with 'ba':")
    ba_words = trie._get_words_from_node(trie.root.children.get('b', TrieNode()).children.get('a', TrieNode()), "ba")
    for word, count, _ in ba_words:
        print(f"  - {word} (count: {count})")

    # Test empty trie
    print("\n\nCreating empty trie for edge cases:")
    empty_trie = Trie()
    empty_trie.search("test")
    empty_trie.starts_with("pre")
    empty_trie.print_statistics()