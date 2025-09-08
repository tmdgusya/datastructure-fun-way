#!/usr/bin/env python3
"""
Simple demo script for testing the trieSearch function
"""

from trie import Trie, trieSearch


def main():
    """Main demo function"""
    print("🌳 Trie Search Function Demo 🌳")
    print("=" * 40)
    
    # Create a new trie
    trie = Trie()
    
    # Demo 1: Basic word insertion and search
    print("\n📝 Demo 1: Basic Words")
    basic_words = ["cat", "car", "card", "care", "careful"]
    
    print(f"Inserting: {basic_words}")
    for word in basic_words:
        trie.insert(word)
    
    test_cases = ["cat", "car", "card", "ca", "care", "careful", "careless", "dog"]
    for test_word in test_cases:
        result = trieSearch(trie, test_word)
        status = "✅ FOUND" if result else "❌ NOT FOUND"
        print(f"  Search '{test_word}': {status}")
    
    # Demo 2: Prefix vs Complete Words
    print("\n📝 Demo 2: Prefix vs Complete Words")
    prefix_trie = Trie()
    prefix_words = ["test", "testing", "tester", "tests"]
    
    print(f"Inserting: {prefix_words}")
    for word in prefix_words:
        prefix_trie.insert(word)
    
    prefix_tests = ["te", "tes", "test", "testi", "testing", "tester", "tests", "testimony"]
    for test_word in prefix_tests:
        result = trieSearch(prefix_trie, test_word)
        status = "✅ FOUND" if result else "❌ NOT FOUND"
        print(f"  Search '{test_word}': {status}")
    
    # Demo 3: Special Characters and Numbers
    print("\n📝 Demo 3: Special Characters & Numbers")
    special_trie = Trie()
    special_words = ["hello-world", "test_case", "version2.0", "file.txt", "user@email.com"]
    
    print(f"Inserting: {special_words}")
    for word in special_words:
        special_trie.insert(word)
    
    special_tests = ["hello-world", "hello_world", "test_case", "testcase", "version2.0", "version", "file.txt", "user@email.com"]
    for test_word in special_tests:
        result = trieSearch(special_trie, test_word)
        status = "✅ FOUND" if result else "❌ NOT FOUND"
        print(f"  Search '{test_word}': {status}")
    
    # Demo 4: Interactive Testing
    print("\n📝 Demo 4: Interactive Testing")
    interactive_trie = Trie()
    sample_words = ["python", "programming", "program", "code", "coding", "computer", "science"]
    
    print(f"Sample trie contains: {sample_words}")
    for word in sample_words:
        interactive_trie.insert(word)
    
    print("\nTry searching for words! (Press Enter with empty input to quit)")
    while True:
        try:
            user_input = input("Enter word to search: ").strip()
            if not user_input:
                break
            
            result = trieSearch(interactive_trie, user_input)
            status = "✅ FOUND" if result else "❌ NOT FOUND"
            print(f"  Result: {status}")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except EOFError:
            break
    
    print("\n🎉 Demo completed!")


if __name__ == "__main__":
    main()
