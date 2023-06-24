

def cypher_message(message):  # Defining a function to cypher a message
    cyphered_message = ""  # Initialize an empty string to store the cyphered message
    
    for char in message:  # Iterating over each character in the input message
        
        if char.isalpha():  # Checking if the character is alphabetic
            unicode_value = ord(char)  # Converting the character to its Unicode value
            
            if char.islower():  # Checking if the character is lowercase
                cypher_value = ((unicode_value - ord('a') + 15) % 26) + ord('a')  # Applying cypher logic for lowercase letters
            
            else:
                cypher_value = ((unicode_value - ord('A') + 15) % 26) + ord('A')  # Applying cypher logic for uppercase letters
            cyphered_message += chr(cypher_value)  # Convert the cypher value back to a character and add it to the cyphered message
        
        else:
            cyphered_message += char  # Keeping non-alphabetic characters unchanged in the cyphered message
    
    return cyphered_message  # Returning the cyphered message

message = "Hello world! Welcome to cyphers." # Testing the function with a message

cyphered_message = cypher_message(message)  # Calling the cypher_message function

print("\n Encoded message: ", cyphered_message)  # Printing the cyphered message

print("\n Plain text message: ", message)  # Printing the original plain text message

