def word_counter():
    result = {}
    for line in open('input.txt'):
        for word in line.split():
            result[word] = result.get(word, 0) + 1  # вместо этого можно использовать setdefault или defaultdict
    # меняем местами
    result = [(v,k) for k, v in result.items()]
    # сортировка будет автоматически сначала по первому значению, затем по второму
    result = sorted(result,reverse=True) 
    print(*[t[1] for t in result],sep='\n')

