"""
The plan:

Based on the problem description, I can see we are going to need the following:

- A list/dictionary.
- Make sure anything being filtered through is being uppercased.

Our Task(s):

1. Get the DNA string for Kaiju1, Kaiju2, Kaiju3, and Kaiju4.
2. Calculate the threat level of each Kaiju by adding up the value of each letter.
3. Print each Kaiju's threat level.
4. Determine and print which Kaiju is the most dangerous (i.e., has the highest threat level).
5. If two or more Kaijus have the same highest threat level, print "It's a tie!".

Programmer's Notes:

Funny thing is, I discovered the ord() function while doing this, which actually made this process way easier.

"""

# Dictionary example



# --------------------------------------------------------------------------------------------------------------------#


# print(ord('A')) - Returns 65, so minus by 64 to get accurate numeric value.

temp = []
value = int(input("How many Kaiju(s) do you have? : "))
for i in range(value):
    name = input("Kaiju's Name: ")
    temp.append(name)

kaiju = [name.upper() for name in temp]  # convert all names to uppercase

threats = {}

for idx, name in enumerate(kaiju):
    threat_level = sum(ord(char) - 64 for char in name)  # calculate threat for this Kaiju only
    threats[temp[idx]] = threat_level  # use original name as key

strongest_kaiju, max_threat = max(threats.items(), key=lambda item: item[1])
print(f"The strongest Kaiju is {strongest_kaiju} with a threat level of {max_threat}!")



    