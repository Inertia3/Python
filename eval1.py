def count_characters(input_string):
    vowels = 0
    consonants = 0
    digits = 0
    special_characters = 0


    vowel_list = ['a','e','i','o','u','A','E','I','O','U']

    for char in input_string:
        if char.isalpha():
            if char.lower() in vowel_list:
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        else:
            special_characters += 1

    return vowels, consonants, digits, special_characters

def main():
    input_string = input("Enter a string: ")
    vowel_count, consonant_count, digit_count, special_count = count_characters(input_string)

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Special Characters:", special_count)

if __name__ == "__main__":
    main()

    # So I'm just experimentiing with the branch feature of git
    # ANd I find this quite intresting
