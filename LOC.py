import os, sys

def main():
    print '+------------------------------------+\n|      Lines of Code by Kulhajs      |\n+------------------------------------+\n'

    lineCount = 0
    ignoredLineCount = 0
    files = 0
    sources = []
    lines = 0
    ignoredLines = 0

    path = raw_input('Path: ')
    filetype = raw_input('File Type: ')
    iE = raw_input('Ignore empty lines? Y/N: ')
    iC = raw_input('Ignore lines containing comments only? Y/N: ')

    if iE == 'Y' or iE == 'y':
        ignoreEmpty = True
    else:
        ignoreEmpty = False

    if iC == 'Y' or iC == 'y':
        comment = raw_input('Comment separator: ')
        ignoreComment = True
    else:
        ignoreComment = False

    for file in os.listdir(path):
        if file.endswith(filetype):
            source = open(path + '/' + file)
            while True:
                line = source.readline()
                if not line:
                    source.close()
                    break
                elif ignoreEmpty and line == '\n':
                    ignoredLines += 1
                elif line.strip().startswith('{') or line.strip().startswith('}'):
                    ignoredLines += 1
                elif ignoreComment and line.strip().startswith(comment):
                    ignoredLines += 1
                else:
                    lines += 1

            lineCount += lines
            ignoredLineCount += ignoredLines
            files += 1
            sources.append((file, lines, ignoredLines))
            lines = 0
            ignoredLines = 0


    print '\n' + str(lineCount) + ' lines of code in ' + str(files) + ' files, ' + str(ignoredLineCount) + ' lines ignored.\n'
    print 'Files included in computation: '
    for s in sources:
        print str(s[1]) + '\tlines of code in ' + str(s[0]) + ', ' + str(s[2]) + ' lines ignored.'

if __name__ == '__main__':
    main()
    i = raw_input()
    if i == 'exit':
        sys.exit(0)
    else:
        main()



