target_word = input()
check_words = [input() for _ in range(int(input()))]
vowels = 'ауоыиэяюёе'


def get_vowels_idx(word):
    result = set(idx for idx, ch in enumerate(word) if ch in vowels)
    return result


target_idx = get_vowels_idx(target_word)

for word in check_words:
    if get_vowels_idx(word) == target_idx:
        print(word)
