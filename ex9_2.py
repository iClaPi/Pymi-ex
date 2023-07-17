import sys
import requests
import bs4

def get_lottery_results():
    r = requests.get("https://ketqua.vn")
    tree = bs4.BeautifulSoup(markup=r.text, features='lxml')

    results = {}

    # Lấy kết quả của giải đặc biệt
    db = tree.find('td', attrs={"class": "txt-special-prize"})
    db_num = db.text.strip()
    results['ĐB'] = db_num

    # Lấy kết quả của giải từ 1 đến 7
    for i in range(1, 8):
        prize_name = f'G{i}'
        prize = tree.find('td', class_="fw-medium", text=f'G{i}')
        prizes = prize.find_all_next('td', class_="txt-normal-prize")
        prize_result = [element.text.strip() for element in prizes]
        if prize_result:
            prize_numbers = ', '.join(prize_result)
        else:
            prize_numbers = ''
        results[prize_name] = prize_numbers

    return results

def check_lottery_numbers(numbers, results):
    for number in numbers:
        matched = False

        # Kiểm tra trúng giải đặc biệt
        if number == results['ĐB']:
            print(f'Số {number}: Trúng giải Đặc biệt')

        # Kiểm tra trúng giải từ 1 đến 7
        for i in range(1, 8):
            prize_name = f'G{i}'
            if number == results[prize_name]:
                print(f'Số {number}: Trúng giải {prize_name}')
                matched = True
                break

        # Nếu không trúng giải nào
        if not matched:
            print(f'Số {number}: Không trúng giải')

def main():
    # Lấy kết quả xổ số từ trang web
    results = get_lottery_results()

    # Kiểm tra các số argument đầu vào
    if len(sys.argv) > 1:
        lottery_numbers = sys.argv[1:]
        check_lottery_numbers(lottery_numbers, results)
    else:
        # Nếu không có số argument nào, in ra tất cả các giải từ Đặc biệt đến giải 7
        print('Kết quả xổ số từ Đặc biệt đến giải 7:')
        print('ĐB:', results['ĐB'])
        for i in range(1, 8):
            prize_name = f'G{i}'
            print(f'{prize_name}:', results[prize_name])

if __name__ == '__main__':
    main()
