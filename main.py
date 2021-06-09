import argparse, config, compile

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f'훈민 v{config.version}\nhttps://github.com/entrity0305/hunmin')
    
    parser.add_argument('--컴파일', help='.hmn 파일을 컴파일합니다')
    
    args = parser.parse_args()

    compile.compile(args.컴파일)

    

