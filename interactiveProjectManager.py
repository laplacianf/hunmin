import compile, config, os

if __name__ == '__main__':
    print(f'훈민 v{config.version} 프로젝트 매니저\nhttps://github.com/entrity0305/hunmin')
    print("자세한 명령어 목록은 '도움말'을 참고하세요")

    while True:
        command = input('> ').split(' ')

        if command[0] == '도움말': #도움말을 출력
            print('도움말 목록입니다 :')
            print('종료 : 훈민을 종료합니다')
            print('정보 : 현재 훈민의 정보를 출력합니다')
            print('생성 <프로젝트명> : 프로젝트를 생성합니다')
            print('컴파일 <프로젝트명> : 프로젝트의 src 폴더의 파일을 컴파일합니다')
            print('실행 <프로젝트명> : 프로젝트의 src 폴더의 main.hmn 파일을 컴파일 후 실행합니다')
        
        elif command[0] == '생성':
            os.makedirs(os.path.dirname(os.path.abspath(__file__)) + f'\\{command[1]}')
            os.makedirs(os.path.dirname(os.path.abspath(__file__)) + f'\\{command[1]}\\src')

            print(f'{command[1]} 프로젝트가 생성되었습니다')
        
        elif command[0] == '컴파일':
            for hunminFile in os.listdir(command[1] + '\\' + 'src'):
                compile.compile(command[1] + '\\' + 'src' + '\\' + str(hunminFile))
            
            print(f'{command[1]} 프로젝트의 컴파일이 완료되었습니다')
        




    


