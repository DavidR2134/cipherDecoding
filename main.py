import string

def atbash(cipher):
	alphabet = ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	reverse_alphabet = ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	reverse_alphabet.reverse()

	c = list(cipher)
	decoded = []

	for letter in c:
		if letter in alphabet:
			x = alphabet.index(letter)
			decoded.append(reverse_alphabet[x])
		else:
			decoded.append(letter)
	d = "".join(decoded)

	return d

def caesar(cipher):
	alphabet = string.ascii_uppercase
	key = int(input("Please enter a numerical key for the Caesar Cipher\n> "))
	decoded = ""
	for letter in cipher:
		if letter in alphabet:
			position = alphabet.find(letter)
			new_position = (position - key) % 26
			new_character = alphabet[new_position]
			decoded += new_character
		else:
			decoded += letter

	return decoded

def a1z26(cipher):
	alphabet = string.ascii_uppercase
	c = cipher.split(" ")
	decoded = ""

	for number in c:
		n = number.split("-")
		for number in n:
			decoded += alphabet[int(number)-1]

		decoded += " "

	return decoded

def viginere(cipher, key):
	pass

def menu():
	print("Welcome to the cipher decoder!")
	print("=" * 50)
	print("\n1) ATBASH Cipher\n2) Caesar Cipher\n3) A1Z26\n4) Quit")

def main():
	#Season 1 Intro: VWDQ LV QRW ZKDW KH VHHPV - STAN IS NOT WHAT HE SEEMS
	#Season 1 EP 2: QHAW ZHHN: VHWXUQ WR EXWW LVODQG - NEXT WEEK: RETURN TO BUTT ISLAND
	#Season 1 EP 3: KH'V VWLOO LQ WKH YHQWV - HE'S STILL IN THE VENTS
	#Season 1 EP 4: FDUOD, ZKB ZRQW BRX FDOO PH? - CARLA, WHY WONT YOU CALL ME?
	#Season 1 EP 5: RQZDUGV DRVKLPD! - ONWARDS AOSHIMA!
	#Season 1 EP 6: PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH. - MR. CAESARIAN WILL BE OUT NEXT WEEK. MR. ATBASH WILL SUBSTITUTE.
	#Season 1 EP 7: KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!" - PAPER JAM DIPPER SAYS: "AUUGHWXQHGADSADUH!"
	#Season 1 EP 8: V. KOFIRYFH GIVNYOVB - E. PLURIBUS TREMBLEY
	#Season 1 EP 9: 

	menu()

	choice = int(input("\n\nPlease make a selection: "))
	cipher = input("Please enter your cipher: ")

	if choice == 1: 
		print(atbash(cipher))
	elif choice == 2:	
		print(caesar(cipher))
	elif choice == 3:
		print(a1z26(cipher))

if __name__ == "__main__":
	main()
