

f = open("my_file.txt", mode = "w")
f.write("hello my name is kartikeya izip_longest requires Python 2.6( or higher). If on Python 2.4 or 2.5, use the definition for izip_longest from the document or change the grouper function to :")
f.close()

f = open("my_file.txt", mode = "r")
data  = f.read()



sbox = [["63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"],
		["ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"],
		["b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"],
		["04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"],
		["09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"],
		["53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"],
		["d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"],
		["51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"],
		["cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"],
		["60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"],
		["e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"],
		["e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"],
		["ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"],
		["70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"],
		["e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"],
		["8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"]]			


key=100
def converttobinary(a):
	 return oc(bin(ord(a)^key).replace("0b", "").zfill(8)[::-1])              
                   



def oc(c):
	r = ""
	for i in range(len(c)):
		if(c[i] == '1'):r+='0'
		else : r+='1'
	return division(r);


def division(k):
	val1 = ""
	val2 = ""
	for i in range(len(k)):
		if(i<=3):
			val1+=k[i]
		else:
			val2+=k[i]

	a= int(val1,2)
	b= int(val2,2)
	return (sbox[a][b])


def encode(data):
	#count = 0
	arr=""
	#row_idx = 0
	for i in range(len(data)):
	#	if(count<16):
			#count = count+1
			x = converttobinary(data[i])
			arr+=x;	

	arr = arr+data[len(data):]

	res = arr.encode('utf-8')
	#with open("my_file.encode" , 'wb') as fo:
	 #           fo.write(res)

	file = open("my_file.txt", mode = "wb")
	file.write(res)
	file.close()
	return arr


def doc(c):
	r = ""
	for i in range(len(c)):
		if(c[i] == '1'):r+='0'
		else : r+='1'
	return r;


def sboxs(a):
	for i in range(len(sbox)):
		for j in range(len(sbox)):
			if(sbox[i][j]==a):
				k = bin(i).replace("0b","").zfill(4)
				l = bin(j).replace("0b","").zfill(4)
				final = k+l
				final = doc(final)
				final = final[::-1]
				final = chr(int(final,2)^key)
				return final


def decode(arr):
	decoded_string = ""
	for i in range (0,len(arr),2):
		joining = ""
		if i==len(arr)-1:
			joining = arr[i]
		else:
			j,k = arr[i:i+2]
			joining  = j+k
		decoded_string = decoded_string+sboxs(joining)
	return decoded_string


encoded_str = ""
decoded_str = ""
print("Eyption/Decryption")
print("Choose your option:")
choice = -1
print("press 1 for encryption")                   
print("press 2 for decryption")
print("press 3 to exit")

"""file handeling code for decoding check if file exist and it is not empty"""
while(1):
	print("inside while")
	choice = int(input("enter"))
	print(choice)

	if choice==1:
		print("you have pressed 1")
		#call encryption function
		encoded_str = encode(data)
		print(encoded_str)

	elif choice==2:
		#call decryption function
		if len(decoded_str)==0:
			print("encode the string first then decode!! try again!!")
		else:
			decoded_str = decode(decoded_str)
			print(decoded_str)
			
	elif choice==3:
		break
	else:
		print("entered wrong choice!!try again!!")




"""
print()
print(decoded_string)"""
                    











