import unittest
from trie import Trie, TrieNode, trieSearch


class TestTrieSearch(unittest.TestCase):
    """Comprehensive test cases for trieSearch function"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.trie = Trie()
    
    def test_empty_trie_search(self):
        """Test searching in an empty trie"""
        self.assertFalse(trieSearch(self.trie, "hello"))
        self.assertFalse(trieSearch(self.trie, ""))
        self.assertFalse(trieSearch(self.trie, "a"))
    
    def test_single_word_trie(self):
        """Test searching in a trie with a single word"""
        self.trie.insert("hello")
        
        # Should find the exact word
        self.assertTrue(trieSearch(self.trie, "hello"))
        
        # Should not find prefixes
        self.assertFalse(trieSearch(self.trie, "h"))
        self.assertFalse(trieSearch(self.trie, "he"))
        self.assertFalse(trieSearch(self.trie, "hel"))
        self.assertFalse(trieSearch(self.trie, "hell"))
        
        # Should not find extensions
        self.assertFalse(trieSearch(self.trie, "hellos"))
        self.assertFalse(trieSearch(self.trie, "hello world"))
        
        # Should not find completely different words
        self.assertFalse(trieSearch(self.trie, "world"))
        self.assertFalse(trieSearch(self.trie, "hi"))
    
    def test_multiple_words_trie(self):
        """Test searching in a trie with multiple words"""
        words = ["cat", "car", "card", "care", "careful", "cars", "carry"]
        for word in words:
            self.trie.insert(word)
        
        # Should find all inserted words
        for word in words:
            self.assertTrue(trieSearch(self.trie, word), f"Should find '{word}'")
        
        # Should not find prefixes that aren't complete words
        self.assertFalse(trieSearch(self.trie, "ca"))
        
        # Should not find extensions
        self.assertFalse(trieSearch(self.trie, "cats"))
        self.assertFalse(trieSearch(self.trie, "caring"))
        
        # Should not find non-existent words
        self.assertFalse(trieSearch(self.trie, "dog"))
        self.assertFalse(trieSearch(self.trie, "carrot"))
    
    def test_prefix_vs_complete_word(self):
        """Test distinguishing between prefixes and complete words"""
        # Insert words where one is a prefix of another
        self.trie.insert("test")
        self.trie.insert("testing")
        self.trie.insert("tester")
        
        # All inserted words should be found
        self.assertTrue(trieSearch(self.trie, "test"))
        self.assertTrue(trieSearch(self.trie, "testing"))
        self.assertTrue(trieSearch(self.trie, "tester"))
        
        # Prefixes that aren't complete words should not be found
        self.assertFalse(trieSearch(self.trie, "te"))
        self.assertFalse(trieSearch(self.trie, "tes"))
        self.assertFalse(trieSearch(self.trie, "testi"))
        self.assertFalse(trieSearch(self.trie, "teste"))
    
    def test_single_character_words(self):
        """Test searching for single character words"""
        single_chars = ["a", "i", "o", "x", "z"]
        for char in single_chars:
            self.trie.insert(char)
        
        # Should find all single character words
        for char in single_chars:
            self.assertTrue(trieSearch(self.trie, char))
        
        # Should not find non-inserted characters
        self.assertFalse(trieSearch(self.trie, "b"))
        self.assertFalse(trieSearch(self.trie, "y"))
    
    def test_empty_string_search(self):
        """Test searching for empty string"""
        # Empty string in empty trie
        self.assertFalse(trieSearch(self.trie, ""))
        
        # Empty string in non-empty trie
        self.trie.insert("hello")
        self.assertFalse(trieSearch(self.trie, ""))
        
        # Insert empty string explicitly (edge case)
        self.trie.root.is_entry = True
        self.assertTrue(trieSearch(self.trie, ""))
    
    def test_case_sensitivity(self):
        """Test that trie search is case sensitive"""
        self.trie.insert("Hello")
        self.trie.insert("WORLD")
        self.trie.insert("python")
        
        # Exact case should be found
        self.assertTrue(trieSearch(self.trie, "Hello"))
        self.assertTrue(trieSearch(self.trie, "WORLD"))
        self.assertTrue(trieSearch(self.trie, "python"))
        
        # Different case should not be found
        self.assertFalse(trieSearch(self.trie, "hello"))
        self.assertFalse(trieSearch(self.trie, "HELLO"))
        self.assertFalse(trieSearch(self.trie, "world"))
        self.assertFalse(trieSearch(self.trie, "World"))
        self.assertFalse(trieSearch(self.trie, "Python"))
        self.assertFalse(trieSearch(self.trie, "PYTHON"))
    
    def test_special_characters(self):
        """Test searching with special characters"""
        special_words = ["hello-world", "test_case", "email@domain.com", "path/to/file", "c++", "C#"]
        for word in special_words:
            self.trie.insert(word)
        
        # Should find all words with special characters
        for word in special_words:
            self.assertTrue(trieSearch(self.trie, word))
        
        # Should not find similar words without special characters
        self.assertFalse(trieSearch(self.trie, "helloworld"))
        self.assertFalse(trieSearch(self.trie, "testcase"))
    
    def test_numbers_and_mixed_content(self):
        """Test searching with numbers and mixed content"""
        mixed_words = ["test123", "123test", "version2.0", "file1", "2023year"]
        for word in mixed_words:
            self.trie.insert(word)
        
        # Should find all mixed content words
        for word in mixed_words:
            self.assertTrue(trieSearch(self.trie, word))
        
        # Should not find partial matches
        self.assertFalse(trieSearch(self.trie, "test"))
        self.assertFalse(trieSearch(self.trie, "123"))
        self.assertFalse(trieSearch(self.trie, "version"))
    
    def test_long_words(self):
        """Test searching with very long words"""
        long_word = "supercalifragilisticexpialidocious"
        very_long_word = "a" * 1000  # 1000 character word
        
        self.trie.insert(long_word)
        self.trie.insert(very_long_word)
        
        self.assertTrue(trieSearch(self.trie, long_word))
        self.assertTrue(trieSearch(self.trie, very_long_word))
        
        # Should not find prefixes
        self.assertFalse(trieSearch(self.trie, long_word[:-1]))
        self.assertFalse(trieSearch(self.trie, very_long_word[:-1]))
    
    def test_null_trie(self):
        """Test searching in a null trie"""
        self.assertFalse(trieSearch(None, "test"))
        
        # Test with trie that has None root
        null_trie = Trie(None)
        self.assertFalse(trieSearch(null_trie, "test"))
    
    def test_overlapping_words(self):
        """Test with words that have overlapping prefixes"""
        overlapping_words = [
            "program", "programming", "programmer", "programs",
            "progress", "progressive", "project", "projection"
        ]
        
        for word in overlapping_words:
            self.trie.insert(word)
        
        # All words should be found
        for word in overlapping_words:
            self.assertTrue(trieSearch(self.trie, word))
        
        # Common prefixes that aren't complete words should not be found
        self.assertFalse(trieSearch(self.trie, "prog"))
        self.assertFalse(trieSearch(self.trie, "progr"))
        self.assertFalse(trieSearch(self.trie, "progra"))
        self.assertFalse(trieSearch(self.trie, "proj"))
        self.assertFalse(trieSearch(self.trie, "proje"))
    
    def test_unicode_characters(self):
        """Test searching with unicode characters"""
        unicode_words = ["café", "naïve", "résumé", "🚀", "한글", "日本語"]
        
        for word in unicode_words:
            self.trie.insert(word)
        
        # Should find all unicode words
        for word in unicode_words:
            self.assertTrue(trieSearch(self.trie, word))
        
        # Should not find ASCII approximations
        self.assertFalse(trieSearch(self.trie, "cafe"))
        self.assertFalse(trieSearch(self.trie, "naive"))
        self.assertFalse(trieSearch(self.trie, "resume"))


def run_trie_search_demo():
    """Demonstration function showing trieSearch in action"""
    print("=== Trie Search Demo ===")
    
    # Create and populate a trie
    demo_trie = Trie()
    words = ["apple", "app", "application", "apply", "apricot", "banana", "band", "bandana"]
    
    print("Inserting words:", words)
    for word in words:
        demo_trie.insert(word)
    
    print("\n--- Search Results ---")
    test_searches = [
        "app",           # Should find (complete word)
        "apple",         # Should find (complete word) 
        "appl",          # Should NOT find (prefix only)
        "application",   # Should find (complete word)
        "applications",  # Should NOT find (extension)
        "banana",        # Should find (complete word)
        "ban",           # Should NOT find (prefix only)
        "orange",        # Should NOT find (not in trie)
        ""               # Should NOT find (empty string)
    ]
    
    for search_term in test_searches:
        result = trieSearch(demo_trie, search_term)
        status = "✓ FOUND" if result else "✗ NOT FOUND"
        print(f"Search '{search_term}': {status}")


if __name__ == "__main__":
    # Run the demo first
    run_trie_search_demo()
    print("\n" + "="*50 + "\n")
    
    # Run the unit tests
    unittest.main(verbosity=2)
