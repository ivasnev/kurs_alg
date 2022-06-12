s = list("0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,a,b,c,d,e,f".split(","))
f = open("gener_in", "w")
s_t = "else if ("
while len(s) != 1:
    tmp = s.pop()
    s_t += "'" + tmp + "' == symbol ||\n"
tmp = s.pop()
s_t += "'" + tmp + "' == symbol"
s_t += "){\n\tstate = ST;\n}\n"
f.write(s_t)
# s_t = "else {\n\tstate = ERROR;\n}\n"
# f.write(s_t)
