trans="A = chi B = tsu C = te D = to E = na F = ni G = nu H = ne I = no J = ha K = hi L = fu M = he N = ho O = ma P = mi Q = mu R = me S = mo T = ya U = yu V = yo W = ra X = ri Y = ru Z = re 1 = a 2 = i 3 = u 4 = u 5 = o 6 = ka 7 = ki 8 = ku 9 = ke 0 = --"
trans = trans.lower()
trans = trans.replace(" = ",":").split(" ")
for i in trans:
    print(i.split(":"),end = "")
trans_dict = {" ":" "}
for i in trans:
    element=i.split(":")
    trans_dict[element[0]]= element[1]
name_eng = input("\nEnter any name: ")
name_jap = ""
for i in name_eng.lower():
    name_jap+=trans_dict[i]
name_jap = name_jap.capitalize()
print("\nYour name in Japaneese: ",name_jap)
          
          
