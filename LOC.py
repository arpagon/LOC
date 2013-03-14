import os, sys

def main():
    print ('+------------------------------------+\n|      Lines of Code by Kulhajs      |\n+------------------------------------+\n')

    lineCount = 0
    ignoredLineCount = 0
    fileCount = 0
    sources = []
    lines = 0
    ignoredLines = 0

    root = input('Path: ')
    filetype = input('File Type: ')
    iE = input('Ignore empty lines? Y/N: ')
    iC = input('Ignore lines containing comments only? Y/N: ')

    if iE == 'Y' or iE == 'y':
        ignoreEmpty = True
    else:
        ignoreEmpty = False

    if iC == 'Y' or iC == 'y':
        comment = input('Comment separator: ')
        ignoreComment = True
    else:
        ignoreComment = False

    for path, subdirs, files in os.walk(root):
        for name in files:
            file = os.path.join(path, name)
            if file.endswith(filetype):
                #print file
                source = open(file)
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
                fileCount += 1
                sources.append((name, lines, ignoredLines))
                lines = 0
                ignoredLines = 0


    print ('\n' + str(lineCount) + ' lines of code in ' + str(fileCount) + ' files, ' + str(ignoredLineCount) + ' lines ignored.\n')
    print ('Files included in computation: ')
    for s in sources:
        print (str(s[1]) + '\tlines of code in ' + str(s[0]) + ', ' + str(s[2]) + ' lines ignored.')

if __name__ == '__main__':
    main()
    i = input()
    if i == 'exit':
        sys.exit(0)
    else:
        main()



