# toán lớp 3##########################
# tìm số lần thoản mãn biểu thức
# ba0>300 với a,b>0; a + b=9; a>b; 
# b là số hàng trăm; a số hàng chục
# tìm số a,b và số lần phương án thỏa mãn
########################################
c = 300
i = 0
for b in range(0,10):
	for a in range(0,10):
		if (a + b == 9) and (a>b) and (a>0) and (b>0):
			if ((b*100 + a*10)> c):
				print("*" * 10)
				print ("b=" + str(b) + ";  " + "a=" + str(a))
				print(str((b*100) + (a*10)) + " > " + str(c))
				print("*" * 10)
				i +=1
print("so phuong an thoa man:", i)