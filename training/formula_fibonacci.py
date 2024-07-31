# sequência fibonacci

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence
    
termo = int(input('Digite um termo: '))
result = fibonacci(termo)
result_str = " ".join(map(str, result))
print(result_str)