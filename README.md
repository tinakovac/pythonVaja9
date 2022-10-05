# pythonVaja9
Conditions and loops

### Homework 9.1: Unit converter
Create a program that converts units. More specifically, kilometers into miles.

The program greets user and describes what's the purpose of the program.
The program asks user to enter number of kilometers.
User enters the amount of kilometers.
The program converts these kilometers into miles and prints them.
The program asks user if s/he'd want to do another conversion.
If yes, repeat the above process (except the greeting).
If not, the program says goodbye and stops.

The program should constantly run as long as the user would want to do conversions.

***

### Homework 9.2: FizzBuzz
User enters a number between 1 and 100
FizzBuzz program starts to count to that number (it prints them in the Terminal). In case the number is divisible with 3, it prints "fizz" instead of the number. If the number is divisible with 5, it prints "buzz". If it's divisible with both 3 and 5, it prints "fizzbuzz".

Example:
```python
Select a number between 1 and 100
16

1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
```

A tip for this project:

How to find a division remainder

If a division remainder is 0, that means some number is divisible with another (without remainder).

Example:
```python
print(15 % 5)
print(15 % 4)
```
15 is divisible with 5, so the remainder is 0. But 15 is not divisible with 4, so the remainder is not 0.

***

### Homework 9.3: Make string lowercase
Sometimes you'd like to make some string lowercase. For example, you have a string like this:
```python "Today Is A BeautiFul DAY" ```
And you'd like to make it like this:
```python "today is a beautiful day" ```

There is a very nice solution in Python to do this. Use Google search and find out how to do it.
 
 ```Where would this come handy? For example if you ask user "Would you like to continue (yes/no)?", the user might respond: "yes", "Yes", "YES" or even "YeS". In this case, changing your user's response into lowercase letters would be very helpful in your if-else statement.```
