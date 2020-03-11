

# https://public.karat.io/content/q093/wordlist.txt

def get_list(N, K):
    
    # url = "https://public.karat.io/content/q093/wordlist.txt"
    # f = urllib.request.urlopen(url)
    # my_file = f.read()

    with open("wordlist.txt") as f:
        content = f.readlines()

    # print()
    formatted = []
    output = []
    lines = [line.split("\t")  for line in content]
    for line in lines:
        line[1] = int(line[1].rstrip())
        formatted.append(line)

    
    for pair in formatted:
        # for  in range(N):
            if 2 <= len(pair[0]) <= K:
                output.append(pair)
            if len(output) == N:        
                return output
         



print(get_list(6,5))
