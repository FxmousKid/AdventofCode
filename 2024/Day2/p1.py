import sys

ALLOWED_DIFF = range(1,4) # [1,2,3]

def bigger_than(n1, n2): return n1 > n2 and n1 - n2 in ALLOWED_DIFF

def check_a_record(record: list[int]) -> int:

    sol: bool = True

    # checking for mistakes assuming it's : [1, 3, 5, 6, ...]
    for v, i in enumerate(record[1:]) :
        if record[v] >= i or i - record[v] not in ALLOWED_DIFF :
            sol = False 
           
    if sol == True :
        return True
    sol = True

    # Checking for mistakes assuming it's : [5, 3 ,2 ,1, ...]
    for v, i in enumerate(record[1:]) :
        if record[v] <= i or record[v] - i not in ALLOWED_DIFF :
            sol = False

    return int(sol)

def check_all_report_comb(report: list[int]) -> int :


    lst: list[int] = []
    lst.append(check_a_record(report))
    for i in range(len(report)) :
        copy = report.copy()
        copy.pop(i)
        lst.append(check_a_record(copy))
    return (max(lst))


def count_safe_reports(lines: list[list[int]]) -> int :

    count_sr: int = 0
    for report in lines :
        print(report)
        if len(report) <= 2 :
            count_sr += 1
        else :
            count_sr += check_all_report_comb(report)
    return count_sr




def main() -> int :
    try :
        with open(sys.argv[1], 'r') as file :
            lines: list[str] = [i.removesuffix('\n') for i in file.readlines()]
            list_lines: list[list[int]] = [[int(i) for i in line.split(' ')] for line in lines]
            res = count_safe_reports(list_lines)
            print(f'Number of safe reports : {res}')
    except FileNotFoundError as e:
        print(e)
        return 1
    return 0

main()
