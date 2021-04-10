## We are team Coffee Cup!

Team members:

- Whitney Svoboda (PM)
- Taylor Lightbourne
- Patrick Groves
- Jorge Gonzalez

The game starts by asking the user's name. The game assigns this name to the warrior.

![welcome](https://user-images.githubusercontent.com/78281930/112057919-e52f4d80-8b27-11eb-8b7a-d3090dc0cf4a.PNG)

The game then has the user roll a magic dice! The magic dice uses the randint function to produce a number from 1 to 6. The result of the dice roll is multiplied by 10 and is assigned to the user as health points. The troll also rolls and gets a number of health points using the same method.

![Screenshot 2021-04-10 181526](https://user-images.githubusercontent.com/78281930/114286971-d18d4d80-9a28-11eb-895c-a5123469d47f.png)

The user decides if they want to fight, do nothing, or run away. 

![battlescreen](https://user-images.githubusercontent.com/78281930/114286990-fed9fb80-9a28-11eb-8348-0f004e7b385f.png)

If the user decides to fight, the user inflicts an amount of damage and the troll also inflicts an amount of damage. The strength of the attack is also determined by the randint function. The warrior can inflict a possible range of 0 to 10 points. The troll can inflict a possible range of 0 to 8 points.

![fight](https://user-images.githubusercontent.com/78281930/112056127-a7c9c080-8b25-11eb-9245-0223fd151b1d.PNG)

It is also possible one or both of the attacks misses. A life status bar is shown after every turn.

![doNothing](https://user-images.githubusercontent.com/78281930/112056169-b617dc80-8b25-11eb-80d6-2aa09da2f83b.PNG)

The game continues until either the user or the troll dies. There is a victory screen and a death screen. If the user ever chooses to run away, the game ends.

![victory](https://user-images.githubusercontent.com/78281930/112056202-be701780-8b25-11eb-84e3-358ddd9b6a05.PNG)
![death](https://user-images.githubusercontent.com/78281930/112056230-c62fbc00-8b25-11eb-96ec-e9be6f892e85.PNG)
