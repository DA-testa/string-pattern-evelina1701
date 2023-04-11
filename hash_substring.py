# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    letter = input()
    if "F" in letter:
        fileName = input()
        if "a" in fileName:
            return
        with open("./tests/"+fileName, mode="r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    if "I" in letter:
        pattern = input().rstrip()
        text = input().rstrip()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pat = 0
    txt = 0
    h = 1
    i = 0
    j = 0
    pat_length = len(pattern)
    txt_length = len(text)
    ch_num = 256
    prime = 101
    for i in range(pat_length-1):
        h = (h*ch_num)%prime

    for i in range(pat_length):
        pat = (ch_num*pat + ord(pattern[i]))%prime
        txt = (ch_num*txt + ord(text[i]))%prime

    occurances = []
    for i in range(txt_length-pat_length+1):
        if pat == txt:
            for j in range(pat_length):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1

            if j == pat_length:
                occurances.append(i)

        if i < txt_length-pat_length:
            txt = (ch_num*(txt-ord(txt[i])*h)+ord(txt[i+pat_length])) % prime

            if txt<0:
                txt=txt + prime
    # and return an iterable variable
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

