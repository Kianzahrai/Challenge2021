# Count the Number of Each Vowel

#string of vowels
vowels = 'aeiou'

ip_str = "Hello, have you tried our tutorial section yet?"

# make it suitable for caseless comparisons
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and a value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_Str:
    if char in count:
        count[char] += 1

print(count)
