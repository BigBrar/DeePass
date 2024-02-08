# import modules
import string
import random
import rsa


def create_pass(user_input):
# store all characters in lists 
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)


    # Ask user about the number of characters
    # user_input = input("How many characters do you want in your password? ")


    # check this input is it number? is it more than 8?
    while True:

        try:

            characters_number = int(user_input)

            if characters_number < 8:

                print("Your number should be at least 8.")

                user_input = input("Please, Enter your number again: ")

            else:

                break

        except:

            print("Please, Enter numbers only.")

            user_input = input("How many characters do you want in your password? ")


    # shuffle all lists
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)


    # calculate 30% & 20% of number of characters
    part1 = round(characters_number * (30/100))
    part2 = round(characters_number * (20/100))


    # generation of the password (60% letters and 40% digits & punctuations)
    result = []

    for x in range(part1):

        result.append(s1[x])
        result.append(s2[x])

    for x in range(part2):

        result.append(s3[x])
        result.append(s4[x])


    # shuffle result
    random.shuffle(result)


    # join result
    password = "".join(result)
    print("Strong Password: ", password)
    return password



#def encrypt_pass(username):

# generate public and private keys with 
# rsa.newkeys method,this method accepts 
# key length as its parameter
# key length should be atleast 16
# publicKey, privateKey = rsa.newkeys(512)

# # this is the string that we will be encrypting
# message = "hello geeks"

# # rsa.encrypt method is used to encrypt 
# # string with public key string should be 
# # encode to byte string before encryption 
# # with encode method
# encMessage = rsa.encrypt(message.encode(), 
# 						publicKey)

# print("original string: ", message)
# print("encrypted string: ", encMessage)

# # the encrypted message can be decrypted 
# # with ras.decrypt method and private key
# # decrypt method returns encoded byte string,
# # use decode method to convert it to string
# # public key cannot be used for decryption
# decMessage = rsa.decrypt(encMessage, privateKey).decode()

# print("decrypted string: ", decMessage)
