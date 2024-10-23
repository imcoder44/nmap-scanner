#! /usr/bin/bash
#echo "Hello"  #echo use to print

# comment

#SYSTEM VARIBLES
#echo $BASH 
#echo $BASH_VERSION
#echo $HOME
#echo $PWD

#USER-Define VARIABLES
#name=Markecho The name is $name
#variable name should not start with the number
#1val=12echo It will print something else $1valval=12
#echo value is $val

#READ-USER INPUT
#echo "Enter full name: "
#read first middle  last
#echo "Name is: $first $middle $last"

#read -p 'username : ' user_val   # -p use for print on same line
#read -sp 'password : ' pass_val  # -s use for silent or to keep hidden
#echo
#echo "Username : $user_val"
#echo "Password : $pass_val"

#echo "Enter numbers : "
#read -a num
#echo ${num[0]} , ${num[1]}

#echo "Where do you live?"
#read                   
#when variable is not define it will use default variable 'REPLY'
#echo "place : $REPLY" 

#PASS ARGUMENTS
#echo $1 $2 $3 ' > echo $1 $2 $3 '
#echo $0 $1 $2 $3 ' > echo $1 $2 $3 '

#args=("$@")  #@ is default variable to make array of the argument

#echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}

#echo $@  #to print value in the array of args without using above statement

#echo $# # to print number of argument 

#IF-STATEMENT (if then, if then else, if elif else)

#integer comparison
# -eq : is equal to -> if ["$a" -eq "$b"]
# -ne : is not equal to -> if ["$a" -ne "$b"]
# -gt : is greater than to -> if ["$a" -gt "$b"]
# -ge : is greater than or equal to -> if ["$a" -ge "$b"]
# -lt : is less than -> if ["$a" -lt "$b"]
# -le : is less than or equal to -> if ["$a" -le "$b"]
# < : is less than -> (("$a" < "$b"))
# <= : is less than equal to -> (("$a" <= "$b"))
# > : is greater than -> (("$a" > "$b"))
# >= : is greater than equal to -> (("$a" >= "$b"))

#string comparision
# = : is equal to -> if ["$a" = "$b"]
# == : is equal to -> if ["$a" == "$b"]
# != : is not equal to -> if ["$a" != "$b"]
# < : is lss than, in ASCII alphbetical order -> if [["$a" < "$b"]]
# > : is greater than, in ASCII alphabetical order -> if [["$a" > "$b"]]
# -z : string is null, that is, has zero length

# count=10
# word="abc"

# if [ $count -eq 10 ]; then #space after bracket is important it's case sensetive
#   echo "condition is true"
# elif [ "$word" == "abc" ]; then
#   echo "word is matched"
# else
#   echo "not correct"
# fi 

#FILE_TEST_OPERATOR
#to test wheather the is character special file and block special file 
#echo -e "Enter the name of the file :  \c"
# -e is used for enable options like \c  
#  \c is used to keep cursor on same line
#read file_name

# if [ -e $file_name ] # -e is used to check weather file exist or not
# then
#   echo "$file_name found"
# else
#   echo "$file_name not found"
# fi

# if [ -f $file_name ] # -f is used for check wheather it's a regular file or not and it's exist or not
# then 
#   echo "$file_name is a file"
# else 
#   echo "$file_name is not a file"
# fi

# if [ -d $file_name ] # -d check directory
# then
#   echo "$file_name found"
# else 
#   echo "$file_name not found"
# fi

# character special file is normal which contain some text and data
# block special file is a binary file, picture or video file
# -b for block special
# -c for character special
# -s check wheather file is empty or not
# -r check wheather file has read permission
# -w check weather file has write permission
# -x check weather file has execution permission

#HOW TO APPEND OUTPUT TO THE END OF THE TEXT FILE
# echo -e "Enter the name of the file : \c"
# read file_name

# if [ -f $file_name ]
# then
#   if [ -w $file_name ]
#   then
#     echo "Type some text data. To quit press ctrl+d."
#     cat >> $file_name
#   else
#     echo "The file do not have write permissions"
#   fi
# else
#   echo "$file_name not exists"
# fi

#LOGICAL OPERATOR - AND
# age=25
# if [[ "$age" -gt 18 && "$age" -lt 30 ]]
# then 
#   echo "valid age"
#   else
#   echo "age is not valid"
# fi

# # -a for AND operator, for single box
# if [[ "$age" -gt 18 && "$age" -lt 30 ]]
# then 
#   echo "valid age"
#   else
#   echo "age is not valid"
# fi

# if [ "$age" -gt 18 ] && [ "$age" -lt 30 ]
# then 
#   echo "valid age"
#   else
#   echo "age is not valid"
# fi

#OR-operator


