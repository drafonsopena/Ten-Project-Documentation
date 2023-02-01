This Text to Speech Converter was completed 16-01-23 By @drafonsopena.
Using python3.9, Pycharm, Thonny, DataFlair.

If you are willing to edit it or make atomic changes please:
Respect the spaces or indentations; since the project is still under developed. Why not change it any way?

It is a great way to get more used to the python language and the TKinter library along with gtts, and playsound.
It is a beginner's project with few explanations. Go to [DataFlair](https://data-flair.training/blogs/alarm-clock-python/) for the original source code and some extra explanations.

***Have fun and Happy coding.***



# Text-to-Speech Converter (16-01-2023)

The sixth project I developed is a Text to Speech that can convert any English text to speech/sound. After the text is converted to speech we save a mp3 file (the copy of the text we converted). It is on version 0.1.06 with the size of 2.7 Kb.

> **Utility or why Develop:** This project was complicated to make because currently it does not accept large sums of text and had some difficulties finding the recommended modules, that aside I say that it is useful to teach people how to read or write.


> **Libraries and Prerequisites:** For the Text to Speech we used TKinter, gtts a library made by Google to aid in the text to speech conversion, and playsound. This project had to be developed used python 3.10 because 3.9 was giving errors regarding  the library gtts, and the funny thing is that while the program is running we can not convert another text to speech (we have to close it and run it again) because our speech is saved as an mp3 file (we cannot have files with the same name but we can override it), so make sure to open, convert, close, open again and convert.


> **Future Changes:** In a later version I am thinking like *“PDF PDF PDF READER”*, which is a good idea specially when it comes to books and other long articles. But before the PDF idea to happen we need to increase the number of characters the program can scan through; allow the user to convert text to speech without having to close the program; add more languages... then *“PDF PDF PDF READER”*.


<details><summary>Pictures</summary>
  
  **Picture 1: Text to Speech main window**
  
  ![texttospeechOne](https://user-images.githubusercontent.com/72225601/216103811-09885683-bb64-4a25-bd95-ac1d52981aca.png)

  **Picture 2: Text to Speech entering input
  
  ![texttospeechTwo](https://user-images.githubusercontent.com/72225601/216104081-358a6ccc-7edd-46a3-a6eb-e8b3a9239ffb.png)
  
  **Picture 3: Text to Speech output**

  ![texttospeechFour](https://user-images.githubusercontent.com/72225601/216104828-a8c8cae0-aae1-46b2-86b9-5d51f76c808c.png)

  
</details>

---


<details> <summary><strong>Error Explanation:</strong></summary>

  
**Picture 4: Error output**
  
  ![texttoSpeechError](https://user-images.githubusercontent.com/72225601/216105446-b4af957f-0c31-4dde-876a-a94a7354f0f8.png)

 
<details> <summary>This means that it failed to connect to the internet/google server.</summary>
  
```
gtts.tts.gTTSError: Failed to connect. Probable cause: Unknown

```

</details>
  
<details> <summary>This is the name of the file each time we press the “Play” button.</summary>

```
speech.save("spoken.mp3")
  
```  
 </details>
  
<details> <summary>This is the error we get when we try to convert a text again without closing the program.</summary>

```
with open(str(savefile), "wb") as f:
PermissionError: [Errno 13] Permission denied: 'spoken.mp3' 
  
```
  </details>
  
  
</details>


