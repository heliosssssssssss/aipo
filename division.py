def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    pos = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[pos])
        k = int(input_data[pos+1])
        pos += 2
        
        # Read the array elements
        a = list(map(int, input_data[pos:pos+n]))
        pos += n
        
        # Count frequencies of residues modulo k
        freq = {}
        residues = []
        for num in a:
            residue = num % k
            residues.append(residue)
            freq[residue] = freq.get(residue, 0) + 1
        
        # Find the smallest index with a unique residue
        answer = -1
        for i, r in enumerate(residues):
            if freq[r] == 1:
                answer = i + 1  # Convert 0-index to 1-index
                break
        
        results.append(str(answer))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
