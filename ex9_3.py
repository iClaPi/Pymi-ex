import requests
import sys

def get_top_questions(N, label):
    url = f"https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&tagged={label}&site=stackoverflow"
    response = requests.get(url)
    data = response.json()

    top_questions = []
    for question in data['items'][:N]:
        title = question['title']
        answer_id = question['accepted_answer_id']
        question_link = question['link']

        answer_link = get_answer_link(answer_id)

        top_questions.append((title, answer_link))

    return top_questions

def get_answer_link(answer_id):
    url = f"https://api.stackexchange.com/2.3/answers/{answer_id}?order=desc&sort=votes&site=stackoverflow"
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        answer_link = data['items'][0]['link']
        return answer_link

    return None

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Vui lòng cung cấp số lượng câu hỏi (N) và nhãn tag (LABEL) từ dòng lệnh.")
    else:
        N = int(sys.argv[1])
        label = sys.argv[2]

        top_questions = get_top_questions(N, label)

        for i, question in enumerate(top_questions, start=1):
            title, answer_link = question
            print(f"{i}. {title}")
            print(f"   Answer: {answer_link}\n")
