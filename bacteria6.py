from webbrowser import get


def get_complementary(s):
    c = ""
    for n in s:
        if n == "A":
            c += "T"
        elif n == "T":
            c += "A"
        elif n == "C":
            c += "G"
        elif n == "G":
            c += "C"
    return c

def get_sticky_end(s, r, rfind_flag ):
    c = get_complementary(s)
    if rfind_flag:
        i = s.rfind(r)
    else:
        i = s.find(r)
    s1 = s[:i + 1]
    s2 = s[i + 1:]
    c1 = c[:i + 5]
    c2 = c[i + 5:]
    return s1, s2, c1, c2

def get_sticky_end_index(s, r, rfind_flag ):
    c = get_complementary(s)
    if rfind_flag:
        i = s.rfind(r)
    else:
        i = s.find(r)
    s1 = s[:i + 1]
    s2 = s[i + 1:]
    c1 = c[:i + 5]
    c2 = c[i + 5:]
    return i + 1, i + 5


def ligate(ps1, ps2, pc1, pc2, gfps, gfpc):
    ps = ps1 + gfps + ps2
    pc = pc1 + gfpc + pc2 
    return ps, pc

file = input()
with open(file) as f:
    lines = f.readlines()

ps = lines[0].strip()
rs = lines[1].strip()
gfps = lines[2].strip()
gfprs1, gfprs2 = lines[3].strip().split(" ")

ps1, ps2, pc1, pc2 = get_sticky_end(ps, rs, False)
#gfpss1, gfpss2, gfpcs1, gfpcs2 = get_sticky_end(gfps, gfprs1, False)
#gfpse1, gfpse2, gfpce1, gfpce2 = get_sticky_end(gfps, gfprs2, True)

ssi, sci = get_sticky_end_index(gfps, gfprs1, False)
esi, eci = get_sticky_end_index(gfps, gfprs2, True)

result_gfps = gfps[ssi:esi]
gfpc = get_complementary(gfps)
result_gfpc = gfpc[sci:eci]

result_ps, result_pc = ligate(ps1, ps2, pc1, pc2, result_gfps, result_gfpc)
print(result_ps)
print(result_pc)