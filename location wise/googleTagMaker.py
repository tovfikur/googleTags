with open('2tagfile', 'r') as d2:
    for j in d2.readlines():
        with open('3tagfile', 'r') as d3:
            for k in d3.readlines():
                with open(k, 'a') as d4:
                    d4.write(j.replace('\n', '') + k.replace('\n', '') + ' map\n')
