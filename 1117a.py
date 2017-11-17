try:
    fh = open("C:/code/tmp1/testfile.txt","w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError as error:
    print "Error:没有找到测试文件或读取文件失败"
    print error
else:
    print "内容写入文件成功"
    fh.close()

print "go on......."
