def ReadandWrite(file_path, key, value):
    with open(file_path,'r') as file:
        lines = file.readlines()

    with open(file_path,'w') as wfile:
        for line in lines:
            if(key in line):
                wfile.write(key+"="+value+"\n")
            else:
                wfile.write(line)


ReadandWrite("ServerConfig.txt", "MAX_CONNECTIONS", "78945")