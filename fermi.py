## step 1
original_number = '123'
## create infinite while loop

while True:
## step 2 and step 6
  guess_number = (str(input("Enter a Three digit  number :")))
  output = []

## step 3 and step 4 (use continue statement)
  if len(original_number) != len(guess_number) :
    continue
    print('invaild input')
  else:
    print('vaild input')
  if len(set(guess_number)) != len(original_number):
         print("Duplicate number", i)
         continue

## step 5 (use break statement for winning condition)
  if guess_number == original_number:
      print("Fermi")
      print("You Win")
      break
## step 7
  for j  in range(len(guess_number)):
    if guess_number[j] == original_number[j]:
       output.append('Fermi')
    elif guess_number[j] in original_number:
      output.append('Pico')
## step 8
  output_string = output
## step 9
  if 0 == len(output):
    print(output)
  else:
    print(output_string)