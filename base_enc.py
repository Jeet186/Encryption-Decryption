import base64

def base_enc(data):
	encoded_data= base64.b64encode(data.encode())
	return encoded_data

if __name__== "__main__":
	data = input("Enter data to be Encode: ")
	print("Encoded data:", base_enc(data))