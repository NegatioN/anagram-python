f = open("word_list.txt", "r")
all_words = [word.strip() for word in f.readlines()]

words = "complicated"

a_counter = 0
b_counter = 0
c_counter = 0
d_counter = 0
e_counter = 0
f_counter = 0
g_counter = 0
h_counter = 0
i_counter = 0
j_counter = 0
k_counter = 0
l_counter = 0
m_counter = 0
n_counter = 0
o_counter = 0
p_counter = 0
q_counter = 0
r_counter = 0
s_counter = 0
t_counter = 0
u_counter = 0
v_counter = 0
w_counter = 0
x_counter = 0
y_counter = 0
z_counter = 0

for letter in words:
    if letter == "a":
        a_counter += 1
    elif letter == "b":
        b_counter += 1
    elif letter == "c":
        c_counter += 1
    elif letter == "d":
        d_counter += 1
    elif letter == "e":
        e_counter += 1
    elif letter == "f":
        f_counter += 1
    elif letter == "g":
        g_counter += 1
    elif letter == "h":
        h_counter += 1
    elif letter == "i":
        i_counter += 1
    elif letter == "j":
        j_counter += 1
    elif letter == "k":
        k_counter += 1
    elif letter == "l":
        l_counter += 1
    elif letter == "m":
        m_counter += 1
    elif letter == "n":
        n_counter += 1
    elif letter == "o":
        o_counter += 1
    elif letter == "p":
        p_counter += 1
    elif letter == "q":
        q_counter += 1
    elif letter == "r":
        r_counter += 1
    elif letter == "s":
        s_counter += 1
    elif letter == "t":
        t_counter += 1
    elif letter == "u":
        u_counter += 1
    elif letter == "v":
        v_counter += 1
    elif letter == "w":
        w_counter += 1
    elif letter == "x":
        x_counter += 1
    elif letter == "y":
        y_counter += 1
    elif letter == "z":
        z_counter += 1

    print(letter)

print("a b c d e f g h i j k l m n o p q r s t u v w x y z")

print(a_counter,b_counter,c_counter,d_counter,e_counter,f_counter,g_counter,h_counter,i_counter,j_counter,k_counter,
      l_counter,m_counter,n_counter,o_counter,p_counter,q_counter,r_counter,s_counter,t_counter,u_counter,v_counter,
      w_counter,x_counter,y_counter,z_counter)


#for word in all_words:

 #   print(word)

#print(all_words)