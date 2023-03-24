#returns max between 3 numbers
def Q_2_a(a,b,c):
    return (max(a,b,c))

#returns the revered string
def reverse(my_string):
    reversed_string= my_string[::-1]
    return reversed_string

#returns a list of the lengths os the strings in the original list
def Q_2_c(word_list):
    len_list= [len(word) for word in word_list]
    return(len_list)

if __name__ == "__main__":
    max_num=Q_2_a(10,20,50);
    print(str(max_num))
    my_reversed_string=reverse("I am testing")
    print(my_reversed_string)
    my_len_list=Q_2_c(["hi", "hello", "helloworld", "hello world"])
    print(str(my_len_list))