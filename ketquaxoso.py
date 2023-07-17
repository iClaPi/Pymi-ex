import sys
import requests
import bs4

def get_lottery_results():
    r = requests.get("https://ketqua.vn")
    tree = bs4.BeautifulSoup(markup=r.text, features='html.parser')

    results = {}

    xsmb = tree.find('div', class_='bg-white br-10 table-shadow m-b-15')
    db = xsmb.find('td', class_="txt-special-prize")
    db_num = db.text.strip()
    results['ĐB'] = db_num

    for i in range(1, 8):
        prize_name = f'G{i}'
        prize = xsmb.find('td', class_="fw-medium", text=f'G{i}')
        if i == 1:
            prizes = prize.find_next('td', {'class': 'txt-normal-prize'})
        if i == 2:
            prizes = prize.find_all_next('td', {'class': 'txt-normal-prize'})[:2]
        if i == 3:
            prizes = prize.find_all_next('td', {'class': 'txt-normal-prize'})[:6]
        if i == 4:
            prizes = prize.find_all_next('td', {'class': 'txt-normal-prize'})[:3]
        if i == 5:
            prizes = prize.find_all_next('td', {'class': 'txt-normal-prize'})[:6]
        if i == 6:
            prizes = prize.find_all_next('td', {'class': 'txt-normal-prize'})[:3]
        if i == 7:
            prizes = prize.find_all_next('td', {'class': 'txt-normal-prize'})[:4]
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
        if number == results.get('ĐB'):
            print(f'Số {number}: Trúng giải Đặc biệt')

        # Kiểm tra trúng giải từ 1 đến 7
        for i in range(1, 8):
            prize_name = f'G{i}'
            if number == results.get(prize_name):
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
        print('ĐB:', results.get('ĐB', ''))
        for i in range(1, 8):
            prize_name = f'G{i}'
            print(f'{prize_name}:', results.get(prize_name, ''))

if __name__ == '__main__':
    main()
