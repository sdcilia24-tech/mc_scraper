import random as r
import argparse

#alphabetic mapping of considents to vowels
ALPHA_MAP = {
"C" : ['B', 'C', 'D', 'F','G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],
"V" : ['A', 'E', 'I', 'O', 'U']
}


#defines word struture
NAME_STRUCTURES= [
    "CVC", "VCV", "CVV", "VVC", "VCC", "CCV",
    "CVCV", "VCVC", "CVCC", "CCVC", "CVVC", "VCCV", "CCVV", "VVCV",
    "CVCVC", "CVCCV", "CCVCV", "VCVCV", "CCVCC", "CCVVC", "CVVCC", 
    "VCCVC", "VCVCC", "VVCVC", "CVVCV", "CCCVC",
    "CVCVCV", "CVCCVC", "CCVCVC", "VCVCVC", "CVCVCC", "CCVCCV", 
    "CCVVCV", "CVCVVC", "CVVCVC", "VCCVCV", "VCCVCC", "CCCVCC", 
    "CCCVCV", "CCCVVC"
]

def usergen(num_names):
    """
    generates num_names usernames based on the mapping/rules above
    """
    names = []
    for _ in range(num_names):
        curr = ""
        struct = r.choice(NAME_STRUCTURES)
        for char in struct:
            mapped_char = ALPHA_MAP[char]
            random_char = r.choice(mapped_char)
            curr += random_char
        names.append(curr)
    return names

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',"--num_times",type=int,default=5)
    args = parser.parse_args()
    with open("generated.txt", 'w', encoding = None) as file:
        print(str(usergen(args.num_times)).strip('[]').replace("'","").replace(",","").replace(" ", "\n"), file = file)
main()

