

def are_similar(a, b):
    c = []

    for v in b:
        c.append(v if v[:4] not in ["SEQ@", "IMM@"] else v[4:])

    return len(set(c).difference(set(a))) == 0 and len(set(a).difference(set(c))) == 0


def is_seq(x):
    return x[:4] == "SEQ@"


def is_immutable(x):
    return x[:4] == "IMM@"


def remove_outliers(hn, N="N", smallest_nary=2):
    for vertex in hn.hypernetwork:
        hs = hn.hypernetwork[vertex]

        if hs.N == N:
            if len(hs.simplex) > smallest_nary:
                for s in hs.simplex:
                    if len(hn.hypernetwork[s].partOf) == 1:
                        hn.delete(vertex=s)


def find_in(val, simplex):
    found = False
    for v in simplex:
        if val == remove_special(v):
            found = True
            break

    return found


def remove_special(vert):
    return vert[4:] if vert[:4] in ["SEQ@", "IMM@"] else vert
