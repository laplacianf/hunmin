import compile, config

if __name__ == '__main__':
    print(f'훈민 v{config.version}\nhttps://github.com/entrity0305/hunmin')
    print("자세한 명령어 목록은 '도움말'을 참고하세요")

    while True:
        command = input('> ').split(' ')

        if command[0] == '도움말': #도움말을 출력
            print('도움말 목록입니다 :')
            print('종료 : 훈민을 종료합니다')
            print('정보 : 현재 훈민의 정보를 출력합니다')
            print('컴파일 <파일명.hmn> : 훈민 파일을 컴파일합니다')
        
        elif command[0] == '종료': #프로그램을 종료
            break

        elif command[0] == '컴파일': #프로그램 실행
            compile.compile(command[1])
            print(f'{command[1]}의 컴파일이 완료되었습니다')

