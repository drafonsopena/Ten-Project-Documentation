I made a  forloop script that needs fixing, it’s silly but please solve it if you can or if you have the time to waste, you just need to remove/include a break, a “\n” or a  \n.

Please answer riddle.md if you want. Else [click here](https://duckduckgo.com).

# No \n between us:
> Have a break before you \n , to run you need an IDE and a forloop but  you  also need to break the number of  “\n’s” present in the sentence. Please dont break your system. If your computer crashes blame it on the break not found and not on the “\n” taken from the sentence.

**NOTE: DONT RUN WITHOUT TRYING IT IN YOUR HEAD. BEACUSE THE OUT COME IS A PERFECT break.**
> This is **NOT** what we want:

![testOne](https://user-images.githubusercontent.com/72225601/216041695-de2a1ec6-8ed0-49a5-89db-ba79dde8117f.png)

> This in **NOT** what we want:

![result_TestOne](https://user-images.githubusercontent.com/72225601/216040458-8c729e11-5de1-4dd7-b6e4-af3c700256cf.png)

> This defenetally is what we **DO NOT** want, so please break the forloop:

![loopBreaker](https://user-images.githubusercontent.com/72225601/216042676-a6a02b74-df7b-40bb-8734-97bbfa27e7c3.png)
---

If you want to break, reduce “\n” than  \n  for real:

The outcome needs to be without any breaks “\n”.

<details><summary>Problem</summary>
  
<p>
  
## Use the code below to start the riddle:

```
# there is something missing
Guido = ["\n", "Thank you for Python"]

hallo = [Guido, "'Zeg Guido dat ik dag zei.'"]
hello = ["""

"Ciao",

"Hola",

"Ola",

"Ciao"""]
for x in hello:
     hello += hallo
     but_hello_is_also_equal_to_x = hello
     print(but_hello_is_also_equal_to_x)
```

  </p>
  
</details>

> If you want the correct one try at least to reach to this output:

![helloGuido](https://user-images.githubusercontent.com/72225601/216040130-e64cd2ff-6c35-4b35-8449-7618f8f57227.png)
---

<details><summary>Answer</summary>
<p>
  
***To  “\n” a  forloop we must \n with break.***

> This is the answer. A “\n” was left because now we know how to  break a forloop with the right \n.
    
```
Guido = ["\n", "Thank you for Python"]
hallo = [Guido, "'Zeg Guido dat ik dag zei.'"]
hello = [""""Ciao","Hola","Ola","Ciao"""]
for x in hello:
hello += hallo
but_hello_is_also_equal_to_x = hello
print(but_hello_is_also_equal_to_x)
break
```
 </p>
</details>





