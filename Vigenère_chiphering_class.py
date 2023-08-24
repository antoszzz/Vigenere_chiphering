'''One very simple type of encryption is the Caesar cipher. In order to encrypt a message using 
the Caesar cipher, each letter in the message is replaced by the letter that is a set number of 
places down the alphabet. 
For example, if a message is encrypted using the Caesar cipher with a 2-shift, the letters in the 
message would be transformed as follows: 
Using this cipher, we could encrypt the message "hello" to "jgnnq". Example 9.2 in the book 
shows how to implement this cipher in Java. 
An extension to the Caesar cipher that was thought to be unbreakable is the Vigenère cipher. In 
this cipher, each letter is shifted by a different amount. This cipher uses a “key," which consists 
of a number for each letter in the message that specifies how much to shift each letter by. 
For example, if the message is "keyboard" and the key is 16458524, the message would be 
encrypted as "lkcgwfth". 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
Your task is to code the Vigenère cipher in Java. You should have one method to encrypt a 
message and one to decrypt a message. 
The method to encrypt a message should: 
• Accept a message as an argument. You may assume the message is all lowercase letters. 
• Create a key by creating an array that has the same length of the message and filling it 
with random values 
• Shift each letter in the message by the corresponding amount in the key. Spaces should 
be left unchanged. 
• Print the message and the key. 
The method to decrypt a message should: 
• Accept a message and a key as arguments. 
• Decrypt the text by shifting each letter in the message by the corresponding amount in 
the key. 
• Print the resulting message'''
import random
def alphabet(chr1=65,chr2=91,chr3=97,chr4=123):
        symbols = list(map(chr,range(chr1,chr2)))
        list1=list(map(chr,range(chr3,chr4)))
        symbols = symbols+list1
        return symbols

class crypting():
    def __init__(self, text='b.',key=''):
        self.dic = alphabet(0,0,97,123)
        self.message = text.lower()
        self.key = key

    def encrypt(self):
        
        key = []
        answer = []
        for i in range(len(self.message)):
            key.append(random.randrange(1,10))
        key_id = 0
        for i in self.message:
            id = 0
            for j in self.dic:
                if i == j:
                    break
                id += 1
            if id == len(self.dic):
                answer.append('-')
            elif id+key[key_id] > len(self.dic)-1:
                a  = id+key[key_id] - len(self.dic)
                answer.append(self.dic[a])
            else:
                a = id+key[key_id]
                answer.append(self.dic[a])
            key_id += 1
        return [''.join(answer), ''.join(map(str,key))]
    def decrypt(self):
        key_id = 0
        answer=[]
        for i in self.message:
            id = 0
            for j in self.dic:
                if i == j: break
                id += 1
            if id == len(self.dic):
                answer.append(i)
            elif id-int(self.key[key_id]) < 0:
                a  = id-int(self.key[key_id]) + len(self.dic)
                answer.append(self.dic[a])
            else:
                a = id-int(self.key[key_id])
                answer.append(self.dic[a])
            key_id += 1
        return ''.join(answer)
def main():
    a = input('Put the text to encrypt:')
    c = crypting(a)
    b=c.encrypt()
    print(f'Original message: {a}\nEncrypted message: {b[0]}\nDecryption key: {b[1]}')
    c= crypting(b[0],b[1])
    print(f'Decrypted message: {c.decrypt()}')

if __name__=='__main__': main()
