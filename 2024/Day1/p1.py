import sys

def sum_distance(l1: list[int], l2: list[int]) -> int :
    l1.sort()
    l2.sort()
    return sum([max(l1[i], l2[i]) - min(l1[i], l2[i]) for i in range(len(l1))])

def occ_count(l: list[int], n: int) -> int :
    return sum([1 for i in l if i == n]);

def similarity_total(l1: list[int], l2: list[int]) -> int :
    score: int = sum([n * occ_count(l2, n) for n in l1])
    return score

def main() -> int :
    try : 
        with open(sys.argv[1], 'r') as f :
            contents = f.readlines()
            contents = [line.removesuffix('\n') for line in contents]
            l1: list[int] = [int(line.split('   ')[0]) for line in contents]
            l2: list[int] = [int(line.split('   ')[1]) for line in contents]
            print(f'Sum of distances : {sum_distance(l1, l2)}')
            print(f'Total similiarity score : {similarity_total(l1, l2)}')
    except Exception as e :
        print(e)
        return 1
    return 0

main()
