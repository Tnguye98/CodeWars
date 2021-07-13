def snail(snail_map):
    ans = []
    count = 0

    while len(snail_map) != 0:
        ans = left(snail_map, ans)
        if len(snail_map) == 0: break
        ans = down(snail_map, ans)
        ans = right(snail_map, ans)
        if len(snail_map) == 0: break
        ans = up(snail_map, ans)
    return ans

def left(snail_map, listAns):
    listAns = listAns + snail_map[0]
    snail_map.pop(0)
    return listAns

def down(snail_map, listAns):
    for sTrack in snail_map:
        listAns.append(sTrack[-1])
        sTrack.pop(-1)
    return listAns

def right(snail_map, listAns):
    listAns = listAns + snail_map[-1][::-1]
    snail_map.pop(-1)
    return listAns

def up(snail_map, listAns):
    for sTrack in snail_map[::-1]:
        listAns.append(sTrack[0])
        sTrack.pop(0)
    return listAns


