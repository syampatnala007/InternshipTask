# InternshipTask


This website is for printing the contents of the file.

There are 4 files in the project. (file1.txt,file2.txt,file3.txt,file4.txt)

To display contents of the file we have to type **localhost:5000/?file=<file_name>&start_line=<Starting_line_number>&end_line=<Ending_line_number>** .


Here,
  **<file_name>** represents the name of file. (For ex: file1.txt)
  
  **<Staring_line_number>** represent an integer in which the file will be displayed from that line number. (For ex: 10)
  
  **<Ending_line_number>** represent an integer in which the file will be displayed upto that line number. (For ex: 30)
  
  (Note:- Here ***start_line*** and ***end_line*** are optional and if no file name is given then by default file1.txt contents will be displayed.)
  
  
  ***Sample link:***
    localhost:5000/?file=file1.txt&start_line=10&end_line=20
    
  ***Output:***
    ***File :- file1.txt***
    
      10: Dog is fighting for coffee while Merry is petting feather.
      
      11: Cat is meowing for coffee while Frodo is boiling matrass.
      
      12: Sam is kissing egg while Sam is biting egg.
      
      13: Tom is fighting for matrass while Frodo is hugging egg.
      
      14: Jeniffer is chewing at tea while Cat is barking at tea.
      
      15: Bill is boiling fish while Jeniffer is meowing for fish.
      
      16: Spotty is meowing for fish while Frodo is shouting at tea.
      
      17: Frodo is chewing at fish while Grandfather is fighting for meat.
      
      18: Merry is fighting for coffee while Dog is shouting at coffee.
      
      19: Dog is hugging pillowcase while Uncle Sam is petting egg.
      
      20: Frodo is kissing meat while Cat is meowing for mug.
      
      

**Tools Used:-**


 In this project I had used the Python language and worked with files using ***with-open*** file handling mechanism.
 
 I've made some conditions to play with contents in the file for getting contents from a starting line to ending line or the total content of the file.
 
 I've used GET method to get the values from the URL directly and display the contents of the file in the website designed by using Flask.
 
 Different types of exception statements had been given in the ***app.py*** file to handle the exceptions caused after entering the URL.
 
 
