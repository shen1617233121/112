try:
    fh = open("C:/code/tmp1/testfile.txt","w")
    fh.write("����һ�������ļ������ڲ����쳣!!")
except IOError as error:
    print "Error:û���ҵ������ļ����ȡ�ļ�ʧ��"
    print error
else:
    print "����д���ļ��ɹ�"
    fh.close()

print "go on......."
