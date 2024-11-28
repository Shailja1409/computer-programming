'''Given a string and a number N, we need to mirror the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.

Examples: 

Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.

Input : N = 6
        pneumonia
Output : pneumlmrz'''

def mirrorChars(input,k):
 
    # create dictionary
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original,reverse))
 
    # separate out string after length k to change
    # characters in mirror
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''
 
    # change into mirror
    for i in range(0,len(suffix)):
         mirror = mirror + dictChars[suffix[i]]
 
    # concat prefix and mirrored part
    print (prefix+mirror)
          
# Driver program
if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChars(input,k)
