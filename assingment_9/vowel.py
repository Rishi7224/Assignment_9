class Count:
    def count_vowel(self,input_string):
        vowels ="aeiouAEIOU"
        count = 0
        for char in input_string:
            if char in vowels:
             count += 1
        return count
    
counter = Count()
input_string = input("Enter a string: ")
count_vowel = counter.count_vowel(input_string)
print("Number of vowels in the string:", count_vowel)

