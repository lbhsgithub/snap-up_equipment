# snap-up_equipment
#### 2019.4.8 - 2019.4.12 part-time  
**Reason**: I need to use X-ray CT to do my master project, while there is only one machine and it must be reserved in the website. After experenced several times failure in competing with others APM, I notice that the verification code ![](https://github.com/lbhsgithub/snap-up_equipment/blob/master/code.jpeg) of this website is very simple. Then I got the idea.
- main idea
    - Website identifies me via *cookie*.
    - All I need is to get verification code and post it.
- get verification
    - Requests.get and save
    - Identify verification code (image → numbers/letters)
        - Image process. Many advanced method can be used to process. Notice that there is a significant difference between
        background color and foreground color, I simply us *Photoshop* to find a proper threshold and realize it in *python*.
        - Identify. Just use pytesseract.py (need configuration)
- auto post in one day
    - Logic operation in time, post at the precise time.
- handle result
    - Need further post sometimes. Read source code of website and find what else need to do.
