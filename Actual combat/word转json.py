

with open('aaa.txt', 'w') as f:
    with open('mg.txt', 'r') as fp:
        for line in fp:
            print(line)
            line = str(line).replace("\n", "")
            line = str(line).replace(" ", "")
            line = str(line).replace("考生填写：", "")
            line = str(line).replace("×", "|||")
            line = str(line).replace("√", "|||")
            f.write(line)


# try:
#     f = open('mg.txt', "r")
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('aaa.txt', 'r') as fp:
#     for line in fp:
#         print(fp)