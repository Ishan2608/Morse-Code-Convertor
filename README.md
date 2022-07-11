<h1> Morse Code Converter </h1>
<p> This simple scripting program written in python. It converts english message to morse code and vice-versa. </p>

<div>
  <img src = "./Morse_Code_Converter.JPG" alt="Code Output">
</div>

<h1> Step 1: Create a Dictionary of Morse Codes </h1>
<p>
  Create a global variable, which is a dictionary. The key:value pair is 'letter':'morse code' and 'digit':'morse code'. 
  We will use it to convert english letters and digits to their morse code equivalents and morse codes to their english letter or digit equivalents.
</p>

<h1> Step 2: Define a Function of Morse Code Conversion </h1>
<p>
  First we ask user if he wants to use converter or not, if he want to, we call the converter function. 
  If the user does not want to, we quit the program. We also intercept the possibility of user entering an invalid response, so we quit in that case also.
</p>

<h1> Step 3: Ask User for Input </h1>
<p>
  Now, define the function logic. Start by asking user what he wants to do? 'Encrypt' a message or 'Decrypt' a message. Then ask user to input the message.
  Do this using input function with <string>.lower() method to convert message to lower case to be able to compare against the dictionary's keys.
</p>

<h1> Step 4: Diving the features of the Function </h1>
<p> 
  Our function has tow features. First, it can encrypt a message, second, it can decrypt a message. These are divided using if-elif-else statements.
  One block to handle encoding, other to handle decoding, and last one to handle invalid user choice.
</p>

<h1> Step 5: Encryption Logic </h1>
<p> 
  Iterate over user string, append each character to a list if it is not a key in the morse_code dictionary. 
  If the character is a key in that dictionary, append the value of that key.
  Output a string using " ".join(output)
</p>

<h1> Step 6: Decryption Logic </h1>
<p> 
  Iterate over user string. Append each character to a string, <b> word </b>, if the character is not a blank space, i.e., " ". 
  If it is, append the word to message_array list, then empty the word back to empty string, since the presence of a blank space signifies the start of a new word.
  We cannot do this for every blank space as the output of encrypted mesage, which we copy has 3 blanks between words, so we also need to check for that.
  If we are at a blank space and next is also a blank space, we don't append. We also check if previous character was not a blank space, if it wasn't, then we append.
  If we have reached the last character, we again append the word. <br>
  We iterate over the message_array list, append the key from morse code dictionary for that value in morse code dictionary. 
  Append blank space if we detect blank space.
</p>
