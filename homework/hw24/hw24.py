import json
from dataclasses import dataclass
from typing import List


@dataclass
class Palindrome:
    word: str
    meaning: str

    def __bool__(self) -> bool:
        return self.word.lower() == self.word[::-1].lower()

    @classmethod
    def read_json(cls) -> List['Palindrome']:
        with open("palindromes.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # for item in data:
        #     if 'слово' in item:
        #         palindrome = Palindrome(word=item['слово'], meaning=item['значение'])
        #         palindromes.append(palindrome)
        return [cls(word=item['слово'], meaning=item['значение']) for item in data]


def main():
    palindromes = Palindrome.read_json()
    palindrome_count = 0
    non_palindrome_count = 0

    for palindrome in palindromes:
        if palindrome:
            palindrome_count += 1
        else:
            non_palindrome_count += 1

    print(f"Число палиндромов: {palindrome_count} ")
    print(f"Число не-палиндромов: {non_palindrome_count} ")


if __name__ == "__main__":
    main()
