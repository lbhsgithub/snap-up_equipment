# snap-up_equipment
#### 2019.4.8 - 2019.4.12 part-time  
**Reason**: I need to use X-ray CT to do my master project, while there is only one machine and it must be reserved in the website. After experenced several times failure in competing with others APM, I notice that the verification code ![](https://github.com/lbhsgithub/snap-up_equipment/blob/master/code.jpeg) of this website is very simple. Then I got the idea.
- main idea
    - website identifies me via *cookie*.
    - all I need is to get verification code and post it.
- get verification
    - requests.get and save
    - identify verification code (image → numbers/letters)
        - Image process. Many advanced method can be used to extract the effective information. Notice that there is a significant difference between
        background color and foreground color, I simply us *Photoshop* to find a proper threshold and make it in *python*.==(图)==
        - 

- auto in a day
