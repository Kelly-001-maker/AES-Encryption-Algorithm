

#defining a 17 by 17 matrix to represent the S_Box
my_S_Box_List=[["","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"],
["0","63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"],
["1","ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"],
["2","b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"],
["3","04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"],
["4","09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"],
["5","53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"],
["6","d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"],
["7","51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"],
["8","cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"],
["9","60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"],
["a","e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"],
["b","e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"],
["c","ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"],
["d","70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"],
["e","e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"],
["f","8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"]]


my_Rounds_List =["01","02","04","08","10","20","40","80","1b","36"]

#A list that i will use to dertimine the row and column indexes of my search
my_index_determiner_list=["","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

#S_box search function
def my_s_box_search_Function(hex_val_list):
    my_hex_list = hex_val_list;
    my_result_list = [];
    for element in my_hex_list:
        my_string = element;
        my_string_list=[];
        for character in my_string:
            my_string_list.append(character)

        row_index_to_serch = my_index_determiner_list.index(my_string_list[0]);
        column_index_to_search=my_index_determiner_list.index(my_string_list[1])
        my_search = my_S_Box_List[row_index_to_serch][column_index_to_search];
        my_result_list.append(my_search);

    return my_result_list;


#Function to shift values to the left by one
def rotword_function(fourth_word_list):
    rotword_List = [];
    rotword_List.append(fourth_word_list[1])
    rotword_List.append(fourth_word_list[2])
    rotword_List.append(fourth_word_list[3])
    rotword_List.append(fourth_word_list[0])
    return  rotword_List;

def subword_Function(rotwordresult_List):
    #Replacing with s box values
    return my_s_box_search_Function(rotwordresult_List)


def get_full_round_constant_word(round_index):
    round_word = ["00"] * 4
    round_word[round_index] = (my_Rounds_List[round_index])
    return round_word;



#Function to get first word of a given encryprion key
def obtain_first_key_word(key_hex_rep_list):
    first_key_word_List = []
    cond=0;
    while cond < 4:
        first_key_word_List.append(key_hex_rep_list[cond])
        cond=cond+1;

    return first_key_word_List

#Function to get second word of a given encryprion key
def obtain_second_key_word(key_hex_rep_list):
    second_key_word_List = []
    cond=4;
    while cond < 8:
        second_key_word_List.append(key_hex_rep_list[cond])
        cond=cond+1;

    return second_key_word_List

#Function to get third word of a given encryprion key
def obtain_third_key_word(key_hex_rep_list):
    third_key_word_List = []
    cond=8;
    while cond < 12:
        third_key_word_List.append(key_hex_rep_list[cond])
        cond=cond+1;
    return third_key_word_List

#Function to get fourth word of a given encryprion key
def obtain_fourth_key_word(key_hex_rep_list):
    fourth_key_word_List = []
    cond=12;
    while cond < 16:
        fourth_key_word_List.append(key_hex_rep_list[cond])
        cond=cond+1;

    return fourth_key_word_List

def get_key_for_expansion_function(key_text):
    my_key_to_expand_list = convert_16bit_text_to_hex(key_text);
    return my_key_to_expand_list;

def Add_Round_Key_Function(my_message_hex_list,my_key_hex_list):
    my_state_array_list = []
    first_msg_word = obtain_first_key_word(my_message_hex_list)
    print("my first msg word is: ", first_msg_word)
    second_msg_word = obtain_second_key_word(my_message_hex_list)
    third_msg_word = obtain_third_key_word(my_message_hex_list)
    fourth_msg_word = obtain_fourth_key_word(my_message_hex_list)

    # Key words
    first_key_word = obtain_first_key_word(my_key_hex_list)
    print("my first key word is: ", first_key_word)
    second_key_word = obtain_second_key_word(my_key_hex_list)
    third_key_word = obtain_third_key_word(my_key_hex_list)
    fourth_key_word = obtain_fourth_key_word(my_key_hex_list)

    state_first_word_msg_bin = convert_hex_bin_Function(first_msg_word)
    state_first_word_key_bin = convert_hex_bin_Function(first_key_word)
    state_first_word_bin = XOR_binary_bits_operation_Function(state_first_word_msg_bin, state_first_word_key_bin)
    state_first_word_hex = convert_bin_to_hex_Function(state_first_word_bin);
    state_first_word_list = Insert_to_a_list(state_first_word_hex);
    for element in state_first_word_list:
        my_state_array_list.append(element)

    state_second_word_msg_bin = convert_hex_bin_Function(second_msg_word)
    state_second_word_key_bin = convert_hex_bin_Function(second_key_word)
    state_second_word_bin = XOR_binary_bits_operation_Function(state_second_word_msg_bin, state_second_word_key_bin)
    state_second_word_hex = convert_bin_to_hex_Function(state_second_word_bin);
    state_second_word_list = Insert_to_a_list(state_second_word_hex);
    for element in state_second_word_list:
        my_state_array_list.append(element)

    state_third_word_msg_bin = convert_hex_bin_Function(third_msg_word)
    state_third_word_key_bin = convert_hex_bin_Function(third_key_word)
    state_third_word_bin = XOR_binary_bits_operation_Function(state_third_word_msg_bin, state_third_word_key_bin)
    state_third_word_hex = convert_bin_to_hex_Function(state_third_word_bin);
    state_third_word_list = Insert_to_a_list(state_third_word_hex);
    for element in state_third_word_list:
        my_state_array_list.append(element)

    state_fourth_word_msg_bin = convert_hex_bin_Function(fourth_msg_word)
    state_fourth_word_key_bin = convert_hex_bin_Function(fourth_key_word)
    state_fourth_word_bin = XOR_binary_bits_operation_Function(state_fourth_word_msg_bin, state_fourth_word_key_bin)
    state_fourth_word_hex = convert_bin_to_hex_Function(state_fourth_word_bin);
    state_fourth_word_list = Insert_to_a_list(state_fourth_word_hex);
    for element in state_fourth_word_list:
        my_state_array_list.append(element)

    return my_state_array_list;


def get_message_and_key_Start_function(message, key):
    my_message_hex_list = convert_16bit_text_to_hex(message);
    my_key_hex_list = convert_16bit_text_to_hex(key);
    #Call for a function of add round key to give a state array result
    state_array = Add_Round_Key_Function(my_message_hex_list,my_key_hex_list)
    return state_array;



#Definition of a function taking a 16 bit text and converts it to hexadecimal;
def convert_16bit_text_to_hex(text):
    #First you put the characters in a list so that you can access each chracter
    my_text_List = [];
    my_text = text;
    for character in my_text:
       my_text_List.append(character);
    #Now you have to take every character and convert to its hexadecimal rep
    my_hex_text_list = [];
    for element in my_text_List:
        hexrep = format(ord(element), "x")
        my_hex_text_list.append(hexrep);

    return my_hex_text_list;


#A function to convert a hexadecimal value to binary
def convert_hex_bin_Function(hex_value_list):
    my_bin_list = [];
    my_list = hex_value_list
    for value in hex_value_list:
         my_hex = value;
         my_hex_bin_string= "{0:08b}".format(int(my_hex, 16))
         for element in my_hex_bin_string:
             my_bin_list.append(element);

    return  my_bin_list;


#A function that converts a binary number to hexadecimal
def convert_bin_to_hex_Function(bin_list):
    my_bin_list=bin_list;
    my_string=""
    for character in my_bin_list:
        my_string=my_string+character
    my_hex_rep= format(int(my_string,2),"x")
    if len(my_hex_rep)==1:
        my_hex_rep = "0"+my_hex_rep
    return my_hex_rep;


#A function for inserting a string of hexadecimal values in a list
def Insert_to_a_list(string):
    my_string=string
    my_new_string_list=["0"]*8;
    length = len(my_string)
    if length < 8:
        mycond=0;
        while mycond < 8:
            if (7-mycond) < length:
                for element in my_string:
                      my_new_string_list[mycond]=element;
                      mycond=mycond+1;
                break;
            mycond = mycond + 1;
        my_string=""
        for element in my_new_string_list:
            my_string=my_string+element;
    my_result_list=[]
    to_append=""
    for element in my_string:
        to_append = to_append + element;
        if len(to_append) == 2:
            my_result_list.append(to_append)
            to_append = "";

    return my_result_list;



#The XOR operation function returns the result of the two binary list in bin
def XOR_binary_bits_operation_Function(msg_bin_list,key_bin_list):
    length = len(msg_bin_list);
    my_msg_list=msg_bin_list;
    my_key_list=key_bin_list;
    my_xor_result_list = [];
    while_xor_cond = 0;
    while while_xor_cond<length:
        if my_msg_list[while_xor_cond]==my_key_list[while_xor_cond]:
            my_xor_result_list.append("0")
        else:
            my_xor_result_list.append("1")
        while_xor_cond=while_xor_cond+1;
    return my_xor_result_list;

#full g function returning a 32 bits binary list
def full_g_Function(forth_word_list,round_index):
    result1 = rotword_function(forth_word_list)
    result2 = subword_Function(result1)
    result3=convert_hex_bin_Function(result2)
    round_word = get_full_round_constant_word(round_index)
    round_word_bin = convert_hex_bin_Function(round_word)
    g_result=XOR_binary_bits_operation_Function(result3,round_word_bin);
    return  g_result;

#Full key expansion function
def get_sub_key_From_xpand_Key_Function(key_list,round_index):
    my_Full_Sub_key_list = []
    my_key_list = key_list;
    first_key_word = obtain_first_key_word(my_key_list);
    second_key_word = obtain_second_key_word(my_key_list)
    third_key_word = obtain_third_key_word(my_key_list);
    fourth_key_word=obtain_fourth_key_word(my_key_list)

    #Dealing with first_sub_key_word
    g_result=full_g_Function(fourth_key_word,round_index)
    first_key_word_bin=convert_hex_bin_Function(first_key_word)
    first_sub_key_bin = XOR_binary_bits_operation_Function(g_result,first_key_word_bin);
    first_sub_key_string = convert_bin_to_hex_Function(first_sub_key_bin)
    first_sub_key_word_list=Insert_to_a_list(first_sub_key_string);
    for element in first_sub_key_word_list:
        my_Full_Sub_key_list.append(element)

    # Dealing with second_sub_key_word
    second_key_word_bin = convert_hex_bin_Function(second_key_word)
    second_sub_key_bin = XOR_binary_bits_operation_Function(first_sub_key_bin, second_key_word_bin);
    second_sub_key_string = convert_bin_to_hex_Function(second_sub_key_bin)
    second_sub_key_word_list = Insert_to_a_list(second_sub_key_string);
    for element in second_sub_key_word_list:
        my_Full_Sub_key_list.append(element)

    # Dealing with third_sub_key_word
    third_key_word_bin = convert_hex_bin_Function(third_key_word)
    third_sub_key_bin = XOR_binary_bits_operation_Function(second_sub_key_bin, third_key_word_bin);
    third_sub_key_string = convert_bin_to_hex_Function(third_sub_key_bin)
    third_sub_key_word_list = Insert_to_a_list(third_sub_key_string);
    for element in third_sub_key_word_list:
        my_Full_Sub_key_list.append(element)

    # Dealing with third_sub_key_word
    fourth_key_word_bin = convert_hex_bin_Function(fourth_key_word)
    fourth_sub_key_bin = XOR_binary_bits_operation_Function(third_sub_key_bin, fourth_key_word_bin);
    fourth_sub_key_string = convert_bin_to_hex_Function(fourth_sub_key_bin)
    fourth_sub_key_word_list = Insert_to_a_list(fourth_sub_key_string);
    for element in fourth_sub_key_word_list:
        my_Full_Sub_key_list.append(element)

    return my_Full_Sub_key_list;



def round_byte_substitution_Function(hex_value_list):
    mylist=hex_value_list;
    my_result=my_s_box_search_Function(mylist)
    return my_result;

def round_Shift_Key_Function(sub_bytes_result_List):
    my_shift_Result_List = [];
    my_shift_while_cond = 0;
    append_position = 0;
    while my_shift_while_cond < 16:
        my_shift_Result_List.append(sub_bytes_result_List[append_position])
        append_position=(append_position+5)%16;
        my_shift_while_cond=my_shift_while_cond+1;

    return my_shift_Result_List;

def remove_repeating_elements(list):
    myloopcond = 0;
    change = 0;
    while myloopcond < len(list):
        list_traverse = myloopcond + 1;
        while list_traverse < len(list):
            element_check = list[myloopcond]
            if element_check == list[list_traverse]:
                del list[list_traverse]
                del list[myloopcond]
                list_traverse = myloopcond + 1;
            else:
                list_traverse = list_traverse + 1;

        myloopcond = myloopcond + 1;


    return list;


def convert_to_Full_8_bit_binary_list(bin_list):
    firstcond = len(bin_list)
    if firstcond < 8:
        copy_list = bin_list;
        start_insert_index = 8-len(copy_list)
        my_list = create_Repeating_List_Function(8)
        my_while_cond =0;
        copy_index = 0;
        while my_while_cond < 8:
            if my_while_cond < start_insert_index:
                my_list[my_while_cond]=0;
            else:
                my_list[my_while_cond]=copy_list[copy_index]
                copy_index=copy_index+1;
            my_while_cond = my_while_cond+1;
    else:
        my_list = bin_list;

    return  my_list;


def Mix_columns_Function(full_list):
    my_original_list = full_list;
    my_first_word = obtain_first_key_word(my_original_list)
    my_second_word = obtain_second_key_word(my_original_list)
    my_third_word = obtain_third_key_word(my_original_list)
    my_fourth_word = obtain_fourth_key_word(my_original_list)
    my_full_result_list = [];
    my_full_list_to_use=[my_first_word,my_second_word,my_third_word,my_fourth_word]
    original_cond = 0;
    while original_cond < 4:
        word_list = my_full_list_to_use[original_cond]
        my_standard_matrix_list=[["02","03","01","01"],["01","02","03","01"],["01","01","02","03"],["03","01","01","02"]]
        my_word_result_list=[]
        my_while_cond=0;
        while my_while_cond < 4:
             my_galloid_list = []
             my_standard_matrix = my_standard_matrix_list[my_while_cond]
             to_deal_word=word_list
             my_indexing = 0;
             while my_indexing < 4:
                   val1=convert_hex_bin_4bit_Function(to_deal_word[my_indexing])
                   val2=convert_hex_bin_4bit_Function(my_standard_matrix[my_indexing])
                   my_mult_list=polynomial_multiplication_Function(val1,val2)
                   for element in my_mult_list:
                        my_galloid_list.append(element);
                   my_indexing=my_indexing+1;
             my_removed_repeating_list=remove_repeating_elements(my_galloid_list)
             num_list = my_removed_repeating_list
             my_bin_galloid_list=List_Num_To_List_Bin_Function(num_list)
             num_bin_list=my_bin_galloid_list;
             my_reduced_list=polynomial_Reducing_Function(num_bin_list)
             my_galloid_full_bin = convert_to_Full_8_bit_binary_list(my_reduced_list)
             my_galloid_bin = convert_bin_num_int_bin_num_string(my_galloid_full_bin)
             my_hex_galloid_value=convert_bin_to_hex_Function(my_galloid_bin)
             my_word_result_list.append(my_hex_galloid_value);
             my_while_cond=my_while_cond+1;

        for value in my_word_result_list:
            my_full_result_list.append(value);
        original_cond=original_cond+1;


    return my_full_result_list;


def Remove_List_Starting_Zero_elements(my_list):
    terminate_condition = 1;
    while terminate_condition == 1:
        if my_list[0]==0:
            del my_list[0];
        else:
            terminate_condition=0;
    return my_list;



#This function reduces a polynomial that has a power greater than 7 to base 2
def polynomial_Reducing_Function(irreducable_list):
    first_cond = len(irreducable_list)
    if first_cond > 8:
        new_list_to_reduce = irreducable_list
        galois_result_List = []
        modulo_list = [1,0,0,0,1,1,0,1,1]
        exit_cond = 0;
        count = 0;
        while exit_cond == 0:
            deal_list = new_list_to_reduce
            new_list_to_reduce=Remove_List_Starting_Zero_elements(deal_list)
            if len(new_list_to_reduce)<9:
                break;
            my_cond = 0;
            while my_cond < 9:
                if new_list_to_reduce[my_cond] == modulo_list[my_cond]:
                    new_list_to_reduce[my_cond] = 0
                else:
                    new_list_to_reduce[my_cond ] = 1
                my_cond =my_cond+1;
            count=count+1;
    else:
        new_list_to_reduce = irreducable_list;


    return new_list_to_reduce;



#A function to convert a hexadecimal value to binary
def convert_hex_bin_4bit_Function(hex_value_list):
    my_bin_list = [];
    my_list = hex_value_list
    for value in hex_value_list:
         my_hex = value;
         my_hex_bin_string= "{0:04b}".format(int(my_hex, 16))
         for element in my_hex_bin_string:
             my_bin_list.append(element);

    return  my_bin_list;

def create_Repeating_List_Function(number_of_times):
    my_repeat_List = [0]*number_of_times;
    return  my_repeat_List;

def List_Num_To_List_Bin_Function(number_list):
    my_expand_list = number_list
    my_expand_sorted_list = sorted(my_expand_list, reverse=True)
    exit_length = len(number_list)
    maximum = my_expand_sorted_list[0];
    expanded_binary = create_Repeating_List_Function(maximum + 1);
    prototype_length = len(expanded_binary)
    my_condition = 0;
    insert_var = 0;
    while my_condition < (maximum+1):
        if my_expand_sorted_list[insert_var] == (prototype_length - (my_condition + 1)):
            expanded_binary[my_condition] = 1;
            insert_var = insert_var + 1;
        my_condition = my_condition + 1;
        if insert_var > (exit_length-1):
            break;

    return expanded_binary
def convert_bin_num_int_bin_num_string(bin_num_int_list):
    my_bin_int=bin_num_int_list;
    my_bin_num_string_list=[]
    for element in my_bin_int:
        value_to_append= str(element)
        my_bin_num_string_list.append(value_to_append)

    return my_bin_num_string_list;


def convert_bin_num_string_bin_num_int(bin_num_string_list):
    my_bin_string=bin_num_string_list;
    my_bin_num_int_list=[]
    for element in my_bin_string:
        value_to_append= int(element)
        my_bin_num_int_list.append(value_to_append)

    return my_bin_num_int_list;


#This function is receiving a binary list for multiplication
def polynomial_multiplication_Function(list1,list2):
    bin1=list1
    bin2=list2
    pol_mult_List = [];
    pol_mult_result_List = [];
    #List to store values of positions with one for multiplication in list1
    polbin1_List=[]
    # List to store values of positions with one for multiplication in list2
    polbin2_List=[]
    bin_pol_cond=0;
    while bin_pol_cond < 8:
        if bin1[bin_pol_cond]=="1":
            polbin1_List.append((7-bin_pol_cond));
        if bin2[bin_pol_cond]=="1":
            polbin2_List.append((7-bin_pol_cond))
        bin_pol_cond = bin_pol_cond+1;
    #Now multiply each element in polbin1_List with all elements in polbin2_list
    for value in polbin1_List:
        for element in polbin2_List:
            sum = value+element;
            pol_mult_List.append(sum)

    pol_mult_result_List = remove_repeating_elements(pol_mult_List);

    return pol_mult_result_List



#NB MY MAIN DRIVER TEST STARTS HERE
message ="secretmessagenow"
key="satishcjisboring"
#Call for a function that receives a key in text and returns its hexadecimal represanation
my_key_for_expansion = get_key_for_expansion_function(key)
#A call for a function that receives message text and key texts, and outputs the state array after several operations
#Gotten also fromperforming the xor operatio or add round key

print("my mix columns result is_mix_columns",Mix_columns_Function)
#A call for a function that expands a key to give its sub key
sub_key_1= get_sub_key_From_xpand_Key_Function(my_key_for_expansion,0)
print("My sub key 1 is ",sub_key_1);
def rounds_function(state_result, sub_key_list):
    my_sub_key=sub_key_list
    state_result=state_array
    substitution_byte_result = round_byte_substitution_Function(state_array)
    shift_key_result = round_Shift_Key_Function(substitution_byte_result)
    mix_column_result = Mix_columns_Function(shift_key_result)
    mix_col_list = mix_column_result;
    round_result = Add_Round_Key_Function(mix_col_list,my_sub_key);
    state_round_result =round_result;

    return  state_round_result

def full_AES_Encryption_Function(message_in_text, key_in_text):
    my_key_for_expansion = get_key_for_expansion_function(key_in_text)
    my_key_to_expand=my_key_for_expansion;
    state_array = get_message_and_key_Start_function(message_in_text,key_in_text)
    my_state=state_array
    round_number = 0;
    while round_number < 10:
        sub_key=get_sub_key_From_xpand_Key_Function(my_key_for_expansion,round_number)
        my_sub_key = sub_key;
        round_result = rounds_function(my_state,my_sub_key);
        result = round_result;
        my_state = result;
        my_key_to_expand = my_sub_key;





#my_expand_key_hex_list=get_key_for_expansion_function(key)
#print("My global key list for key expansion is : ",my_expand_key_hex_list);



