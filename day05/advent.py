#!/usr/bin/env python3

class AString:
    def __init__(self, s):
        self.s = s

    def has_3_vowels(self):
        count = sum(self.s.count(vowel) for vowel in "aeiou")
        return count >= 3

    def has_one_letter_appear_twice(self):
        current_char = self.s[0]
        for c in self.s[1:]:
            if c == current_char:
                return True
            current_char = c
        return False

    def does_not_contains(self):
        for s in "ab", "cd", "pq", "xy":
            if self.s.find(s) != -1:
                return False
        return True

    def ok_string_1st_pass(self):
        return self.does_not_contains() and self.has_3_vowels() and self.has_one_letter_appear_twice()

    def contains_a_pair_of_2_letters(self):
        i=0
        while i < len(self.s) - 2:
            current_2_letters = self.s[i:i+2]
            if self.s[i+2:].find(current_2_letters) != -1:
                return True
            i = i + 1
        return False

    def contains_a_repeating_letter(self):
        i=0
        while i < len(self.s) - 2:
            if self.s[i+2] == self.s[i]:
                return True
            i = i + 1
        return False

    def ok_string_2nd_pass(self):
        return self.contains_a_pair_of_2_letters() and self.contains_a_repeating_letter()


def first_pass():
    with open("input.txt") as lines:
        strings = [ AString(l) for l in lines.readlines() ]
        good_strings = [s for s in strings if s.ok_string_1st_pass()]
        print(len(good_strings))

def second_pass():
    with open("input.txt") as lines:
        strings = [ AString(l) for l in lines.readlines() ]
        good_strings = [s for s in strings if s.ok_string_2nd_pass()]
        print(len(good_strings))

if __name__ == '__main__':
    # first_pass()
    second_pass()
    print(AString("qjhvhtzxzqqjkmpb").ok_string_2nd_pass())
    print(AString("xxyxx").ok_string_2nd_pass())
    print(AString("uurcxstgmygtbstg").ok_string_2nd_pass())
    print(AString("ieodomkazucvgmuy").ok_string_2nd_pass())
