#문항 리스트 목록
# 교통수단=[
#     '걸어서 갔나요?',
#     '버스를 탔나요?',
#     '지하철을 탔나요?',
#     '출근은 어떻게 했나요?',
#     '운전을 했나요?'
# ]
# 식사메뉴=[
#     '점심은 뭘 먹었나요?',
#     '오늘 한식을 먹었나요?',
#     '오늘 양식을 먹었나요?',
#     '치킨을 먹었나요?',
#     '밥은 잘 먹고 다니나요?'
# ]
# 옷=[
#     '어떤 옷을 입고 갔나요?',
#     '패딩은 입었나요?',
#     '코트를 입었나요?',
#     '포멀하게 입었나요?',
#     '츄리닝을 입었나요?',
#     '어떤 신발을 신었나요?'
# ]
# 랜덤질문=[
#     '오늘 들은 음악은 어땠나요?',
#     '오늘 몇번 웃었나요?',
#     '푹 잤나요?',
#     '피곤하지는 않았나요?',
# ]
# 특별한경험=[
#     '좋은 사람과 함께 했나요?',
#     '연인과 함께였나요?',
#     '특별하게 적을만한 내용이 있나요?'
# ]
인사=[
    '하이빵까루 오늘 너무 춥지 않았어?',
    '오늘 나는 강아지랑 신나게 놀았다!!'
]
날씨=[
    '오늘 날씨는 어땠나요?',
    '비가 왔나요?',
    '구름이 많았나요?',
    '오늘은 따뜻했나요?',
    '날이 많이 춥진 않았나요?'
]
일상질문=[
    '오늘 너는 뭐하며 지냈어?',
    '기분은 어땠어?',
    '오늘 하루는 어땠어?',
]
인상적인경험=[
    '오늘 가장 기억에 남는건 뭐였어?',
    '오늘은 뭐가 제일 기억에 남았어?',
    '어떤 일들이 기억에 남았어?'
]
하루점수=[
    '오늘 하루는 10점 만점에 몇점?',
    '오늘을 점수로 나타내면 몇점같아?'
]
대화=[
    '혹시 좋아하는 노래장르가 뭐야?',
    '노래부르는 것은 좋아해?'
]
마무리=[
    '그거알아? 받는 것보다 주는 것이 더 행복하대',
    '내일도 화이팅!!'
]
중립답변=[
    '그렇구나',
    '으응'
]
동조답변=[
    '그렇지?',
    '그랬구나!',
]

#일기를 직접 직성하는 부분

import random
print('일기를 써볼까요? y/n')
답변=input()
if 'y' in 답변:
    #사용자 이름을 가져오고 바탕화면에 일기장 폴더 만들기
    import os
    save_file_name='diary1.txt'
    windows_user_name=os.path.expanduser('~')
    print(windows_user_name)

    try:
        os.makedirs(f'{windows_user_name}//Desktop//일기장')
    except FileExistsError:
        pass
    일기장파일=f'{windows_user_name}//Desktop//일기장//{save_file_name}'

    with open(일기장파일,'w') as f:
        인사선택=random.choice(인사)
        print(인사선택)
        #날씨를 물어보고
        날씨선택=random.choice(날씨)
        print(날씨선택)
        날씨선택답변=input()
        f.write(날씨선택답변+'\n')
        #일상질문
        일상선택=random.choice(일상질문)
        print(일상선택)
        일상선택답변=input()
        f.write(일상선택답변+'\n')
        #인상적인 일
        인상선택=random.choice(인상적인경험)
        print(인상선택)
        인상선택답변=input()
        f.write(인상선택답변+'\n')
        #하루점수
        점수선택=random.choice(하루점수)
        print(점수선택)
        점수선택답변=input()
        f.write('오늘 점수는'+점수선택답변+'\n')
        #대화
        대화선택=random.choice(대화)
        print(대화선택)
        대화선택답변=input()
        f.write(대화선택답변+'\n')
        #마무리
        마무리선택=random.choice(마무리)
        print(마무리선택)
    
    # #랜덤 질문이 먼저 온다음
    # 랜덤선택=random.choice(랜덤질문)
    # print(랜덤선택)
    # 랜덤선택답변=input()
    
    # #옷을 물어본다
    # 옷선택=random.choice(옷)
    # print(옷선택)
    # 옷선택답변=input()
    # #교통수단을 물어본다
    # 교통수단선택=random.choice(교통수단)
    # print(교통수단선택)
    # 교통수단답변=input()
    # #식사메뉴를 물어본다
    # 식사메뉴선택=random.choice(식사메뉴)
    # print(식사메뉴선택)
    # 식사메뉴답변=input()
    # #특별한 경험을 물어본다
    # 특별한경험선택=random.choice(특별한경험)
    # print(특별한경험선택)
    # 특별한경험답변=input()
else:
    exit()
#저장 및 모아서 출력 기능 추가
#test
#박진우
