"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.
Implement a function likes :: [String] -> String, which must take in input array,
containing the names of people who like an item. It must return the display text as shown in the examples:
"""


def likes(*args) -> str:
    pass


def test_if_likes_works_correct():
    word = 'Mike'

    result = likes(word)

    assert result == 'Mike likes '